"""
.. module:: akit.integration.upnp.devices.extensions.sonos.zps23
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the a Upnp device for a Sonos Zps23.

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

from akit.integration.upnp.devices.upnpdevice import UpnpDevice
from akit.integration.upnp.devices.upnprootdevice import UpnpRootDevice

class SonosDevice(UpnpRootDevice):
    """
    """

    def __init__(self):
        self._bood_id = None
        self._boot_seq = None
        self._household = None
        self._smart_speaker = None
        self._variant = None
        self._wifimode = None
        return

    @property
    def boot_id(self):
        return self._bood_id

    @property
    def boot_seq(self):
        return self._boot_seq

    @property
    def household(self):
        return self._household

    @property
    def smart_speaker(self):
        return self._smart_speaker

    @property
    def variant(self):
        return self._variant

    @property
    def wifimode(self):
        return self._wifimode

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

    def _process_embedded_device_node(self, devNode, namespaces=None):
        dev = UpnpDevice1Device(child, namespaces=namespaces)
        return dev

    def _process_other_node(self, otherNode, namespaces=None):
        return

    def _process_servicelist_node(self, listNode, namespaces=None):
        self._process_servicelist_node(self, listNode, namespaces=namespaces)
        return
