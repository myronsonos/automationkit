"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class HVAC_UserOperatingMode1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'HVAC_UserOperatingMode1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:HVAC_UserOperatingMode:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:HVAC_UserOperatingMode'


    def get_ModeStatus(self):
        """
            Gets the "ModeStatus" variable.
        """
        rval = self.proxy_get_variable_value("ModeStatus")
        return rval


    def set_ModeStatus(self, val):
        """
            Sets the "ModeStatus" variable.
        """
        self.proxy_set_variable_value("ModeStatus", val)
        return


    def get_ModeTarget(self):
        """
            Gets the "ModeTarget" variable.
        """
        rval = self.proxy_get_variable_value("ModeTarget")
        return rval


    def set_ModeTarget(self, val):
        """
            Sets the "ModeTarget" variable.
        """
        self.proxy_set_variable_value("ModeTarget", val)
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


    def action_GetModeStatus(self):
        """
            Calls the GetModeStatus action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetModeStatus", arguments=arguments)

        (CurrentModeStatus,) = out_params

        return CurrentModeStatus


    def action_GetModeTarget(self):
        """
            Calls the GetModeTarget action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetModeTarget", arguments=arguments)

        (CurrentModeTarget,) = out_params

        return CurrentModeTarget


    def action_GetName(self):
        """
            Calls the GetName action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetName", arguments=arguments)

        (CurrentName,) = out_params

        return CurrentName


    def action_SetModeTarget(self, NewModeTarget):
        """
            Calls the SetModeTarget action.
        """
        arguments = {
            "NewModeTarget": NewModeTarget,
        }

        out_params = self.proxy_call_action("SetModeTarget", arguments=arguments)

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

