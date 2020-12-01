"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class RemoteUIClient1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'RemoteUIClient1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:RemoteUIClient:1'

    SERVICE_EVENT_VARIABLES = {}

    def action_AddUIListing(self, InputUIList, extract_returns=True):
        """
            Calls the AddUIListing action.

            :returns: "TimeToLive"
        """
        arguments = {
            "InputUIList": InputUIList,
        }

        out_params = self._proxy_call_action("AddUIListing", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("TimeToLive",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_Connect(self, RequestedConnections, extract_returns=True):
        """
            Calls the Connect action.

            :returns: "CurrentConnectionsList"
        """
        arguments = {
            "RequestedConnections": RequestedConnections,
        }

        out_params = self._proxy_call_action("Connect", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentConnectionsList",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_Disconnect(self, RequestedDisconnects, extract_returns=True):
        """
            Calls the Disconnect action.

            :returns: "CurrentConnectionsList"
        """
        arguments = {
            "RequestedDisconnects": RequestedDisconnects,
        }

        out_params = self._proxy_call_action("Disconnect", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentConnectionsList",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_DisplayMessage(self, MessageType, Message, extract_returns=True):
        """
            Calls the DisplayMessage action.

            :returns: "result"
        """
        arguments = {
            "MessageType": MessageType,
            "Message": Message,
        }

        out_params = self._proxy_call_action("DisplayMessage", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetCurrentConnections(self, extract_returns=True):
        """
            Calls the GetCurrentConnections action.

            :returns: "CurrentConnectionsList"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetCurrentConnections", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentConnectionsList",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetDeviceProfile(self, extract_returns=True):
        """
            Calls the GetDeviceProfile action.

            :returns: "StaticDeviceInfo"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetDeviceProfile", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("StaticDeviceInfo",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetUIListing(self, extract_returns=True):
        """
            Calls the GetUIListing action.

            :returns: "CompatibleUIList"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetUIListing", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CompatibleUIList",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_ProcessInput(self, InputDataType, InputData, extract_returns=True):
        """
            Calls the ProcessInput action.

            :returns: "result"
        """
        arguments = {
            "InputDataType": InputDataType,
            "InputData": InputData,
        }

        out_params = self._proxy_call_action("ProcessInput", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_RemoveUIListing(self, RemoveUIList, extract_returns=True):
        """
            Calls the RemoveUIListing action.

            :returns: "result"
        """
        arguments = {
            "RemoveUIList": RemoveUIList,
        }

        out_params = self._proxy_call_action("RemoveUIListing", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args
