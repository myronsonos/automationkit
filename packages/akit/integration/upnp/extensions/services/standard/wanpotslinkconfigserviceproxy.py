"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class WANPOTSLinkConfigServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'WANPOTSLinkConfig' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:WANPOTSLinkConfig:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:WANPOTSLinkConfig'


    def get_DataCompression(self):
        """
            Gets the "DataCompression" variable.
        """
        rval = self.proxy_get_variable_value("DataCompression")
        return rval


    def set_DataCompression(self, val):
        """
            Sets the "DataCompression" variable.
        """
        self.proxy_set_variable_value("DataCompression", val)
        return


    def get_DataModulationSupported(self):
        """
            Gets the "DataModulationSupported" variable.
        """
        rval = self.proxy_get_variable_value("DataModulationSupported")
        return rval


    def set_DataModulationSupported(self, val):
        """
            Sets the "DataModulationSupported" variable.
        """
        self.proxy_set_variable_value("DataModulationSupported", val)
        return


    def get_DataProtocol(self):
        """
            Gets the "DataProtocol" variable.
        """
        rval = self.proxy_get_variable_value("DataProtocol")
        return rval


    def set_DataProtocol(self, val):
        """
            Sets the "DataProtocol" variable.
        """
        self.proxy_set_variable_value("DataProtocol", val)
        return


    def get_DelayBetweenRetries(self):
        """
            Gets the "DelayBetweenRetries" variable.
        """
        rval = self.proxy_get_variable_value("DelayBetweenRetries")
        return rval


    def set_DelayBetweenRetries(self, val):
        """
            Sets the "DelayBetweenRetries" variable.
        """
        self.proxy_set_variable_value("DelayBetweenRetries", val)
        return


    def get_Fclass(self):
        """
            Gets the "Fclass" variable.
        """
        rval = self.proxy_get_variable_value("Fclass")
        return rval


    def set_Fclass(self, val):
        """
            Sets the "Fclass" variable.
        """
        self.proxy_set_variable_value("Fclass", val)
        return


    def get_ISPInfo(self):
        """
            Gets the "ISPInfo" variable.
        """
        rval = self.proxy_get_variable_value("ISPInfo")
        return rval


    def set_ISPInfo(self, val):
        """
            Sets the "ISPInfo" variable.
        """
        self.proxy_set_variable_value("ISPInfo", val)
        return


    def get_ISPPhoneNumber(self):
        """
            Gets the "ISPPhoneNumber" variable.
        """
        rval = self.proxy_get_variable_value("ISPPhoneNumber")
        return rval


    def set_ISPPhoneNumber(self, val):
        """
            Sets the "ISPPhoneNumber" variable.
        """
        self.proxy_set_variable_value("ISPPhoneNumber", val)
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


    def get_NumberOfRetries(self):
        """
            Gets the "NumberOfRetries" variable.
        """
        rval = self.proxy_get_variable_value("NumberOfRetries")
        return rval


    def set_NumberOfRetries(self, val):
        """
            Sets the "NumberOfRetries" variable.
        """
        self.proxy_set_variable_value("NumberOfRetries", val)
        return


    def get_PlusVTRCommandSupported(self):
        """
            Gets the "PlusVTRCommandSupported" variable.
        """
        rval = self.proxy_get_variable_value("PlusVTRCommandSupported")
        return rval


    def set_PlusVTRCommandSupported(self, val):
        """
            Sets the "PlusVTRCommandSupported" variable.
        """
        self.proxy_set_variable_value("PlusVTRCommandSupported", val)
        return


    def action_GetCallRetryInfo(self):
        """
            Calls the GetCallRetryInfo action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetCallRetryInfo", arguments=arguments)

        (NewNumberOfRetries, NewDelayBetweenRetries,) = out_params

        return NewNumberOfRetries, NewDelayBetweenRetries


    def action_GetDataCompression(self):
        """
            Calls the GetDataCompression action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDataCompression", arguments=arguments)

        (NewDataCompression,) = out_params

        return NewDataCompression


    def action_GetDataModulationSupported(self):
        """
            Calls the GetDataModulationSupported action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDataModulationSupported", arguments=arguments)

        (NewDataModulationSupported,) = out_params

        return NewDataModulationSupported


    def action_GetDataProtocol(self):
        """
            Calls the GetDataProtocol action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDataProtocol", arguments=arguments)

        (NewDataProtocol,) = out_params

        return NewDataProtocol


    def action_GetFclass(self):
        """
            Calls the GetFclass action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetFclass", arguments=arguments)

        (NewFclass,) = out_params

        return NewFclass


    def action_GetISPInfo(self):
        """
            Calls the GetISPInfo action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetISPInfo", arguments=arguments)

        (NewISPPhoneNumber, NewISPInfo, NewLinkType,) = out_params

        return NewISPPhoneNumber, NewISPInfo, NewLinkType


    def action_GetPlusVTRCommandSupported(self):
        """
            Calls the GetPlusVTRCommandSupported action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetPlusVTRCommandSupported", arguments=arguments)

        (NewPlusVTRCommandSupported,) = out_params

        return NewPlusVTRCommandSupported


    def action_SetCallRetryInfo(self, NewNumberOfRetries, NewDelayBetweenRetries):
        """
            Calls the SetCallRetryInfo action.
        """
        arguments = {
            "NewNumberOfRetries": NewNumberOfRetries,
            "NewDelayBetweenRetries": NewDelayBetweenRetries,
        }

        out_params = self.proxy_call_action("SetCallRetryInfo", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetISPInfo(self, NewISPPhoneNumber, NewISPInfo, NewLinkType):
        """
            Calls the SetISPInfo action.
        """
        arguments = {
            "NewISPPhoneNumber": NewISPPhoneNumber,
            "NewISPInfo": NewISPInfo,
            "NewLinkType": NewLinkType,
        }

        out_params = self.proxy_call_action("SetISPInfo", arguments=arguments)

        (result,) = out_params

        return result

