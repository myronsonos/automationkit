"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class TemperatureSensor1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'TemperatureSensor1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:TemperatureSensor:1'
    SERVICE_ID = 'urn:schemas-upnp-org:service:TemperatureSensor'


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


    def get_CurrentTemperature(self):
        """
            Gets the "CurrentTemperature" variable.
        """
        rval = self.proxy_get_variable_value("CurrentTemperature")
        return rval


    def set_CurrentTemperature(self, val):
        """
            Sets the "CurrentTemperature" variable.
        """
        self.proxy_set_variable_value("CurrentTemperature", val)
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


    def action_GetApplication(self):
        """
            Calls the GetApplication action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetApplication", arguments=arguments)

        (CurrentApplication,) = out_params

        return CurrentApplication


    def action_GetCurrentTemperature(self):
        """
            Calls the GetCurrentTemperature action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetCurrentTemperature", arguments=arguments)

        (CurrentTemp,) = out_params

        return CurrentTemp


    def action_GetName(self):
        """
            Calls the GetName action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetName", arguments=arguments)

        (CurrentName,) = out_params

        return CurrentName


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

