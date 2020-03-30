

from akit.integration.upnp.devices.upnpdevice import UpnpDevice
from akit.integration.upnp.devices.upnprootdevice import UpnpRootDevice

class UpnpDeviceFactory:
    """
    """

    _instance = None
    _initialized = False

    def __new__(cls):
        """
            Constructs new instances of the UpnpDeviceFactory object from the
            :class:`UpnpDeviceFactory`.  This is a singlton object that is used
            to register and instantiate UPNP devices based on their devicetype id.
        """
        if cls._instance is None:
            cls._instance = super(UpnpDeviceFactory, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """
            Initializes the Singleton initializer class
        """
        this_cls = type(self)
        if not this_cls._initialized:
            this_cls._initialized = True
            self._embedded_device_registry = {}
            self._root_device_registry = {}
        return

    def create_embedded_device_instance(self, devicetype: str):
        deviceClass = UpnpDevice
        if devicetype in self._embedded_device_registry:
            deviceClass = self._embedded_device_registry[devicetype]
        return deviceClass()

    def create_root_device_instance(self, devicetype: str):
        deviceClass = UpnpRootDevice
        if devicetype in self._root_device_registry:
            deviceClass = self._root_device_registry[devicetype]
        return deviceClass()
