"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class Dimming1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'Dimming1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:Dimming:1'

    SERVICE_EVENT_VARIABLES = {
        "IsRamping": { "data_type": "boolean", "default": "0", "allowed_list": None},
        "LoadLevelStatus": { "data_type": "ui1", "default": "0", "allowed_list": None},
        "RampPaused": { "data_type": "boolean", "default": "0", "allowed_list": None},
        "RampRate": { "data_type": "ui1", "default": "0", "allowed_list": None},
        "StepDelta": { "data_type": "ui1", "default": "Manufacturer defined default value", "allowed_list": None},
    }

    def action_GetIsRamping(self, extract_returns=True):
        """
            Calls the GetIsRamping action.

            :returns: "retIsRamping"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetIsRamping", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("retIsRamping",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetLoadLevelStatus(self, extract_returns=True):
        """
            Calls the GetLoadLevelStatus action.

            :returns: "retLoadlevelStatus"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetLoadLevelStatus", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("retLoadlevelStatus",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetLoadLevelTarget(self, extract_returns=True):
        """
            Calls the GetLoadLevelTarget action.

            :returns: "GetLoadlevelTarget"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetLoadLevelTarget", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("GetLoadlevelTarget",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetOnEffectParameters(self, extract_returns=True):
        """
            Calls the GetOnEffectParameters action.

            :returns: "retOnEffect", "retOnEffectLevel"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetOnEffectParameters", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("retOnEffect", "retOnEffectLevel",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetRampPaused(self, extract_returns=True):
        """
            Calls the GetRampPaused action.

            :returns: "retRampPaused"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetRampPaused", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("retRampPaused",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetRampRate(self, extract_returns=True):
        """
            Calls the GetRampRate action.

            :returns: "retRampRate"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetRampRate", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("retRampRate",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetRampTime(self, extract_returns=True):
        """
            Calls the GetRampTime action.

            :returns: "retRampTime"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetRampTime", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("retRampTime",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetStepDelta(self, extract_returns=True):
        """
            Calls the GetStepDelta action.

            :returns: "retStepDelta"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetStepDelta", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("retStepDelta",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_PauseRamp(self, extract_returns=True):
        """
            Calls the PauseRamp action.

            :returns: "result"
        """
        arguments = { }

        out_params = self._proxy_call_action("PauseRamp", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_ResumeRamp(self, extract_returns=True):
        """
            Calls the ResumeRamp action.

            :returns: "result"
        """
        arguments = { }

        out_params = self._proxy_call_action("ResumeRamp", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetLoadLevelTarget(self, newLoadlevelTarget, extract_returns=True):
        """
            Calls the SetLoadLevelTarget action.

            :returns: "result"
        """
        arguments = {
            "newLoadlevelTarget": newLoadlevelTarget,
        }

        out_params = self._proxy_call_action("SetLoadLevelTarget", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetOnEffect(self, newOnEffect, extract_returns=True):
        """
            Calls the SetOnEffect action.

            :returns: "result"
        """
        arguments = {
            "newOnEffect": newOnEffect,
        }

        out_params = self._proxy_call_action("SetOnEffect", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetOnEffectLevel(self, newOnEffectLevel, extract_returns=True):
        """
            Calls the SetOnEffectLevel action.

            :returns: "result"
        """
        arguments = {
            "newOnEffectLevel": newOnEffectLevel,
        }

        out_params = self._proxy_call_action("SetOnEffectLevel", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetRampRate(self, newRampRate, extract_returns=True):
        """
            Calls the SetRampRate action.

            :returns: "result"
        """
        arguments = {
            "newRampRate": newRampRate,
        }

        out_params = self._proxy_call_action("SetRampRate", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetStepDelta(self, newStepDelta, extract_returns=True):
        """
            Calls the SetStepDelta action.

            :returns: "result"
        """
        arguments = {
            "newStepDelta": newStepDelta,
        }

        out_params = self._proxy_call_action("SetStepDelta", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_StartRampDown(self, extract_returns=True):
        """
            Calls the StartRampDown action.

            :returns: "result"
        """
        arguments = { }

        out_params = self._proxy_call_action("StartRampDown", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_StartRampToLevel(self, newLoadLevelTarget, newRampTime, extract_returns=True):
        """
            Calls the StartRampToLevel action.

            :returns: "result"
        """
        arguments = {
            "newLoadLevelTarget": newLoadLevelTarget,
            "newRampTime": newRampTime,
        }

        out_params = self._proxy_call_action("StartRampToLevel", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_StartRampUp(self, extract_returns=True):
        """
            Calls the StartRampUp action.

            :returns: "result"
        """
        arguments = { }

        out_params = self._proxy_call_action("StartRampUp", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_StepDown(self, extract_returns=True):
        """
            Calls the StepDown action.

            :returns: "result"
        """
        arguments = { }

        out_params = self._proxy_call_action("StepDown", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_StepUp(self, extract_returns=True):
        """
            Calls the StepUp action.

            :returns: "result"
        """
        arguments = { }

        out_params = self._proxy_call_action("StepUp", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_StopRamp(self, extract_returns=True):
        """
            Calls the StopRamp action.

            :returns: "result"
        """
        arguments = { }

        out_params = self._proxy_call_action("StopRamp", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args
