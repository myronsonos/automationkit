"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class WANIPConnection1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'WANIPConnection1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:WANIPConnection:1'

    SERVICE_EVENT_VARIABLES = {}


    def action_AddPortMapping(self, NewRemoteHost, NewExternalPort, NewProtocol, NewInternalPort, NewInternalClient, NewEnabled, NewPortMappingDescription, NewLeaseDuration, extract_returns=True):
        """
            Calls the AddPortMapping action.

            :returns: "result"
        """
        arguments = {
            "NewRemoteHost": NewRemoteHost,
            "NewExternalPort": NewExternalPort,
            "NewProtocol": NewProtocol,
            "NewInternalPort": NewInternalPort,
            "NewInternalClient": NewInternalClient,
            "NewEnabled": NewEnabled,
            "NewPortMappingDescription": NewPortMappingDescription,
            "NewLeaseDuration": NewLeaseDuration,
        }

        out_params = self._proxy_call_action("AddPortMapping", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_DeletePortMapping(self, NewRemoteHost, NewExternalPort, NewProtocol, extract_returns=True):
        """
            Calls the DeletePortMapping action.

            :returns: "result"
        """
        arguments = {
            "NewRemoteHost": NewRemoteHost,
            "NewExternalPort": NewExternalPort,
            "NewProtocol": NewProtocol,
        }

        out_params = self._proxy_call_action("DeletePortMapping", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_ForceTermination(self, extract_returns=True):
        """
            Calls the ForceTermination action.

            :returns: "result"
        """
        arguments = { }

        out_params = self._proxy_call_action("ForceTermination", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetAutoDisconnectTime(self, extract_returns=True):
        """
            Calls the GetAutoDisconnectTime action.

            :returns: "NewAutoDisconnectTime"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetAutoDisconnectTime", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewAutoDisconnectTime",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetConnectionTypeInfo(self, extract_returns=True):
        """
            Calls the GetConnectionTypeInfo action.

            :returns: "NewConnectionType", "NewPossibleConnectionTypes"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetConnectionTypeInfo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewConnectionType", "NewPossibleConnectionTypes",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetExternalIPAddress(self, extract_returns=True):
        """
            Calls the GetExternalIPAddress action.

            :returns: "NewExternalIPAddress"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetExternalIPAddress", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewExternalIPAddress",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetGenericPortMappingEntry(self, NewPortMappingIndex, extract_returns=True):
        """
            Calls the GetGenericPortMappingEntry action.

            :returns: "NewRemoteHost", "NewExternalPort", "NewProtocol", "NewInternalPort", "NewInternalClient", "NewEnabled", "NewPortMappingDescription", "NewLeaseDuration"
        """
        arguments = {
            "NewPortMappingIndex": NewPortMappingIndex,
        }

        out_params = self._proxy_call_action("GetGenericPortMappingEntry", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewRemoteHost", "NewExternalPort", "NewProtocol", "NewInternalPort", "NewInternalClient", "NewEnabled", "NewPortMappingDescription", "NewLeaseDuration",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetIdleDisconnectTime(self, extract_returns=True):
        """
            Calls the GetIdleDisconnectTime action.

            :returns: "NewIdleDisconnectTime"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetIdleDisconnectTime", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewIdleDisconnectTime",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetNATRSIPStatus(self, extract_returns=True):
        """
            Calls the GetNATRSIPStatus action.

            :returns: "NewRSIPAvailable", "NewNATEnabled"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetNATRSIPStatus", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewRSIPAvailable", "NewNATEnabled",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetSpecificPortMappingEntry(self, NewRemoteHost, NewExternalPort, NewProtocol, extract_returns=True):
        """
            Calls the GetSpecificPortMappingEntry action.

            :returns: "NewInternalPort", "NewInternalClient", "NewEnabled", "NewPortMappingDescription", "NewLeaseDuration"
        """
        arguments = {
            "NewRemoteHost": NewRemoteHost,
            "NewExternalPort": NewExternalPort,
            "NewProtocol": NewProtocol,
        }

        out_params = self._proxy_call_action("GetSpecificPortMappingEntry", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewInternalPort", "NewInternalClient", "NewEnabled", "NewPortMappingDescription", "NewLeaseDuration",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetStatusInfo(self, extract_returns=True):
        """
            Calls the GetStatusInfo action.

            :returns: "NewConnectionStatus", "NewLastConnectionError", "NewUptime"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetStatusInfo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewConnectionStatus", "NewLastConnectionError", "NewUptime",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetWarnDisconnectDelay(self, extract_returns=True):
        """
            Calls the GetWarnDisconnectDelay action.

            :returns: "NewWarnDisconnectDelay"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetWarnDisconnectDelay", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewWarnDisconnectDelay",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_RequestConnection(self, extract_returns=True):
        """
            Calls the RequestConnection action.

            :returns: "result"
        """
        arguments = { }

        out_params = self._proxy_call_action("RequestConnection", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_RequestTermination(self, extract_returns=True):
        """
            Calls the RequestTermination action.

            :returns: "result"
        """
        arguments = { }

        out_params = self._proxy_call_action("RequestTermination", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetAutoDisconnectTime(self, NewAutoDisconnectTime, extract_returns=True):
        """
            Calls the SetAutoDisconnectTime action.

            :returns: "result"
        """
        arguments = {
            "NewAutoDisconnectTime": NewAutoDisconnectTime,
        }

        out_params = self._proxy_call_action("SetAutoDisconnectTime", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetConnectionType(self, NewConnectionType, extract_returns=True):
        """
            Calls the SetConnectionType action.

            :returns: "result"
        """
        arguments = {
            "NewConnectionType": NewConnectionType,
        }

        out_params = self._proxy_call_action("SetConnectionType", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetIdleDisconnectTime(self, NewIdleDisconnectTime, extract_returns=True):
        """
            Calls the SetIdleDisconnectTime action.

            :returns: "result"
        """
        arguments = {
            "NewIdleDisconnectTime": NewIdleDisconnectTime,
        }

        out_params = self._proxy_call_action("SetIdleDisconnectTime", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetWarnDisconnectDelay(self, NewWarnDisconnectDelay, extract_returns=True):
        """
            Calls the SetWarnDisconnectDelay action.

            :returns: "result"
        """
        arguments = {
            "NewWarnDisconnectDelay": NewWarnDisconnectDelay,
        }

        out_params = self._proxy_call_action("SetWarnDisconnectDelay", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

