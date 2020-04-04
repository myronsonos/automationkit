"""
.. module:: akit.integration.upnp.extensions.services.standard.renderingcontrol
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing :class:`RenderingControlService` which implements
    the standard UPNP RenderingControl service.

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
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class RenderingControlService(UpnpServiceProxy, LoadableExtension):
    """
    """

    SERVICE_ID = "urn:schemas-upnp-org:serviceId:RenderingControl"
    SERVICE_TYPE = "urn:schemas-upnp-org:service:RenderingControl:1"
