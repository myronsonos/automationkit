"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class WANEthernetLinkConfigServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'WANEthernetLinkConfig' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:WANEthernetLinkConfig:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:WANEthernetLinkConfig'


    def get_EthernetLinkStatus(self):
        """
            Gets the "EthernetLinkStatus" variable.
        """
        rval = self.proxy_get_variable_value("EthernetLinkStatus")
        return rval


    def set_EthernetLinkStatus(self, val):
        """
            Sets the "EthernetLinkStatus" variable.
        """
        self.proxy_set_variable_value("EthernetLinkStatus", val)
        return


    def action_GetEthernetLinkStatus(self):
        """
            Calls the GetEthernetLinkStatus action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetEthernetLinkStatus", arguments=arguments)

        (NewEthernetLinkStatus,) = out_params

        return NewEthernetLinkStatus

