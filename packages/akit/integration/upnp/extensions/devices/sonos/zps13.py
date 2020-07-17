"""
.. module:: akit.integration.upnp.extensions.sonos.zps13
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the a Upnp device for a Sonos Zps13.

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

from akit.extensible import LoadableExtension

from akit.integration.upnp.extensions.devices.sonos.sonosdevice import SonosDevice
from akit.integration.upnp.devices.upnprootdevice import UpnpRootDevice

class SonosDeviceZpS13(SonosDevice, LoadableExtension):
    """
    """

    MANUFACTURER = "Sonos, Inc."
    MODEL_NUMBER = "S13"
    MODEL_DESCRIPTION = "Sonos One"

    def serviceAlarmClock(self):
        svc = self.lookup_service("urn:schemas-upnp-org:service:AlarmClock:1")
        return svc
    
    def serviceDeviceProperties(self):
        svc = self.lookup_service("urn:schemas-upnp-org:service:DeviceProperties:1")
        return svc

    def serviceGroupManagement(self):
        svc = self.lookup_service("urn:schemas-upnp-org:service:GroupManagement:1")
        return svc

    def serviceMusicService(self):
        svc = self.lookup_service("urn:schemas-upnp-org:service:MusicService:1")
        return svc

    def serviceSystemProperties(self):
        svc = self.lookup_service("urn:schemas-upnp-org:service:SystemProperties:1")
        return svc

    def serviceQPlay(self):
        svc = self.lookup_service("urn:schemas-upnp-org:service:QPlay:1")
        return svc

    def serviceZoneTopologyGroup(self):
        svc = self.lookup_service("urn:schemas-upnp-org:service:ZoneTopologyGroup:1")
        return svc