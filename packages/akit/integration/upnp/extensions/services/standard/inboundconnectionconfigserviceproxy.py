"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class InboundConnectionConfigServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'InboundConnectionConfig' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:InboundConnectionConfig:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:InboundConnectionConfig'


    def get_DynamicDNSConfigInfo(self):
        """
            Gets the "DynamicDNSConfigInfo" variable.
        """
        rval = self.proxy_get_variable_value("DynamicDNSConfigInfo")
        return rval


    def set_DynamicDNSConfigInfo(self, val):
        """
            Sets the "DynamicDNSConfigInfo" variable.
        """
        self.proxy_set_variable_value("DynamicDNSConfigInfo", val)
        return


    def get_DynamicDNSSupportedProtocols(self):
        """
            Gets the "DynamicDNSSupportedProtocols" variable.
        """
        rval = self.proxy_get_variable_value("DynamicDNSSupportedProtocols")
        return rval


    def set_DynamicDNSSupportedProtocols(self, val):
        """
            Sets the "DynamicDNSSupportedProtocols" variable.
        """
        self.proxy_set_variable_value("DynamicDNSSupportedProtocols", val)
        return


    def get_NetworkTopologyInfo(self):
        """
            Gets the "NetworkTopologyInfo" variable.
        """
        rval = self.proxy_get_variable_value("NetworkTopologyInfo")
        return rval


    def set_NetworkTopologyInfo(self, val):
        """
            Sets the "NetworkTopologyInfo" variable.
        """
        self.proxy_set_variable_value("NetworkTopologyInfo", val)
        return


    def get_STUNServerAddress(self):
        """
            Gets the "STUNServerAddress" variable.
        """
        rval = self.proxy_get_variable_value("STUNServerAddress")
        return rval


    def set_STUNServerAddress(self, val):
        """
            Sets the "STUNServerAddress" variable.
        """
        self.proxy_set_variable_value("STUNServerAddress", val)
        return


    def action_GetDynamicDNSSupportedProtocols(self):
        """
            Calls the GetDynamicDNSSupportedProtocols action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDynamicDNSSupportedProtocols", arguments=arguments)

        (DynamicDNSSupportedProtocols,) = out_params

        return DynamicDNSSupportedProtocols


    def action_GetNetworkTopologyInfo(self):
        """
            Calls the GetNetworkTopologyInfo action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetNetworkTopologyInfo", arguments=arguments)

        (CurrentNetworkTopologyInfo,) = out_params

        return CurrentNetworkTopologyInfo


    def action_SetDynamicDNSConfigInfo(self, NewDynamicDNSConfigInfo):
        """
            Calls the SetDynamicDNSConfigInfo action.
        """
        arguments = {
            "NewDynamicDNSConfigInfo": NewDynamicDNSConfigInfo,
        }

        out_params = self.proxy_call_action("SetDynamicDNSConfigInfo", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetSTUNServerAddress(self, NewSTUNServerAddress):
        """
            Calls the SetSTUNServerAddress action.
        """
        arguments = {
            "NewSTUNServerAddress": NewSTUNServerAddress,
        }

        out_params = self.proxy_call_action("SetSTUNServerAddress", arguments=arguments)

        (result,) = out_params

        return result

