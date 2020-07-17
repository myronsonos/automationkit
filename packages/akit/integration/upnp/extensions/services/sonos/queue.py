"""
.. module:: akit.integration.upnp.extensions.services.sonos.queue
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing :class:`QueueService` which implements
    the Sonos Queue service.

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
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class QueueService(UpnpServiceProxy, LoadableExtension):
    """
    """

    SERVICE_ID = "urn:schemas-sonos-com:serviceId:Queue"
    SERVICE_TYPE = "urn:schemas-sonos-com:service:Queue:1"
