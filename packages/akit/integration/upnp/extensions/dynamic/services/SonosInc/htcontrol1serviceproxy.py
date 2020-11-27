"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class HTControl1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'HTControl1' service.
    """

    SERVICE_MANUFACTURER = 'SonosInc'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:HTControl:1'

    SERVICE_EVENT_VARIABLES = {
        "IRRepeaterState": { "data_type": "string", "default": None, "allowed_list": "['On', 'Off', 'Disabled']"},
        "TOSLinkConnected": { "data_type": "boolean", "default": None, "allowed_list": None},
    }


    def action_CommitLearnedIRCodes(self, Name, extract_returns=True):
        """
            Calls the CommitLearnedIRCodes action.

            :returns: "result"
        """
        arguments = {
            "Name": Name,
        }

        out_params = self._proxy_call_action("CommitLearnedIRCodes", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetIRRepeaterState(self, extract_returns=True):
        """
            Calls the GetIRRepeaterState action.

            :returns: "CurrentIRRepeaterState"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetIRRepeaterState", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentIRRepeaterState",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetLEDFeedbackState(self, extract_returns=True):
        """
            Calls the GetLEDFeedbackState action.

            :returns: "LEDFeedbackState"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetLEDFeedbackState", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("LEDFeedbackState",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_IdentifyIRRemote(self, Timeout, extract_returns=True):
        """
            Calls the IdentifyIRRemote action.

            :returns: "result"
        """
        arguments = {
            "Timeout": Timeout,
        }

        out_params = self._proxy_call_action("IdentifyIRRemote", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_IsRemoteConfigured(self, extract_returns=True):
        """
            Calls the IsRemoteConfigured action.

            :returns: "RemoteConfigured"
        """
        arguments = { }

        out_params = self._proxy_call_action("IsRemoteConfigured", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RemoteConfigured",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_LearnIRCode(self, IRCode, Timeout, extract_returns=True):
        """
            Calls the LearnIRCode action.

            :returns: "result"
        """
        arguments = {
            "IRCode": IRCode,
            "Timeout": Timeout,
        }

        out_params = self._proxy_call_action("LearnIRCode", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetIRRepeaterState(self, DesiredIRRepeaterState, extract_returns=True):
        """
            Calls the SetIRRepeaterState action.

            :returns: "result"
        """
        arguments = {
            "DesiredIRRepeaterState": DesiredIRRepeaterState,
        }

        out_params = self._proxy_call_action("SetIRRepeaterState", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetLEDFeedbackState(self, LEDFeedbackState, extract_returns=True):
        """
            Calls the SetLEDFeedbackState action.

            :returns: "result"
        """
        arguments = {
            "LEDFeedbackState": LEDFeedbackState,
        }

        out_params = self._proxy_call_action("SetLEDFeedbackState", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

