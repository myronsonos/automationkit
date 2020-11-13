"""
.. module:: upnpfactory
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the :class:`UpnpFactory` class and associated diagnostic.

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

from akit.exceptions import AKitSemanticError
from akit.extensible import generate_extension_key

from akit.integration.upnp.devices.upnpdevice import UpnpDevice
from akit.integration.upnp.devices.upnpembeddeddevice import UpnpEmbeddedDevice
from akit.integration.upnp.devices.upnprootdevice import UpnpRootDevice
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

from akit.integration.upnp.extensions import dynamic as dynamic_extensions
from akit.integration.upnp.extensions import standard as standard_extensions

from akit.extensible import collect_extensions_under_code_container

class UpnpFactory:
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
            cls._instance = super(UpnpFactory, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        """
            Initializes the Singleton initializer class
        """
        thisType = type(self)
        if not thisType._initialized:
            thisType._initialized = True
            self._embedded_device_registry = {}
            self._root_device_registry = {}
            self._service_registry = {}
            self._scan_for_device_extensions_under_code_container(dynamic_extensions)
            self._scan_for_device_extensions_under_code_container(standard_extensions)
            self._scan_for_service_extensions_under_code_container(dynamic_extensions)
            self._scan_for_service_extensions_under_code_container(standard_extensions)
        return

    def create_embedded_device_instance(self, manufacturer:str, modelNumber: str, modelDescription: str):
        deviceClass = UpnpEmbeddedDevice
        extkey = generate_extension_key(manufacturer, modelNumber, modelDescription)
        if extkey in self._embedded_device_registry:
            deviceClass = self._embedded_device_registry[extkey]
        return deviceClass()

    def create_root_device_instance(self, manufacturer:str, modelNumber: str, modelDescription: str):
        deviceClass = UpnpRootDevice
        if manufacturer is not None and modelNumber is not None and modelDescription is not None:
            extkey = generate_extension_key(manufacturer, modelNumber, modelDescription)
            if extkey in self._root_device_registry:
                deviceClass = self._root_device_registry[extkey]
        return deviceClass(manufacturer, modelNumber, modelDescription)

    def create_service_instance(self, serviceManufacturer, serviceType):
        serviceInst = None
        if serviceType is not None:
            extkey = generate_extension_key(serviceManufacturer, serviceType)
            if extkey in self._service_registry:
                serviceClass = self._service_registry[extkey]
                serviceInst = serviceClass()
        return serviceInst

    def _register_root_device(self, extkey, extcls):
        if extkey not in self._root_device_registry:
            self._root_device_registry[extkey] = extcls
        else:
            raise AKitSemanticError("A root device extension with the key=%r was already registered. (%s)" % (extkey, extcls))
        return

    def _register_service(self, extkey, extcls):
        if extkey not in self._service_registry:
            self._service_registry[extkey] = extcls
        else:
            self._service_registry[extkey] = extcls
        return

    def _scan_for_device_extensions_under_code_container(self, container):
        extcoll = collect_extensions_under_code_container(container, UpnpRootDevice)
        for _, extcls in extcoll:
            if hasattr(extcls, "MANUFACTURER") and hasattr(extcls, "MODEL_NUMBER") and hasattr(extcls, "MODEL_DESCRIPTION"):
                extkey = generate_extension_key(getattr(extcls, "MANUFACTURER"),
                    getattr(extcls, "MODEL_NUMBER"), getattr(extcls, "MODEL_DESCRIPTION"))
                self._register_root_device(extkey, extcls)
        return

    def _scan_for_service_extensions_under_code_container(self, container):
        extcoll = collect_extensions_under_code_container(container, UpnpServiceProxy)
        for _, extcls in extcoll:
            if (hasattr(extcls, "SERVICE_MANUFACTURER") and hasattr(extcls, "SERVICE_TYPE")):
                svc_manufacturer = getattr(extcls, "SERVICE_MANUFACTURER")
                svc_type = getattr(extcls, "SERVICE_TYPE")
                extkey = generate_extension_key(svc_manufacturer, svc_type)
                self._register_service(extkey, extcls)
        return