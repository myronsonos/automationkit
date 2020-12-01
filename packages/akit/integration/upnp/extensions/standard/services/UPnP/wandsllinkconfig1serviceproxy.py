"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class WANDSLLinkConfig1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'WANDSLLinkConfig1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:WANDSLLinkConfig:1'

    SERVICE_EVENT_VARIABLES = {}

    def action_GetATMEncapsulation(self, extract_returns=True):
        """
            Calls the GetATMEncapsulation action.

            :returns: "NewATMEncapsulation"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetATMEncapsulation", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewATMEncapsulation",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetAutoConfig(self, extract_returns=True):
        """
            Calls the GetAutoConfig action.

            :returns: "NewAutoConfig"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetAutoConfig", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewAutoConfig",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetDSLLinkInfo(self, extract_returns=True):
        """
            Calls the GetDSLLinkInfo action.

            :returns: "NewLinkType", "NewLinkStatus"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetDSLLinkInfo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewLinkType", "NewLinkStatus",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetDestinationAddress(self, extract_returns=True):
        """
            Calls the GetDestinationAddress action.

            :returns: "NewDestinationAddress"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetDestinationAddress", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewDestinationAddress",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetFCSPreserved(self, extract_returns=True):
        """
            Calls the GetFCSPreserved action.

            :returns: "NewFCSPreserved"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetFCSPreserved", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewFCSPreserved",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetModulationType(self, extract_returns=True):
        """
            Calls the GetModulationType action.

            :returns: "NewModulationType"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetModulationType", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewModulationType",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetATMEncapsulation(self, NewATMEncapsulation, extract_returns=True):
        """
            Calls the SetATMEncapsulation action.

            :returns: "result"
        """
        arguments = {
            "NewATMEncapsulation": NewATMEncapsulation,
        }

        out_params = self._proxy_call_action("SetATMEncapsulation", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetDSLLinkType(self, NewLinkType, extract_returns=True):
        """
            Calls the SetDSLLinkType action.

            :returns: "result"
        """
        arguments = {
            "NewLinkType": NewLinkType,
        }

        out_params = self._proxy_call_action("SetDSLLinkType", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetDestinationAddress(self, NewDestinationAddress, extract_returns=True):
        """
            Calls the SetDestinationAddress action.

            :returns: "result"
        """
        arguments = {
            "NewDestinationAddress": NewDestinationAddress,
        }

        out_params = self._proxy_call_action("SetDestinationAddress", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetFCSPreserved(self, NewFCSPreserved, extract_returns=True):
        """
            Calls the SetFCSPreserved action.

            :returns: "result"
        """
        arguments = {
            "NewFCSPreserved": NewFCSPreserved,
        }

        out_params = self._proxy_call_action("SetFCSPreserved", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args
