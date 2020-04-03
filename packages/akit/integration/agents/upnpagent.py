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
import queue
import requests
import socket
import ssdp
import struct
import threading
import time

from xml.etree.ElementTree import fromstring as parsefromstring
from xml.etree.ElementTree import ElementTree

from akit.exceptions import AKitSemanticError
from akit.integration.upnp.upnpfactory import UpnpFactory
from akit.integration.upnp.upnpprotocol import MSearchKeys, UpnpProtocol
from akit.integration.upnp.xml.upnpdevice1 import UPNP_DEVICE1_NAMESPACE

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

    def __init__(self, iface):
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

        self._listen_loop = None
        self._connect = None
        self._transport = None
        self._protocol = None

        return

    def children(self):
        """
        """
        return

    def begin_search(self):
        """
        """
        notify = ssdp.SSDPRequest('M-SEARCH', headers=UpnpProtocol.HEADERS)
        notify.sendto(self._transport, (UpnpProtocol.MULTICAST_ADDRESS, UpnpProtocol.PORT))
        return

    def start(self):
        """
        """
        if self._listen_loop:
            raise AKitSemanticError("The UpnpAgent was already started.")

        self._egate = threading.Semaphore(3)

        try:
            sgate = threading.Event()

            sgate.clear()
            self._notify_thread = threading.Thread(name="UpnpAgent(%s) Notify" % self._iface, target=self._notify_thread_entry, 
                                                   daemon=True, args=(sgate,))
            self._notify_thread.start()
            sgate.wait()

            sgate.clear()
            self._response_thread = threading.Thread(name="UpnpAgent(%s) Response" % self._iface, target=self._response_thread_entry,
                                                    daemon=True, args=(sgate,))
            self._response_thread.start()
            sgate.wait()

            sgate.clear()
            self._listen_thread = threading.Thread(name="UpnpAgent(%s) Listen" % self._iface, target=self._listen_thread_entry,
                                                   daemon=True, args=(sgate,))
            self._listen_thread.start()
            sgate.wait()
        except:
            for i in range(3):
                self._egate.release()
            raise

        return

    def wait(self, timeout=None):
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

    def _update_root_device(self, location, deviceinfo: dict):
        """
        """
        usn = deviceinfo[MSearchKeys.USN]
        devuuid = usn.split("::")[0]
        rootdev = None

        resp = requests.get(location)
        if resp.status_code == 200:
            xmlcontent = resp.content
            docTree = ElementTree(parsefromstring(xmlcontent))

            # {urn:schemas-upnp-org:device-1-0}root
            defaultns = {"": UPNP_DEVICE1_NAMESPACE}

            devNode = docTree.find("device", namespaces=defaultns)

            manufacturer = None
            modelNumber = None
            modelDescription = None

            manufacturerNode = devNode.find("manufacturer", namespaces=defaultns)
            if manufacturerNode is not None:
                manufacturer = manufacturerNode.text

            modelNumberNode = devNode.find("modelNumber", namespaces=defaultns)
            if modelNumberNode is not None:
                modelNumber = modelNumberNode.text

            modelDescNode = devNode.find("modelDescription", namespaces=defaultns)
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
                        rootdev.initialize(location, deviceinfo)

                        # Refresh the description
                        rootdev.refresh_description(self._factory, docTree.getroot(), namespaces=defaultns)
                    finally:
                        self._lock.acquire()

                    # If the device is still not in the table, add it
                    if location not in self._children:
                        self._children[location] = rootdev
                else:
                    rootdev = self._children[location]
                    # Refresh the description
                    rootdev.refresh_description(self._factory, docTree.getroot(), namespaces=defaultns)
            finally:
                self._lock.release()

        return

    def _listen_thread_entry(self, sgate):

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
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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
            pass
        finally:
            if self._transport is not None:
                self._transport.close()
            if self._connect is not None:
                self._connect.close()

            self._egate.release()

        return

    def _notify_thread_entry(self, sgate):

        self._egate.acquire()

        try:
            sgate.set()

            self._notify_queue = queue.Queue()
            while True:
                request, addr = self._notify_queue.get()

                print(request)
                print()

                self._notify_queue.task_done()
        finally:
            self._egate.release()

        return

    def _response_thread_entry(self, sgate):

        self._egate.acquire()

        try:
            sgate.set()

            self._response_queue = queue.Queue()
            while True:
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

                self._update_root_device(location, headers)

                self._response_queue.task_done()
        finally:
            self._egate.release()

        return



if __name__ == "__main__":
    agent = UpnpAgent("wlo1")
    agent.start()
    agent.begin_search()
    time.sleep(60 * 5)
    agent.begin_search()
    agent.wait()
    pass

