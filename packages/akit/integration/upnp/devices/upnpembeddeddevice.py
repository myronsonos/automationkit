"""
.. module:: akit.integration.upnp.device.upnpembeddeddevice
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the :class:`UpnpEmbeddedDevice` class and associated diagnostic.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>

"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@automationmojo.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import requests
import traceback

from akit.exceptions import AKitSemanticError
from akit.integration.upnp.protocols.msearch import MSearchKeys
from akit.integration.upnp.devices.upnpdevice import UpnpDevice

class UpnpEmbeddedDevice(UpnpDevice):
    """
        The UPNP Embedded device is the base device for the hierarchy that is
        associated with a unique network devices location.  The :class:`UpnpEmbeddedDevice`
        and its subdevices are linked by thier location url. 

        http://www.upnp.org/specs/arch/UPnP-arch-DeviceArchitecture-v1.0.pdf
    """

    def __init__(self):
        """
            Creates a root device object.
        """
        super(UpnpEmbeddedDevice, self).__init__()

        self._decription = None
        return

    def update_description(self, host, baseUrl, description):
        self._host = host
        self._urlBase = baseUrl
        self._decription = description
        return

    def _populate_embedded_devices(self, factory, description):
        raise AKitSemanticError("Embedded devices inside an embedded device is currently not supported.")
        return
