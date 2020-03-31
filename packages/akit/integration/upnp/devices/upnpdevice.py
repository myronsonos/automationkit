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

from akit.integration.upnp.protocols.msearch import MSearchKeys

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
        self._extra = {}
        self._cachecontrol = None
        self._ext = None
        self._location = None
        self._server = None
        self._st = None
        self._usn = None
        return

    @property
    def cachecontrol(self):
        return self._cachecontrol

    @property
    def ext(self):
        return self._ext

    @property
    def extra(self):
        return self._extra

    @property
    def location(self):
        return self._location

    @property
    def server(self):
        return self._server

    def initialize(self, location: str, devinfo: dict):
        """
        """
        self._location = location
        self._cachecontrol = devinfo.pop(MSearchKeys.CACHE_CONTROL)
        self._ext = devinfo.pop(MSearchKeys.EXT)
        self._server = devinfo.pop(MSearchKeys.SERVER)
        self._st = devinfo.pop(MSearchKeys.ST)
        self._usn = devinfo.pop(MSearchKeys.USN)

        self._consume_upnp_extra(devinfo)
        return

    def _consume_upnp_extra(self, extrainfo):
        self._extra = extrainfo
        return

