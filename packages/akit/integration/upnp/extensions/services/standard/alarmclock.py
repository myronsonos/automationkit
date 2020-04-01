"""
.. module:: akit.integration.upnp.extensions.services.standard.alarmclock
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing :class:`AlarmClockService` which implements
    the standard UPNP AlarmClock service.

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
from akit.integration.upnp.services.upnpservice import UpnpService

class AlarmClockService(UpnpService, LoadableExtension):
    """
    """

    SERVICE_ID = "urn:schemas-upnp-org:serviceId:AlarmClock"
    SERVICE_TYPE = "urn:schemas-upnp-org:service:AlarmClock:1"
