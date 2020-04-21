"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class ControlValve1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'ControlValve1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:ControlValve:1'
    SERVICE_ID = 'urn:schemas-upnp-org:service:ControlValve'


    def get_ControlMode(self):
        """
            Gets the "ControlMode" variable.
        """
        rval = self.proxy_get_variable_value("ControlMode")
        return rval


    def set_ControlMode(self, val):
        """
            Sets the "ControlMode" variable.
        """
        self.proxy_set_variable_value("ControlMode", val)
        return


    def get_MaxPosition(self):
        """
            Gets the "MaxPosition" variable.
        """
        rval = self.proxy_get_variable_value("MaxPosition")
        return rval


    def set_MaxPosition(self, val):
        """
            Sets the "MaxPosition" variable.
        """
        self.proxy_set_variable_value("MaxPosition", val)
        return


    def get_MinPosition(self):
        """
            Gets the "MinPosition" variable.
        """
        rval = self.proxy_get_variable_value("MinPosition")
        return rval


    def set_MinPosition(self, val):
        """
            Sets the "MinPosition" variable.
        """
        self.proxy_set_variable_value("MinPosition", val)
        return


    def get_PositionStatus(self):
        """
            Gets the "PositionStatus" variable.
        """
        rval = self.proxy_get_variable_value("PositionStatus")
        return rval


    def set_PositionStatus(self, val):
        """
            Sets the "PositionStatus" variable.
        """
        self.proxy_set_variable_value("PositionStatus", val)
        return


    def get_PositionTarget(self):
        """
            Gets the "PositionTarget" variable.
        """
        rval = self.proxy_get_variable_value("PositionTarget")
        return rval


    def set_PositionTarget(self, val):
        """
            Sets the "PositionTarget" variable.
        """
        self.proxy_set_variable_value("PositionTarget", val)
        return


    def action_GetMinMax(self):
        """
            Calls the GetMinMax action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetMinMax", arguments=arguments)

        (CurrentMinPosition, CurrentMaxPosition,) = out_params

        return CurrentMinPosition, CurrentMaxPosition


    def action_GetMode(self):
        """
            Calls the GetMode action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetMode", arguments=arguments)

        (CurrentControlMode,) = out_params

        return CurrentControlMode


    def action_GetPosition(self):
        """
            Calls the GetPosition action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetPosition", arguments=arguments)

        (CurrentPositionStatus,) = out_params

        return CurrentPositionStatus


    def action_GetPositionTarget(self):
        """
            Calls the GetPositionTarget action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetPositionTarget", arguments=arguments)

        (CurrentPositionTarget,) = out_params

        return CurrentPositionTarget


    def action_SetMinMax(self, NewMinPosition, NewMaxPosition):
        """
            Calls the SetMinMax action.
        """
        arguments = {
            "NewMinPosition": NewMinPosition,
            "NewMaxPosition": NewMaxPosition,
        }

        out_params = self.proxy_call_action("SetMinMax", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetMode(self, NewControlMode):
        """
            Calls the SetMode action.
        """
        arguments = {
            "NewControlMode": NewControlMode,
        }

        out_params = self.proxy_call_action("SetMode", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetPosition(self, NewPositionTarget):
        """
            Calls the SetPosition action.
        """
        arguments = {
            "NewPositionTarget": NewPositionTarget,
        }

        out_params = self.proxy_call_action("SetPosition", arguments=arguments)

        (result,) = out_params

        return result

