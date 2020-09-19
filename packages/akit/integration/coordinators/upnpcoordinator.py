
import os
import netifaces
import requests
import socket
import struct
import threading
import time
import traceback
import typing

from urllib.parse import urlparse

from xml.etree.ElementTree import tostring as xml_tostring
from xml.etree.ElementTree import fromstring as xml_fromstring
from xml.etree.ElementTree import ElementTree, Element, SubElement
from xml.etree.ElementTree import register_namespace

from akit.integration import upnp as upnp_module

from akit.exceptions import AKitSemanticError, AKitTimeoutError

from akit.integration.upnp.devices.upnprootdevice import UpnpRootDevice
from akit.integration.upnp.upnpfactory import UpnpFactory
from akit.integration.upnp.upnpprotocol import MSearchKeys, UpnpProtocol
from akit.integration.upnp.upnpprotocol import msearch_parse_request, notify_parse_request
from akit.integration.upnp.xml.upnpdevice1 import UPNP_DEVICE1_NAMESPACE
from akit.integration.upnp.upnpprotocol import msearch_scan, MSearchKeys, MSearchRouteKeys

from akit.networking.interfaces import get_ipv4_address

from akit.xlogging import getAutomatonKitLogger

EMPTY_LIST = []

UPNP_DIR = os.path.dirname(upnp_module.__file__)

GENERATOR_DYNAMIC_ROOTDEVICES_DIR = os.path.join(UPNP_DIR, "generator", "dynamic", "rootdevices")
GENERATOR_DYNAMIC_EMBEDDEDDEVICES_DIR = os.path.join(UPNP_DIR, "generator", "dynamic", "embeddeddevices")
GENERATOR_DYNAMIC_SERVICES_DIR = os.path.join(UPNP_DIR, "generator", "dynamic", "services")

GENERATOR_STANDARD_ROOTDEVICES_DIR = os.path.join(UPNP_DIR, "generator", "standard", "rootdevices")
GENERATOR_STANDARD_EMBEDDEDDEVICES_DIR = os.path.join(UPNP_DIR, "generator", "standard", "embeddeddevices")
GENERATOR_STANDARD_SERVICES_DIR = os.path.join(UPNP_DIR, "generator", "standard", "services")

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
            self._watch_all = watch_all

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

    def startup_scan(self, upnp_hint_list, watchlist=None, exclude_interfaces=[], response_timeout=45, retry=2):
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
        
        for ridx in range(0, retry):
            if ridx > 0:
                self._logger.info("MSEARCH: Not all devices found, retrying (count=%d)..." % ridx)
            iter_found_devices, iter_matching_devices = msearch_scan(upnp_hint_list, 
                interface_list=interface_list, response_timeout=response_timeout)
            found_devices.update(iter_found_devices)
            matching_devices.update(iter_matching_devices)
            if len(matching_devices) >= hint_count:
                break

        devmsg = "FOUND DEVICES:\n"
        for dkey, dval in found_devices.items():
            devmsg += "    %s\n" % dkey
            addr = dval[MSearchKeys.IP]
            location = dval[MSearchKeys.LOCATION]
            self._update_root_device(addr, location, dval)
        devmsg += "\n"

        devmsg += "MATCHING DEVICES:\n"
        for dkey, dval in matching_devices.items():
            devmsg += "    %s\n" % dkey
        devmsg += "\n"
        self._logger.info(devmsg)

        for dkey, dval in found_devices.items():
            addr = dval[MSearchKeys.IP]
            location = dval[MSearchKeys.LOCATION]
            self._update_root_device(addr, location, dval)
        
        ifacelist = []
        for dev in matching_devices.values():
            ifname = dev[MSearchKeys.ROUTES][0][MSearchRouteKeys.IFNAME]
            if ifname not in ifacelist:
                ifacelist.append(ifname)

        if watchlist is not None and len(watchlist) > 0:
            for dev in self.children:
                devusn = dev.USN
                if devusn in watchlist:
                    self._watched_devices[devusn] = dev

        self._start_monitor_and_worker_threads()

        return

    def _create_root_device(self, manufacturer, modelNumber, modelDescription):
        dev = self._factory.create_root_device_instance(manufacturer, modelNumber, modelDescription)
        return dev

    def _normalize_name(self, name):

        normal_chars = [ nc for nc in name if str.isalnum(nc) ]
        normal_name = ''.join(normal_chars)

        return normal_name

    def _process_device_notification(self, usn, target, subtype):
        self._logger.debug("PROCESSING NOTIFY - USN: %s TARGET: %s SUBTYPE: %s", usn, target, subtype)
        return

    def _process_request_for_msearch(self, addr, request):
        
        reqinfo = msearch_parse_request(request)
        self._logger.debug("RESPONDING TO MSEARCH")

        return

    def _process_request_for_notify(self, addr, request):

        reqinfo = notify_parse_request(request)

        usn = reqinfo["USN"]
        target = reqinfo["NT"]
        subtype = reqinfo["NTS"]
        
        if usn in self._watched_devices:
            self._process_device_notification(usn, target, subtype)

        return

    def _record_embedded_device(self, manufacturer: str, embDevNode: typing.Any, namespaces: str):

        deviceTypeNode = embDevNode.find("deviceType", namespaces=namespaces)
        if deviceTypeNode is not None:
            deviceType = deviceTypeNode.text

            std_dev_filename = os.path.join(GENERATOR_STANDARD_EMBEDDEDDEVICES_DIR, deviceType + ".xml")
            if not os.path.exists(std_dev_filename):

                dyn_dev_dir = os.path.join(GENERATOR_DYNAMIC_EMBEDDEDDEVICES_DIR, manufacturer)
                if not os.path.exists(dyn_dev_dir):
                    os.makedirs(dyn_dev_dir)

                dyn_dev_filename = os.path.join(dyn_dev_dir, deviceType + ".xml")
                if not os.path.exists(dyn_dev_filename):
                    pretty_sl_content = ""

                    srcSvcListNode = embDevNode.find("serviceList", namespaces=namespaces)
                    if srcSvcListNode is not None:
                        register_namespace('', namespaces[''])
                        pretty_sl_content = xml_tostring(srcSvcListNode)

                    with open(dyn_dev_filename, 'wb') as edf:
                        edf.write(b"<device>\n")
                        edf.write(pretty_sl_content)
                        edf.write(b"</device\n")

        return

    def _record_root_device(self, urlBase: str, manufacturer: str, modelNumber: str, docTree: typing.Any, devNode: typing.Any, namespaces: str):

        manufacturerNormalized = self._normalize_name(manufacturer)
        modelNumberNormalized = self._normalize_name(modelNumber)

        root_dev_dir = os.path.join(GENERATOR_DYNAMIC_ROOTDEVICES_DIR, manufacturerNormalized)
        if not os.path.exists(root_dev_dir):
            os.makedirs(root_dev_dir)
        
        root_dev_def_file = os.path.join(root_dev_dir, modelNumberNormalized + ".xml")
        if not os.path.exists(root_dev_def_file):
            docNode = docTree.getroot()
            register_namespace('', namespaces[''])
            pretty_dev_content = xml_tostring(docNode, short_empty_elements=False)
            with open(root_dev_def_file, 'wb') as rddf:
                rddf.write(pretty_dev_content)

            embDevList = devNode.find("deviceList", namespaces=namespaces)
            if embDevList is not None:
                for embDevNode in embDevList:
                    self._record_embedded_device( manufacturerNormalized, embDevNode, namespaces)

            svcList = devNode.find("serviceList", namespaces=namespaces)
            if svcList is not None:
                for svcNode in svcList:
                    self._record_service( urlBase, manufacturerNormalized, svcNode, namespaces)

        return

    def _record_service(self, urlBase: str, manufacturer: str, svcNode: typing.Any, namespaces: str):

        serviceTypeNode = svcNode.find("serviceType", namespaces=namespaces)
        scpdUrlNode = svcNode.find("SCPDURL", namespaces=namespaces)
        if serviceTypeNode is not None and scpdUrlNode is not None:
            serviceType = serviceTypeNode.text

            scpdUrl = scpdUrlNode.text
            if urlBase is not None:
                scpdUrl = urlBase.rstrip("/") + "/" + scpdUrl.lstrip("/")

            std_svc_filename = os.path.join(GENERATOR_STANDARD_SERVICES_DIR, serviceType + ".xml")
            if not os.path.exists(std_svc_filename):

                dyn_service_dir = os.path.join(GENERATOR_DYNAMIC_SERVICES_DIR, manufacturer)
                if not os.path.exists(dyn_service_dir):
                    os.makedirs(dyn_service_dir)

                dyn_svc_filename = os.path.join(dyn_service_dir, serviceType + ".xml")
                if not os.path.exists(dyn_svc_filename):
                    try:
                        resp = requests.get(scpdUrl)
                        if resp.status_code == 200:
                            svc_content = resp.content
                            with open(dyn_svc_filename, 'wb') as sdf:
                                sdf.write(svc_content)
                        else:
                            self._logger.warn("Unable to retrieve service description for manf=%s st=%s url=%s" % (manufacturer, serviceType, scpdUrl))
                    except Exception:
                        self._logger.exception("Exception while retreiving service description.")

        return

    def _start_monitor_and_worker_threads(self):
        """
        """

        self._shutdown_gate = threading.Semaphore(1)

        try:
            sgate = threading.Event()

            self._running = True

            self._shutdown_gate = threading.Semaphore(self._worker_count + 1)

            sgate.clear()
            self._monitor_thread = threading.Thread(name="UpnpCoordinator - Monitor", target=self._thread_entry_monitor, 
                                                   daemon=True, args=(sgate,))
            self._monitor_thread.start()
            sgate.wait()

            for wkrid in range(0, self._worker_count):
                sgate.clear()
                wthread = threading.Thread(name="UpnpCoordinator - Worker(%d)" % wkrid, target=self._thread_entry_worker, 
                                                   daemon=True, args=(sgate,))
                wthread.start()
                sgate.wait()

        except:
            self._running = False

            for i in range(0, self._worker_count + 1):
                self._shutdown_gate.release()

            raise

        return

    def _thread_entry_monitor(self, sgate):

        self._shutdown_gate.acquire()

        multicast_address = UpnpProtocol.MULTICAST_ADDRESS
        multicast_port = UpnpProtocol.PORT

        try:
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

    def _update_root_device(self, ip_addr: str, location: str, deviceinfo: dict):
        """
        """
        
        rootdev = None

        if MSearchKeys.USN in deviceinfo:
            try:
                usn = deviceinfo[MSearchKeys.USN]
                devuuid = usn.split("::")[0]

                resp = requests.get(location)
                if resp.status_code == 200:
                    xmlcontent = resp.content

                    try:
                        docTree = ElementTree(xml_fromstring(xmlcontent))

                        # {urn:schemas-upnp-org:device-1-0}root
                        namespaces = {"": UPNP_DEVICE1_NAMESPACE}

                        devNode = docTree.find("device", namespaces=namespaces)

                        urlBase = None
                        baseURLNode = devNode.find("URLBase", namespaces=namespaces)
                        if baseURLNode is not None:
                            urlBase = baseURLNode.text

                        url_parts = urlparse(location)
                        host = url_parts.netloc

                        # If urlBase was not set we need to try to use the schema and host as the urlBase
                        if urlBase is None:
                            urlBase = "%s://%s" % (url_parts.scheme, host)

                        manufacturer = None
                        modelNumber = None
                        modelDescription = None

                        manufacturerNode = devNode.find("manufacturer", namespaces=namespaces)
                        if manufacturerNode is not None:
                            manufacturer = manufacturerNode.text

                        modelNumberNode = devNode.find("modelNumber", namespaces=namespaces)
                        if modelNumberNode is not None:
                            modelNumber = modelNumberNode.text

                        modelDescNode = devNode.find("modelDescription", namespaces=namespaces)
                        if modelDescNode is not None:
                            modelDescription = modelDescNode.text

                        try:
                            # Acquire the lock before we decide if the location exists in the children table
                            self._lock.acquire()
                            if location not in self._children:
                                try:
                                    # Unlock while we do some expensive stuff, we have already decided to
                                    # create the device
                                    self._lock.release()

                                    # We create the device
                                    rootdev = self._create_root_device(manufacturer, modelNumber, modelDescription)
                                    if type(rootdev) == UpnpRootDevice:
                                        self._record_root_device(urlBase, manufacturer, modelNumber, docTree, devNode, namespaces)

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
    upnp_hint_list = lscape.get_upnp_device_lookup_table()
    
    upnpcoord = UpnpCoordinator()
    upnpcoord.startup_scan(upnp_hint_list, watchlist=upnp_hint_list, exclude_interfaces=['lo'])

    firstdev = upnpcoord.watch_devices[0]
    print(type(firstdev))

    aclock = firstdev.serviceAlarmClock()

    time.sleep(600)