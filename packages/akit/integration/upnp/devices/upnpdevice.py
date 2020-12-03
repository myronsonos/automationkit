"""
.. module:: upnpdevice
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the :class:`UpnpDevice` class and associated diagnostic.

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

import threading
import weakref

from xml.etree.ElementTree import fromstring as xml_fromstring
from xml.etree.ElementTree import tostring as xml_tostring
from xml.etree.ElementTree import register_namespace
from xml.etree.ElementTree import dump as dump_node
from xml.etree.ElementTree import ElementTree

import requests

from requests.compat import urljoin

from akit.exceptions import AKitNotOverloadedError, AKitCommunicationsProtocolError
from akit.extensible import generate_extension_key
from akit.paths import normalize_name_for_path

from akit.integration.upnp.upnpprotocol import MSearchKeys

UPNP_SERVICE1_NAMESPACE = "urn:schemas-upnp-org:service-1-0"

from akit.paths import normalize_name_for_path


class UpnpDevice:
    """
        The UPNP Root device is the base device for the hierarchy that is
        associated with a unique network devices location.  The :class:`RootDevice`
        and its subdevices are linked by thier location url.

        http://www.upnp.org/specs/arch/UPnP-arch-DeviceArchitecture-v1.0.pdf
    """

    MANUFACTURER = "unknown"
    MODEL_NUMBER = "unknown"
    MODEL_DESCRIPTION = "unknown"

    def __init__(self):
        """
            Creates a root device object.
        """
        super(UpnpDevice, self).__init__()

        self._description = None
        self._host = None
        self._urlBase = None

        self._device_lock = threading.RLock()

        self._services_descriptions = {}
        self._services = {}

        return

    @property
    def description(self):
        return self._description

    @property
    def host(self):
        return self._host

    @property
    def services(self):
        service_list = None

        self._device_lock.acquire()
        try:
            service_list = [svc for svc in self._services.values()]
        finally:
            self._device_lock.release()

        return service_list

    @property
    def services_descriptions(self):
        return self._services_descriptions

    @property
    def URLBase(self):
        return self._urlBase

    def get_service_description(self, service_type):

        svc_content = None

        devDesc = self.description

        for nxtsvc in devDesc.serviceList:
            if nxtsvc.serviceType == service_type:
                fullurl = self.URLBase.rstrip("/") + "/" + nxtsvc.SCPDURL.lstrip("/")

                resp = requests.get(fullurl)
                if resp.status_code == 200:
                    svc_content = resp.text
                    break

        return svc_content

    def lookup_service(self, serviceManufacturer, serviceType):
        serviceManufacturer = normalize_name_for_path(serviceManufacturer)
        svckey = generate_extension_key(serviceManufacturer, serviceType)

        self._device_lock.acquire()
        try:
            svc = self._services[svckey]
        finally:
            self._device_lock.release()

        return svc

    def to_dict(self, brief=False):

        dval = None
        desc = self._description

        if desc is not None:
            dval = desc.to_dict(brief=brief)

            dval["URLBase"] = self.URLBase

            if not brief:
                serviceDescList = []
                serviceList = dval["serviceList"]
                for svc_info in serviceList:
                    svc_type = svc_info["serviceType"]
                    sdurl = self._urlBase.rstrip("/") + "/" + svc_info["SCPDURL"].lstrip("/")
                    sdesc = self._process_full_service_description(sdurl)
                    sdesc["serviceType"] = svc_type
                    serviceDescList.append(sdesc)

                dval["serviceDescriptionList"] = serviceDescList

        return dval

    def to_json(self, brief=False):
        json_str = None
        desc = self._description

        if desc is not None:
            json_str = self._description.to_json(brief=brief)

        return json_str

    def _locked_populate_embedded_device_descriptions(self, factory, description):
        raise AKitNotOverloadedError("UpnpDevice._populate_embedded_devices: must be overridden.")
        return

    def _locked_populate_icons(self):

        desc = self._description

        if desc is not None:
            for icon in desc.iconList:
                pass

        return

    def _locked_populate_services_descriptions(self, factory, description):

        for serviceInfo in description.serviceList:
            serviceManufacturer = normalize_name_for_path(serviceInfo.serviceManufacturer)
            serviceType = serviceInfo.serviceType

            svckey = generate_extension_key(serviceManufacturer, serviceType)
            if serviceType not in self._services_descriptions:
                self._services_descriptions[svckey] = serviceInfo

                svc_inst = factory.create_service_instance(serviceManufacturer, serviceType)
                if svc_inst is not None:
                    device_ref = weakref.ref(self)
                    svc_inst._proxy_link_service_to_device(device_ref, serviceInfo)
                    self._services[svckey] = svc_inst
            else:
                svc_inst = self._services[svckey]

        return

    def _locked_process_full_service_description(self, sdurl):
        svcdesc = None

        resp = requests.get(sdurl)
        if resp.status_code == 200:
            svcdesc = {}

            namespaces = {"": UPNP_SERVICE1_NAMESPACE}

            try:
                xml_content = resp.text
                descDoc = xml_fromstring(xml_content)

                specVersionNode = descDoc.find("specVersion", namespaces=namespaces)
                verInfo = self._process_node_spec_version(specVersionNode, namespaces=namespaces)
                svcdesc["specVersion"] = verInfo

                serviceStateTableNode = descDoc.find("serviceStateTable", namespaces=namespaces)
                variablesTable, typesTable, eventsTable = self._process_node_state_table(serviceStateTableNode, namespaces=namespaces)
                svcdesc["variablesTable"] = variablesTable
                svcdesc["typesTable"] = typesTable
                svcdesc["eventsTable"] = eventsTable

                actionListNode = descDoc.find("actionList", namespaces=namespaces)
                actionsTable = self._process_node_action_list(actionListNode, namespaces=namespaces)
                svcdesc["actionsTable"] = actionsTable
            except:
                print("Service Description Failure: %s" % sdurl)
                raise

        return svcdesc

    def _locked_process_node_action_list(self, actionListNode, namespaces=None):
        actionTable = {}

        actionNodeList = actionListNode.findall("action", namespaces=namespaces)
        for actionNode in actionNodeList:
            actionName = actionNode.find("name", namespaces=namespaces).text
            actionArgs = {}

            argumentListNode = actionNode.find("argumentList", namespaces=namespaces)
            if argumentListNode is not None:
                argumentNodeList = argumentListNode.findall("argument", namespaces=namespaces)
                for argumentNode in argumentNodeList:
                    argName = argumentNode.find("name", namespaces=namespaces).text
                    argDirection = argumentNode.find("direction", namespaces=namespaces).text

                    argRelStateVar = None
                    argRelStateNode = argumentNode.find("relatedStateVariable", namespaces=namespaces)
                    if argRelStateNode is not None:
                        argRelStateVar = argRelStateNode.text

                    actionArgs[argName] = {
                        "name": argName,
                        "direction": argDirection,
                        "relatedStateVariable": argRelStateVar
                        }

            actionTable[actionName] = {
                    "name": actionName,
                    "arguments" : actionArgs
                }

        return actionTable

    def _locked_process_node_spec_version(self, specVersionNode, namespaces=None):
        verInfo = {}

        verInfo["major"] = specVersionNode.find("major", namespaces=namespaces).text
        verInfo["minor"] = specVersionNode.find("minor", namespaces=namespaces).text

        return verInfo

    def _locked_process_node_state_table(self, serviceStateTableNode, namespaces=None):
        variablesTable = {}
        typesTable = {}
        eventsTable = {}

        stateVariableList = serviceStateTableNode.findall("stateVariable", namespaces=namespaces)
        for stateVariableNode in stateVariableList:
            name = stateVariableNode.find("name", namespaces=namespaces).text
            dataType = stateVariableNode.find("dataType", namespaces=namespaces).text

            varInfo = { "name": name, "dataType": dataType}
            if name.startswith("A_ARG_TYPE_"):
                typesTable[name] = varInfo
            else:
                variablesTable[name] = varInfo

                sendEvents = "no"
                if "sendEvents" in stateVariableNode.attrib:
                    sendEvents = stateVariableNode.attrib["sendEvents"]

                if sendEvents == "yes":
                    eventsTable[name] = varInfo

        return variablesTable, typesTable, eventsTable
