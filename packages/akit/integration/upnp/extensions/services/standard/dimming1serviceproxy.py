"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class Dimming1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'Dimming1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:Dimming:1'
    SERVICE_ID = 'urn:schemas-upnp-org:service:Dimming'


    def get_IsRamping(self):
        """
            Gets the "IsRamping" variable.
        """
        rval = self.proxy_get_variable_value("IsRamping")
        return rval


    def set_IsRamping(self, val):
        """
            Sets the "IsRamping" variable.
        """
        self.proxy_set_variable_value("IsRamping", val)
        return


    def get_LoadLevelStatus(self):
        """
            Gets the "LoadLevelStatus" variable.
        """
        rval = self.proxy_get_variable_value("LoadLevelStatus")
        return rval


    def set_LoadLevelStatus(self, val):
        """
            Sets the "LoadLevelStatus" variable.
        """
        self.proxy_set_variable_value("LoadLevelStatus", val)
        return


    def get_LoadLevelTarget(self):
        """
            Gets the "LoadLevelTarget" variable.
        """
        rval = self.proxy_get_variable_value("LoadLevelTarget")
        return rval


    def set_LoadLevelTarget(self, val):
        """
            Sets the "LoadLevelTarget" variable.
        """
        self.proxy_set_variable_value("LoadLevelTarget", val)
        return


    def get_OnEffect(self):
        """
            Gets the "OnEffect" variable.
        """
        rval = self.proxy_get_variable_value("OnEffect")
        return rval


    def set_OnEffect(self, val):
        """
            Sets the "OnEffect" variable.
        """
        self.proxy_set_variable_value("OnEffect", val)
        return


    def get_OnEffectLevel(self):
        """
            Gets the "OnEffectLevel" variable.
        """
        rval = self.proxy_get_variable_value("OnEffectLevel")
        return rval


    def set_OnEffectLevel(self, val):
        """
            Sets the "OnEffectLevel" variable.
        """
        self.proxy_set_variable_value("OnEffectLevel", val)
        return


    def get_RampPaused(self):
        """
            Gets the "RampPaused" variable.
        """
        rval = self.proxy_get_variable_value("RampPaused")
        return rval


    def set_RampPaused(self, val):
        """
            Sets the "RampPaused" variable.
        """
        self.proxy_set_variable_value("RampPaused", val)
        return


    def get_RampRate(self):
        """
            Gets the "RampRate" variable.
        """
        rval = self.proxy_get_variable_value("RampRate")
        return rval


    def set_RampRate(self, val):
        """
            Sets the "RampRate" variable.
        """
        self.proxy_set_variable_value("RampRate", val)
        return


    def get_RampTime(self):
        """
            Gets the "RampTime" variable.
        """
        rval = self.proxy_get_variable_value("RampTime")
        return rval


    def set_RampTime(self, val):
        """
            Sets the "RampTime" variable.
        """
        self.proxy_set_variable_value("RampTime", val)
        return


    def get_StepDelta(self):
        """
            Gets the "StepDelta" variable.
        """
        rval = self.proxy_get_variable_value("StepDelta")
        return rval


    def set_StepDelta(self, val):
        """
            Sets the "StepDelta" variable.
        """
        self.proxy_set_variable_value("StepDelta", val)
        return


    def get_ValidOutputValues(self):
        """
            Gets the "ValidOutputValues" variable.
        """
        rval = self.proxy_get_variable_value("ValidOutputValues")
        return rval


    def set_ValidOutputValues(self, val):
        """
            Sets the "ValidOutputValues" variable.
        """
        self.proxy_set_variable_value("ValidOutputValues", val)
        return


    def action_GetIsRamping(self):
        """
            Calls the GetIsRamping action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetIsRamping", arguments=arguments)

        (retIsRamping,) = out_params

        return retIsRamping


    def action_GetLoadLevelStatus(self):
        """
            Calls the GetLoadLevelStatus action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetLoadLevelStatus", arguments=arguments)

        (retLoadlevelStatus,) = out_params

        return retLoadlevelStatus


    def action_GetLoadLevelTarget(self):
        """
            Calls the GetLoadLevelTarget action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetLoadLevelTarget", arguments=arguments)

        (GetLoadlevelTarget,) = out_params

        return GetLoadlevelTarget


    def action_GetOnEffectParameters(self):
        """
            Calls the GetOnEffectParameters action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetOnEffectParameters", arguments=arguments)

        (retOnEffect, retOnEffectLevel,) = out_params

        return retOnEffect, retOnEffectLevel


    def action_GetRampPaused(self):
        """
            Calls the GetRampPaused action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetRampPaused", arguments=arguments)

        (retRampPaused,) = out_params

        return retRampPaused


    def action_GetRampRate(self):
        """
            Calls the GetRampRate action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetRampRate", arguments=arguments)

        (retRampRate,) = out_params

        return retRampRate


    def action_GetRampTime(self):
        """
            Calls the GetRampTime action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetRampTime", arguments=arguments)

        (retRampTime,) = out_params

        return retRampTime


    def action_GetStepDelta(self):
        """
            Calls the GetStepDelta action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetStepDelta", arguments=arguments)

        (retStepDelta,) = out_params

        return retStepDelta


    def action_PauseRamp(self):
        """
            Calls the PauseRamp action.
        """
        arguments = { }

        out_params = self.proxy_call_action("PauseRamp", arguments=arguments)

        (retRampRate,) = out_params

        return retRampRate


    def action_ResumeRamp(self):
        """
            Calls the ResumeRamp action.
        """
        arguments = { }

        out_params = self.proxy_call_action("ResumeRamp", arguments=arguments)

        (retRampRate,) = out_params

        return retRampRate


    def action_SetLoadLevelTarget(self, newLoadlevelTarget):
        """
            Calls the SetLoadLevelTarget action.
        """
        arguments = {
            "newLoadlevelTarget": newLoadlevelTarget,
        }

        out_params = self.proxy_call_action("SetLoadLevelTarget", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetOnEffect(self, newOnEffect):
        """
            Calls the SetOnEffect action.
        """
        arguments = {
            "newOnEffect": newOnEffect,
        }

        out_params = self.proxy_call_action("SetOnEffect", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetOnEffectLevel(self, newOnEffectLevel):
        """
            Calls the SetOnEffectLevel action.
        """
        arguments = {
            "newOnEffectLevel": newOnEffectLevel,
        }

        out_params = self.proxy_call_action("SetOnEffectLevel", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetRampRate(self, newRampRate):
        """
            Calls the SetRampRate action.
        """
        arguments = {
            "newRampRate": newRampRate,
        }

        out_params = self.proxy_call_action("SetRampRate", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetStepDelta(self, newStepDelta):
        """
            Calls the SetStepDelta action.
        """
        arguments = {
            "newStepDelta": newStepDelta,
        }

        out_params = self.proxy_call_action("SetStepDelta", arguments=arguments)

        (result,) = out_params

        return result


    def action_StartRampDown(self):
        """
            Calls the StartRampDown action.
        """
        arguments = { }

        out_params = self.proxy_call_action("StartRampDown", arguments=arguments)

        (retOnEffect, retOnEffectLevel,) = out_params

        return retOnEffect, retOnEffectLevel


    def action_StartRampToLevel(self, newLoadLevelTarget, newRampTime):
        """
            Calls the StartRampToLevel action.
        """
        arguments = {
            "newLoadLevelTarget": newLoadLevelTarget,
            "newRampTime": newRampTime,
        }

        out_params = self.proxy_call_action("StartRampToLevel", arguments=arguments)

        (result,) = out_params

        return result


    def action_StartRampUp(self):
        """
            Calls the StartRampUp action.
        """
        arguments = { }

        out_params = self.proxy_call_action("StartRampUp", arguments=arguments)

        (retOnEffect, retOnEffectLevel,) = out_params

        return retOnEffect, retOnEffectLevel


    def action_StepDown(self):
        """
            Calls the StepDown action.
        """
        arguments = { }

        out_params = self.proxy_call_action("StepDown", arguments=arguments)

        (retOnEffect, retOnEffectLevel,) = out_params

        return retOnEffect, retOnEffectLevel


    def action_StepUp(self):
        """
            Calls the StepUp action.
        """
        arguments = { }

        out_params = self.proxy_call_action("StepUp", arguments=arguments)

        (retOnEffect, retOnEffectLevel,) = out_params

        return retOnEffect, retOnEffectLevel


    def action_StopRamp(self):
        """
            Calls the StopRamp action.
        """
        arguments = { }

        out_params = self.proxy_call_action("StopRamp", arguments=arguments)

        (retOnEffect, retOnEffectLevel,) = out_params

        return retOnEffect, retOnEffectLevel

