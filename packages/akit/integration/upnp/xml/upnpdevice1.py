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

from xml.etree.ElementTree import fromstring as parsefromstring
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
        self._depth = iconNode.find("depth", namespaces=namespaces)
        self._height = iconNode.find("height", namespaces=namespaces)
        self._id = iconNode.find("id", namespaces=namespaces)
        self._mimetype = iconNode.find("mimetype", namespaces=namespaces)
        self._url = iconNode.find("url", namespaces=namespaces)
        self._width = iconNode.find("width", namespaces=namespaces)
        return

    @property
    def depth(self):
        return self._depth

    @property
    def height(self):
        return self._height

    @property
    def id(self):
        return self._id

    @property
    def url(self):
        return self._url

    @property
    def mimetype(self):
        return self._mimetype

    @property
    def width(self):
        return self._width

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
        self._controlURL = svcNode.find("controlURL", namespaces=namespaces)
        self._eventSubURL = svcNode.find("eventSubURL", namespaces=namespaces)
        self._SCPDURL = svcNode.find("SCPDURL", namespaces=namespaces)
        self._serviceId = svcNode.find("serviceId", namespaces=namespaces)
        self._serviceType = svcNode.find("serviceType", namespaces=namespaces)
        return

    @property
    def controlURL(self):
        return self._controlURL

    @property
    def eventSubURL(self):
        return self._eventSubURL

    @property
    def SCPDURL(self):
        return self._SCPDURL

    @property
    def serviceId(self):
        return self._serviceId

    @property
    def serviceType(self):
        return self._serviceType

class UpnpDevice1SpecVersion:
    """
    <specVersion>
        <major>1</major>
        <minor>0</minor>
    </specVersion>
    """
    def __init__(self, iconNode, namespaces=None):
        self._major = iconNode.find("major", namespaces=namespaces)
        self._minor = iconNode.find("minor", namespaces=namespaces)
        return

    @property
    def major(self):
        return self._major

    @property
    def minor(self):
        return self._minor


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
        self._deviceType = None
        self._friendlyName = None
        self._manufacturer = None
        self._manufacturerURL = None
        self._modelDescription = None
        self._modelName = None
        self._modelNumber = None
        self._modelURL = None
        self._serialNumber = None
        self._UDN = None
        self._UPC = None
        self._presentationURL = None

        self._deviceList = None
        self._iconList = None
        self._serviceList = None

        self._process_device_node(devNode, namespaces=namespaces)
        return

    @property
    def cachecontrol(self):
        return self._cachecontrol

    @property
    def ext(self):
        return self._ext

    @property
    def location(self):
        return self._location

    @property
    def server(self):
        return self._server

    @property
    def deviceType(self):
        return self._deviceType

    @property
    def friendlyName(self):
        return self._friendlyName

    @property
    def manufacturer(self):
        return self._manufacturer

    @property
    def manufacturerURL(self):
        return self._manufacturerURL

    @property
    def modelDescription(self):
        return self._modelDescription

    @property
    def modelName(self):
        return self._modelName

    @property
    def modelNumber(self):
        return self._modelNumber

    @property
    def modelURL(self):
        return self._modelURL

    @property
    def serialNumber(self):
        return self._serialNumber

    @property
    def UDN(self):
        return self._UDN

    @property
    def UPC(self):
        return self._UPC

    @property
    def presentationURL(self):
        return self._presentationURL

    def _process_device_node(self, devNode, namespaces=None):

        for child in devNode:
            if child.tag == UpnpDevice1ElementTags.deviceType:
                self._deviceType = child.text
            elif child.tag == UpnpDevice1ElementTags.friendlyName:
                self._friendlyName = child.text
            elif child.tag == UpnpDevice1ElementTags.manufacturer:
                self._manufacturer = child.text
            elif child.tag == UpnpDevice1ElementTags.manufacturerURL:
                self._manufacturerURL = child.text
            elif child.tag == UpnpDevice1ElementTags.modelDescription:
                self._modelDescription = child.text
            elif child.tag == UpnpDevice1ElementTags.modelName:
                self._modelName = child.text
            elif child.tag == UpnpDevice1ElementTags.modelNumber:
                self._modelNumber = child.text
            elif child.tag == UpnpDevice1ElementTags.modelURL:
                self._modelURL = child.text
            elif child.tag == UpnpDevice1ElementTags.serialNumber:
                self._serialNumber = child.text
            elif child.tag == UpnpDevice1ElementTags.UDN:
                self._UDN = child.text
            elif child.tag == UpnpDevice1ElementTags.UPC:
                self._UPC = child.text
            elif child.tag == UpnpDevice1ElementTags.presentationURL:
                self._presentationURL = child.text
            # List based elements
            elif child.tag == UpnpDevice1ElementTags.deviceList:
                self._process_devicelist_node(child, namespaces=namespaces)
            elif child.tag == UpnpDevice1ElementTags.iconList:
                self._process_iconlist_node(child, namespaces=namespaces)
            elif child.tag == UpnpDevice1ElementTags.serviceList:
                self._process_servicelist_node(child, namespaces=namespaces)
            else:
                self._process_other_node(child, namespaces=namespaces)

        return

    def _process_devicelist_node(self, listNode, namespaces=None):
        """
        """
        self._deviceList = [ self._process_embedded_device_node(child, namespaces=namespaces) for child in listNode ]
        return

    def _process_iconlist_node(self, listNode, namespaces=None):
        """
        """
        self._iconList = [ UpnpDevice1Icon(child, namespaces=namespaces) for child in listNode ]
        return

    def _process_embedded_device_node(self, devNode, namespaces=None):
        dev = UpnpDevice1Device(devNode, namespaces=namespaces)
        return dev

    def _process_other_node(self, otherNode, namespaces=None):
        
        tag = otherNode.tag
        namespace = ""
        if "}" in tag:
            namespace, tag = tag.split("}")
            namespace = namespace[1:]

        if len(otherNode) == 0:
            mvarname = "" + tag
            setattr(self, mvarname, otherNode.text)
        else:
            print("Found an unknown list node ns=%s tag=%s" % (namespace, tag))

        return

    def _process_servicelist_node(self, listNode, namespaces=None):
        """
        """
        self._serviceList = [ UpnpDevice1Service(child) for child in listNode ]
        return

