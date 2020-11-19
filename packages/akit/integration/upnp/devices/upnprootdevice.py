"""
.. module:: upnprootdevice
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
import re
import requests
import threading
import traceback
import typing
import weakref

from datetime import datetime

from urllib.parse import urlparse

from requests.compat import urljoin

from xml.etree.ElementTree import tostring as xml_tostring
from xml.etree.ElementTree import fromstring as xml_fromstring
from xml.etree.ElementTree import ElementTree, Element, SubElement
from xml.etree.ElementTree import register_namespace

from akit.exceptions import AKitCommunicationsProtocolError
from akit.extensible import generate_extension_key
from akit.paths import normalize_name_for_path

from akit.integration.landscaping.landscapedeviceextension import LandscapeDeviceExtension

from akit.integration.upnp.upnpprotocol import MSearchKeys, MSearchRouteKeys
from akit.integration.upnp.devices.upnpdevice import UpnpDevice, normalize_name_for_path
from akit.integration.upnp.xml.upnpdevice1 import UPNP_DEVICE1_NAMESPACE, UpnpDevice1Device, UpnpDevice1SpecVersion
from akit.integration.upnp.soap import NS_UPNP_EVENT

from akit.integration.upnp.paths import DIR_UPNP_GENERATOR_DYNAMIC_EMBEDDEDDEVICES
from akit.integration.upnp.paths import DIR_UPNP_GENERATOR_DYNAMIC_ROOTDEVICES
from akit.integration.upnp.paths import DIR_UPNP_GENERATOR_DYNAMIC_SERVICES
from akit.integration.upnp.paths import DIR_UPNP_GENERATOR_STANDARD_EMBEDDEDDEVICES
from akit.integration.upnp.paths import DIR_UPNP_GENERATOR_STANDARD_ROOTDEVICES
from akit.integration.upnp.paths import DIR_UPNP_GENERATOR_STANDARD_SERVICES

from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy
from akit.integration.upnp.services.upnpeventvar import UpnpEventVar

from akit.integration import upnp as upnp_module

from akit.networking.constants import USER_AGENT

from akit.xlogging.foundations import getAutomatonKitLogger

UPNP_DIR = os.path.dirname(upnp_module.__file__)

REGEX_SUBSCRIPTION_TIMEOUT = re.compile("^seconds-([0-9]+|infinite)", flags=re.IGNORECASE)

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

class UpnpRootDevice(UpnpDevice, LandscapeDeviceExtension):
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
        self._primary_route = None

        self._devices = {}
        self._device_descriptions = {}

        self._mode = None

        self._logger = getAutomatonKitLogger()

        self._coord_ref = None

        self._root_device_lock = threading.RLock()

        self._subscriptions = {}
        self._sid_to_service_lookup = {}
        self._variables = {}
        return

    @property
    def cachecontrol(self):
        return self._cachecontrol

    @property
    def description(self):
        desc = self._description
        return desc

    @property
    def device_descriptions(self):
        dev_desc = self._device_descriptions
        if dev_desc is not None:
            dev_desc_list = [devdesc for devdesc in dev_desc.values()]
        return dev_desc_list

    @property
    def devices(self):
        devices_list = None

        devices = self._devices
        if devices is not None:
            devices_list = [dev for dev in devices]

        return devices_list

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
    def MACAddress(self):
        macaddr = None
        desc = self.description
        if desc is not None:
            macaddr = desc.MACAddress
        return macaddr

    @property
    def mode(self):
        return self._mode
    
    @property
    def modelName(self):
        mname = None
        desc = self.description
        if desc is not None:
            mname = desc.modelName
        return mname

    @property
    def routes(self):
        return self._routes

    @property
    def server(self):
        return self._server

    @property
    def services(self):
        services_list = None

        services = self._services
        if services is not None:
            services_list = [svc for svc in services]

        return services_list

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

    def initialize(self, coord_ref: weakref.ReferenceType, basedevice_ref: weakref.ReferenceType, extid: str, location: str, configinfo: dict, devinfo: dict):
        """
            Initializes the landscape device extension.

            :param coord_ref: A weak reference to the coordinator that is managing interactions through this
                              device extension.
            :type coord_ref: weakref.ReferenceType
            :param extid: A unique reference that can be used to identify this device via the coordinator even if its location changes.
            :type extid: str
            :param location: The location reference where this device can be found via the coordinator.
            :type location: str
            :param 
        """
        LandscapeDeviceExtension.initialize(self, coord_ref, basedevice_ref, extid, location, configinfo)

        self._cachecontrol = devinfo.pop(MSearchKeys.CACHE_CONTROL)
        self._ext = devinfo.pop(MSearchKeys.EXT)
        self._server = devinfo.pop(MSearchKeys.SERVER)
        self._st = devinfo.pop(MSearchKeys.ST)
        self._usn = devinfo.pop(MSearchKeys.USN)
        self._routes = devinfo.pop(MSearchKeys.ROUTES)
        self._primary_route = self._routes[0]

        self._consume_upnp_extra(devinfo)
        return

    def lookup_device(self, device_type):
        device = None

        self._device_lock.acquire()
        try:
            device = self._devices[device_type]
        finally:
            self._device_lock.release()

        return device

    def process_subscription_callback(self, sid, headers, body):

        have_subscription = False

        service = None

        self._device_lock.acquire()
        try:
            service = self._sid_to_service_lookup[sid]
        finally:
            self._device_lock.release()

        if service is not None:
            service_type = service.SERVICE_TYPE

            docTree = ElementTree(xml_fromstring(body))

            psetNode = docTree.getroot()

            if psetNode is not None and psetNode.tag == "{%s}propertyset" % NS_UPNP_EVENT:
                propertyNodeList = psetNode.findall("{%s}property" % NS_UPNP_EVENT)

                service._update_event_variables(propertyNodeList)
        return

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

    def refresh_description(self, ipaddr, factory, docNode, namespaces=None):
        """
        """
        try:
            self._ip_address = ipaddr

            specVerNode = docNode.find("specVersion", namespaces=namespaces)
            if specVerNode is not None:
                self._locked_process_version_node(specVerNode, namespaces=namespaces)

            baseURLNode = docNode.find("URLBase", namespaces=namespaces)
            if baseURLNode is not None:
                self._locked_process_urlbase_node(baseURLNode, namespaces=namespaces)

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

    def subscribe_to_events(self, service: UpnpServiceProxy, timeout: typing.Optional[float]):

        """
            Creates a subscription to the event name specified and returns a
            UpnpEventVar object that can be used to read the current value for
            the given event.
        """
        sub_sid = None
        sub_timeout = None

        service_type = service.SERVICE_TYPE

        new_subscription = False
        self._device_lock.acquire()
        try:
            if not service_type in self._subscriptions:
                new_subscription = True
                self._subscriptions[service_type] = True
        finally:
            self._device_lock.release()

        if new_subscription:
            # If we created an uninitialized variable and added it to the subsciptions table
            # we need to statup the subsciption here.  If the startup process fails, we can
            # later remove the subscription from the subscription table.

            serviceManufacturer = normalize_name_for_path(self.MANUFACTURER)
            svckey = generate_extension_key(serviceManufacturer, service_type)
            service = self._services[svckey]

            subscribe_url = urljoin(self.URLBase, service.eventSubURL)
            subscribe_auth = ""

            coord = self._coord_ref()

            ifname = self._primary_route[MSearchRouteKeys.IFNAME]
            callback_url = "<http://%s>" % coord.lookup_callback_url_for_interface(ifname)

            headers = { "HOST": self._host, "User-Agent": USER_AGENT, "CALLBACK": callback_url, "NT": "upnp:event"}
            if timeout is not None:
                headers["TIMEOUT"] = "Seconds-%s" % timeout
            resp = requests.request(
                "SUBSCRIBE", subscribe_url, headers=headers, auth=subscribe_auth
            )
            if resp.status_code == 200:
                #============================== Expected Response Headers ==============================
                # SID: uuid:RINCON_7828CA09247C01400_sub0000000207
                # TIMEOUT: Second-86400
                # Server: Linux UPnP/1.0 Sonos/62.1-82260-monaco_dev (ZPS13)
                # Connection: close
                resp_headers = {k.upper(): v for k, v in resp.headers.items()}

                nxtheader = None
                try:
                    nxtheader = "SID"
                    sub_sid = resp_headers[nxtheader]

                    nxtheader = "TIMEOUT"
                    sub_timeout_str = resp_headers[nxtheader]
                except KeyError:
                    errmsg = "Event subscription response was missing in %r header." % nxtheader
                    raise AKitCommunicationsProtocolError(errmsg)

                mobj = REGEX_SUBSCRIPTION_TIMEOUT.match(sub_timeout_str)
                if mobj is not None:
                    timeout_str = mobj.groups()[0]
                    sub_timeout = None if timeout_str == "infinite" else int(timeout_str)
                
                if sub_sid is not None:
                    self._device_lock.acquire()
                    try:
                        self._sid_to_service_lookup[sub_sid] = service
                    finally:
                        self._device_lock.release()
                    
                    # Notify the coordinator which device has this subscription
                    coord.register_subscription_for_device(sub_sid, self)
                else:
                    self._device_lock.acquire()
                    try:
                        if service_type in self._subscriptions:
                            del self._subscriptions[service_type]
                    finally:
                        self._device_lock.release()

            else:
                resp.raise_for_status()

        return sub_sid, sub_timeout

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

    def _locked_populate_embedded_device_descriptions(self, factory, description):

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

    def _locked_process_urlbase_node(self, urlBaseNode, namespaces=None):
        self._urlBase = urlBaseNode.text.rstrip("/")
        return

    def _locked_process_version_node(self, verNode, namespaces=None):
        self._specVersion = UpnpDevice1SpecVersion(verNode, namespaces=namespaces)
        return

    def _process_device_node(self, factory, devNode, namespaces=None):

        description = self._create_device_description_node(devNode, namespaces=namespaces)

        self._device_lock.acquire()
        try:
            self._locked_populate_services_descriptions(factory, description)

            self._locked_populate_embedded_device_descriptions(factory, description)

            self._description = description
        finally:
            self._device_lock.release()

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

    def __str__(self):
        rtnstr = "%s: USN:%s MAC=%s IP=%s" % (self.modelName, self.USN, self.MACAddress, self.IPAddress)
        return rtnstr

