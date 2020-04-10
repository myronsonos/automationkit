"""
.. module:: akit.integration.upnp.device.upnpdevice
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the :class:`UpnpDevice` class and associated diagnostic.

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

from akit.exceptions import AKitNotOverloadedError

from akit.integration.upnp.upnpprotocol import MSearchKeys

class UpnpDevice:
    """
        The UPNP Root device is the base device for the hierarchy that is
        associated with a unique network devices location.  The :class:`RootDevice`
        and its subdevices are linked by thier location url. 

        http://www.upnp.org/specs/arch/UPnP-arch-DeviceArchitecture-v1.0.pdf
    """

    DEVICE_IDENTIFIER = None

    def __init__(self):
        """
            Creates a root device object.
        """
        super(UpnpDevice, self).__init__()
        
        self._description = None
        return

    @property
    def description(self):
        return self._description

    def _populate_embedded_devices(self, factory, description):
        raise AKitNotOverloadedError("UpnpDevice._populate_embedded_devices: must be overridden.")
        return

    def _populate_icons(self):
        for icon in self._description.iconList:
            pass
        return

    def _populate_services(self, factory, description):
        raise AKitNotOverloadedError("UpnpDevice._populate_services: must be overridden.")
        return
