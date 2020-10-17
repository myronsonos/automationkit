"""
.. module:: akit.integration.upnp.extensions.sonos.zps23
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the a Upnp device for a Sonos Zps23.

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

from akit.integration.upnp.devices.upnpdevice import UpnpDevice
from akit.integration.upnp.devices.upnprootdevice import UpnpRootDevice

from akit.integration.upnp.xml.upnpdevice1 import UpnpDevice1Device

class SonosUpnpDevice1Device(UpnpDevice1Device):
    """
    """

    @property
    def ampOnTime(self):
        rtnval = self._find_value("ampOnTime", namespaces=self._namespaces)
        return rtnval

    @property
    def apiVersion(self):
        rtnval = self._find_value("apiVersion", namespaces=self._namespaces)
        return rtnval

    @property
    def bassExtension(self):
        rtnval = self._find_value("bassExtension", namespaces=self._namespaces)
        return rtnval

    @property
    def displayName(self):
        rtnval = self._find_value("displayName", namespaces=self._namespaces)
        return rtnval

    @property
    def displayVersion(self):
        rtnval = self._find_value("displayVersion", namespaces=self._namespaces)
        return rtnval

    @property
    def extraVersion(self):
        rtnval = self._find_value("extraVersion", namespaces=self._namespaces)
        return rtnval

    @property
    def feature1(self):
        rtnval = self._find_value("feature1", namespaces=self._namespaces)
        return rtnval

    @property
    def feature2(self):
        rtnval = self._find_value("feature2", namespaces=self._namespaces)
        return rtnval

    @property
    def feature3(self):
        rtnval = self._find_value("feature3", namespaces=self._namespaces)
        return rtnval

    @property
    def flash(self):
        rtnval = self._find_value("flash", namespaces=self._namespaces)
        return rtnval

    @property
    def hardwareVersion(self):
        rtnval = self._find_value("hardwareVersion", namespaces=self._namespaces)
        return rtnval

    @property
    def internalSpeakerSize(self):
        rtnval = self._find_value("internalSpeakerSize", namespaces=self._namespaces)
        return rtnval

    @property
    def legacyCompatibleVersion(self):
        rtnval = self._find_value("legacyCompatibleVersion", namespaces=self._namespaces)
        return rtnval

    @property
    def memory(self):
        rtnval = self._find_value("memory", namespaces=self._namespaces)
        return rtnval

    @property
    def minApiVersion(self):
        rtnval = self._find_value("minApiVersion", namespaces=self._namespaces)
        return rtnval

    @property
    def minCompatibleVersion(self):
        rtnval = self._find_value("minCompatibleVersion", namespaces=self._namespaces)
        return rtnval

    @property
    def retailMode(self):
        rtnval = self._find_value("retailMode", namespaces=self._namespaces)
        return rtnval

    @property
    def roomName(self):
        rtnval = self._find_value("roomName", namespaces=self._namespaces)
        return rtnval

    @property
    def satGainOffset(self):
        rtnval = self._find_value("satGainOffset", namespaces=self._namespaces)
        return rtnval

    @property
    def seriesid(self):
        rtnval = self._find_value("seriesid", namespaces=self._namespaces)
        return rtnval

    @property
    def softwareVersion(self):
        rtnval = self._find_value("softwareVersion", namespaces=self._namespaces)
        return rtnval

    @property
    def swGen(self):
        rtnval = self._find_value("swGen", namespaces=self._namespaces)
        return rtnval

    @property
    def variant(self):
        rtnval = self._find_value("variant", namespaces=self._namespaces)
        return rtnval

    @property
    def zoneType(self):
        rtnval = self._find_value("zoneType", namespaces=self._namespaces)
        return rtnval


class SonosDevice(UpnpRootDevice):
    """
    """

    MANUFACTURER = "SonosInc"

    def __init__(self):
        super(SonosDevice, self).__init__()

        self._bood_id = None
        self._boot_seq = None
        self._household = None
        self._smart_speaker = None
        self._variant = None
        self._wifimode = None
        return

    @property
    def bootId(self):
        return self._bood_id

    @property
    def bootSeq(self):
        return self._boot_seq

    @property
    def household(self):
        return self._household

    @property
    def smartSpeaker(self):
        return self._smart_speaker

    @property
    def variant(self):
        return self._variant

    @property
    def wifiMode(self):
        return self._wifimode

    def deviceMediaRenderer(self):
        return

    def deviceMediaServer(self):
        return

    def serviceAlarmClock(self):
        svctype = 'urn:schemas-upnp-org:service:AlarmClock:1'
        svc = self.lookup_service(self.MANUFACTURER, svctype)
        return svc
    
    def serviceDeviceProperties(self):
        svctype = 'urn:schemas-upnp-org:service:DeviceProperties:1'
        svc = self.lookup_service(self.MANUFACTURER, svctype)
        return svc

    def serviceGroupManagement(self):
        svctype = 'urn:schemas-upnp-org:service:GroupManagement:1'
        svc = self.lookup_service(self.MANUFACTURER, svctype)
        return svc

    def serviceMusicService(self):
        svctype = 'urn:schemas-upnp-org:service:MusicService:1'
        svc = self.lookup_service(self.MANUFACTURER, svctype)
        return svc

    def serviceSystemProperties(self):
        svctype = 'urn:schemas-upnp-org:service:SystemProperties:1'
        svc = self.lookup_service(self.MANUFACTURER, svctype)
        return svc

    def serviceQPlay(self):
        svctype = 'urn:schemas-upnp-org:service:QPlay:1'
        svc = self.lookup_service(self.MANUFACTURER, svctype)
        return svc

    def serviceZoneTopologyGroup(self):
        svctype = 'urn:schemas-upnp-org:service:ZoneTopologyGroup:1'
        svc = self.lookup_service(self.MANUFACTURER, svctype)
        return svc

    def _consume_upnp_extra(self, extrainfo):

        if "BOOTID.UPNP.ORG" in extrainfo:
            self._bood_id = extrainfo.pop("BOOTID.UPNP.ORG")
        if "X-RINCON-BOOTSEQ" in extrainfo:
            self._boot_seq = extrainfo.pop("X-RINCON-BOOTSEQ")
        if "X-RINCON-HOUSEHOLD" in extrainfo:
            self._household = extrainfo.pop("X-RINCON-HOUSEHOLD")
        if "HOUSEHOLD.SMARTSPEAKER.AUDIO" in extrainfo:
            self._smart_speaker = extrainfo.pop("HOUSEHOLD.SMARTSPEAKER.AUDIO")
        if "X-RINCON-VARIANT" in extrainfo:
            self._variant = extrainfo.pop("X-RINCON-VARIANT")
        if "X-RINCON-WIFIMODE" in extrainfo:
            self._wifimode = extrainfo.pop("X-RINCON-WIFIMODE")

        self._extra = extrainfo
        return

    def _create_device_description_node(self, devNode, namespaces=None):
        dev_desc_node = SonosUpnpDevice1Device(devNode, namespaces=namespaces)
        return dev_desc_node

    def _process_embedded_device_node(self, devNode, namespaces=None):
        dev = UpnpDevice1Device(devNode, namespaces=namespaces)
        return dev

    def _process_other_node(self, otherNode, namespaces=None):
        return

    def _process_servicelist_node(self, listNode, namespaces=None):
        self._process_servicelist_node(self, listNode, namespaces=namespaces)
        return

    def to_dict(self, brief=False):
        dval = super(SonosDevice, self).to_dict(brief=brief)

        dval["bootId"] = self.bootId
        dval["bootSeq"] = self.bootSeq
        dval["household"] = self.household
        dval["smartSpeaker"] = self.smartSpeaker
        dval["variant"] = self.variant
        dval["wifiMode"] = self.wifiMode

        return dval
