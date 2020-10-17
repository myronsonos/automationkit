"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class CallManagement1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'CallManagement1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:CallManagement:1'


    def action_AcceptCall(self, TelCPName, SecretKey, TargetCallID, MediaCapabilityInfo, CallMode, extract_returns=True):
        """
            Calls the AcceptCall action.

            :returns: "result"
        """
        arguments = {
            "TelCPName": TelCPName,
            "SecretKey": SecretKey,
            "TargetCallID": TargetCallID,
            "MediaCapabilityInfo": MediaCapabilityInfo,
            "CallMode": CallMode,
        }

        out_params = self.proxy_call_action("AcceptCall", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_AcceptModifyCall(self, TelCPName, SecretKey, TargetCallID, MediaCapabilityInfo, extract_returns=True):
        """
            Calls the AcceptModifyCall action.

            :returns: "result"
        """
        arguments = {
            "TelCPName": TelCPName,
            "SecretKey": SecretKey,
            "TargetCallID": TargetCallID,
            "MediaCapabilityInfo": MediaCapabilityInfo,
        }

        out_params = self.proxy_call_action("AcceptModifyCall", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_ChangeMonopolizer(self, CurrentMonopolizer, SecretKey, CallID, NewMonopolizer, extract_returns=True):
        """
            Calls the ChangeMonopolizer action.

            :returns: "result"
        """
        arguments = {
            "CurrentMonopolizer": CurrentMonopolizer,
            "SecretKey": SecretKey,
            "CallID": CallID,
            "NewMonopolizer": NewMonopolizer,
        }

        out_params = self.proxy_call_action("ChangeMonopolizer", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_ChangeTelCPName(self, CurrentTelCPName, CurrentSecretKey, NewTelCPName, extract_returns=True):
        """
            Calls the ChangeTelCPName action.

            :returns: "NewSecretKey", "Expires"
        """
        arguments = {
            "CurrentTelCPName": CurrentTelCPName,
            "CurrentSecretKey": CurrentSecretKey,
            "NewTelCPName": NewTelCPName,
        }

        out_params = self.proxy_call_action("ChangeTelCPName", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewSecretKey", "Expires",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_ClearCallBack(self, CallBackID, extract_returns=True):
        """
            Calls the ClearCallBack action.

            :returns: "result"
        """
        arguments = {
            "CallBackID": CallBackID,
        }

        out_params = self.proxy_call_action("ClearCallBack", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_ClearCallLogs(self, extract_returns=True):
        """
            Calls the ClearCallLogs action.

            :returns: "result"
        """
        arguments = { }

        out_params = self.proxy_call_action("ClearCallLogs", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetCallBackInfo(self, extract_returns=True):
        """
            Calls the GetCallBackInfo action.

            :returns: "CallBackInfo"
        """
        arguments = { }

        out_params = self.proxy_call_action("GetCallBackInfo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CallBackInfo",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetCallInfo(self, TelCPName, SecretKey, TargetCallID, extract_returns=True):
        """
            Calls the GetCallInfo action.

            :returns: "CallInfoList"
        """
        arguments = {
            "TelCPName": TelCPName,
            "SecretKey": SecretKey,
            "TargetCallID": TargetCallID,
        }

        out_params = self.proxy_call_action("GetCallInfo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CallInfoList",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetCallLogs(self, extract_returns=True):
        """
            Calls the GetCallLogs action.

            :returns: "CallLogs"
        """
        arguments = { }

        out_params = self.proxy_call_action("GetCallLogs", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CallLogs",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetMediaCapabilities(self, TCMediaCapabilityInfo, extract_returns=True):
        """
            Calls the GetMediaCapabilities action.

            :returns: "SupportedMediaCapabilityInfo"
        """
        arguments = {
            "TCMediaCapabilityInfo": TCMediaCapabilityInfo,
        }

        out_params = self.proxy_call_action("GetMediaCapabilities", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("SupportedMediaCapabilityInfo",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetTelCPNameList(self, extract_returns=True):
        """
            Calls the GetTelCPNameList action.

            :returns: "TelCPNameList"
        """
        arguments = { }

        out_params = self.proxy_call_action("GetTelCPNameList", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("TelCPNameList",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetTelephonyIdentity(self, extract_returns=True):
        """
            Calls the GetTelephonyIdentity action.

            :returns: "TelephonyIdentity"
        """
        arguments = { }

        out_params = self.proxy_call_action("GetTelephonyIdentity", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("TelephonyIdentity",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_InitiateCall(self, CalleeID, extract_returns=True):
        """
            Calls the InitiateCall action.

            :returns: "CallID"
        """
        arguments = {
            "CalleeID": CalleeID,
        }

        out_params = self.proxy_call_action("InitiateCall", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CallID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_ModifyCall(self, TelCPName, SecretKey, TargetCallID, MediaCapabilityInfo, extract_returns=True):
        """
            Calls the ModifyCall action.

            :returns: "result"
        """
        arguments = {
            "TelCPName": TelCPName,
            "SecretKey": SecretKey,
            "TargetCallID": TargetCallID,
            "MediaCapabilityInfo": MediaCapabilityInfo,
        }

        out_params = self.proxy_call_action("ModifyCall", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_RegisterCallBack(self, CalleeID, extract_returns=True):
        """
            Calls the RegisterCallBack action.

            :returns: "CallBackID"
        """
        arguments = {
            "CalleeID": CalleeID,
        }

        out_params = self.proxy_call_action("RegisterCallBack", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CallBackID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_RegisterTelCPName(self, TelCPName, CurrentSecretKey, extract_returns=True):
        """
            Calls the RegisterTelCPName action.

            :returns: "NewSecretKey", "Expires"
        """
        arguments = {
            "TelCPName": TelCPName,
            "CurrentSecretKey": CurrentSecretKey,
        }

        out_params = self.proxy_call_action("RegisterTelCPName", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewSecretKey", "Expires",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_RejectCall(self, TelCPName, SecretKey, TargetCallID, RejectReason, extract_returns=True):
        """
            Calls the RejectCall action.

            :returns: "result"
        """
        arguments = {
            "TelCPName": TelCPName,
            "SecretKey": SecretKey,
            "TargetCallID": TargetCallID,
            "RejectReason": RejectReason,
        }

        out_params = self.proxy_call_action("RejectCall", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_StartCall(self, TelCPName, SecretKey, CalleeID, CallPriority, MediaCapabilityInfo, CallMode, extract_returns=True):
        """
            Calls the StartCall action.

            :returns: "CallID"
        """
        arguments = {
            "TelCPName": TelCPName,
            "SecretKey": SecretKey,
            "CalleeID": CalleeID,
            "CallPriority": CallPriority,
            "MediaCapabilityInfo": MediaCapabilityInfo,
            "CallMode": CallMode,
        }

        out_params = self.proxy_call_action("StartCall", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CallID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_StartMediaTransfer(self, TelCPName, SecretKey, TargetCallID, TCList, MediaCapabilityInfo, extract_returns=True):
        """
            Calls the StartMediaTransfer action.

            :returns: "result"
        """
        arguments = {
            "TelCPName": TelCPName,
            "SecretKey": SecretKey,
            "TargetCallID": TargetCallID,
            "TCList": TCList,
            "MediaCapabilityInfo": MediaCapabilityInfo,
        }

        out_params = self.proxy_call_action("StartMediaTransfer", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_StopCall(self, TelCPName, SecretKey, CallID, extract_returns=True):
        """
            Calls the StopCall action.

            :returns: "result"
        """
        arguments = {
            "TelCPName": TelCPName,
            "SecretKey": SecretKey,
            "CallID": CallID,
        }

        out_params = self.proxy_call_action("StopCall", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_UnregisterTelCPName(self, TelCPName, SecretKey, extract_returns=True):
        """
            Calls the UnregisterTelCPName action.

            :returns: "result"
        """
        arguments = {
            "TelCPName": TelCPName,
            "SecretKey": SecretKey,
        }

        out_params = self.proxy_call_action("UnregisterTelCPName", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

