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
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import os
import requests
import threading
import traceback
import typing

from urllib.parse import urlparse

from xml.etree.ElementTree import tostring as xml_tostring
from xml.etree.ElementTree import fromstring as xml_fromstring
from xml.etree.ElementTree import ElementTree, Element, SubElement
from xml.etree.ElementTree import register_namespace

from akit.integration.upnp.upnpprotocol import MSearchKeys
from akit.integration.upnp.devices.upnpdevice import UpnpDevice, normalize_name_for_path
from akit.integration.upnp.xml.upnpdevice1 import UPNP_DEVICE1_NAMESPACE, UpnpDevice1Device, UpnpDevice1SpecVersion

from akit.integration.upnp.paths import DIR_UPNP_GENERATOR_DYNAMIC_EMBEDDEDDEVICES
from akit.integration.upnp.paths import DIR_UPNP_GENERATOR_DYNAMIC_ROOTDEVICES
from akit.integration.upnp.paths import DIR_UPNP_GENERATOR_DYNAMIC_SERVICES
from akit.integration.upnp.paths import DIR_UPNP_GENERATOR_STANDARD_EMBEDDEDDEVICES
from akit.integration.upnp.paths import DIR_UPNP_GENERATOR_STANDARD_ROOTDEVICES
from akit.integration.upnp.paths import DIR_UPNP_GENERATOR_STANDARD_SERVICES

from akit.integration import upnp as upnp_module

from akit.xlogging.foundations import getAutomatonKitLogger

UPNP_DIR = os.path.dirname(upnp_module.__file__)

def device_description_load(location):
    docTree = None

    resp = requests.get(location)
    if resp.status_code == 200:
        xmlcontent = resp.content

        docTree = ElementTree(xml_fromstring(xmlcontent))

    return  docTree


def device_description_find_components(location, docTree, namespaces={"": UPNP_DEVICE1_NAMESPACE}):

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
    modelName = None
    modelNumber = None
    modelDescription = None

    manufacturerNode = devNode.find("manufacturer", namespaces=namespaces)
    if manufacturerNode is not None:
        manufacturer = manufacturerNode.text

    modelNameNode = devNode.find("modelName", namespaces=namespaces)
    if modelNameNode is not None:
        modelName = modelNameNode.text

    modelNumberNode = devNode.find("modelNumber", namespaces=namespaces)
    if modelNumberNode is not None:
        modelNumber = modelNumberNode.text

    modelDescNode = devNode.find("modelDescription", namespaces=namespaces)
    if modelDescNode is not None:
        modelDescription = modelDescNode.text

    return devNode, urlBase, manufacturer, modelName, modelNumber, modelDescription

class UpnpRootDevice(UpnpDevice):
    """
        The UPNP Root device is the base device for the hierarchy that is
        associated with a unique network devices location.  The :class:`UpnpRootDevice`
        and its subdevices are linked by thier location url. 

        http://www.upnp.org/specs/arch/UPnP-arch-DeviceArchitecture-v1.0.pdf
    """

    MANUFACTURER = "unknown"
    MODEL_NUMBER = "unknown"
    MODEL_DESCRIPTION = "unknown"

    def __init__(self, manufacturer: str, modelNumber: str, modelDescription):
        """
            Creates a root device object.
        """
        super(UpnpRootDevice, self).__init__()

        if self.MANUFACTURER != manufacturer:
            self.MANUFACTURER = manufacturer
        if self.MODEL_NUMBER != modelNumber:
            self.MODEL_NUMBER = modelNumber
        if self.MODEL_DESCRIPTION != modelDescription:
            self.MODEL_DESCRIPTION = modelDescription

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
        self._routes = None

        self._devices = {}
        self._device_descriptions = {}

        self._mode = None

        self._logger = getAutomatonKitLogger()

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
    def modelName(self):
        mname = self.description.modelName
        return mname

    @property
    def routes(self):
        return self._routes

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
        self._routes = devinfo.pop(MSearchKeys.ROUTES)

        self._consume_upnp_extra(devinfo)
        return

    def lookup_device(self, device_type):
        device = self._devices[device_type]
        return device

    def record_description(self, urlBase: str, manufacturer: str, modelName: str, docTree: typing.Any, devNode: typing.Any, namespaces: str, force_recording: bool = False):

        manufacturerNormalized = normalize_name_for_path(manufacturer)
        modelName = normalize_name_for_path(modelName)

        root_dev_dir = os.path.join(DIR_UPNP_GENERATOR_DYNAMIC_ROOTDEVICES, manufacturerNormalized)
        if not os.path.exists(root_dev_dir):
            os.makedirs(root_dev_dir)
        
        root_dev_def_file = os.path.join(root_dev_dir, modelName + ".xml")
        if force_recording or not os.path.exists(root_dev_def_file):
            docNode = docTree.getroot()
            register_namespace('', namespaces[''])
            pretty_dev_content = xml_tostring(docNode, short_empty_elements=False)
            with open(root_dev_def_file, 'wb') as rddf:
                rddf.write(pretty_dev_content)

        embDevList = devNode.find("deviceList", namespaces=namespaces)
        if embDevList is not None:
            for embDevNode in embDevList:
                self._record_embedded_device( manufacturerNormalized, embDevNode, namespaces)

        svcList = devNode.find("serviceList", namespaces=namespaces)
        if svcList is not None:
            for svcNode in svcList:
                self._record_service( urlBase, manufacturerNormalized, svcNode, namespaces)

        return
    
    def _record_embedded_device(self, manufacturer: str, embDevNode: typing.Any, namespaces: str, force_recording: bool = False):

        deviceTypeNode = embDevNode.find("deviceType", namespaces=namespaces)
        if deviceTypeNode is not None:
            deviceType = deviceTypeNode.text

            dyn_dev_dir = os.path.join(DIR_UPNP_GENERATOR_DYNAMIC_EMBEDDEDDEVICES, manufacturer)
            if not os.path.exists(dyn_dev_dir):
                os.makedirs(dyn_dev_dir)

            dyn_dev_filename = os.path.join(dyn_dev_dir, deviceType + ".xml")
            if force_recording or not os.path.exists(dyn_dev_filename):
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

    def _record_service(self, urlBase: str, manufacturer: str, svcNode: typing.Any, namespaces: str, force_recording: bool = False):

        serviceTypeNode = svcNode.find("serviceType", namespaces=namespaces)
        scpdUrlNode = svcNode.find("SCPDURL", namespaces=namespaces)
        if serviceTypeNode is not None and scpdUrlNode is not None:

            serviceType = serviceTypeNode.text

            scpdUrl = scpdUrlNode.text
            if urlBase is not None:
                scpdUrl = urlBase.rstrip("/") + "/" + scpdUrl.lstrip("/")

            dyn_service_dir = os.path.join(DIR_UPNP_GENERATOR_DYNAMIC_SERVICES, manufacturer)
            if not os.path.exists(dyn_service_dir):
                os.makedirs(dyn_service_dir)

            dyn_svc_filename = os.path.join(dyn_service_dir, "%s.xml" % (serviceType,))
            if force_recording or not os.path.exists(dyn_svc_filename):
                try:
                    resp = requests.get(scpdUrl)
                    if resp.status_code == 200:
                        svc_content = resp.content
                        with open(dyn_svc_filename, 'wb') as sdf:
                            sdf.write(svc_content)
                    else:
                        self._logger.warn("Unable to retrieve service description for manf=%s st=%s url=%s" % (manufacturer, serviceType, scpdUrl))
                except Exception:
                    self._logger.exception("Exception while retreiving service description.")

        return

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

            self._enhance_device_detail()

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

    def _enhance_device_detail(self):
        return

    def _populate_embedded_device_descriptions(self, factory, description):

        for deviceInfo in description.deviceList:
            manufacturer = deviceInfo.manufacturer.strip()
            modelNumber = deviceInfo.modelNumber.strip()
            modelDescription = deviceInfo.modelDescription.strip()

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
        self._urlBase = urlBaseNode.text.rstrip("/")
        return

    def _process_version_node(self, verNode, namespaces=None):
        self._specVersion = UpnpDevice1SpecVersion(verNode, namespaces=namespaces)
        return

    def __str__(self):
        rtnstr = "%s: USN:%s MAC=%s IP=%s" % (self.modelName, self.USN, self.MACAddress, self.IPAddress)
        return rtnstr

