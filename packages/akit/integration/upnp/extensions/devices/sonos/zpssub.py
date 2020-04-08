"""
.. module:: akit.integration.upnp.extensions.sonos.zps18
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the a Upnp device for a Sonos Zps18.

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

from akit.extensible import LoadableExtension

from akit.integration.upnp.extensions.devices.sonos.sonosdevice import SonosDevice
from akit.integration.upnp.devices.upnprootdevice import UpnpRootDevice

class SonosDeviceZpSub(SonosDevice, LoadableExtension):
    """
    """

    MANUFACTURER = "Sonos, Inc."
    MODEL_NUMBER = "Sub"
    MODEL_DESCRIPTION = "Sonos Sub"

    def _consume_upnp_extra(self, extrainfo):
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
