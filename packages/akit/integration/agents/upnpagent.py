

import asyncio
import socket
import ssdp
import threading

from akit.exceptions import AKitSemanticError
from akit.integration.upnp.devices.upnpdevicefactory import UpnpDeviceFactory
from akit.integration.upnp.protocols.msearch import MSearchKeys, MSearchRootDeviceProtocol

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
        self._factory = UpnpDeviceFactory()
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

    def _create_root_device(self, devicetype):
        dev = self._factory.create_root_device_instance(devicetype)
        return dev

    def _update_root_device(self, location, deviceinfo: dict):
        """
        """
        usn = deviceinfo[MSearchKeys.USN]
        devuuid = usn.split("::")[0]
        rootdev = None
        try:
            self._lock.acquire()
            if location not in self._children:
                rootdev = self._create_root_device(devuuid)
                self._children[location] = rootdev
                rootdev.initialize(location, deviceinfo)
            else:
                rootdev = self._children[location]
        finally:
            self._lock.release()

        rootdev.refresh_description()
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

