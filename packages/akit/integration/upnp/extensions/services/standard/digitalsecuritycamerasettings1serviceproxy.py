"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class DigitalSecurityCameraSettings1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'DigitalSecurityCameraSettings1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:DigitalSecurityCameraSettings:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:DigitalSecurityCameraSettings'


    def get_AutomaticWhiteBalance(self):
        """
            Gets the "AutomaticWhiteBalance" variable.
        """
        rval = self.proxy_get_variable_value("AutomaticWhiteBalance")
        return rval


    def set_AutomaticWhiteBalance(self, val):
        """
            Sets the "AutomaticWhiteBalance" variable.
        """
        self.proxy_set_variable_value("AutomaticWhiteBalance", val)
        return


    def get_AvailableRotations(self):
        """
            Gets the "AvailableRotations" variable.
        """
        rval = self.proxy_get_variable_value("AvailableRotations")
        return rval


    def set_AvailableRotations(self, val):
        """
            Sets the "AvailableRotations" variable.
        """
        self.proxy_set_variable_value("AvailableRotations", val)
        return


    def get_Brightness(self):
        """
            Gets the "Brightness" variable.
        """
        rval = self.proxy_get_variable_value("Brightness")
        return rval


    def set_Brightness(self, val):
        """
            Sets the "Brightness" variable.
        """
        self.proxy_set_variable_value("Brightness", val)
        return


    def get_ColorSaturation(self):
        """
            Gets the "ColorSaturation" variable.
        """
        rval = self.proxy_get_variable_value("ColorSaturation")
        return rval


    def set_ColorSaturation(self, val):
        """
            Sets the "ColorSaturation" variable.
        """
        self.proxy_set_variable_value("ColorSaturation", val)
        return


    def get_DefaultRotation(self):
        """
            Gets the "DefaultRotation" variable.
        """
        rval = self.proxy_get_variable_value("DefaultRotation")
        return rval


    def set_DefaultRotation(self, val):
        """
            Sets the "DefaultRotation" variable.
        """
        self.proxy_set_variable_value("DefaultRotation", val)
        return


    def get_FixedWhiteBalance(self):
        """
            Gets the "FixedWhiteBalance" variable.
        """
        rval = self.proxy_get_variable_value("FixedWhiteBalance")
        return rval


    def set_FixedWhiteBalance(self, val):
        """
            Sets the "FixedWhiteBalance" variable.
        """
        self.proxy_set_variable_value("FixedWhiteBalance", val)
        return


    def action_DecreaseBrightness(self):
        """
            Calls the DecreaseBrightness action.
        """
        arguments = { }

        out_params = self.proxy_call_action("DecreaseBrightness", arguments=arguments)

        (RetBrightness,) = out_params

        return RetBrightness


    def action_DecreaseColorSaturation(self):
        """
            Calls the DecreaseColorSaturation action.
        """
        arguments = { }

        out_params = self.proxy_call_action("DecreaseColorSaturation", arguments=arguments)

        (RetColorSaturation,) = out_params

        return RetColorSaturation


    def action_GetAutomaticWhiteBalance(self):
        """
            Calls the GetAutomaticWhiteBalance action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetAutomaticWhiteBalance", arguments=arguments)

        (RetAutomaticWhiteBalance,) = out_params

        return RetAutomaticWhiteBalance


    def action_GetAvailableRotations(self):
        """
            Calls the GetAvailableRotations action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetAvailableRotations", arguments=arguments)

        (RetAvailableRotations,) = out_params

        return RetAvailableRotations


    def action_GetBrightness(self):
        """
            Calls the GetBrightness action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetBrightness", arguments=arguments)

        (RetBrightness,) = out_params

        return RetBrightness


    def action_GetColorSaturation(self):
        """
            Calls the GetColorSaturation action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetColorSaturation", arguments=arguments)

        (RetColorSaturation,) = out_params

        return RetColorSaturation


    def action_GetDefaultRotation(self):
        """
            Calls the GetDefaultRotation action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDefaultRotation", arguments=arguments)

        (RetRotation,) = out_params

        return RetRotation


    def action_GetFixedWhiteBalance(self):
        """
            Calls the GetFixedWhiteBalance action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetFixedWhiteBalance", arguments=arguments)

        (RetFixedWhiteBalance,) = out_params

        return RetFixedWhiteBalance


    def action_IncreaseBrightness(self):
        """
            Calls the IncreaseBrightness action.
        """
        arguments = { }

        out_params = self.proxy_call_action("IncreaseBrightness", arguments=arguments)

        (RetBrightness,) = out_params

        return RetBrightness


    def action_IncreaseColorSaturation(self):
        """
            Calls the IncreaseColorSaturation action.
        """
        arguments = { }

        out_params = self.proxy_call_action("IncreaseColorSaturation", arguments=arguments)

        (RetColorSaturation,) = out_params

        return RetColorSaturation


    def action_SetAutomaticWhiteBalance(self, NewAutomaticWhiteBalance):
        """
            Calls the SetAutomaticWhiteBalance action.
        """
        arguments = {
            "NewAutomaticWhiteBalance": NewAutomaticWhiteBalance,
        }

        out_params = self.proxy_call_action("SetAutomaticWhiteBalance", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetBrightness(self, NewBrightness):
        """
            Calls the SetBrightness action.
        """
        arguments = {
            "NewBrightness": NewBrightness,
        }

        out_params = self.proxy_call_action("SetBrightness", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetColorSaturation(self, NewColorSaturation):
        """
            Calls the SetColorSaturation action.
        """
        arguments = {
            "NewColorSaturation": NewColorSaturation,
        }

        out_params = self.proxy_call_action("SetColorSaturation", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetDefaultRotation(self, NewRotation):
        """
            Calls the SetDefaultRotation action.
        """
        arguments = {
            "NewRotation": NewRotation,
        }

        out_params = self.proxy_call_action("SetDefaultRotation", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetFixedWhiteBalance(self, NewFixedWhiteBalance):
        """
            Calls the SetFixedWhiteBalance action.
        """
        arguments = {
            "NewFixedWhiteBalance": NewFixedWhiteBalance,
        }

        out_params = self.proxy_call_action("SetFixedWhiteBalance", arguments=arguments)

        (result,) = out_params

        return result

