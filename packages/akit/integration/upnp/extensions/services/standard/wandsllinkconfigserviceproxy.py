"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class WANDSLLinkConfigServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'WANDSLLinkConfig' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:WANDSLLinkConfig:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:WANDSLLinkConfig'


    def get_ATMEncapsulation(self):
        """
            Gets the "ATMEncapsulation" variable.
        """
        rval = self.proxy_get_variable_value("ATMEncapsulation")
        return rval


    def set_ATMEncapsulation(self, val):
        """
            Sets the "ATMEncapsulation" variable.
        """
        self.proxy_set_variable_value("ATMEncapsulation", val)
        return


    def get_AutoConfig(self):
        """
            Gets the "AutoConfig" variable.
        """
        rval = self.proxy_get_variable_value("AutoConfig")
        return rval


    def set_AutoConfig(self, val):
        """
            Sets the "AutoConfig" variable.
        """
        self.proxy_set_variable_value("AutoConfig", val)
        return


    def get_DestinationAddress(self):
        """
            Gets the "DestinationAddress" variable.
        """
        rval = self.proxy_get_variable_value("DestinationAddress")
        return rval


    def set_DestinationAddress(self, val):
        """
            Sets the "DestinationAddress" variable.
        """
        self.proxy_set_variable_value("DestinationAddress", val)
        return


    def get_FCSPreserved(self):
        """
            Gets the "FCSPreserved" variable.
        """
        rval = self.proxy_get_variable_value("FCSPreserved")
        return rval


    def set_FCSPreserved(self, val):
        """
            Sets the "FCSPreserved" variable.
        """
        self.proxy_set_variable_value("FCSPreserved", val)
        return


    def get_LinkStatus(self):
        """
            Gets the "LinkStatus" variable.
        """
        rval = self.proxy_get_variable_value("LinkStatus")
        return rval


    def set_LinkStatus(self, val):
        """
            Sets the "LinkStatus" variable.
        """
        self.proxy_set_variable_value("LinkStatus", val)
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


    def get_ModulationType(self):
        """
            Gets the "ModulationType" variable.
        """
        rval = self.proxy_get_variable_value("ModulationType")
        return rval


    def set_ModulationType(self, val):
        """
            Sets the "ModulationType" variable.
        """
        self.proxy_set_variable_value("ModulationType", val)
        return


    def action_GetATMEncapsulation(self):
        """
            Calls the GetATMEncapsulation action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetATMEncapsulation", arguments=arguments)

        (NewATMEncapsulation,) = out_params

        return NewATMEncapsulation


    def action_GetAutoConfig(self):
        """
            Calls the GetAutoConfig action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetAutoConfig", arguments=arguments)

        (NewAutoConfig,) = out_params

        return NewAutoConfig


    def action_GetDSLLinkInfo(self):
        """
            Calls the GetDSLLinkInfo action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDSLLinkInfo", arguments=arguments)

        (NewLinkType, NewLinkStatus,) = out_params

        return NewLinkType, NewLinkStatus


    def action_GetDestinationAddress(self):
        """
            Calls the GetDestinationAddress action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDestinationAddress", arguments=arguments)

        (NewDestinationAddress,) = out_params

        return NewDestinationAddress


    def action_GetFCSPreserved(self):
        """
            Calls the GetFCSPreserved action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetFCSPreserved", arguments=arguments)

        (NewFCSPreserved,) = out_params

        return NewFCSPreserved


    def action_GetModulationType(self):
        """
            Calls the GetModulationType action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetModulationType", arguments=arguments)

        (NewModulationType,) = out_params

        return NewModulationType


    def action_SetATMEncapsulation(self, NewATMEncapsulation):
        """
            Calls the SetATMEncapsulation action.
        """
        arguments = {
            "NewATMEncapsulation": NewATMEncapsulation,
        }

        out_params = self.proxy_call_action("SetATMEncapsulation", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetDSLLinkType(self, NewLinkType):
        """
            Calls the SetDSLLinkType action.
        """
        arguments = {
            "NewLinkType": NewLinkType,
        }

        out_params = self.proxy_call_action("SetDSLLinkType", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetDestinationAddress(self, NewDestinationAddress):
        """
            Calls the SetDestinationAddress action.
        """
        arguments = {
            "NewDestinationAddress": NewDestinationAddress,
        }

        out_params = self.proxy_call_action("SetDestinationAddress", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetFCSPreserved(self, NewFCSPreserved):
        """
            Calls the SetFCSPreserved action.
        """
        arguments = {
            "NewFCSPreserved": NewFCSPreserved,
        }

        out_params = self.proxy_call_action("SetFCSPreserved", arguments=arguments)

        (result,) = out_params

        return result

