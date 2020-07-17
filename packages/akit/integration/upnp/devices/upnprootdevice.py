"""
.. module:: akit.integration.upnp.device.upnprootdevice
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the :class:`UpnpRootDevice` class and associated diagnostic.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>

"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@automationmojo.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import requests
import threading
import traceback

from urllib.parse import urlparse

from akit.integration.upnp.upnpprotocol import MSearchKeys
from akit.integration.upnp.devices.upnpdevice import UpnpDevice
from akit.integration.upnp.xml.upnpdevice1 import UpnpDevice1Device, UpnpDevice1SpecVersion

class UpnpRootDevice(UpnpDevice):
    """
        The UPNP Root device is the base device for the hierarchy that is
        associated with a unique network devices location.  The :class:`UpnpRootDevice`
        and its subdevices are linked by thier location url. 

        http://www.upnp.org/specs/arch/UPnP-arch-DeviceArchitecture-v1.0.pdf
    """

    def __init__(self):
        """
            Creates a root device object.
        """
        super(UpnpRootDevice, self).__init__()

        self._extra = {}
        self._cachecontrol = None
        self._ext = None
        self._location = None
        self._server = None
        self._st = None
        self._usn = None

        self._specVersion = None

        self._host = None
        self._ip_address = None

        self._devices = {}
        self._device_descriptions = {}

        self._mode = None

        self._lock = threading.RLock()
        return

    @property
    def cachecontrol(self):
        return self._cachecontrol

    @property
    def description(self):
        desc = None
        self._lock.acquire()
        try:
            desc = self._description
        finally:
            self._lock.release()
        return desc

    @property
    def device_descriptions(self):
        return self._device_descriptions.values()

    @property
    def devices(self):
        return self._devices.values()

    @property
    def ext(self):
        return self._ext

    @property
    def extra(self):
        return self._extra

    @property
    def IPAddress(self):
        return self._ip_address

    @property
    def location(self):
        return self._location

    @property
    def MACAddress(self):
        desc = self.description
        return desc.MACAddress

    @property
    def mode(self):
        return self._mode

    @property
    def server(self):
        return self._server

    @property
    def services(self):
        return self._services.values()

    @property
    def serialNumber(self):
        desc = self.description
        return desc.serialNumber

    @property
    def specVersion(self):
        return self._specVersion

    @property
    def USN(self):
        return self._usn

    def initialize(self, location: str, devinfo: dict):
        """
        """
        self._location = location
        self._cachecontrol = devinfo.pop(MSearchKeys.CACHE_CONTROL)
        self._ext = devinfo.pop(MSearchKeys.EXT)
        self._server = devinfo.pop(MSearchKeys.SERVER)
        self._st = devinfo.pop(MSearchKeys.ST)
        self._usn = devinfo.pop(MSearchKeys.USN)

        self._consume_upnp_extra(devinfo)
        return

    def lookup_device(self, device_type):
        device = self._devices[device_type]
        return device

    def refresh_description(self, ipaddr, factory, docNode, namespaces=None):
        """
        """
        try:
            self._ip_address = ipaddr

            specVerNode = docNode.find("specVersion", namespaces=namespaces)
            if specVerNode is not None:
                self._process_version_node(specVerNode, namespaces=namespaces)

            baseURLNode = docNode.find("URLBase", namespaces=namespaces)
            if baseURLNode is not None:
                self._process_urlbase_node(baseURLNode, namespaces=namespaces)

            url_parts = urlparse(self._location)
            self._host = url_parts.netloc

            # If urlBase was not set we need to try to use the schema and host as the urlBase
            if self._urlBase is None:
                self._urlBase = "%s://%s" % (url_parts.scheme, self._host)

            devNode = docNode.find("device", namespaces=namespaces)
            if devNode is not None:
                self._process_device_node(factory, devNode, namespaces=namespaces)
        except Exception as xcpt:
            err_msg = traceback.format_exc()
            print(err_msg)
            raise

        return

    def switchModes(self, mode):
        self._mode = mode
        return

    def to_dict(self, brief=False):
        dval = super(UpnpRootDevice, self).to_dict(brief=brief)
        dval["IPAddress"] = self.IPAddress
        dval["USN"] = self.USN
        return dval

    def to_json(self, brief=False):
        json_str = super(UpnpRootDevice, self).to_json(brief=brief)
        return json_str

    def _consume_upnp_extra(self, extrainfo):
        self._extra = extrainfo
        return

    def _create_device_description_node(self, devNode, namespaces=None):
        dev_desc_node = UpnpDevice1Device(devNode, namespaces=namespaces)
        return dev_desc_node

    def _populate_embedded_device_descriptions(self, factory, description):

        for deviceInfo in description.deviceList:
            manufacturer = deviceInfo.manufacturer
            modelNumber = deviceInfo.modelNumber
            modelDescription = deviceInfo.modelDescription

            devkey = ":".join([manufacturer, modelNumber, modelDescription])

            if devkey not in self._device_descriptions:
                dev_inst = factory.create_embedded_device_instance(manufacturer, modelNumber, modelDescription)
                self._device_descriptions[devkey] = dev_inst
            else:
                dev_inst = self._device_descriptions[devkey]

            dev_inst.update_description(self._host, self._urlBase, deviceInfo)
        return

    def _process_device_node(self, factory, devNode, namespaces=None):

        description = self._create_device_description_node(devNode, namespaces=namespaces)

        self._populate_services_descriptions(factory, description)

        self._populate_embedded_device_descriptions(factory, description)

        # Lock and then swap out the description
        self._lock.acquire()
        try:
            self._description = description
        finally:
            self._lock.release()

        return

    def _process_urlbase_node(self, urlBaseNode, namespaces=None):
        self._urlBase = urlBaseNode.text
        return

    def _process_version_node(self, verNode, namespaces=None):
        self._specVersion = UpnpDevice1SpecVersion(verNode, namespaces=namespaces)
        return

