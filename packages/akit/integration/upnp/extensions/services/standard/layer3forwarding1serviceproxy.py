"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class Layer3Forwarding1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'Layer3Forwarding1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:Layer3Forwarding:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:Layer3Forwarding'


    def get_DefaultConnectionService(self):
        """
            Gets the "DefaultConnectionService" variable.
        """
        rval = self.proxy_get_variable_value("DefaultConnectionService")
        return rval


    def set_DefaultConnectionService(self, val):
        """
            Sets the "DefaultConnectionService" variable.
        """
        self.proxy_set_variable_value("DefaultConnectionService", val)
        return


    def action_GetDefaultConnectionService(self):
        """
            Calls the GetDefaultConnectionService action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDefaultConnectionService", arguments=arguments)

        (NewDefaultConnectionService,) = out_params

        return NewDefaultConnectionService


    def action_SetDefaultConnectionService(self, NewDefaultConnectionService):
        """
            Calls the SetDefaultConnectionService action.
        """
        arguments = {
            "NewDefaultConnectionService": NewDefaultConnectionService,
        }

        out_params = self.proxy_call_action("SetDefaultConnectionService", arguments=arguments)

        (result,) = out_params

        return result

