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
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

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

from akit.integration.upnp.upnpprotocol import UpnpProtocol

class UpnpAgent:
    """
    """

<<<<<<< HEAD
    def __init__(self, coordinator, ifname, ifaddress, msearch_interval=60):
=======
    _instance_table = {}
    _initialized_table = {}

    def __new__(cls, **kwargs):
        """
            Constructs new instances of the UpnpAgent object. The :class:`UpnpAgent`
            object is a singleton so following instantiations of the object will
            reference the existing singleton
        """
        instanceid = "default"
        if "instanceid" in kwargs:
            instanceid = kwargs["instanceid"]

        instance = None
        if instanceid not in cls._instance_table:
            instance = super(UpnpAgent, cls).__new__(cls)
            cls._instance_table[instanceid] = instance
            # Put any initialization here.
        else:
            instance = cls._instance_table[instanceid]
        return instance

    def __init__(self, instanceid="default", interface=None, msearch_interval=60):

        this_type = type(self)
        if instanceid not in this_type._initialized_table:
                this_type._initialized_table[instanceid] = True
                self._instanceid = instanceid
                self._interface = interface
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
>>>>>>> 4c9330c5ecfeda74b70ca641bd58360c293411dc

        self._coordinator = coordinator
        self._ifname = ifname
        self._ifaddress = ifaddress

        self._egate = None
        
        self._event_thread = None

        self._running = False

        return

    def start(self):
        """
        """

        self._egate = threading.Semaphore(1)

        try:
            sgate = threading.Event()

            self._running = True

            sgate.clear()
<<<<<<< HEAD
            self._events_thread = threading.Thread(name="UpnpAgent(%s) Events" % self._ifname, target=self._thread_entry_monitor, 
=======
            self._notify_thread = threading.Thread(name="UpnpAgent(%s) Notify" % self._interface, target=self._thread_entry_notify, 
                                                   daemon=True, args=(sgate,))
            self._notify_thread.start()
            sgate.wait()

            sgate.clear()
            self._response_thread = threading.Thread(name="UpnpAgent(%s) Response" % self._interface, target=self._thread_entry_response,
                                                    daemon=True, args=(sgate,))
            self._response_thread.start()
            sgate.wait()

            sgate.clear()
            self._listen_thread = threading.Thread(name="UpnpAgent(%s) Listen" % self._interface, target=self._thread_entry_listen,
>>>>>>> 4c9330c5ecfeda74b70ca641bd58360c293411dc
                                                   daemon=True, args=(sgate,))
            self._events_thread.start()
            sgate.wait()

<<<<<<< HEAD
=======
            sgate.clear()
            self._tick_thread = threading.Thread(name="UpnpAgent(%s) Tick" % self._interface, target=self._thread_entry_tick,
                                                   daemon=True, args=(sgate,))
            self._tick_thread.start()
            sgate.wait()
>>>>>>> 4c9330c5ecfeda74b70ca641bd58360c293411dc
        except:
            self._running = False
            self._egate.release()

            raise

        return

    def shutdown(self):
        self._running = False
        self._events_thread.join(timeout=5)
        return

    def wait_for_shutdown(self, timeout=None):
        # We need to be able to get 3 acquires to ensure all three threads
        # have exited
        acquires = 0
        try:
            self._egate.acquire(timeout=timeout)
            acquires += 1
        except TimeoutError:
            if acquires > 0:
                self._egate.release()
        return

    def _thread_entry_monitor(self, sgate):

        self._egate.acquire()

        multicast_address = UpnpProtocol.MULTICAST_ADDRESS
        multicast_port = UpnpProtocol.PORT

        try:
            sgate.set()

<<<<<<< HEAD
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
=======
                bind_ip = '0.0.0.0'
                if self._interface is not None:
                    bind_ip = get_ip_address(self._interface)

                multicast_address = UpnpProtocol.MULTICAST_ADDRESS
                multicast_port = UpnpProtocol.PORT
                multicast_group = (bind_ip, UpnpProtocol.PORT)

                # Set us up to be a member of the group, this allows us to receive all the packets
                # that are sent to the group
                req = struct.pack("=4sl", socket.inet_aton(multicast_address), socket.INADDR_ANY)
                sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, req)
                sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.INADDR_ANY)
>>>>>>> 4c9330c5ecfeda74b70ca641bd58360c293411dc

            try:
                # Make sure other Automation processes can also bind to the UPNP address and port
                # so they can also get responses.
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)


                # Set us up to be a member of the group, this allows us to receive all the packets
                # that are sent to the group
                sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(multicast_address) + socket.inet_aton(self._ifaddress))

                sock.bind((multicast_address, multicast_port))

                while self._running:
                    request, addr = sock.recvfrom(1024)

                    print('IFNAME: %s ' % self._ifname)
                    print(request)
                    print()

            finally:
                sock.close()

        finally:
            self._egate.release()

        return

    

    

if __name__ == "__main__":
    agent = UpnpAgent("wlo1")
    agent.start()
    agent.begin_search()
    time.sleep(60 * 5)
    agent.begin_search()
    agent.wait_for_shutdown()
    pass

