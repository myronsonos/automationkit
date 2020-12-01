"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class MusicServices1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'MusicServices1' service.
    """

    SERVICE_MANUFACTURER = 'SonosInc'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:MusicServices:1'

    SERVICE_EVENT_VARIABLES = {
        "ServiceListVersion": { "data_type": "string", "default": None, "allowed_list": None},
    }

    def action_GetSessionId(self, ServiceId, Username, extract_returns=True):
        """
            Calls the GetSessionId action.

            :returns: "SessionId"
        """
        arguments = {
            "ServiceId": ServiceId,
            "Username": Username,
        }

        out_params = self._proxy_call_action("GetSessionId", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("SessionId",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_ListAvailableServices(self, extract_returns=True):
        """
            Calls the ListAvailableServices action.

            :returns: "AvailableServiceDescriptorList", "AvailableServiceTypeList", "AvailableServiceListVersion"
        """
        arguments = { }

        out_params = self._proxy_call_action("ListAvailableServices", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("AvailableServiceDescriptorList", "AvailableServiceTypeList", "AvailableServiceListVersion",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_UpdateAvailableServices(self, extract_returns=True):
        """
            Calls the UpdateAvailableServices action.

            :returns: "result"
        """
        arguments = { }

        out_params = self._proxy_call_action("UpdateAvailableServices", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args
