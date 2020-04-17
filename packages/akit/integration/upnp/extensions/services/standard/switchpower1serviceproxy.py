"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class SwitchPower1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'SwitchPower1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:SwitchPower:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:SwitchPower'


    def get_Status(self):
        """
            Gets the "Status" variable.
        """
        rval = self.proxy_get_variable_value("Status")
        return rval


    def set_Status(self, val):
        """
            Sets the "Status" variable.
        """
        self.proxy_set_variable_value("Status", val)
        return


    def get_Target(self):
        """
            Gets the "Target" variable.
        """
        rval = self.proxy_get_variable_value("Target")
        return rval


    def set_Target(self, val):
        """
            Sets the "Target" variable.
        """
        self.proxy_set_variable_value("Target", val)
        return


    def action_GetStatus(self):
        """
            Calls the GetStatus action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetStatus", arguments=arguments)

        (ResultStatus,) = out_params

        return ResultStatus


    def action_GetTarget(self):
        """
            Calls the GetTarget action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetTarget", arguments=arguments)

        (RetTargetValue,) = out_params

        return RetTargetValue


    def action_SetTarget(self, newTargetValue):
        """
            Calls the SetTarget action.
        """
        arguments = {
            "newTargetValue": newTargetValue,
        }

        out_params = self.proxy_call_action("SetTarget", arguments=arguments)

        (result,) = out_params

        return result

