"""
.. module:: akit.integration.upnp.extensions.services.tencent.qplay
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing :class:`QPlayService` which implements
    the tencent UPNP QPlay service.

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

class QPlayService(UpnpService, LoadableExtension):
    """
    """

    SERVICE_ID = "urn:schemas-tencent-com:serviceId:QPlay"
    SERVICE_TYPE = "urn:schemas-tencent-com:service:QPlay:1"
