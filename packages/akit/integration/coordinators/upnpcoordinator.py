
import os
import netifaces
import requests
import socket
import struct
import threading
import time
import traceback
import typing

from io import BytesIO

from urllib.parse import urlparse

from xml.etree.ElementTree import tostring as xml_tostring
from xml.etree.ElementTree import fromstring as xml_fromstring
from xml.etree.ElementTree import ElementTree, Element, SubElement
from xml.etree.ElementTree import register_namespace

from akit.integration import upnp as upnp_module

from akit.exceptions import AKitSemanticError, AKitTimeoutError

from akit.integration.upnp.devices.upnprootdevice import UpnpRootDevice
from akit.integration.upnp.devices.upnprootdevice import device_description_load
from akit.integration.upnp.devices.upnprootdevice import device_description_find_components

from akit.integration.upnp.upnperrors import UpnpError
from akit.integration.upnp.upnpfactory import UpnpFactory
from akit.integration.upnp.upnpprotocol import MSearchKeys, UpnpProtocol
from akit.integration.upnp.upnpprotocol import msearch_parse_request, notify_parse_request
from akit.integration.upnp.xml.upnpdevice1 import UPNP_DEVICE1_NAMESPACE
from akit.integration.upnp.upnpprotocol import msearch_scan, MSearchKeys, MSearchRouteKeys

from akit.networking.interfaces import get_ipv4_address

from akit.xlogging import getAutomatonKitLogger

EMPTY_LIST = []

UPNP_DIR = os.path.dirname(upnp_module.__file__)

class UpnpCoordinator:

    instance = None
    initialized = False

    def __new__(cls, **kwargs):
        """
            Constructs new instances of the :class:`UpnpCoordinator` object. The 
            :class:`UpnpCoordinator` object is a singleton so following instantiations
            of the object will reference the existing singleton
        """

        if cls.instance is None:
            cls.instance = super(UpnpCoordinator, cls).__new__(cls)
        return cls.instance

    def __init__(self, control_point=False, workers=5, watch_all=False):
        if not self.initialized:
            self.initialized = True

            self._control_point = control_point
            self._worker_count = workers
            self._worker_threads = []
            self._watch_all = watch_all

            self._callback_threads = []

            self._logger = getAutomatonKitLogger()

            self._factory = UpnpFactory()

            self._lock = threading.RLock()

            self._shutdown_gate = None

            self._agents = []

            self._children = {}

            self._queue_lock = threading.RLock()
            self._queue_available = threading.Semaphore(0)
            self._queue_work = []

            self._worker_pool = []

            self._running = False

            self._watched_devices = {}

            self._iface_callback_addr_lookup = None
        return

    @property
    def agents(self):
        aglist = EMPTY_LIST

        self._lock.acquire()
        try:
            aglist = [a for a in self._agents]
        finally:
            self._lock.release()

        return aglist

    @property
    def children(self):
        """
        """
        chlist = EMPTY_LIST

        self._lock.acquire()
        try:
            chlist = [c for c in self._children.values()]
        finally:
            self._lock.release()

        return chlist

    @property
    def watch_devices(self):
        wlist = []

        self._lock.acquire()
        try:
            wlist = [wd for wd in self._watched_devices.values()]
        finally:
            self._lock.release()

        return wlist

    def lookup_device_by_mac(self, mac):
        """
            Lookup a UPNP device by its MAC address.
        """

        found = None
        for nxtdev in self.children:
            if mac == nxtdev.MACAddress:
                found = nxtdev
                break

        return found

    def lookup_device_by_usn(self, usn):
        """
            Lookup a UPNP device by its USN id.
        """

        found = None
        for nxtdev in self.children:
            if usn == nxtdev.USN:
                found = nxtdev
                break

        return found

    def lookup_device_list_by_usn(self, usnlist):
        """
        """
        found = []

        for usn in usnlist:
            for nxtdev in self.children:
                if usn == nxtdev.USN:
                    found.append(nxtdev)

        return found

    def startup_scan(self, upnp_hint_list, watchlist=None, exclude_interfaces=[], response_timeout=45, retry=2, force_recording=False):
        """
            Starts up and initilizes the UPNP coordinator by utilizing a hint list to determine
            what network interfaces to setup UPNP monitoring on.
        """
        if upnp_hint_list is None:
            upnp_hint_list = []

        hint_count = len(upnp_hint_list)

        interface_list = [ifname for ifname in netifaces.interfaces()]
        for exif in exclude_interfaces:
            interface_list.remove(exif)

        found_devices = {}
        matching_devices = {}
        missing_devices = []

        for ridx in range(0, retry):
            if ridx > 0:
                self._logger.info("MSEARCH: Not all devices found, retrying (count=%d)..." % ridx)
            iter_found_devices, iter_matching_devices = msearch_scan(upnp_hint_list, 
                interface_list=interface_list, response_timeout=response_timeout)
            found_devices.update(iter_found_devices)
            matching_devices.update(iter_matching_devices)
            if len(matching_devices) >= hint_count:
                break

        for expusn in upnp_hint_list:
            if expusn not in matching_devices:
                missing_devices.append(expusn)

        devmsg = "FOUND DEVICES:\n"
        for dkey, dval in found_devices.items():
            devmsg += "    %s\n" % dkey
            addr = dval[MSearchKeys.IP]
            location = dval[MSearchKeys.LOCATION]
            self._update_root_device(addr, location, dval, force_recording=force_recording)
        devmsg += "\n"

        devmsg += "MATCHING DEVICES:\n"
        for dkey, dval in matching_devices.items():
            devmsg += "    %s\n" % dkey
        devmsg += "\n"

        devmsg += "MISSING DEVICES:\n"
        for dkey in missing_devices:
            devmsg += "    %s\n" % dkey
        devmsg += "\n"

        self._logger.info(devmsg)

        if watchlist is not None and len(watchlist) > 0:
            for dev in self.children:
                devusn = dev.USN
                if devusn in watchlist:
                    self._watched_devices[devusn] = dev

        self._start_all_threads()

        return

    def _create_root_device(self, manufacturer, modelNumber, modelDescription):
        dev = self._factory.create_root_device_instance(manufacturer, modelNumber, modelDescription)
        return dev

    def _normalize_name(self, name):

        normal_chars = [ nc for nc in name if str.isalnum(nc) ]
        normal_name = ''.join(normal_chars)

        return normal_name

    def _process_device_notification(self, usn, request_info):

        host = request_info["HOST"]
        target = request_info["NT"]
        subtype = request_info["NTS"]

        if subtype == "ssdp:alive":
            self._logger.debug("PROCESSING NOTIFY - USN: %s HOST: %s SUBTYPE: %s", usn, host, subtype)
        elif subtype == "ssdp:byebye":
            self._logger.debug("PROCESSING NOTIFY - USN: %s HOST: %s SUBTYPE: %s", usn, host, subtype)
        else:
            self._logger.debug("PROCESSING NOTIFY - USN: %s HOST: %s SUBTYPE: %s", usn, host, subtype)

        return

    def _process_callback(self, ifname, claddr, request):
        
        reqinfo = msearch_parse_request(request)
        self._logger.debug("RESPONDING TO MSEARCH")

        return

    def _process_request_for_msearch(self, addr, request):
        
        reqinfo = msearch_parse_request(request)
        self._logger.debug("RESPONDING TO MSEARCH")

        return

    def _process_request_for_notify(self, addr, request):

        request_info = notify_parse_request(request)

        usn = request_info["USN"]

        if usn in self._watched_devices:
            self._process_device_notification(usn, request_info)

        return

    def _start_all_threads(self):
        """
        """

        ifacelist = []
        for dev in self.watch_devices.values():
            primary_route = dev[MSearchKeys.ROUTES][0]
            ifname = [MSearchRouteKeys.IFNAME]
            if ifname not in ifacelist:
                ifacelist.append(ifname)
        ifacecount = len(ifacelist)

        self._shutdown_gate = threading.Semaphore(1)

        try:
            sgate = threading.Event()

            self._running = True

            self._shutdown_gate = threading.Semaphore(self._worker_count + ifacecount + 1)

            # Spin-up the worker thread first so they will be ready to handle work
            for wkrid in range(0, self._worker_count):
                sgate.clear()
                wthread = threading.Thread(name="UpnpCoordinator - Worker(%d)" % wkrid, target=self._thread_entry_worker, 
                                                   daemon=True, args=(sgate,))
                self._worker_threads.append(wthread)
                wthread.start()
                sgate.wait()

            # Spin-up the Monitor thread so it can monitor notification traffic
            sgate.clear()
            self._monitor_thread = threading.Thread(name="UpnpCoordinator - Monitor", target=self._thread_entry_monitor, 
                                                   daemon=True, args=(sgate,))
            self._monitor_thread.start()
            sgate.wait()

            # Spin-up a Callback thread for each interface
            self._iface_callback_addr_lookup = {}

            for ifaceidx in range(0, ifacecount):
                ifname = ifacelist[ifaceidx]
                sgate.clear()
                cbthread = threading.Thread(name="UpnpCoordinator - Callback(%s)" % ifname, target=self._thread_entry_callback, 
                                                    daemon=True, args=(sgate, ifname))
                self._callback_threads.append(cbthread)
                cbthread.start()
                sgate.wait()

        except:
            self._running = False

            for i in range(0, self._worker_count + ifacecount + 1):
                self._shutdown_gate.release()

            raise

        return

    def _thread_entry_callback(self, sgate, ifname):

        self._shutdown_gate.acquire()

        try:
            service_addr = ""

            sock = socket.socket(socket.AF_INET, socket.AF_INET, socket.IPPROTO_UDP)

            # Bind to port zero so we can get an ephimeral port address
            sock.bind((service_addr, 0))

            host, port = sock.getsockname()

            iface_callback_addr = "%s:%s" % (host, port)

            self._iface_callback_addr_lookup[ifname] = iface_callback_addr

            # Set the start gate to allow the thread spinning us up to continue
            sgate.set()

            sock.listen(1)

            cbbuffer = BytesIO()

            while self._running:
                asock, claddr = sock.accept()

                self._logger.info("CBTHREAD(%s): Processing callback from %r" % (ifname, claddr))
                try:
                    while self._running:
                        # Process the requests
                        nxtbuff = asock.recv(1024)
                        if nxtbuff == 0:
                            break
                        cbbuffer.write(nxtbuff)
                finally:
                    asock.close()

                request = cbbuffer.getvalue()

                cbbuffer.truncate(0)
                cbbuffer.seek(0)

                # Queue the callback workpacket for dispatching by a worker thread
                wkpacket = (self._process_callback, (ifname, claddr, request))
                self._queue_lock.acquire()
                try:
                    self._queue_work.append(wkpacket)
                    self._queue_available.release()
                finally:
                    self._queue_lock.release()

        finally:
            self._shutdown_gate.release()

        return

    def _thread_entry_monitor(self, sgate):

        self._shutdown_gate.acquire()

        multicast_address = UpnpProtocol.MULTICAST_ADDRESS
        multicast_port = UpnpProtocol.PORT

        try:
            # Set the start gate to allow the thread spinning us up to continue
            sgate.set()

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

            try:
                # Make sure other Automation processes can also bind to the UPNP address and port
                # so they can also get responses.
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

                # Set us up to be a member of the group, this allows us to receive all the packets
                # that are sent to the group
                sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(multicast_address) + socket.inet_aton('0.0.0.0'))

                sock.bind((multicast_address, multicast_port))

                while self._running:
                    request, addr = sock.recvfrom(1024)

                    if request.startswith(b"M-SEARCH"):
                        if self._control_point:
                            wkpacket = (self._process_request_for_msearch, (addr, request))
                            self._queue_lock.acquire()
                            try:
                                self._queue_work.append(wkpacket)
                                self._queue_available.release()
                            finally:
                                self._queue_lock.release()
                    elif request.startswith(b"NOTIFY"):
                        wkpacket = (self._process_request_for_notify, (addr, request))
                        self._queue_lock.acquire()
                        try:
                            self._queue_work.append(wkpacket)
                            self._queue_available.release()
                        finally:
                            self._queue_lock.release()
                    else:
                        dbgmsg = b"UNKNOWN REQUEST TYPE:\n" + request
                        dbgmsg = dbgmsg.decode("utf-8")
                        self._logger.debug(dbgmsg)

            finally:
                sock.close()

        finally:
            self._shutdown_gate.release()

        return

    def _thread_entry_worker(self, sgate):

        try:
            # Set the start gate to allow the thread spinning us up to continue
            sgate.set()

            while self._running:
                self._queue_available.acquire()

                self._queue_lock.acquire()
                try:
                    wkfunc, wkargs = self._queue_work.pop(0)
                    wkfunc(*wkargs)
                except:
                    self._logger.exception("UpnpCoordinator: Worker exception.")
                finally:
                    self._queue_lock.release()

        finally:
            self._shutdown_gate.release()
        
        return

    def _update_root_device(self, ip_addr: str, location: str, deviceinfo: dict, force_recording: bool = False):
        """
        """
        
        rootdev = None

        if MSearchKeys.USN in deviceinfo:
            try:
                usn = deviceinfo[MSearchKeys.USN]
                devuuid = usn.split("::")[0]

                docTree = device_description_load(location)
    
                try:
                    # {urn:schemas-upnp-org:device-1-0}root
                    namespaces = {"": UPNP_DEVICE1_NAMESPACE}

                    deviceDescParts = device_description_find_components(location, docTree, namespaces=namespaces)
                    devNode, urlBase, manufacturer, modelName, modelNumber, modelDescription = deviceDescParts

                    try:
                        # Acquire the lock before we decide if the location exists in the children table
                        self._lock.acquire()
                        if location not in self._children:
                            try:
                                # Unlock while we do some expensive stuff, we have already decided to
                                # create the device
                                self._lock.release()

                                try:
                                    # We create the device
                                    rootdev = self._create_root_device(manufacturer, modelNumber, modelDescription)
                                except:
                                    errmsg = "ERROR: Unable to create device mfg=%s model=%s desc=%s\nTRACEBACK:\n" % (manufacturer, modelNumber, modelDescription)
                                    errmsg += traceback.format_exc()
                                    self._logger.error(errmsg)
                                    raise

                                if type(rootdev) == UpnpRootDevice:
                                    rootdev.record_description(urlBase, manufacturer, modelName, docTree, devNode, namespaces=namespaces, force_recording=force_recording)

                                rootdev.initialize(location, deviceinfo)

                                # Refresh the description
                                rootdev.refresh_description(ip_addr, self._factory, docTree.getroot(), namespaces=namespaces)
                            finally:
                                self._lock.acquire()

                            # If the device is still not in the table, add it
                            if location not in self._children:
                                self._children[location] = rootdev
                        else:
                            rootdev = self._children[location]
                            # Refresh the description
                            rootdev.refresh_description(ip_addr, self._factory, docTree.getroot(), namespaces=namespaces)
                    finally:
                        self._lock.release()
                except:
                    errmsg = "ERROR: Unable to parse description for. IP: %s LOCATION: %s\n" % (ip_addr, location)
                    for k, v in deviceinfo.items():
                        errmsg += "    %s: %s\n" % (k, v)
                    self._logger.debug(errmsg)
            except:
                errmsg = "ERROR: Unable to parse description for. IP: %s LOCATION: %s\n" % (ip_addr, location)
                for k, v in deviceinfo.items():
                    errmsg += "    %s: %s\n" % (k, v)
                self._logger.debug(errmsg)

        return



if __name__ == "__main__":

    from akit.integration.landscaping import Landscape


    lscape = Landscape()
    lscape.first_contact()

    upnpcoord = lscape.upnp_coord
    firstdev = upnpcoord.watch_devices[0]
    print(type(firstdev))
    print(firstdev)

    devProps = firstdev.serviceDeviceProperties()

    value = devProps.action_GetLEDState()

    devProps.proxy_subscribe_to_event("MicEnabled")

    LEDSTATES = ["Off", "On"]

    index = 0
    while True:
        time.sleep(2)
        if index == 0:
            print("tick")
        else:
            print("tock")
        index = (index + 1) % 2
