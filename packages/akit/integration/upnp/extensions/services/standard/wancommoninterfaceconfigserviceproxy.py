"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class WANCommonInterfaceConfigServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'WANCommonInterfaceConfig' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:WANCommonInterfaceConfig:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:WANCommonInterfaceConfig'


    def get_ActiveConnectionDeviceContainer(self):
        """
            Gets the "ActiveConnectionDeviceContainer" variable.
        """
        rval = self.proxy_get_variable_value("ActiveConnectionDeviceContainer")
        return rval


    def set_ActiveConnectionDeviceContainer(self, val):
        """
            Sets the "ActiveConnectionDeviceContainer" variable.
        """
        self.proxy_set_variable_value("ActiveConnectionDeviceContainer", val)
        return


    def get_ActiveConnectionServiceID(self):
        """
            Gets the "ActiveConnectionServiceID" variable.
        """
        rval = self.proxy_get_variable_value("ActiveConnectionServiceID")
        return rval


    def set_ActiveConnectionServiceID(self, val):
        """
            Sets the "ActiveConnectionServiceID" variable.
        """
        self.proxy_set_variable_value("ActiveConnectionServiceID", val)
        return


    def get_EnabledForInternet(self):
        """
            Gets the "EnabledForInternet" variable.
        """
        rval = self.proxy_get_variable_value("EnabledForInternet")
        return rval


    def set_EnabledForInternet(self, val):
        """
            Sets the "EnabledForInternet" variable.
        """
        self.proxy_set_variable_value("EnabledForInternet", val)
        return


    def get_Layer1DownstreamMaxBitRate(self):
        """
            Gets the "Layer1DownstreamMaxBitRate" variable.
        """
        rval = self.proxy_get_variable_value("Layer1DownstreamMaxBitRate")
        return rval


    def set_Layer1DownstreamMaxBitRate(self, val):
        """
            Sets the "Layer1DownstreamMaxBitRate" variable.
        """
        self.proxy_set_variable_value("Layer1DownstreamMaxBitRate", val)
        return


    def get_Layer1UpstreamMaxBitRate(self):
        """
            Gets the "Layer1UpstreamMaxBitRate" variable.
        """
        rval = self.proxy_get_variable_value("Layer1UpstreamMaxBitRate")
        return rval


    def set_Layer1UpstreamMaxBitRate(self, val):
        """
            Sets the "Layer1UpstreamMaxBitRate" variable.
        """
        self.proxy_set_variable_value("Layer1UpstreamMaxBitRate", val)
        return


    def get_MaximumActiveConnections(self):
        """
            Gets the "MaximumActiveConnections" variable.
        """
        rval = self.proxy_get_variable_value("MaximumActiveConnections")
        return rval


    def set_MaximumActiveConnections(self, val):
        """
            Sets the "MaximumActiveConnections" variable.
        """
        self.proxy_set_variable_value("MaximumActiveConnections", val)
        return


    def get_NumberOfActiveConnections(self):
        """
            Gets the "NumberOfActiveConnections" variable.
        """
        rval = self.proxy_get_variable_value("NumberOfActiveConnections")
        return rval


    def set_NumberOfActiveConnections(self, val):
        """
            Sets the "NumberOfActiveConnections" variable.
        """
        self.proxy_set_variable_value("NumberOfActiveConnections", val)
        return


    def get_PhysicalLinkStatus(self):
        """
            Gets the "PhysicalLinkStatus" variable.
        """
        rval = self.proxy_get_variable_value("PhysicalLinkStatus")
        return rval


    def set_PhysicalLinkStatus(self, val):
        """
            Sets the "PhysicalLinkStatus" variable.
        """
        self.proxy_set_variable_value("PhysicalLinkStatus", val)
        return


    def get_TotalBytesReceived(self):
        """
            Gets the "TotalBytesReceived" variable.
        """
        rval = self.proxy_get_variable_value("TotalBytesReceived")
        return rval


    def set_TotalBytesReceived(self, val):
        """
            Sets the "TotalBytesReceived" variable.
        """
        self.proxy_set_variable_value("TotalBytesReceived", val)
        return


    def get_TotalBytesSent(self):
        """
            Gets the "TotalBytesSent" variable.
        """
        rval = self.proxy_get_variable_value("TotalBytesSent")
        return rval


    def set_TotalBytesSent(self, val):
        """
            Sets the "TotalBytesSent" variable.
        """
        self.proxy_set_variable_value("TotalBytesSent", val)
        return


    def get_TotalPacketsReceived(self):
        """
            Gets the "TotalPacketsReceived" variable.
        """
        rval = self.proxy_get_variable_value("TotalPacketsReceived")
        return rval


    def set_TotalPacketsReceived(self, val):
        """
            Sets the "TotalPacketsReceived" variable.
        """
        self.proxy_set_variable_value("TotalPacketsReceived", val)
        return


    def get_TotalPacketsSent(self):
        """
            Gets the "TotalPacketsSent" variable.
        """
        rval = self.proxy_get_variable_value("TotalPacketsSent")
        return rval


    def set_TotalPacketsSent(self, val):
        """
            Sets the "TotalPacketsSent" variable.
        """
        self.proxy_set_variable_value("TotalPacketsSent", val)
        return


    def get_WANAccessProvider(self):
        """
            Gets the "WANAccessProvider" variable.
        """
        rval = self.proxy_get_variable_value("WANAccessProvider")
        return rval


    def set_WANAccessProvider(self, val):
        """
            Sets the "WANAccessProvider" variable.
        """
        self.proxy_set_variable_value("WANAccessProvider", val)
        return


    def get_WANAccessType(self):
        """
            Gets the "WANAccessType" variable.
        """
        rval = self.proxy_get_variable_value("WANAccessType")
        return rval


    def set_WANAccessType(self, val):
        """
            Sets the "WANAccessType" variable.
        """
        self.proxy_set_variable_value("WANAccessType", val)
        return


    def action_GetActiveConnection(self, NewActiveConnectionIndex):
        """
            Calls the GetActiveConnection action.
        """
        arguments = {
            "NewActiveConnectionIndex": NewActiveConnectionIndex,
        }

        out_params = self.proxy_call_action("GetActiveConnection", arguments=arguments)

        (NewActiveConnDeviceContainer, NewActiveConnectionServiceID,) = out_params

        return NewActiveConnDeviceContainer, NewActiveConnectionServiceID


    def action_GetCommonLinkProperties(self):
        """
            Calls the GetCommonLinkProperties action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetCommonLinkProperties", arguments=arguments)

        (NewWANAccessType, NewLayer1UpstreamMaxBitRate, NewLayer1DownstreamMaxBitRate, NewPhysicalLinkStatus,) = out_params

        return NewWANAccessType, NewLayer1UpstreamMaxBitRate, NewLayer1DownstreamMaxBitRate, NewPhysicalLinkStatus


    def action_GetEnabledForInternet(self):
        """
            Calls the GetEnabledForInternet action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetEnabledForInternet", arguments=arguments)

        (NewEnabledForInternet,) = out_params

        return NewEnabledForInternet


    def action_GetMaximumActiveConnections(self):
        """
            Calls the GetMaximumActiveConnections action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetMaximumActiveConnections", arguments=arguments)

        (NewMaximumActiveConnections,) = out_params

        return NewMaximumActiveConnections


    def action_GetTotalBytesReceived(self):
        """
            Calls the GetTotalBytesReceived action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetTotalBytesReceived", arguments=arguments)

        (NewTotalBytesReceived,) = out_params

        return NewTotalBytesReceived


    def action_GetTotalBytesSent(self):
        """
            Calls the GetTotalBytesSent action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetTotalBytesSent", arguments=arguments)

        (NewTotalBytesSent,) = out_params

        return NewTotalBytesSent


    def action_GetTotalPacketsReceived(self):
        """
            Calls the GetTotalPacketsReceived action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetTotalPacketsReceived", arguments=arguments)

        (NewTotalPacketsReceived,) = out_params

        return NewTotalPacketsReceived


    def action_GetTotalPacketsSent(self):
        """
            Calls the GetTotalPacketsSent action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetTotalPacketsSent", arguments=arguments)

        (NewTotalPacketsSent,) = out_params

        return NewTotalPacketsSent


    def action_GetWANAccessProvider(self):
        """
            Calls the GetWANAccessProvider action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetWANAccessProvider", arguments=arguments)

        (NewWANAccessProvider,) = out_params

        return NewWANAccessProvider


    def action_SetEnabledForInternet(self, NewEnabledForInternet):
        """
            Calls the SetEnabledForInternet action.
        """
        arguments = {
            "NewEnabledForInternet": NewEnabledForInternet,
        }

        out_params = self.proxy_call_action("SetEnabledForInternet", arguments=arguments)

        (result,) = out_params

        return result

