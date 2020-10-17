"""
.. module:: akit.integration.upnp.extensions.sonos.zps14
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the a Upnp device for a Sonos Zps14.

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

from akit.integration.upnp.extensions.standard.rootdevices.sonos.sonosdevice import SonosDevice
from akit.integration.upnp.devices.upnprootdevice import UpnpRootDevice

class SonosDeviceZpS14(SonosDevice, LoadableExtension):
    """
    """

    MANUFACTURER = "Sonos, Inc."
    MODEL_NUMBER = "S14"
    MODEL_DESCRIPTION = "Sonos Beam"


