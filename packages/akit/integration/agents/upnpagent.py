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
import requests
import socket
import ssdp
import threading

from xml.etree.ElementTree import fromstring as parsefromstring
from xml.etree.ElementTree import ElementTree

from akit.exceptions import AKitSemanticError
from akit.integration.upnp.upnpfactory import UpnpFactory
from akit.integration.upnp.protocols.msearch import MSearchKeys, MSearchRootDeviceProtocol
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
        self._name = "UpnpAgent - %s" % self._iface
        self._factory = UpnpFactory()
        self._children = {}
        self._lock = threading.RLock()
        self._sgate = threading.Event()
        self._egate = threading.Event()
        self._thread = threading.Thread(name=self._name, target=self._thread_entry, daemon=True)

        self._loop = None
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
        notify = ssdp.SSDPRequest('M-SEARCH', headers=MSearchRootDeviceProtocol.HEADERS)
        notify.sendto(self._transport, (MSearchRootDeviceProtocol.MULTICAST_ADDRESS, MSearchRootDeviceProtocol.PORT))
        return

    def start(self):
        """
        """
        if self._loop:
            raise AKitSemanticError("The UpnpAgent was already started.")

        self._sgate.clear()
        self._egate.clear()
        self._thread.start()
        self._sgate.wait()
        return

    def wait(self, timeout=None):
        self._egate.wait(timeout=timeout)
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
            finally:
                self._lock.release()

        return

    def _thread_entry(self):

        def protocol_factory():
            return MSearchRootDeviceProtocol(self)

        self._loop = asyncio.new_event_loop()
        self._connect = self._loop.create_datagram_endpoint(protocol_factory, family=socket.AF_INET)
        self._transport, self._protocol = self._loop.run_until_complete(self._connect)

        # Release the gate so the caller to 'start' will return
        self._sgate.set()

        try:
            self._loop.run_forever()
        except KeyboardInterrupt as kerr:
            pass

        self._transport.close()
        self._loop.close()

        self._egate.set()

        return


if __name__ == "__main__":
    agent = UpnpAgent("wlo1")
    agent.start()
    agent.begin_search()
    agent.wait()
    pass

