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

from typing import List, Optional, Union

import json
import os
import socket
import threading
import traceback
import weakref

from io import BytesIO

import netifaces

from akit.exceptions import AKitConfigurationError, AKitRuntimeError, AKitTimeoutError
from akit.environment.context import Context

from akit.integration import upnp as upnp_module
from akit.integration.landscaping.landscapedevice import LandscapeDevice

from akit.integration.upnp.devices.upnprootdevice import UpnpRootDevice
from akit.integration.upnp.devices.upnprootdevice import device_description_load
from akit.integration.upnp.devices.upnprootdevice import device_description_find_components

from akit.integration.upnp.upnpfactory import UpnpFactory
from akit.integration.upnp.upnpprotocol import mquery, msearch_scan, notify_parse_request
from akit.integration.upnp.upnpprotocol import MSearchKeys, MSearchRouteKeys, UpnpProtocol
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy
from akit.integration.upnp.xml.upnpdevice1 import UPNP_DEVICE1_NAMESPACE

from akit.integration.coordinators.coordinatorbase import CoordinatorBase

from akit.networking.interfaces import get_ipv4_address

from akit.paths import get_path_for_testresults

EMPTY_LIST = []

UPNP_DIR = os.path.dirname(upnp_module.__file__)

class UpnpCoordinator(CoordinatorBase):
    """
        The UpnpCoordinator utilizes the expected device declarations of type 'network/upnp' to establish and maintain connectivity
        and interoperability with UPNP based network devices.  The UpnpCoordinator will scan all interfaces except for the excluded
        interfaces.  It also creates a general broadcast monitor thread and a subscription dispatch thread for each interface it
        is monitoring.
    """
    # pylint: disable=attribute-defined-outside-init

    def __init__(self, lscape, control_point=None, workers: int = 5):
        super(UpnpCoordinator, self).__init__(lscape, control_point=control_point, workers=workers)
        return

    def _initialize(self, *_args, control_point=None, workers: int = 5, **_kwargs):
        """
            Called by the CoordinatorBase constructor to perform the one time initialization of the coordinator Singleton
            of a given type.

            :param control_point: An object that acts as a UPNP control point.
            :param workers: The number of worker threads to spin up for handling work packets.
        """
        # pylint: disable=arguments-differ

        # ============================ Fixed Variables ============================
        # These variables are fixed at the start of the UpnpCoordinator and because
        # they are fixed, we don't protect them with the all.

        self._control_point = control_point
        self._worker_count = workers

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

        self._match_table = {
            "modelName": ('upnp', UpnpRootDevice._matches_model_name), # pylint: disable=protected-access
            "modelNumber": ('upnp', UpnpRootDevice._matches_model_number) # pylint: disable=protected-access
        }

        return

    @property
    def watch_devices(self) -> List[LandscapeDevice]:
        """
            Returns a list of the devices being watched by the UPNP coordinator.
        """
        wlist = []

        self._coord_lock.acquire()
        try:
            wlist = [wd for wd in self._cl_watched_devices.values()]
        finally:
            self._coord_lock.release()

        return wlist

    def lookup_callback_url_for_interface(self, ifname: str) -> str:
        """
            The callback url that is utilized by devices to determine the URL that should be used as a callback
            for a given network interface.

            :param ifname: The interface name of the interface to get the callback url for.

            :returns: Returns the callback url being monintored by the coordinator for a given interface.
        """
        callback_url = None

        self._coord_lock.acquire()
        try:
            if ifname in self._cl_iface_callback_addr_lookup:
                callback_url = self._cl_iface_callback_addr_lookup[ifname]
        finally:
            self._coord_lock.release()

        return callback_url

    def lookup_device_by_mac(self, mac: str) -> Union[LandscapeDevice, None]:
        """
            Lookup a UPNP device by its MAC address.

            :param mac: The mac address of the device to search for.

            :returns: The device found with the associated MAC address or None
        """

        found = None

        self._coord_lock.acquire()
        try:
            for nxtdev in self._cl_children.values():
                if mac == nxtdev.MACAddress:
                    found = nxtdev.basedevice
                    break
        finally:
            self._coord_lock.release()

        return found

    def lookup_device_by_usn(self, usn: str) -> Union[LandscapeDevice, None]:
        """
            Lookup a UPNP device by its USN id.

            :param usn: The usn of the device to search for.

            :returns: The device found with the associated USN address or None
        """

        found = None

        self._coord_lock.acquire()
        try:
            for nxtdev in self._cl_children.values():
                if usn == nxtdev.USN:
                    found = nxtdev.basedevice
                    break
        finally:
            self._coord_lock.release()

        return found

    def lookup_device_list_by_usn(self, usnlist: List[str]) -> List[LandscapeDevice]:
        """
            Lookup a list of UPNP devices by thier USN id.

            :param usn: A list of USN identifiers for devices to search for.

            :returns: A list of devices found with USN(s) in the usn search list.
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

    def lookup_device_instance_for_sid(self, sid: str) -> UpnpServiceProxy:
        """
            Lookup a device instance that has been registered with a subscription id.

            :param sid: The sid of a service device to search for.

            :returns: A device found to be associated with the sid provided.
        """
        device_inst = None

        self._coord_lock.acquire()
        try:
            if sid in self._cl_subscription_id_to_device:
                device_inst = self._cl_subscription_id_to_device[sid]
        finally:
            self._coord_lock.release()

        return device_inst

    def register_subscription_for_device(self, sid: str, device: LandscapeDevice):
        """
            Registers a service instance for event callbacks via a 'sid'.

            :param sid: The service subscription id to register a device with.
            :param device: The device to register as a handler for notifications for the sid provided.
        """

        self._coord_lock.acquire()
        try:
            self._cl_subscription_id_to_device[sid] = device
        finally:
            self._coord_lock.release()

        return

    def startup_scan(self, upnp_hint_list: List[str], watchlist: Optional[List[str]] = None, exclude_interfaces: List = [], response_timeout: float = 20, retry: int = 2, force_recording: bool = False):
        """
            Starts up and initilizes the UPNP coordinator by utilizing a hint list to determine
            what network interfaces to setup UPNP monitoring on.

            :param upnp_hint_list: A list of upnp USN(s) to search for.
            :param watchlist: A list of required USN(s) that we will setup watching and updates for.
            :param exclude_interfaces: Network interfaces that will be excluded from the search for devices.
            :param response_timeout: A timeout to wait for a response.
            :param retry: The number of retry attempts to make before giving up on finding devices.
            :param force_recording: Forces the updating or recording of device descriptions from devices found on the network.
        """
        # pylint: disable=dangerous-default-value

        lscape = self._lscape_ref()

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

        config_lookup = lscape._internal_get_upnp_device_config_lookup_table() # pylint: disable=protected-access

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

        missing_devices = []
        for expusn in upnp_hint_list:
            if expusn not in matching_devices:
                missing_devices.append(expusn)

        # As a last resort, rescan for the missing devices directly on each interface.
        query_devices = [mdev for mdev in missing_devices]
        for expusn in query_devices:
            try:
                query_results = mquery(expusn, interface_list=interface_list, response_timeout=response_timeout)
                if len(query_results) > 0:
                    device_info = query_results.values()[0]
                    found_devices[expusn] = device_info
                    missing_devices.remove(expusn)
            except AKitTimeoutError:
                pass

        self._log_scan_results(found_devices, matching_devices, missing_devices)

        if len(missing_devices) > 0:
            errmsg_list = [
                "Error devices missing from configuration.",
                "MISSING DEVICES:"
            ]
            for expusn in missing_devices:
                errmsg_list.append("    %s" % expusn)
            errmsg = os.linesep.join(errmsg_list)
            raise AKitConfigurationError(errmsg)

        for _, dval in matching_devices.items():
            addr = dval[MSearchKeys.IP]
            location = dval[MSearchKeys.LOCATION]
            self._update_root_device(lscape, config_lookup, addr, location, dval, force_recording=force_recording)

        if watchlist is not None and len(watchlist) > 0:
            for wdev in self.children:
                devusn = wdev.upnp.USN
                if devusn in watchlist:
                    self._cl_watched_devices[devusn] = wdev

        self._start_all_threads()

        self._found_devices = found_devices
        self._available_devices = matching_devices
        self._unavailable_devices = missing_devices

        return found_devices, matching_devices, missing_devices

    def _create_root_device(self, manufacturer: str, model_number: str, model_description: str) -> UpnpRootDevice:
        """
            Create a root UPNP device using the provided manufacturer and modelNumber provided.  If no
            device is found for the provided manufacturer and model_number then a generic UPNP root device
            will be instantiated using the manufacturer, model_number and model_description.

            :param manufacturer: The manufacturer of the root device to instantiate.
            :param model_number: The model_number of the root device to instantiate.
            :param model_description: The description to give to a device when it is instantiated.

            :returns: A upnp root device instance.
        """
        dev = self._factory.create_root_device_instance(manufacturer, model_number, model_description)
        return dev

    def _log_scan_results(self, found_devices: dict, matching_devices:dict , missing_devices: list):
        """
            Logs the results of the device scan.

            :param found_devices: A list of found devices.
            :param matching_devices: A list of devices matching the expected devices listed in the upnp_hint_list.
            :param missing_devices: A list of USN(s) for devices that were not found.
        """
        devmsg_lines = ["FOUND DEVICES:"]
        for dkey, _ in found_devices.items():
            devmsg_lines.append("    %s" % dkey)
        devmsg_lines.append("")

        devmsg_lines.append("MATCHING DEVICES:")
        for dkey, _ in matching_devices.items():
            devmsg_lines.append("    %s" % dkey)
        devmsg_lines.append("")

        if len(missing_devices) > 0:
            devmsg_lines.append("MISSING DEVICES:")
            for dkey in missing_devices:
                devmsg_lines.append("    %s" % dkey)
            devmsg_lines.append("")

        devmsg = os.linesep.join(devmsg_lines)
        self._logger.info(devmsg)

        return

    def _normalize_name(self, name: str) -> str:
        """
            Normalizes a name by removing non-alphanumeric characters.

            :param name: A name to normalize.

            :returns: The normalized name with all the non-alphanumeric characters removed.
        """
        # pylint: disable=no-self-use

        normal_chars = [ nc for nc in name if str.isalnum(nc) ]
        normal_name = ''.join(normal_chars)

        return normal_name

    def _process_device_notification(self, usn: str, request_info: dict):
        """
            Processes a device notification when given the USN and dictionary of header keys and values.

            :param usn: The USN of the device which the notification is from.
            :param request_info: The headers from the notification request.
        """
        host = request_info["HOST"]
        subtype = request_info["NTS"]

        if subtype == "ssdp:alive":
            self._logger.info("PROCESSING NOTIFY - USN: %s HOST: %s SUBTYPE: %s", usn, host, subtype)
        elif subtype == "ssdp:byebye":
            self._logger.info("PROCESSING NOTIFY - USN: %s HOST: %s SUBTYPE: %s", usn, host, subtype)
        else:
            self._logger.info("PROCESSING NOTIFY - USN: %s HOST: %s SUBTYPE: %s", usn, host, subtype)

        return

    def _process_subscription_callback(self, ifname: str, claddr: str, request: str):
        """
            Processes a callback request on the specified interface and address request.

            :param ifname: The name of the ifname the request came from.
            :param claddr: The address of the client that made the callback.
            :param request: The content of the callback request.
        """
        # pylint: disable=unused-argument

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

    def _process_request_for_msearch(self, addr: str, request: str):
        """
            Process an msearch request from the given address.

            :param addr: The address of machine making the msearch request.
            :param request: The request content of the msearch request to process.
        """
        #reqinfo = msearch_parse_request(request)
        self._logger.debug("RESPONDING TO MSEARCH")

        return

    def _process_request_for_notify(self, addr: str, request: str):
        """
            Process a notify request.

            :param addr: The address of machine making the notify request.
            :param request: The request content of the notify request to process.
        """
        req_headers, _ = notify_parse_request(request)

        usn = req_headers["USN"]

        if usn in self._cl_watched_devices:
            self._process_device_notification(usn, req_headers)

        return

    def _start_all_threads(self):
        """
            Starts up all the thread the UPNP coordinator uses for monitoring, callback notification servicing and
            the worker threads used for processing work packges from notifications and callbacks.
        """

        ifacelist = []
        for wdev in self.watch_devices:
            primary_route = wdev.upnp.routes[0]
            ifname = primary_route[MSearchRouteKeys.IFNAME]
            if ifname not in ifacelist:
                ifacelist.append(ifname)
        ifacecount = len(ifacelist)

        self._coord_lock.acquire()
        try:
            sgate = threading.Event()

            self._running = True

            self._shutdown_gate = threading.Semaphore(self._worker_count + ifacecount + 1)

            # Spin-up the worker threads first so they will be ready to handle work packets
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

            for _ in range(0, self._worker_count + ifacecount + 1):
                self._shutdown_gate.release()

            raise
        finally:
            self._coord_lock.release()

        return

    def _thread_entry_callback(self, sgate: threading.Event, ifname: str):
        """
            The entry point for callback processing threads.

            :param sgate: The startup gate that is used to indicate to the thread spinning up the coordinator
                          that the callback thread has started.
            :param ifname: The interface name of interface this thread is assigned to process callbacks for.
        """
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

    def _thread_entry_monitor(self, sgate: threading.Event):
        """
            The entry point for monitor thread.  The monitor thread sets up monitoring on all interfaces.

            :param sgate: The startup gate that is used to indicate to the thread spinning up the coordinator
                          that the monitor thread has started.
        """
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

    def _thread_entry_worker(self, sgate: threading.Event):
        """
            The entry point for worker threads.  Worker threads process work packets queued up by other threads.

            :param sgate: The startup gate that is used to indicate to the thread spinning up the coordinator
                          that this worker thread has started.
        """
        try:
            # Set the start gate to allow the thread spinning us up to continue
            sgate.set()

            while self._running:
                self._queue_available.acquire()

                self._queue_lock.acquire()
                try:
                    wkfunc, wkargs = self._queue_work.pop(0)
                    wkfunc(*wkargs)
                except: # pylint: disable=bare-except
                    self._logger.exception("UpnpCoordinator: Worker exception.")
                finally:
                    self._queue_lock.release()

        finally:
            self._shutdown_gate.release()

        return

    def _update_root_device(self, lscape, config_lookup: dict, ip_addr: str, location: str, deviceinfo: dict, force_recording: bool = False):
        """
            Updates a UPNP root device.

            :param lscape: The landscape singleton instance.
            :param config_lookup: A configuration lookup table that can be used to lookup configuration information for upnp devices.
            :param ip_addr: The IP address of the device to update.
            :param location: The location URL associated with the device.
            :param deviceinfo: The device information from the msearch response headers.
            :param force_recording: Forces the UpnpCoordinator to record device and service descriptions.
        """

        if MSearchKeys.USN in deviceinfo:
            try:
                usn = deviceinfo[MSearchKeys.USN]

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

                                if isinstance(dev_extension, UpnpRootDevice):
                                    dev_extension.record_description(urlBase, manufacturer, modelName, docTree, devNode, namespaces=namespaces, force_recording=force_recording)

                                coord_ref = weakref.ref(self)

                                basedevice = LandscapeDevice(lscape, usn, "network/upnp", configinfo)
                                basedevice.initialize_features()
                                basedevice.update_match_table(self._match_table)

                                basedevice_ref = weakref.ref(basedevice)

                                dev_extension.initialize(coord_ref, basedevice_ref, usn, location, configinfo, deviceinfo)

                                # Refresh the description
                                dev_extension.refresh_description(ip_addr, self._factory, docTree.getroot(), namespaces=namespaces)

                                basedevice.attach_extension("upnp", dev_extension)

                                lscape._internal_register_device(usn, basedevice) # pylint: disable=protected-access
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
                except:  # pylint: disable=bare-except
                    errmsg_lines = [
                        "ERROR: Unable to parse description for. IP: %s LOCATION: %s" % (ip_addr, location)
                    ]
                    for k, v in deviceinfo.items():
                        errmsg_lines.append("    %s: %s" % (k, v))

                    errmsg = os.linesep.join(errmsg_lines)
                    self._logger.debug(errmsg)
            except:  # pylint: disable=bare-except
                errmsg_lines = [
                    "ERROR: Unable to parse description for. IP: %s LOCATION: %s" % (ip_addr, location)
                ]
                for k, v in deviceinfo.items():
                    errmsg_lines.append("    %s: %s" % (k, v))

                errmsg = os.linesep.join(errmsg_lines)
                self._logger.debug(errmsg)

        return
