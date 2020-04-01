"""
.. module:: akit.integration.upnp.devices.embedded.mediarenderer
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the a Upnp device for a UpnpEmbeddedDevice.

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

from akit.integration.upnp.devices.upnpembeddeddevice import UpnpEmbeddedDevice

class MediaServerDevice(UpnpEmbeddedDevice, LoadableExtension):
    """
    """

    DEVICE_TYPE = "urn:schemas-upnp-org:device:MediaServer:1"
