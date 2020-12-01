"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class Calendar1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'Calendar1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:Calendar:1'

    SERVICE_EVENT_VARIABLES = {
        "CalendarItem": { "data_type": "string", "default": None, "allowed_list": None},
        "MemoInfo": { "data_type": "string", "default": None, "allowed_list": None},
        "TriggeredItem": { "data_type": "string", "default": None, "allowed_list": None},
    }

    def action_AddCalendarItems(self, Caltems, extract_returns=True):
        """
            Calls the AddCalendarItems action.

            :returns: "ItemIDs"
        """
        arguments = {
            "Caltems": Caltems,
        }

        out_params = self._proxy_call_action("AddCalendarItems", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("ItemIDs",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_DeleteCalendarItems(self, ItemIDs, extract_returns=True):
        """
            Calls the DeleteCalendarItems action.

            :returns: "result"
        """
        arguments = {
            "ItemIDs": ItemIDs,
        }

        out_params = self._proxy_call_action("DeleteCalendarItems", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetCalendarItems(self, ItemIDs, extract_returns=True):
        """
            Calls the GetCalendarItems action.

            :returns: "Caltems"
        """
        arguments = {
            "ItemIDs": ItemIDs,
        }

        out_params = self._proxy_call_action("GetCalendarItems", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("Caltems",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetMemo(self, MemoID, extract_returns=True):
        """
            Calls the GetMemo action.

            :returns: "MemoInfoList"
        """
        arguments = {
            "MemoID": MemoID,
        }

        out_params = self._proxy_call_action("GetMemo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("MemoInfoList",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetTelCPNameList(self, extract_returns=True):
        """
            Calls the GetTelCPNameList action.

            :returns: "TelCPName"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetTelCPNameList", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("TelCPName",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetTriggeredItems(self, extract_returns=True):
        """
            Calls the GetTriggeredItems action.

            :returns: "TriggeredItemIDs"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetTriggeredItems", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("TriggeredItemIDs",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_PostMemo(self, Memo, extract_returns=True):
        """
            Calls the PostMemo action.

            :returns: "MemoID"
        """
        arguments = {
            "Memo": Memo,
        }

        out_params = self._proxy_call_action("PostMemo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("MemoID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_RegisterItemDelivery(self, ItemDeliveryMethod, Expires, extract_returns=True):
        """
            Calls the RegisterItemDelivery action.

            :returns: "result"
        """
        arguments = {
            "ItemDeliveryMethod": ItemDeliveryMethod,
            "Expires": Expires,
        }

        out_params = self._proxy_call_action("RegisterItemDelivery", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_RegisterTelCPName(self, TelCPName, extract_returns=True):
        """
            Calls the RegisterTelCPName action.

            :returns: "result"
        """
        arguments = {
            "TelCPName": TelCPName,
        }

        out_params = self._proxy_call_action("RegisterTelCPName", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_UnregisterTelCPName(self, TelCPName, extract_returns=True):
        """
            Calls the UnregisterTelCPName action.

            :returns: "result"
        """
        arguments = {
            "TelCPName": TelCPName,
        }

        out_params = self._proxy_call_action("UnregisterTelCPName", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_UpdateCalendarItems(self, Caltems, extract_returns=True):
        """
            Calls the UpdateCalendarItems action.

            :returns: "result"
        """
        arguments = {
            "Caltems": Caltems,
        }

        out_params = self._proxy_call_action("UpdateCalendarItems", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args
