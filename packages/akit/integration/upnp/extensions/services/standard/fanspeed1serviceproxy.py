"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class FanSpeed1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'FanSpeed1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:FanSpeed:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:FanSpeed'


    def get_DirectionStatus(self):
        """
            Gets the "DirectionStatus" variable.
        """
        rval = self.proxy_get_variable_value("DirectionStatus")
        return rval


    def set_DirectionStatus(self, val):
        """
            Sets the "DirectionStatus" variable.
        """
        self.proxy_set_variable_value("DirectionStatus", val)
        return


    def get_DirectionTarget(self):
        """
            Gets the "DirectionTarget" variable.
        """
        rval = self.proxy_get_variable_value("DirectionTarget")
        return rval


    def set_DirectionTarget(self, val):
        """
            Sets the "DirectionTarget" variable.
        """
        self.proxy_set_variable_value("DirectionTarget", val)
        return


    def get_FanSpeedStatus(self):
        """
            Gets the "FanSpeedStatus" variable.
        """
        rval = self.proxy_get_variable_value("FanSpeedStatus")
        return rval


    def set_FanSpeedStatus(self, val):
        """
            Sets the "FanSpeedStatus" variable.
        """
        self.proxy_set_variable_value("FanSpeedStatus", val)
        return


    def get_FanSpeedTarget(self):
        """
            Gets the "FanSpeedTarget" variable.
        """
        rval = self.proxy_get_variable_value("FanSpeedTarget")
        return rval


    def set_FanSpeedTarget(self, val):
        """
            Sets the "FanSpeedTarget" variable.
        """
        self.proxy_set_variable_value("FanSpeedTarget", val)
        return


    def action_GetFanDirection(self):
        """
            Calls the GetFanDirection action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetFanDirection", arguments=arguments)

        (CurrentDirectionStatus,) = out_params

        return CurrentDirectionStatus


    def action_GetFanDirectionTarget(self):
        """
            Calls the GetFanDirectionTarget action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetFanDirectionTarget", arguments=arguments)

        (CurrentDirectionTarget,) = out_params

        return CurrentDirectionTarget


    def action_GetFanSpeed(self):
        """
            Calls the GetFanSpeed action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetFanSpeed", arguments=arguments)

        (CurrentFanSpeedStatus,) = out_params

        return CurrentFanSpeedStatus


    def action_GetFanSpeedTarget(self):
        """
            Calls the GetFanSpeedTarget action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetFanSpeedTarget", arguments=arguments)

        (CurrentFanSpeedTarget,) = out_params

        return CurrentFanSpeedTarget


    def action_SetFanDirection(self, NewDirectionTarget):
        """
            Calls the SetFanDirection action.
        """
        arguments = {
            "NewDirectionTarget": NewDirectionTarget,
        }

        out_params = self.proxy_call_action("SetFanDirection", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetFanSpeed(self, NewFanSpeedTarget):
        """
            Calls the SetFanSpeed action.
        """
        arguments = {
            "NewFanSpeedTarget": NewFanSpeedTarget,
        }

        out_params = self.proxy_call_action("SetFanSpeed", arguments=arguments)

        (result,) = out_params

        return result

