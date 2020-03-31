"""
.. module:: akit.integration.upnp.device.upnpdevicefactory
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the :class:`UpnpDeviceFactory` class and associated diagnostic.

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

import os

from akit.exceptions import AKitSemanticError

from akit.integration.upnp.devices.upnpdevice import UpnpDevice
from akit.integration.upnp.devices.upnprootdevice import UpnpRootDevice
from akit.integration.upnp.devices import extensions as extensions_module

from akit.extensible import collect_extensions_under_module

class UpnpDeviceFactory:
    """
    """

    _instance = None
    _initialized = False

    def __new__(cls):
        """
            Constructs new instances of the UpnpDeviceFactory object from the :class:`UpnpDeviceFactory`.
            This is a singlton object that is used to register and instantiate UPNP devices based on
            their devicetype id.
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
            self._scan_for_extensions_under_module(extensions_module)
        return

    def create_embedded_device_instance(self, manufacturer:str, modelNumber: str, modelDescription: str):
        deviceClass = UpnpDevice
        extkey = self._generate_extension_key(manufacturer, modelNumber, modelDescription)
        if extkey in self._embedded_device_registry:
            deviceClass = self._embedded_device_registry[extkey]
        return deviceClass()

    def create_root_device_instance(self, manufacturer:str, modelNumber: str, modelDescription: str):
        deviceClass = UpnpRootDevice
        if manufacturer is not None and modelNumber is not None and modelDescription is not None:
            extkey = self._generate_extension_key(manufacturer, modelNumber, modelDescription)
            if extkey in self._root_device_registry:
                deviceClass = self._root_device_registry[extkey]
        return deviceClass()

    def _generate_extension_key(self, manufacturer:str, modelNumber: str, modelDescription: str):
        extkey = "%s:%s:%s" % (manufacturer, modelNumber, modelDescription)
        return extkey

    def _register_root_device(self, extkey, extcls):
        if extkey not in self._root_device_registry:
            self._root_device_registry[extkey] = extcls
        else:
            raise AKitSemanticError("An extension with the key=%r was already registered. (%s)" % (extkey, extcls))
        return

    def _scan_for_extensions_under_module(self, module):
        extcoll = collect_extensions_under_module(module, UpnpRootDevice)
        for extname, extcls in extcoll:
            if hasattr(extcls, "MANUFACTURER") and hasattr(extcls, "MODEL_NUMBER") and hasattr(extcls, "MODEL_DESCRIPTION"):
                extkey = self._generate_extension_key(getattr(extcls, "MANUFACTURER"),
                    getattr(extcls, "MODEL_NUMBER"), getattr(extcls, "MODEL_DESCRIPTION"))
                self._register_root_device(extkey, extcls)
        return