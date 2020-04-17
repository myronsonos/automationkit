"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class WANCableLinkConfig1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'WANCableLinkConfig1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:WANCableLinkConfig:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:WANCableLinkConfig'


    def get_BPIEncryptionEnabled(self):
        """
            Gets the "BPIEncryptionEnabled" variable.
        """
        rval = self.proxy_get_variable_value("BPIEncryptionEnabled")
        return rval


    def set_BPIEncryptionEnabled(self, val):
        """
            Sets the "BPIEncryptionEnabled" variable.
        """
        self.proxy_set_variable_value("BPIEncryptionEnabled", val)
        return


    def get_CableLinkConfigState(self):
        """
            Gets the "CableLinkConfigState" variable.
        """
        rval = self.proxy_get_variable_value("CableLinkConfigState")
        return rval


    def set_CableLinkConfigState(self, val):
        """
            Sets the "CableLinkConfigState" variable.
        """
        self.proxy_set_variable_value("CableLinkConfigState", val)
        return


    def get_ConfigFile(self):
        """
            Gets the "ConfigFile" variable.
        """
        rval = self.proxy_get_variable_value("ConfigFile")
        return rval


    def set_ConfigFile(self, val):
        """
            Sets the "ConfigFile" variable.
        """
        self.proxy_set_variable_value("ConfigFile", val)
        return


    def get_DownstreamFrequency(self):
        """
            Gets the "DownstreamFrequency" variable.
        """
        rval = self.proxy_get_variable_value("DownstreamFrequency")
        return rval


    def set_DownstreamFrequency(self, val):
        """
            Sets the "DownstreamFrequency" variable.
        """
        self.proxy_set_variable_value("DownstreamFrequency", val)
        return


    def get_DownstreamModulation(self):
        """
            Gets the "DownstreamModulation" variable.
        """
        rval = self.proxy_get_variable_value("DownstreamModulation")
        return rval


    def set_DownstreamModulation(self, val):
        """
            Sets the "DownstreamModulation" variable.
        """
        self.proxy_set_variable_value("DownstreamModulation", val)
        return


    def get_LinkType(self):
        """
            Gets the "LinkType" variable.
        """
        rval = self.proxy_get_variable_value("LinkType")
        return rval


    def set_LinkType(self, val):
        """
            Sets the "LinkType" variable.
        """
        self.proxy_set_variable_value("LinkType", val)
        return


    def get_TFTPServer(self):
        """
            Gets the "TFTPServer" variable.
        """
        rval = self.proxy_get_variable_value("TFTPServer")
        return rval


    def set_TFTPServer(self, val):
        """
            Sets the "TFTPServer" variable.
        """
        self.proxy_set_variable_value("TFTPServer", val)
        return


    def get_UpstreamChannelID(self):
        """
            Gets the "UpstreamChannelID" variable.
        """
        rval = self.proxy_get_variable_value("UpstreamChannelID")
        return rval


    def set_UpstreamChannelID(self, val):
        """
            Sets the "UpstreamChannelID" variable.
        """
        self.proxy_set_variable_value("UpstreamChannelID", val)
        return


    def get_UpstreamFrequency(self):
        """
            Gets the "UpstreamFrequency" variable.
        """
        rval = self.proxy_get_variable_value("UpstreamFrequency")
        return rval


    def set_UpstreamFrequency(self, val):
        """
            Sets the "UpstreamFrequency" variable.
        """
        self.proxy_set_variable_value("UpstreamFrequency", val)
        return


    def get_UpstreamModulation(self):
        """
            Gets the "UpstreamModulation" variable.
        """
        rval = self.proxy_get_variable_value("UpstreamModulation")
        return rval


    def set_UpstreamModulation(self, val):
        """
            Sets the "UpstreamModulation" variable.
        """
        self.proxy_set_variable_value("UpstreamModulation", val)
        return


    def get_UpstreamPowerLevel(self):
        """
            Gets the "UpstreamPowerLevel" variable.
        """
        rval = self.proxy_get_variable_value("UpstreamPowerLevel")
        return rval


    def set_UpstreamPowerLevel(self, val):
        """
            Sets the "UpstreamPowerLevel" variable.
        """
        self.proxy_set_variable_value("UpstreamPowerLevel", val)
        return


    def action_GetBPIEncryptionEnabled(self):
        """
            Calls the GetBPIEncryptionEnabled action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetBPIEncryptionEnabled", arguments=arguments)

        (NewBPIEncryptionEnabled,) = out_params

        return NewBPIEncryptionEnabled


    def action_GetCableLinkConfigInfo(self):
        """
            Calls the GetCableLinkConfigInfo action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetCableLinkConfigInfo", arguments=arguments)

        (NewCableLinkConfigState, NewLinkType,) = out_params

        return NewCableLinkConfigState, NewLinkType


    def action_GetConfigFile(self):
        """
            Calls the GetConfigFile action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetConfigFile", arguments=arguments)

        (NewConfigFile,) = out_params

        return NewConfigFile


    def action_GetDownstreamFrequency(self):
        """
            Calls the GetDownstreamFrequency action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDownstreamFrequency", arguments=arguments)

        (NewDownstreamFrequency,) = out_params

        return NewDownstreamFrequency


    def action_GetDownstreamModulation(self):
        """
            Calls the GetDownstreamModulation action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDownstreamModulation", arguments=arguments)

        (NewDownstreamModulation,) = out_params

        return NewDownstreamModulation


    def action_GetTFTPServer(self):
        """
            Calls the GetTFTPServer action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetTFTPServer", arguments=arguments)

        (NewTFTPServer,) = out_params

        return NewTFTPServer


    def action_GetUpstreamChannelID(self):
        """
            Calls the GetUpstreamChannelID action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetUpstreamChannelID", arguments=arguments)

        (NewUpstreamChannelID,) = out_params

        return NewUpstreamChannelID


    def action_GetUpstreamFrequency(self):
        """
            Calls the GetUpstreamFrequency action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetUpstreamFrequency", arguments=arguments)

        (NewUpstreamFrequency,) = out_params

        return NewUpstreamFrequency


    def action_GetUpstreamModulation(self):
        """
            Calls the GetUpstreamModulation action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetUpstreamModulation", arguments=arguments)

        (NewUpstreamModulation,) = out_params

        return NewUpstreamModulation


    def action_GetUpstreamPowerLevel(self):
        """
            Calls the GetUpstreamPowerLevel action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetUpstreamPowerLevel", arguments=arguments)

        (NewUpstreamPowerLevel,) = out_params

        return NewUpstreamPowerLevel

