"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class ScheduledRecording1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'ScheduledRecording1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:ScheduledRecording:1'

    SERVICE_EVENT_VARIABLES = {
        "LastChange": { "data_type": "string", "default": None, "allowed_list": None},
    }

    def action_BrowseRecordSchedules(self, Filter, StartingIndex, RequestedCount, SortCriteria, extract_returns=True):
        """
            Calls the BrowseRecordSchedules action.

            :returns: "Result", "NumberReturned", "TotalMatches", "UpdateID"
        """
        arguments = {
            "Filter": Filter,
            "StartingIndex": StartingIndex,
            "RequestedCount": RequestedCount,
            "SortCriteria": SortCriteria,
        }

        out_params = self._proxy_call_action("BrowseRecordSchedules", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("Result", "NumberReturned", "TotalMatches", "UpdateID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_BrowseRecordTasks(self, RecordScheduleID, Filter, StartingIndex, RequestedCount, SortCriteria, extract_returns=True):
        """
            Calls the BrowseRecordTasks action.

            :returns: "Result", "NumberReturned", "TotalMatches", "UpdateID"
        """
        arguments = {
            "RecordScheduleID": RecordScheduleID,
            "Filter": Filter,
            "StartingIndex": StartingIndex,
            "RequestedCount": RequestedCount,
            "SortCriteria": SortCriteria,
        }

        out_params = self._proxy_call_action("BrowseRecordTasks", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("Result", "NumberReturned", "TotalMatches", "UpdateID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_CreateRecordSchedule(self, Elements, extract_returns=True):
        """
            Calls the CreateRecordSchedule action.

            :returns: "RecordScheduleID", "Result", "UpdateID"
        """
        arguments = {
            "Elements": Elements,
        }

        out_params = self._proxy_call_action("CreateRecordSchedule", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RecordScheduleID", "Result", "UpdateID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_DeleteRecordSchedule(self, RecordScheduleID, extract_returns=True):
        """
            Calls the DeleteRecordSchedule action.

            :returns: "result"
        """
        arguments = {
            "RecordScheduleID": RecordScheduleID,
        }

        out_params = self._proxy_call_action("DeleteRecordSchedule", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_DeleteRecordTask(self, RecordTaskID, extract_returns=True):
        """
            Calls the DeleteRecordTask action.

            :returns: "result"
        """
        arguments = {
            "RecordTaskID": RecordTaskID,
        }

        out_params = self._proxy_call_action("DeleteRecordTask", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_DisableRecordSchedule(self, RecordScheduleID, extract_returns=True):
        """
            Calls the DisableRecordSchedule action.

            :returns: "result"
        """
        arguments = {
            "RecordScheduleID": RecordScheduleID,
        }

        out_params = self._proxy_call_action("DisableRecordSchedule", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_DisableRecordTask(self, RecordTaskID, extract_returns=True):
        """
            Calls the DisableRecordTask action.

            :returns: "result"
        """
        arguments = {
            "RecordTaskID": RecordTaskID,
        }

        out_params = self._proxy_call_action("DisableRecordTask", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_EnableRecordSchedule(self, RecordScheduleID, extract_returns=True):
        """
            Calls the EnableRecordSchedule action.

            :returns: "result"
        """
        arguments = {
            "RecordScheduleID": RecordScheduleID,
        }

        out_params = self._proxy_call_action("EnableRecordSchedule", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_EnableRecordTask(self, RecordTaskID, extract_returns=True):
        """
            Calls the EnableRecordTask action.

            :returns: "result"
        """
        arguments = {
            "RecordTaskID": RecordTaskID,
        }

        out_params = self._proxy_call_action("EnableRecordTask", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetAllowedValues(self, DataTypeID, Filter, extract_returns=True):
        """
            Calls the GetAllowedValues action.

            :returns: "PropertyInfo"
        """
        arguments = {
            "DataTypeID": DataTypeID,
            "Filter": Filter,
        }

        out_params = self._proxy_call_action("GetAllowedValues", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("PropertyInfo",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetPropertyList(self, DataTypeID, extract_returns=True):
        """
            Calls the GetPropertyList action.

            :returns: "PropertyList"
        """
        arguments = {
            "DataTypeID": DataTypeID,
        }

        out_params = self._proxy_call_action("GetPropertyList", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("PropertyList",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetRecordSchedule(self, RecordScheduleID, Filter, extract_returns=True):
        """
            Calls the GetRecordSchedule action.

            :returns: "Result", "UpdateID"
        """
        arguments = {
            "RecordScheduleID": RecordScheduleID,
            "Filter": Filter,
        }

        out_params = self._proxy_call_action("GetRecordSchedule", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("Result", "UpdateID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetRecordScheduleConflicts(self, RecordScheduleID, extract_returns=True):
        """
            Calls the GetRecordScheduleConflicts action.

            :returns: "RecordScheduleConflictIDList", "UpdateID"
        """
        arguments = {
            "RecordScheduleID": RecordScheduleID,
        }

        out_params = self._proxy_call_action("GetRecordScheduleConflicts", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RecordScheduleConflictIDList", "UpdateID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetRecordTask(self, RecordTaskID, Filter, extract_returns=True):
        """
            Calls the GetRecordTask action.

            :returns: "Result", "UpdateID"
        """
        arguments = {
            "RecordTaskID": RecordTaskID,
            "Filter": Filter,
        }

        out_params = self._proxy_call_action("GetRecordTask", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("Result", "UpdateID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetRecordTaskConflicts(self, RecordTaskID, extract_returns=True):
        """
            Calls the GetRecordTaskConflicts action.

            :returns: "RecordTaskConflictIDList", "UpdateID"
        """
        arguments = {
            "RecordTaskID": RecordTaskID,
        }

        out_params = self._proxy_call_action("GetRecordTaskConflicts", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RecordTaskConflictIDList", "UpdateID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetSortCapabilities(self, extract_returns=True):
        """
            Calls the GetSortCapabilities action.

            :returns: "SortCaps", "SortLevelCap"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetSortCapabilities", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("SortCaps", "SortLevelCap",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetStateUpdateID(self, extract_returns=True):
        """
            Calls the GetStateUpdateID action.

            :returns: "Id"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetStateUpdateID", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("Id",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_ResetRecordTask(self, RecordTaskID, extract_returns=True):
        """
            Calls the ResetRecordTask action.

            :returns: "result"
        """
        arguments = {
            "RecordTaskID": RecordTaskID,
        }

        out_params = self._proxy_call_action("ResetRecordTask", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args
