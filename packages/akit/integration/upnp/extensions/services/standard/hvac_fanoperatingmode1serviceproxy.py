"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class HVAC_FanOperatingMode1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'HVAC_FanOperatingMode1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:HVAC_FanOperatingMode:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:HVAC_FanOperatingMode'


    def get_FanStatus(self):
        """
            Gets the "FanStatus" variable.
        """
        rval = self.proxy_get_variable_value("FanStatus")
        return rval


    def set_FanStatus(self, val):
        """
            Sets the "FanStatus" variable.
        """
        self.proxy_set_variable_value("FanStatus", val)
        return


    def get_Mode(self):
        """
            Gets the "Mode" variable.
        """
        rval = self.proxy_get_variable_value("Mode")
        return rval


    def set_Mode(self, val):
        """
            Sets the "Mode" variable.
        """
        self.proxy_set_variable_value("Mode", val)
        return


    def get_Name(self):
        """
            Gets the "Name" variable.
        """
        rval = self.proxy_get_variable_value("Name")
        return rval


    def set_Name(self, val):
        """
            Sets the "Name" variable.
        """
        self.proxy_set_variable_value("Name", val)
        return


    def action_GetFanStatus(self):
        """
            Calls the GetFanStatus action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetFanStatus", arguments=arguments)

        (CurrentStatus,) = out_params

        return CurrentStatus


    def action_GetMode(self):
        """
            Calls the GetMode action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetMode", arguments=arguments)

        (CurrentMode,) = out_params

        return CurrentMode


    def action_GetName(self):
        """
            Calls the GetName action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetName", arguments=arguments)

        (CurrentName,) = out_params

        return CurrentName


    def action_SetMode(self, NewMode):
        """
            Calls the SetMode action.
        """
        arguments = {
            "NewMode": NewMode,
        }

        out_params = self.proxy_call_action("SetMode", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetName(self, NewName):
        """
            Calls the SetName action.
        """
        arguments = {
            "NewName": NewName,
        }

        out_params = self.proxy_call_action("SetName", arguments=arguments)

        (result,) = out_params

        return result

