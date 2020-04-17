"""
.. module:: akit.integration.upnp.extensions.services.standard.avtransport
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing :class:`AVTransportService` which implements
    the standard UPNP AVTransport service.

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

class AVTransportService(UpnpServiceProxy, LoadableExtension):
    """
    """

    SERVICE_ID = "urn:schemas-upnp-org:serviceId:AVTransport"
    SERVICE_TYPE = "urn:schemas-upnp-org:service:AVTransport:1"

    def get_TransportState(self):
        """
            Gets the 'TransportState' variable.
        """

        value = self.proxy_get_variable_value("TransportState")

        return value

    def set_TransportState(self, value):
        """
            Sets the 'TransportState' variable.

            :param value: The value to set this variable to.
        """

        self.proxy_set_variable_value("TransportState", value)

        return

    def action_SetAVTransportURI(self, InstanceID, CurrentURI, CurrentURIMetaData):
        """
            Calls the SetAVTransportURI action.
        """
        out_params = self.proxy_call_action("SetAVTransportURI", InstanceID, CurrentURI, CurrentURIMetaData)

        (result,) = out_params

        return result
