"""
.. module:: upnpcoordinator
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Contains the UpnpCoordinator which is used for managing connectivity upnp devices visible in the automation landscape.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import os
import netifaces
import requests
import socket
import struct
import threading
import time
import traceback
import typing
import weakref

from io import BytesIO

from urllib.parse import urlparse

from xml.etree.ElementTree import tostring as xml_tostring
from xml.etree.ElementTree import fromstring as xml_fromstring
from xml.etree.ElementTree import ElementTree, Element, SubElement
from xml.etree.ElementTree import register_namespace

from akit.exceptions import AKitRuntimeError, AKitCommunicationsProtocolError, AKitSemanticError, AKitTimeoutError

from akit.integration import upnp as upnp_module
from akit.integration.landscaping.landscapedevice import LandscapeDevice

from akit.integration.upnp.devices.upnprootdevice import UpnpRootDevice
from akit.integration.upnp.devices.upnprootdevice import device_description_load
from akit.integration.upnp.devices.upnprootdevice import device_description_find_components

from akit.integration.upnp.upnperrors import UpnpError
from akit.integration.upnp.upnpfactory import UpnpFactory
from akit.integration.upnp.upnpprotocol import MSearchKeys, UpnpProtocol
from akit.integration.upnp.upnpprotocol import msearch_parse_request, notify_parse_request
from akit.integration.upnp.xml.upnpdevice1 import UPNP_DEVICE1_NAMESPACE
from akit.integration.upnp.upnpprotocol import msearch_scan, MSearchKeys, MSearchRouteKeys
from akit.integration.upnp.services.upnpeventvar import UpnpEventVar

from akit.networking.interfaces import get_ipv4_address

from akit.xlogging.foundations import getAutomatonKitLogger

EMPTY_LIST = []

UPNP_DIR = os.path.dirname(upnp_module.__file__)

class UpnpCoordinator:
    """
    """

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
        thisType = type(self)
        if not thisType.initialized:
            thisType.initialized = True

            # ============================ Fixed Variables ============================
            # These variables are fixed at the start of the UpnpCoordinator and because
            # they are fixed, we don't protect them with the all.
            self._logger = getAutomatonKitLogger()

            self._control_point = control_point
            self._worker_count = workers
            self._watch_all = watch_all

            self._factory = UpnpFactory()

            self._running = False

            # The count for the shutdown gate semaphore is set at startup so we don't
            # need to lock protect it.  Once it is set, it is fixed for the lifespan
            # of the UpnpCoordinator
            self._shutdown_gate = None

            # ======================= Coordinator Lock Variables =======================
            # These variables are protected and read/write synchronized by the coordinator
            # lock.  They are all prefixed with _cl_ so it is easy to identify in code
            # if the lock is being held properly when the variables are being accessed.

            self._coord_lock = threading.RLock()

            # Callback threads are created on a per interface basis so we use a list
            # to manage them.
            self._cl_callback_threads = []
            
            # We don't want our threads that are answering requests or filtering traffic
            # to do extensive amounts of work, so we have a pool of worker threads that
            # that work is dispatched to for incoming requests and information processing.
            self._cl_worker_threads = []

            # Collection that manages UPNP device loop by location -> UpnpRootDevice
            self._cl_children = {}

            # A lookup table from USN -> devinfo for devices that were declared as
            # watched devices, the watched devices are devices that will be monitored
            # under special constraints and the coordinator will ensure they are found
            # during startup and will expend thread resources to ensure they are updated
            self._cl_watched_devices = {}

            self._cl_iface_callback_addr_lookup = None

            # A lookup table that store device registrations for differen subscription id(s)
            # The UpnpCoordinator spins up one thread per interface that needs to be monitored
            # for callback traffic from devices and provides a callback URL for subscriptions
            # to the devices,  the callback threads use this table to dispatch subscription
            # callbacks on given interfaces to the appropriate device. So UpnpEventVar instances
            # can be updated.
            self._cl_subscription_id_to_device = {}

            # =========================== Queue Lock Variables ==========================
            # Variables that manage the work queue and dispatching of work to worker threads
            self._queue_lock = threading.RLock()
            self._queue_available = threading.Semaphore(0)
            self._queue_work = []

        return

    @property
    def children(self):
        """
        """
        chlist = EMPTY_LIST

        self._coord_lock.acquire()
        try:
            chlist = [c for c in self._cl_children.values()]
        finally:
            self._coord_lock.release()

        return chlist

    @property
    def watch_devices(self):
        wlist = []

        self._coord_lock.acquire()
        try:
            wlist = [wd for wd in self._cl_watched_devices.values()]
        finally:
            self._coord_lock.release()

        return wlist

    def lookup_callback_url_for_interface(self, ifname):
        """
        """
        callback_url = None

        self._coord_lock.acquire()
        try:
            if ifname in self._cl_iface_callback_addr_lookup:
                callback_url = self._cl_iface_callback_addr_lookup[ifname]
        finally:
            self._coord_lock.release()

        return callback_url

    def lookup_device_by_mac(self, mac):
        """
            Lookup a UPNP device by its MAC address.
        """

        found = None

        self._coord_lock.acquire()
        try:
            for nxtdev in self._cl_children.values():
                if mac == nxtdev.MACAddress:
                    found = nxtdev
                    break
        finally:
            self._coord_lock.release()

        return found

    def lookup_device_by_usn(self, usn):
        """
            Lookup a UPNP device by its USN id.
        """

        found = None

        self._coord_lock.acquire()
        try:
            for nxtdev in self._cl_children.values():
                if usn == nxtdev.USN:
                    found = nxtdev
                    break
        finally:
            self._coord_lock.release()

        return found

    def lookup_device_list_by_usn(self, usnlist):
        """
        """
        found = []

        self._coord_lock.acquire()
        try:
            for usn in usnlist:
                for nxtdev in self._cl_children.values():
                    if usn == nxtdev.USN:
                        found.append(nxtdev)
        finally:
            self._coord_lock.release()

        return found

    def lookup_service_instance_by_sid(self, sid):
        """
            Lookup a service instance that had registered for subscription callbacks by sid
        """
        svc_inst = None

        self._coord_lock.acquire()
        try:
            if sid in self._cl_subscription_id_to_device:
                svc_inst = self._cl_subscription_id_to_device[sid]
        finally:
            self._coord_lock.release()

        return svc_inst

    def register_subscription_for_device(self, sid, device):
        """
            Registers a service instance for event callbacks via a 'sid'.
        """

        self._coord_lock.acquire()
        try:
            self._cl_subscription_id_to_device[sid] = device
        finally:
            self._coord_lock.release()

        return

    def startup_scan(self, lscape, upnp_hint_list, watchlist=None, exclude_interfaces=[], response_timeout=45, retry=2, force_recording=False):
        """
            Starts up and initilizes the UPNP coordinator by utilizing a hint list to determine
            what network interfaces to setup UPNP monitoring on.
        """

        if self._running:
            raise AKitRuntimeError("UpnpCoordinator.startup_scan called twice, The UpnpCoordinator is already running.")

        # Because we only allow this method to be called once, We don't need to lock the UpnpCoordinator
        # for most of this activity because the only thread with a reference to use is the caller.  At
        # the end of this function when we startup all the callback and worker threads is when we need to
        # start using the lock.
        if upnp_hint_list is None:
            upnp_hint_list = []

        hint_count = len(upnp_hint_list)

        interface_list = [ifname for ifname in netifaces.interfaces()]
        for exif in exclude_interfaces:
            interface_list.remove(exif)

        found_devices = {}
        matching_devices = {}
        missing_devices = []

        config_lookup = lscape._internal_get_upnp_device_config_lookup_table()

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

        devmsg_lines = ["FOUND DEVICES:"]
        for dkey, dval in found_devices.items():
            devmsg_lines.append("    %s" % dkey)
            addr = dval[MSearchKeys.IP]
            location = dval[MSearchKeys.LOCATION]
            self._update_root_device(lscape, config_lookup, addr, location, dval, force_recording=force_recording)
        devmsg_lines.append("")

        devmsg_lines.append("MATCHING DEVICES:")
        for dkey, dval in matching_devices.items():
            devmsg_lines.append("    %s" % dkey)
        devmsg_lines.append("")

        if len(missing_devices) > 0:
            devmsg_lines.append("MISSING DEVICES:")
            for dkey in missing_devices:
                devmsg_lines.append("    %s" % dkey)
            devmsg_lines.append("")

        devmsg = os.linesep.join(devmsg_lines)
        self._logger.info(devmsg)

        if watchlist is not None and len(watchlist) > 0:
            for dev in self.children:
                devusn = dev.USN
                if devusn in watchlist:
                    self._cl_watched_devices[devusn] = dev

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

    def _process_subscription_callback(self, ifname, claddr, request):

        self._logger.debug("RESPONDING TO SUBSCRIPTION CALLBACK")
        self._logger.debug(request)

        req_headers, req_body = notify_parse_request(request)

        sid = req_headers["SID"]

        device = None
        #lookup the device that needs to handle this subscription
        self._coord_lock.acquire()
        try:
            if sid in self._cl_subscription_id_to_device:
                device = self._cl_subscription_id_to_device[sid]
        finally:
            self._coord_lock.release()

        if device is not None:
            device.process_subscription_callback(sid, req_headers, req_body)

        return

    def _process_request_for_msearch(self, addr, request):
        
        reqinfo = msearch_parse_request(request)
        self._logger.debug("RESPONDING TO MSEARCH")

        return

    def _process_request_for_notify(self, addr, request):

        req_headers, req_body = notify_parse_request(request)

        usn = req_headers["USN"]

        if usn in self._cl_watched_devices:
            self._process_device_notification(usn, req_headers)

        return

    def _start_all_threads(self):
        """
        """

        ifacelist = []
        for dev in self.watch_devices:
            primary_route = dev.routes[0]
            ifname = primary_route[MSearchRouteKeys.IFNAME]
            if ifname not in ifacelist:
                ifacelist.append(ifname)
        ifacecount = len(ifacelist)

        self._coord_lock.acquire()
        try:
            sgate = threading.Event()

            self._running = True

            self._shutdown_gate = threading.Semaphore(self._worker_count + ifacecount + 1)

            # Spin-up the worker thread first so they will be ready to handle work
            for wkrid in range(0, self._worker_count):
                sgate.clear()
                wthread = threading.Thread(name="UpnpCoordinator - Worker(%d)" % wkrid, target=self._thread_entry_worker, 
                                                   daemon=True, args=(sgate,))
                self._cl_worker_threads.append(wthread)

                # Release the coordinator lock while starting up the thread so we are not holding it
                # so the new thread can get access to register itself with internal UpnpCoordinator state
                self._coord_lock.release()
                try:
                    wthread.start()
                    sgate.wait()
                finally:
                    self._coord_lock.acquire()

            # Spin-up the Monitor thread so it can monitor notification traffic
            sgate.clear()
            self._monitor_thread = threading.Thread(name="UpnpCoordinator - Monitor", target=self._thread_entry_monitor, 
                                                   daemon=True, args=(sgate,))
            self._monitor_thread.start()
            sgate.wait()

            # Spin-up a Callback thread for each interface
            self._cl_iface_callback_addr_lookup = {}

            for ifaceidx in range(0, ifacecount):
                ifname = ifacelist[ifaceidx]
                sgate.clear()
                cbthread = threading.Thread(name="UpnpCoordinator - Callback(%s)" % ifname, target=self._thread_entry_callback, 
                                                    daemon=True, args=(sgate, ifname))
                self._cl_callback_threads.append(cbthread)

                # Release the coordinator lock while starting up the thread so we are not holding it
                # so the new thread can get access to register itself with internal UpnpCoordinator state
                self._coord_lock.release()
                try:
                    cbthread.start()
                    sgate.wait()
                finally:
                    self._coord_lock.acquire()

        except:
            self._running = False

            for i in range(0, self._worker_count + ifacecount + 1):
                self._shutdown_gate.release()

            raise
        finally:
            self._coord_lock.release()

        return

    def _thread_entry_callback(self, sgate, ifname):

        self._shutdown_gate.acquire()

        try:
            service_addr = ""

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Bind to port zero so we can get an ephimeral port address
            sock.bind((service_addr, 0))

            _, port = sock.getsockname()
            host = get_ipv4_address(ifname)

            iface_callback_addr = "%s:%s" % (host, port)

            self._cl_iface_callback_addr_lookup[ifname] = iface_callback_addr

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
                        if len(nxtbuff) == 0:
                            break
                        cbbuffer.write(nxtbuff)
                finally:
                    asock.close()

                request = cbbuffer.getvalue()

                cbbuffer.truncate(0)
                cbbuffer.seek(0)

                # Queue the callback workpacket for dispatching by a worker thread
                wkpacket = (self._process_subscription_callback, (ifname, claddr, request))
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

    def _update_root_device(self, lscape, config_lookup, ip_addr: str, location: str, deviceinfo: dict, force_recording: bool = False):
        """
        """
        rootdev = None

        if MSearchKeys.USN in deviceinfo:
            try:
                usn = deviceinfo[MSearchKeys.USN]
                devuuid = usn.split("::")[0]

                configinfo = None
                if usn in config_lookup:
                    configinfo = config_lookup[usn]

                docTree = device_description_load(location)
    
                try:
                    # {urn:schemas-upnp-org:device-1-0}root
                    namespaces = {"": UPNP_DEVICE1_NAMESPACE}

                    deviceDescParts = device_description_find_components(location, docTree, namespaces=namespaces)
                    devNode, urlBase, manufacturer, modelName, modelNumber, modelDescription = deviceDescParts

                    dev_extension = None
                    try:
                        # Acquire the lock before we decide if the location exists in the children table
                        self._coord_lock.acquire()
                        if location not in self._cl_children:
                            try:
                                # Unlock while we do some expensive stuff, we have already decided to
                                # create the device
                                self._coord_lock.release()

                                try:
                                    # We create the device
                                    dev_extension = self._create_root_device(manufacturer, modelNumber, modelDescription)
                                except:
                                    errmsg = "ERROR: Unable to create device mfg=%s model=%s desc=%s\nTRACEBACK:\n" % (manufacturer, modelNumber, modelDescription)
                                    errmsg += traceback.format_exc()
                                    self._logger.error(errmsg)
                                    raise

                                if type(dev_extension) == UpnpRootDevice:
                                    dev_extension.record_description(urlBase, manufacturer, modelName, docTree, devNode, namespaces=namespaces, force_recording=force_recording)

                                coord_ref = weakref.ref(self)

                                basedevice = LandscapeDevice("network/upnp", deviceinfo)

                                basedevice_ref = weakref.ref(basedevice)
                                
                                dev_extension.initialize(coord_ref, basedevice_ref, usn, location, configinfo, deviceinfo)

                                # Refresh the description
                                dev_extension.refresh_description(ip_addr, self._factory, docTree.getroot(), namespaces=namespaces)

                                basedevice.attach_extension("upnp", dev_extension)

                                lscape._internal_register_device(usn, basedevice)
                            finally:
                                self._coord_lock.acquire()

                            # If the device is still not in the table, add it
                            if location not in self._cl_children:
                                self._cl_children[location] = dev_extension
                        else:
                            dev_extension = self._cl_children[location]
                            # Refresh the description
                            dev_extension.refresh_description(ip_addr, self._factory, docTree.getroot(), namespaces=namespaces)
                    finally:
                        self._coord_lock.release()
                except:
                    errmsg_lines = [
                        "ERROR: Unable to parse description for. IP: %s LOCATION: %s" % (ip_addr, location)
                    ]
                    for k, v in deviceinfo.items():
                        errmsg_lines.append("    %s: %s" % (k, v))

                    errmsg = os.linesep.join(errmsg_lines)
                    self._logger.debug(errmsg)
            except:
                errmsg_lines = [
                    "ERROR: Unable to parse description for. IP: %s LOCATION: %s" % (ip_addr, location)
                ]
                for k, v in deviceinfo.items():
                    errmsg_lines.append("    %s: %s" % (k, v))

                errmsg = os.linesep.join(errmsg_lines)
                self._logger.debug(errmsg)

        return



if __name__ == "__main__":

    import paramiko
    import akit.environment.activate

    from akit.xlogging.foundations import logging_initialize
    logging_initialize()

    from akit.integration.landscaping.landscape import Landscape


    lscape = Landscape()
    lscape.first_contact()

    #muse_coord = lscape.muse_coord
    #firstMuseAgent = muse_coord.device_agents[0]

    #firstMuseAgent.households()

    upnpcoord = lscape.upnp_coord
    firstdev = upnpcoord.watch_devices[0]
    print(type(firstdev))
    print(firstdev)

    devProps = firstdev.serviceDeviceProperties()

    value = devProps.action_GetLEDState()

    var_mic_enabled = devProps.subscribe_to_event("MicEnabled")
    meval = var_mic_enabled.wait_for_value()

    var_zonename = devProps.subscribe_to_event("ZoneName")
    znval = var_zonename.wait_for_value()

    isbval = devProps.lookup_event_variable("IsZoneBridge")

    LEDSTATES = ["Off", "On"]

    index = 0
    while True:
        time.sleep(2)
        if index == 0:
            print("tick")
        else:
            print("tock")
        index = (index + 1) % 2
