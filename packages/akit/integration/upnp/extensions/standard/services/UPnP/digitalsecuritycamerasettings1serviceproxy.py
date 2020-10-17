"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class DigitalSecurityCameraSettings1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'DigitalSecurityCameraSettings1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:DigitalSecurityCameraSettings:1'


    def action_DecreaseBrightness(self, extract_returns=True):
        """
            Calls the DecreaseBrightness action.

            :returns: "result"
        """
        arguments = { }

        out_params = self.proxy_call_action("DecreaseBrightness", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_DecreaseColorSaturation(self, extract_returns=True):
        """
            Calls the DecreaseColorSaturation action.

            :returns: "result"
        """
        arguments = { }

        out_params = self.proxy_call_action("DecreaseColorSaturation", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetAutomaticWhiteBalance(self, extract_returns=True):
        """
            Calls the GetAutomaticWhiteBalance action.

            :returns: "RetAutomaticWhiteBalance"
        """
        arguments = { }

        out_params = self.proxy_call_action("GetAutomaticWhiteBalance", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RetAutomaticWhiteBalance",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetAvailableRotations(self, extract_returns=True):
        """
            Calls the GetAvailableRotations action.

            :returns: "RetAvailableRotations"
        """
        arguments = { }

        out_params = self.proxy_call_action("GetAvailableRotations", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RetAvailableRotations",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetBrightness(self, extract_returns=True):
        """
            Calls the GetBrightness action.

            :returns: "RetBrightness"
        """
        arguments = { }

        out_params = self.proxy_call_action("GetBrightness", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RetBrightness",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetColorSaturation(self, extract_returns=True):
        """
            Calls the GetColorSaturation action.

            :returns: "RetColorSaturation"
        """
        arguments = { }

        out_params = self.proxy_call_action("GetColorSaturation", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RetColorSaturation",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetDefaultRotation(self, extract_returns=True):
        """
            Calls the GetDefaultRotation action.

            :returns: "RetRotation"
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDefaultRotation", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RetRotation",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetFixedWhiteBalance(self, extract_returns=True):
        """
            Calls the GetFixedWhiteBalance action.

            :returns: "RetFixedWhiteBalance"
        """
        arguments = { }

        out_params = self.proxy_call_action("GetFixedWhiteBalance", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RetFixedWhiteBalance",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_IncreaseBrightness(self, extract_returns=True):
        """
            Calls the IncreaseBrightness action.

            :returns: "result"
        """
        arguments = { }

        out_params = self.proxy_call_action("IncreaseBrightness", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_IncreaseColorSaturation(self, extract_returns=True):
        """
            Calls the IncreaseColorSaturation action.

            :returns: "result"
        """
        arguments = { }

        out_params = self.proxy_call_action("IncreaseColorSaturation", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetAutomaticWhiteBalance(self, NewAutomaticWhiteBalance, extract_returns=True):
        """
            Calls the SetAutomaticWhiteBalance action.

            :returns: "result"
        """
        arguments = {
            "NewAutomaticWhiteBalance": NewAutomaticWhiteBalance,
        }

        out_params = self.proxy_call_action("SetAutomaticWhiteBalance", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetBrightness(self, NewBrightness, extract_returns=True):
        """
            Calls the SetBrightness action.

            :returns: "result"
        """
        arguments = {
            "NewBrightness": NewBrightness,
        }

        out_params = self.proxy_call_action("SetBrightness", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetColorSaturation(self, NewColorSaturation, extract_returns=True):
        """
            Calls the SetColorSaturation action.

            :returns: "result"
        """
        arguments = {
            "NewColorSaturation": NewColorSaturation,
        }

        out_params = self.proxy_call_action("SetColorSaturation", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetDefaultRotation(self, NewRotation, extract_returns=True):
        """
            Calls the SetDefaultRotation action.

            :returns: "result"
        """
        arguments = {
            "NewRotation": NewRotation,
        }

        out_params = self.proxy_call_action("SetDefaultRotation", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetFixedWhiteBalance(self, NewFixedWhiteBalance, extract_returns=True):
        """
            Calls the SetFixedWhiteBalance action.

            :returns: "result"
        """
        arguments = {
            "NewFixedWhiteBalance": NewFixedWhiteBalance,
        }

        out_params = self.proxy_call_action("SetFixedWhiteBalance", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

