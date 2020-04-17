"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class ExternalActivityServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'ExternalActivity' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:ExternalActivity:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:ExternalActivity'


    def get_Activity(self):
        """
            Gets the "Activity" variable.
        """
        rval = self.proxy_get_variable_value("Activity")
        return rval


    def set_Activity(self, val):
        """
            Sets the "Activity" variable.
        """
        self.proxy_set_variable_value("Activity", val)
        return


    def get_AvailableRegistrations(self):
        """
            Gets the "AvailableRegistrations" variable.
        """
        rval = self.proxy_get_variable_value("AvailableRegistrations")
        return rval


    def set_AvailableRegistrations(self, val):
        """
            Sets the "AvailableRegistrations" variable.
        """
        self.proxy_set_variable_value("AvailableRegistrations", val)
        return


    def get_ButtonName(self):
        """
            Gets the "ButtonName" variable.
        """
        rval = self.proxy_get_variable_value("ButtonName")
        return rval


    def set_ButtonName(self, val):
        """
            Sets the "ButtonName" variable.
        """
        self.proxy_set_variable_value("ButtonName", val)
        return


    def get_DisplayString(self):
        """
            Gets the "DisplayString" variable.
        """
        rval = self.proxy_get_variable_value("DisplayString")
        return rval


    def set_DisplayString(self, val):
        """
            Sets the "DisplayString" variable.
        """
        self.proxy_set_variable_value("DisplayString", val)
        return


    def get_DisplayStringSize(self):
        """
            Gets the "DisplayStringSize" variable.
        """
        rval = self.proxy_get_variable_value("DisplayStringSize")
        return rval


    def set_DisplayStringSize(self, val):
        """
            Sets the "DisplayStringSize" variable.
        """
        self.proxy_set_variable_value("DisplayStringSize", val)
        return


    def get_Duration(self):
        """
            Gets the "Duration" variable.
        """
        rval = self.proxy_get_variable_value("Duration")
        return rval


    def set_Duration(self, val):
        """
            Sets the "Duration" variable.
        """
        self.proxy_set_variable_value("Duration", val)
        return


    def get_RegistrationID(self):
        """
            Gets the "RegistrationID" variable.
        """
        rval = self.proxy_get_variable_value("RegistrationID")
        return rval


    def set_RegistrationID(self, val):
        """
            Sets the "RegistrationID" variable.
        """
        self.proxy_set_variable_value("RegistrationID", val)
        return


    def action_Register(self, ButtonNameIn, DisplayStringIn, DurationIn):
        """
            Calls the Register action.
        """
        arguments = {
            "ButtonNameIn": ButtonNameIn,
            "DisplayStringIn": DisplayStringIn,
            "DurationIn": DurationIn,
        }

        out_params = self.proxy_call_action("Register", arguments=arguments)

        (ActualDurationOut, RegistrationIDOut,) = out_params

        return ActualDurationOut, RegistrationIDOut

