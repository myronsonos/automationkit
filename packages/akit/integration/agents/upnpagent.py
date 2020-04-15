"""
.. module:: akit.integration.agents.upnpagent
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the :class:`UpnpAgent` class and associated diagnostic.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>

"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@automationmojo.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = ""

import asyncio
import os
import queue
import requests
import socket
import ssdp
import struct
import threading
import time
import typing
import traceback

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
from akit.integration.upnp.xml.upnpdevice1 import UPNP_DEVICE1_NAMESPACE
from akit.networking.interfaces import get_ip_address



UPNP_DIR = os.path.dirname(upnp_module.__file__)

GENERATOR_DYNAMIC_ROOTDEVICES_DIR = os.path.join(UPNP_DIR, "generator", "dynamic", "rootdevices")
GENERATOR_DYNAMIC_EMBEDDEDDEVICES_DIR = os.path.join(UPNP_DIR, "generator", "dynamic", "embeddeddevices")
GENERATOR_DYNAMIC_SERVICES_DIR = os.path.join(UPNP_DIR, "generator", "dynamic", "services")

GENERATOR_STANDARD_ROOTDEVICES_DIR = os.path.join(UPNP_DIR, "generator", "standard", "rootdevices")
GENERATOR_STANDARD_EMBEDDEDDEVICES_DIR = os.path.join(UPNP_DIR, "generator", "standard", "embeddeddevices")
GENERATOR_STANDARD_SERVICES_DIR = os.path.join(UPNP_DIR, "generator", "standard", "services")

class UpnpAgent:
    """
    """

    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        """
            Constructs new instances of the UpnpAgent object. The :class:`UpnpAgent`
            object is a singleton so following instantiations of the object will
            reference the existing singleton
        """
        if cls._instance is None:
            cls._instance = super(UpnpAgent, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance

    def __init__(self, iface=None, msearch_interval=60):

        this_type = type(self)
        if not this_type._initialized:
            this_type._initialized = True
            self._iface = iface
            self._factory = UpnpFactory()
            self._children = {}
            self._lock = threading.RLock()
            self._egate = None
            self._listen_thread = None
            self._notify_thread = None
            self._notify_queue = None
            self._response_thread = None
            self._response_queue = None
            self._tick_thread = None
            self._msearch_interval = msearch_interval
            self._msearch_lock = threading.RLock()

            self._running = False

            self._listen_loop = None
            self._connect = None
            self._transport = None
            self._protocol = None

        return

    @property
    def children(self):
        """
        """
        children = []

        self._lock.acquire()
        try:
            for nxtk, nxtv in self._children.items():
                children.append(nxtv)
        finally:
            self._lock.release()

        return children

    def begin_search(self):
        """
        """
        # Set this up to be a critical section of code so only one thread
        # can use the transport to send at a time
        self._msearch_lock.acquire()
        try:
            notify = ssdp.SSDPRequest('M-SEARCH', headers=UpnpProtocol.HEADERS)
            notify.sendto(self._transport, (UpnpProtocol.MULTICAST_ADDRESS, UpnpProtocol.PORT))
        except:
            pass
        finally:
            self._msearch_lock.release()
        return

    def lookup_device_by_mac(self, mac):

        found = None
        for nxtdev in self.children:
            if mac == nxtdev.MACAddress:
                found = nxtdev
                break

        return found

    def normalize_name(self, name):
        normal_chars = [ nc for nc in name if str.isalnum(nc) ]
        normal_name = ''.join(normal_chars)
        return normal_name

    def record_embedded_device(self, manufacturer: str, embDevNode: typing.Any, namespaces: str):
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

    def record_root_device(self, urlBase: str, manufacturer: str, modelNumber: str, docTree: typing.Any, devNode: typing.Any, namespaces: str):
        manufacturerNormalized = self.normalize_name(manufacturer)
        modelNumberNormalized = self.normalize_name(modelNumber)

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
                    self.record_embedded_device( manufacturerNormalized, embDevNode, namespaces)

            svcList = devNode.find("serviceList", namespaces=namespaces)
            if svcList is not None:
                for svcNode in svcList:
                    self.record_service( urlBase, manufacturerNormalized, svcNode, namespaces)

        return

    def record_service(self, urlBase: str, manufacturer: str, svcNode: typing.Any, namespaces: str):

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
                            print("Unable to retrieve service description for manf=%s st=%s url=%s" % (manufacturer, serviceType, scpdUrl))
                    except Exception as xcpt:
                        errmsg = traceback.format_exc()
                        print(errmsg)

        return

    def start(self):
        """
        """
        if self._listen_loop:
            raise AKitSemanticError("The UpnpAgent was already started.")

        self._egate = threading.Semaphore(4)

        try:
            sgate = threading.Event()

            self._running = True

            sgate.clear()
            self._notify_thread = threading.Thread(name="UpnpAgent(%s) Notify" % self._iface, target=self._thread_entry_notify, 
                                                   daemon=True, args=(sgate,))
            self._notify_thread.start()
            sgate.wait()

            sgate.clear()
            self._response_thread = threading.Thread(name="UpnpAgent(%s) Response" % self._iface, target=self._thread_entry_response,
                                                    daemon=True, args=(sgate,))
            self._response_thread.start()
            sgate.wait()

            sgate.clear()
            self._listen_thread = threading.Thread(name="UpnpAgent(%s) Listen" % self._iface, target=self._thread_entry_listen,
                                                   daemon=True, args=(sgate,))
            self._listen_thread.start()
            sgate.wait()

            sgate.clear()
            self._tick_thread = threading.Thread(name="UpnpAgent(%s) Tick" % self._iface, target=self._thread_entry_tick,
                                                   daemon=True, args=(sgate,))
            self._tick_thread.start()
            sgate.wait()
        except:
            self._running = False
            for i in range(3):
                self._egate.release()
            raise

        return

    def shutdown(self):
        self._running = False
        self.begin_search() # Trigger a search to wake up the threads
        self._response_thread.join(timeout=5)
        self._notify_thread.join(timeout=5)
        self._listen_loop.stop()
        return

    def wait_for_devices(self, upnp_hint_list: list, timeout: int = 300, retry: int = 30):

        hint_list_len = len(upnp_hint_list)

        have_count = 0
        for upnp_hint in upnp_hint_list:
            if "MACAddress" in upnp_hint:
                have_count += 1

        if have_count == hint_list_len:
            # Collect all the MAC addresses for the upnp devices
            mac_addresses = [ upnp_hint["MACAddress"] for upnp_hint in upnp_hint_list ]
            self._wait_for_devices_by_mac_address(mac_addresses, timeout=timeout, retry=retry)
            return

        have_count = 0
        for upnp_hint in upnp_hint_list:
            if "serialNumber" in upnp_hint:
                have_count += 1

        if have_count == hint_list_len:
            # Collect all the MAC addresses for the upnp devices
            serial_numbers = [ upnp_hint["serialNumber"] for upnp_hint in upnp_hint_list ]
            self._wait_for_devices_by_serial_number(serial_numbers, timeout=timeout, retry=retry)
            return

        # If the hints provided did not provide accurate enough information to perform the wait, raise
        # an exceptions.
        err_msg = "The upnp hints provided did not have a common supported lookup key. (MACAddress, serialNumber)"
        raise AKitSemanticError(err_msg)

    def wait_for_shutdown(self, timeout=None):
        # We need to be able to get 3 acquires to ensure all three threads
        # have exited
        acquires = 0
        try:
            self._egate.acquire(timeout=timeout)
            acquires += 1
            try:
                self._egate.acquire(timeout=timeout)
                acquires += 1
                try:
                    self._egate.acquire(timeout=timeout)
                    acquires += 1
                    try:
                        self._egate.acquire(timeout=timeout)
                        acquires += 1
                    except TimeoutError:
                        if acquires > 0:
                            self._egate.release()
                except TimeoutError:
                    if acquires > 0:
                        self._egate.release()
            except TimeoutError:
                if acquires > 0:
                    self._egate.release()
        except TimeoutError:
            if acquires > 0:
                self._egate.release()
        return

    def _create_root_device(self, manufacturer: str, modelNumber: str, modelDescription: str):
        dev = self._factory.create_root_device_instance(manufacturer, modelNumber, modelDescription)
        return dev

    def _thread_entry_listen(self, sgate):

        self._egate.acquire()

        try:
            try:
                self._listen_loop = asyncio.new_event_loop()

                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

                multicast_address = UpnpProtocol.MULTICAST_ADDRESS
                multicast_port = UpnpProtocol.PORT
                multicast_group = ('0.0.0.0', UpnpProtocol.PORT)

                # Set us up to be a member of the group, this allows us to receive all the packets
                # that are sent to the group
                req = struct.pack("=4sl", socket.inet_aton(multicast_address), socket.INADDR_ANY)
                sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, req)
                sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.INADDR_ANY)

                # Make sure other Automation processes can also bind to the UPNP address and port
                # so they can also get responses.
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
                
                sock.bind(multicast_group)

                def protocol_factory():
                    return UpnpProtocol(self._notify_queue, self._response_queue)

                self._connect = self._listen_loop.create_datagram_endpoint(protocol_factory, sock=sock)
                self._transport, self._protocol = self._listen_loop.run_until_complete(self._connect)

            finally:
                # Release the gate so the caller to 'start' will return
                sgate.set()

            self._listen_loop.run_forever()

        except KeyboardInterrupt as kerr:
            raise
        finally:
            if self._transport is not None:
                self._transport.close()
            if self._connect is not None:
                self._connect.close()

            self._egate.release()

        return

    def _thread_entry_notify(self, sgate):

        self._egate.acquire()

        try:
            sgate.set()

            self._notify_queue = queue.Queue()
            while self._running:
                request, addr = self._notify_queue.get()

                print(request)
                print()

                self._notify_queue.task_done()
        finally:
            self._egate.release()

        return

    def _thread_entry_response(self, sgate):

        self._egate.acquire()

        try:
            sgate.set()

            self._response_queue = queue.Queue()
            while self._running:
                response, addr = self._response_queue.get()

                lines = str(response).splitlines(False)
                for nxtline in lines:
                    print("    %s" % nxtline)
                print()

                reason = response.reason
                status_code = response.status_code
                version = response.version
                headers = dict([ (k.upper(), v) for k, v in response.headers])

                # Process the packet
                location = headers[MSearchKeys.LOCATION]

                try:
                    self._update_root_device(addr, location, headers)
                except requests.exceptions.ConnectionError as cerr:
                    # We can ignore connection errors, we may have UPNP devices on the
                    # network that have invalid IP addresses.
                    pass 


                self._response_queue.task_done()
        finally:
            self._egate.release()

        return

    def _thread_entry_tick(self, sgate):

        self._egate.acquire()

        try:
            sgate.set()

            msg = b"\r\n".join([  
                b'M-SEARCH * HTTP/1.1',
                b'Host:239.255.255.250:1900',
                b'ST: upnp:rootdevice',
                b'Man:"ssdp:discover"',
                b'MX:1',
                b''])

            while self._running:
                time.sleep(self._msearch_interval)

                self.begin_search()

        finally:
            self._egate.release()

        return

    def _update_root_device(self, addr, location, deviceinfo: dict):
        """
        """
        ip_addr = addr[0]
        usn = deviceinfo[MSearchKeys.USN]
        devuuid = usn.split("::")[0]
        rootdev = None

        resp = requests.get(location)
        if resp.status_code == 200:
            xmlcontent = resp.content
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
                            self.record_root_device(urlBase, manufacturer, modelNumber, docTree, devNode, namespaces)

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

        return

    def _wait_for_devices_by_mac_address(self, mac_addresses: list, timeout: int = 300, retry: int = 30):

        now_time = time.time()
        begin_time = now_time
        end_time = now_time + timeout

        while True:
            not_found = [mac for mac in mac_addresses]

            for dev in self.children:
                mac_addr = dev.MACAddress
                if mac_addr is not None and mac_addr in not_found:
                    not_found.remove(mac_addr)

            # If we found all the devices, then break
            if len(not_found) == 0:
                break

            # Restart the search
            self.begin_search()

            time.sleep(retry)

            now_time = time.time()
            if now_time > end_time:
                err_msg = "Timeout waiting for devices to respond to M-SEARCH.  MACAddress List:\n"
                for mac_addr in mac_addresses:
                    err_msg = "%s    %s\n" % (err_msg, mac_addr)
                raise AKitTimeoutError(err_msg)

        return

    def _wait_for_devices_by_serial_number(self, serial_numbers: list, timeout: int = 300, retry: int = 30):

        now_time = time.time()
        begin_time = now_time
        end_time = now_time + timeout

        while True:
            not_found = [ns for sn in serial_numbers]

            for dev in self.children:
                sn = dev.serialNumber
                if sn is not None and sn in not_found:
                    not_found.remove(sn)

            # If we found all the devices, then break
            if len(not_found) == 0:
                break

            # Restart the search
            self.begin_search()

            time.sleep(retry)

            now_time = time.time()
            if now_time > end_time:
                err_msg = "Timeout waiting for devices to respond to M-SEARCH.  serialNumber List:\n"
                for sn in serial_numbers:
                    err_msg = "%s    %s\n" % (err_msg, sn)
                raise AKitTimeoutError(err_msg)

        return

if __name__ == "__main__":
    agent = UpnpAgent("wlo1")
    agent.start()
    agent.begin_search()
    time.sleep(60 * 5)
    agent.begin_search()
    agent.wait_for_shutdown()
    pass

