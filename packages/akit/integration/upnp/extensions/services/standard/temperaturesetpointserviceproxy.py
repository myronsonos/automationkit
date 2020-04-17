"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class TemperatureSetpointServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'TemperatureSetpoint' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:TemperatureSetpoint:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:TemperatureSetpoint'


    def get_Application(self):
        """
            Gets the "Application" variable.
        """
        rval = self.proxy_get_variable_value("Application")
        return rval


    def set_Application(self, val):
        """
            Sets the "Application" variable.
        """
        self.proxy_set_variable_value("Application", val)
        return


    def get_CurrentSetpoint(self):
        """
            Gets the "CurrentSetpoint" variable.
        """
        rval = self.proxy_get_variable_value("CurrentSetpoint")
        return rval


    def set_CurrentSetpoint(self, val):
        """
            Sets the "CurrentSetpoint" variable.
        """
        self.proxy_set_variable_value("CurrentSetpoint", val)
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


    def get_SetpointAchieved(self):
        """
            Gets the "SetpointAchieved" variable.
        """
        rval = self.proxy_get_variable_value("SetpointAchieved")
        return rval


    def set_SetpointAchieved(self, val):
        """
            Sets the "SetpointAchieved" variable.
        """
        self.proxy_set_variable_value("SetpointAchieved", val)
        return


    def action_GetApplication(self):
        """
            Calls the GetApplication action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetApplication", arguments=arguments)

        (CurrentApplication,) = out_params

        return CurrentApplication


    def action_GetCurrentSetpoint(self):
        """
            Calls the GetCurrentSetpoint action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetCurrentSetpoint", arguments=arguments)

        (CurrentSP,) = out_params

        return CurrentSP


    def action_GetName(self):
        """
            Calls the GetName action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetName", arguments=arguments)

        (CurrentName,) = out_params

        return CurrentName


    def action_GetSetpointAchieved(self):
        """
            Calls the GetSetpointAchieved action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetSetpointAchieved", arguments=arguments)

        (CurrentSPA,) = out_params

        return CurrentSPA


    def action_SetApplication(self, NewApplication):
        """
            Calls the SetApplication action.
        """
        arguments = {
            "NewApplication": NewApplication,
        }

        out_params = self.proxy_call_action("SetApplication", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetCurrentSetpoint(self, NewCurrentSetpoint):
        """
            Calls the SetCurrentSetpoint action.
        """
        arguments = {
            "NewCurrentSetpoint": NewCurrentSetpoint,
        }

        out_params = self.proxy_call_action("SetCurrentSetpoint", arguments=arguments)

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

