"""
.. module:: akit.integration.upnp.xml.upnpdevice1
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the Xml classes used to process the Xml content
               in a UPNP Device1 description document.

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

import json

from xml.etree.ElementTree import fromstring as xml_fromstring
from xml.etree.ElementTree import tostring as xml_tostring
from xml.etree.ElementTree import register_namespace
from xml.etree.ElementTree import dump as dump_node
from xml.etree.ElementTree import ElementTree

UPNP_DEVICE1_NAMESPACE = "urn:schemas-upnp-org:device-1-0"
UPNP_DEVICE1_TAG_PREFIX = "{urn:schemas-upnp-org:device-1-0}"

class UpnpDevice1ElementTags:
    deviceType = UPNP_DEVICE1_TAG_PREFIX + "deviceType"
    friendlyName = UPNP_DEVICE1_TAG_PREFIX + "friendlyName"
    manufacturer = UPNP_DEVICE1_TAG_PREFIX + "manufacturer"
    manufacturerURL = UPNP_DEVICE1_TAG_PREFIX + "manufacturerURL"
    modelDescription = UPNP_DEVICE1_TAG_PREFIX + "modelDescription"
    modelName = UPNP_DEVICE1_TAG_PREFIX + "modelName"
    modelNumber = UPNP_DEVICE1_TAG_PREFIX + "modelNumber"
    modelURL = UPNP_DEVICE1_TAG_PREFIX + "modelURL"
    serialNumber = UPNP_DEVICE1_TAG_PREFIX + "serialNumber"
    UDN = UPNP_DEVICE1_TAG_PREFIX + "UDN"
    UPC = UPNP_DEVICE1_TAG_PREFIX + "UPC"
    presentationURL = UPNP_DEVICE1_TAG_PREFIX + "presentationURL"
    deviceList = UPNP_DEVICE1_TAG_PREFIX + "deviceList"
    iconList = UPNP_DEVICE1_TAG_PREFIX + "iconList"
    serviceList = UPNP_DEVICE1_TAG_PREFIX + "serviceList"

class UpnpDevice1Icon:
    """
        <icon>
            <id>0</id>
            <mimetype>image/png</mimetype>
            <width>48</width>
            <height>48</height>
            <depth>24</depth>
            <url>/img/icon-S18.png</url>
        </icon>
    """
    def __init__(self, iconNode, namespaces=None):
        self._iconNode = iconNode
        self._namespaces = namespaces
        return

    @property
    def depth(self):
        rtnval = self._find_value("depth", namespaces=self._namespaces)
        return rtnval

    @property
    def height(self):
        rtnval = self._find_value("height", namespaces=self._namespaces)
        return rtnval

    @property
    def id(self):
        rtnval = self._find_value("id", namespaces=self._namespaces)
        return rtnval

    @property
    def url(self):
        rtnval = self._find_value("url", namespaces=self._namespaces)
        return rtnval

    @property
    def mimetype(self):
        rtnval = self._find_value("mimetype", namespaces=self._namespaces)
        return rtnval

    @property
    def width(self):
        rtnval = self._find_value("width", namespaces=self._namespaces)
        return rtnval

    @property
    def xmlNode(self):
        return self._iconNode

    def to_dict(self):
        dval = {
            "depth": self.depth,
            "height": self.height,
            "id": self.id,
            "url": self.url,
            "mimetype": self.mimetype,
            "width": self.width
        }
        return dval

    def to_json(self):
        dval = self.to_dict()
        json_str = json.dumps(dval, indent=4)
        return json_str

    def _find_value(self, path, namespaces=None):
        rtnval = None
        try:
            valNode = self._iconNode.find(path, namespaces=self._namespaces)
            if valNode is not None:
                rtnval = valNode.text
        except Exception as err:
            print(str(err))
            register_namespace('', None)
            xmlcontent = xml_tostring(self._iconNode)
            print(xmlcontent)
            print("")
        return rtnval

class UpnpDevice1Service:
    """
        <service>
            <serviceType>urn:schemas-upnp-org:service:AlarmClock:1</serviceType>
            <serviceId>urn:upnp-org:serviceId:AlarmClock</serviceId>
            <controlURL>/AlarmClock/Control</controlURL>
            <eventSubURL>/AlarmClock/Event</eventSubURL>
            <SCPDURL>/xml/AlarmClock1.xml</SCPDURL>
        </service>
    """
    def __init__(self, svcNode, namespaces=None):
        self._svcNode = svcNode
        self._namespaces = namespaces
        return

    @property
    def controlURL(self):
        rtnval = self._find_value("controlURL", namespaces=self._namespaces)
        return rtnval

    @property
    def eventSubURL(self):
        rtnval = self._find_value("eventSubURL", namespaces=self._namespaces)
        return rtnval

    @property
    def SCPDURL(self):
        rtnval = self._find_value("SCPDURL", namespaces=self._namespaces)
        return rtnval

    @property
    def serviceId(self):
        rtnval = self._find_value("serviceId", namespaces=self._namespaces)
        return rtnval

    @property
    def serviceType(self):
        rtnval = self._find_value("serviceType", namespaces=self._namespaces)
        return rtnval

    @property
    def xmlNode(self):
        return self._svcNode

    def to_dict(self):
        dval = {
            "controlURL": self.controlURL,
            "eventSubURL": self.eventSubURL,
            "SCPDURL": self.SCPDURL,
            "serviceId": self.serviceId,
            "serviceType": self.serviceType
        }
        return dval

    def to_json(self):
        dval = self.to_dict()
        json_str = json.dumps(dval, indent=4)
        return json_str

    def _find_value(self, path, namespaces=None):
        rtnval = None
        valNode = self._svcNode.find(path, namespaces=self._namespaces)
        if valNode is not None:
            try:
                rtnval = valNode.text
            except:
                dump_node(self._svcNode)
                print("")
        else:
            dump_node(self._svcNode)
            print("")
        return rtnval



class UpnpDevice1SpecVersion:
    """
    <specVersion>
        <major>1</major>
        <minor>0</minor>
    </specVersion>
    """
    def __init__(self, verNode, namespaces=None):
        self._verNode = verNode
        self._namespaces=namespaces
        return

    @property
    def major(self):
        rtnval = self._find_value("major", namespaces=self._namespaces)
        return rtnval

    @property
    def minor(self):
        rtnval = self._find_value("minor", namespaces=self._namespaces)
        return rtnval

    @property
    def xmlNode(self):
        return self._verNode

    def to_dict(self):
        dval = {
            "major": self.major,
            "minor": self.minor
        }
        return dval

    def to_json(self):
        dval = self.to_dict()
        json_str = json.dumps(dval, indent=4)
        return json_str

    def _find_value(self, path, namespaces=None):
        rtnval = None
        try:
            valNode = self._verNode.find(path, namespaces=self._namespaces)
            if valNode is not None:
                rtnval = valNode.text
        except Exception as err:
            print(str(err))
            register_namespace('', None)
            xmlcontent = xml_tostring(self._verNode)
            print(xmlcontent)
            print("")
        return rtnval


class UpnpDevice1Device:
    """
        The UPNP Root device is the base device for the hierarchy that is
        associated with a unique network devices location.  The :class:`RootDevice`
        and its subdevices are linked by thier location url. 

        http://www.upnp.org/specs/arch/UPnP-arch-DeviceArchitecture-v1.0.pdf

        ```
        <device>
            <deviceType>urn:schemas-upnp-org:device:deviceType:v</deviceType>
            <friendlyName>short user-friendly title</friendlyName>
            <manufacturer>manufacturer name</manufacturer>
            <manufacturerURL>URL to manufacturer site</manufacturerURL>
            <modelDescription>long user-friendly title</modelDescription>
            <modelName>model name</modelName>
            <modelNumber>model number</modelNumber>
            <modelURL>URL to model site</modelURL>
            <serialNumber>manufacturer's serial number</serialNumber>
            <UDN>uuid:UUID</UDN>
            <UPC>Universal Product Code</UPC>
            <iconList>
                <icon>
                <mimetype>image/format</mimetype>
                <width>horizontal pixels</width>
                <height>vertical pixels</height>
                <depth>color depth</depth>
                <url>URL to icon</url>
                </icon>
                XML to declare other icons, if any, go here
            </iconList>
            <serviceList>
                <service>
                    <serviceType>urn:schemas-upnp-org:service:serviceType:v</serviceType>
                    <serviceId>urn:upnp-org:serviceId:serviceID</serviceId>
                    <SCPDURL>URL to service description</SCPDURL>
                    <controlURL>URL for control</controlURL>
                    <eventSubURL>URL for eventing</eventSubURL>
                </service>
                Declarations for other services defined by a UPnP Forum working committee (if any)
                go here Declarations for other services added by UPnP vendor (if any) go here
            </serviceList>
            <presentationURL>URL for presentation</presentationURL>
        </device>
        ```
    """

    def __init__(self, devNode, namespaces=None):
        """
            Creates a root device object.
        """
        # Fields populated from XML according the the device spec
        self._devNode = devNode
        self._namespaces = namespaces
        return

    @property
    def deviceList(self):
        resultList = []
        listNode = self._devNode.find("deviceList", namespaces=self._namespaces)
        if listNode is not None:
            resultList = [ UpnpDevice1Device(child, namespaces=self._namespaces) for child in listNode ]
        return resultList

    @property
    def iconList(self):
        resultList = []
        listNode = self._devNode.find("iconList", namespaces=self._namespaces)
        if listNode is not None:
            resultList = [ UpnpDevice1Icon(child, namespaces=self._namespaces) for child in listNode ]
        return resultList

    @property
    def serviceList(self):
        listNode = self._devNode.find("serviceList", namespaces=self._namespaces)
        if listNode is not None:
            resultList = [ UpnpDevice1Service(child, namespaces=self._namespaces) for child in listNode ]
        return resultList

    @property
    def deviceType(self):
        rtnval = self._find_value("deviceType", namespaces=self._namespaces)
        return rtnval

    @property
    def friendlyName(self):
        rtnval = self._find_value("friendlyName", namespaces=self._namespaces)
        return rtnval

    @property
    def MACAddress(self):
        rtnval = self._find_value("MACAddress", namespaces=self._namespaces)
        return rtnval

    @property
    def manufacturer(self):
        rtnval = self._find_value("manufacturer", namespaces=self._namespaces)
        return rtnval

    @property
    def manufacturerURL(self):
        rtnval = self._find_value("manufacturerURL", namespaces=self._namespaces)
        return rtnval

    @property
    def modelDescription(self):
        rtnval = self._find_value("modelDescription", namespaces=self._namespaces)
        return rtnval

    @property
    def modelName(self):
        rtnval = self._find_value("modelName", namespaces=self._namespaces)
        return rtnval

    @property
    def modelNumber(self):
        rtnval = self._find_value("modelNumber", namespaces=self._namespaces)
        return rtnval

    @property
    def modelURL(self):
        rtnval = self._find_value("modelURL", namespaces=self._namespaces)
        return rtnval

    @property
    def serialNumber(self):
        rtnval = self._find_value("serialNumber", namespaces=self._namespaces)
        return rtnval

    @property
    def UDN(self):
        rtnval = self._find_value("UDN", namespaces=self._namespaces)
        return rtnval

    @property
    def UPC(self):
        rtnval = self._find_value("UPC", namespaces=self._namespaces)
        return rtnval

    @property
    def presentationURL(self):
        rtnval = self._find_value("presentationURL", namespaces=self._namespaces)
        return rtnval

    @property
    def xmlNode(self):
        return self._devNode

    def to_dict(self, brief=False):

        dval = {}

        for nxt_child in self._devNode:
            # We only use the generic value processing for
            # children that are singular
            if len(nxt_child) == 0:
                nxt_tag_full = nxt_child.tag
                start_index = nxt_tag_full.find("}") + 1
                nxt_tag = nxt_tag_full[start_index:]
                dval[nxt_tag] = nxt_child.text

        firstIcon = None
        if not brief:
            device_list = []
            for dvc in self.deviceList:
                lival = dvc.to_dict()
                device_list.append(lival)
            dval["deviceList"] = device_list

            icon_list = []
            for icon in self.iconList:
                lival = icon.to_dict()
                icon_list.append(lival)
                if firstIcon is None:
                    firstIcon = lival
            dval["iconList"] = icon_list

            service_list = []
            for svc in self.serviceList:
                lsval = svc.to_dict()
                service_list.append(lsval)
            dval["serviceList"] = service_list
        else:
            for icon in self.iconList:
                lival = icon.to_dict()
                if firstIcon is None:
                    firstIcon = lival
                    break

        dval["firstIcon"] = firstIcon

        return dval

    def to_json(self, brief=False):
        dval = self.to_dict(brief=brief)

        json_str = json.dumps(dval, indent=4)
        return json_str

    def _find_value(self, path, namespaces=None):
        rtnval = None
        try:
            valNode = self._devNode.find(path, namespaces=self._namespaces)
            if valNode is not None:
                rtnval = valNode.text
        except Exception as err:
            print(str(err))
            register_namespace('', None)
            xmlcontent = xml_tostring(self._devNode)
            print(xmlcontent)
            print("")
        return rtnval
