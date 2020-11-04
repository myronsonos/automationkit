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
        self._primary_route = None

        self._devices = {}
        self._device_descriptions = {}

        self._mode = None

        self._logger = getAutomatonKitLogger()

        self._lock = threading.RLock()

        self._coord_ref = None

        self._subscription_lock = threading.RLock()
        self._subscriptions = {}
        self._sid_to_subscription_key_lookup = {}
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

    def initialize(self, coord_ref: weakref.ReferenceType, location: str, devinfo: dict):
        """
        """
        self._coord_ref = coord_ref
        self._location = location

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
        device = self._devices[device_type]
        return device

    def process_subscription_callback(self, sid, headers, body):

        eventvar = None
        subscription_key = None

        self._subscription_lock.acquire()
        try:
            subscription_key = self._sid_to_subscription_key_lookup[sid]
            eventvar = self._subscriptions[subscription_key]
        finally:
            self._subscription_lock.release()

        if eventvar is not None:
            service_type, _ = subscription_key.split("/") 

            docTree = ElementTree(xml_fromstring(body))

            psetNode = docTree.getroot()

            if psetNode is not None and psetNode.tag == "{%s}propertyset" % NS_UPNP_EVENT:
                propertyNodeList = psetNode.findall("{%s}property" % NS_UPNP_EVENT)
                for propNodeOuter in propertyNodeList:
                    # Get the first node of the outer property node
                    propNode = propNodeOuter.getchildren()[0]

                    event_name = propNode.tag
                    event_value = propNode.text

                    if event_name == eventvar.name:
                        timestamp = datetime.now()
                        eventvar.sync_update(event_value, timestamp)
                    else:
                        otherkey = "{}/{}".format(service_type, event_name)
                        othervar = None

                        self._subscription_lock.acquire()
                        try:
                            if otherkey in self._subscriptions:
                                othervar = self._subscriptions[subscription_key]
                        finally:
                            self._subscription_lock.release()
                        
                        if othervar is not None:
                            timestamp = datetime.now()
                            othervar.sync_update(event_value, timestamp)
                        else:
                            # If we get here, we have a value for a variable that we are not subscribed
                            # create a none subscribed entry for the variable and its value
                            self._subscription_lock.acquire()
                            try:
                                event_var = UpnpEventVar(subscription_key, event_name, self._subscription_lock, value=event_value)
                                self._subscriptions[subscription_key] = event_var
                            finally:
                                self._subscription_lock.release()
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

    def subscribe_to_event(self, service_type: str, event_name: str, timeout: typing.Optional[float]):

        """
            Creates a subscription to the event name specified and returns a
            UpnpEventVar object that can be used to read the current value for
            the given event.
        """
        event_var = None

        subscription_key = "{}/{}".format(service_type, event_name)

        new_subscription = False
        self._subscription_lock.acquire()
        try:
            if not subscription_key in self._subscriptions:
                new_subscription = True
                # Create the subscription event variable. It is created with an invalid
                # value and marked as uninitialized because we need to get an update
                # response in order to set its values.  We can handle the update response
                # in a Notify thread.
                event_var = UpnpEventVar(subscription_key, event_name, self._subscription_lock)

                self._subscriptions[subscription_key] = event_var
            else:
                # We could have an entry for this variable due to a first notify property broadcast,
                # so look to to see if we have a variable and see if it is missing an SID or if its
                # subscription has expired.  If either of these are true we should create a subscription 
                event_var = self._subscriptions[subscription_key]
                if event_var.sid is None:
                    new_subscription = True
                elif event_var.expired:
                    new_subscription = True
        finally:
            self._subscription_lock.release()

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
                sub_sid = None
                sub_timeout = None

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
                    self._subscription_lock.acquire()
                    try:
                        if subscription_key in self._subscriptions:
                            # Create the subscription event variable. It is created with an invalid
                            # value and marked as uninitialized because we need to get an update
                            # response in order to set its values.  We can handle the update response
                            # in a Notify thread.
                            event_var = self._subscriptions[subscription_key]
                            event_var.update_subscription_details(sub_sid, sub_timeout)

                            self._sid_to_subscription_key_lookup[sub_sid] = subscription_key
                    finally:
                        self._subscription_lock.release()
                    
                    # Notify the coordinator which device has this subscription
                    coord.register_subscription_for_device(sub_sid, self)

            else:
                resp.raise_for_status()

        return event_var

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

