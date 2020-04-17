"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class ScheduledRecording1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'ScheduledRecording1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:ScheduledRecording:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:ScheduledRecording'


    def get_LastChange(self):
        """
            Gets the "LastChange" variable.
        """
        rval = self.proxy_get_variable_value("LastChange")
        return rval


    def set_LastChange(self, val):
        """
            Sets the "LastChange" variable.
        """
        self.proxy_set_variable_value("LastChange", val)
        return


    def get_SortCapabilities(self):
        """
            Gets the "SortCapabilities" variable.
        """
        rval = self.proxy_get_variable_value("SortCapabilities")
        return rval


    def set_SortCapabilities(self, val):
        """
            Sets the "SortCapabilities" variable.
        """
        self.proxy_set_variable_value("SortCapabilities", val)
        return


    def get_SortLevelCapability(self):
        """
            Gets the "SortLevelCapability" variable.
        """
        rval = self.proxy_get_variable_value("SortLevelCapability")
        return rval


    def set_SortLevelCapability(self, val):
        """
            Sets the "SortLevelCapability" variable.
        """
        self.proxy_set_variable_value("SortLevelCapability", val)
        return


    def get_StateUpdateID(self):
        """
            Gets the "StateUpdateID" variable.
        """
        rval = self.proxy_get_variable_value("StateUpdateID")
        return rval


    def set_StateUpdateID(self, val):
        """
            Sets the "StateUpdateID" variable.
        """
        self.proxy_set_variable_value("StateUpdateID", val)
        return


    def action_BrowseRecordSchedules(self, Filter, StartingIndex, RequestedCount, SortCriteria):
        """
            Calls the BrowseRecordSchedules action.
        """
        arguments = {
            "Filter": Filter,
            "StartingIndex": StartingIndex,
            "RequestedCount": RequestedCount,
            "SortCriteria": SortCriteria,
        }

        out_params = self.proxy_call_action("BrowseRecordSchedules", arguments=arguments)

        (Result, NumberReturned, TotalMatches, UpdateID,) = out_params

        return Result, NumberReturned, TotalMatches, UpdateID


    def action_BrowseRecordTasks(self, RecordScheduleID, Filter, StartingIndex, RequestedCount, SortCriteria):
        """
            Calls the BrowseRecordTasks action.
        """
        arguments = {
            "RecordScheduleID": RecordScheduleID,
            "Filter": Filter,
            "StartingIndex": StartingIndex,
            "RequestedCount": RequestedCount,
            "SortCriteria": SortCriteria,
        }

        out_params = self.proxy_call_action("BrowseRecordTasks", arguments=arguments)

        (Result, NumberReturned, TotalMatches, UpdateID,) = out_params

        return Result, NumberReturned, TotalMatches, UpdateID


    def action_CreateRecordSchedule(self, Elements):
        """
            Calls the CreateRecordSchedule action.
        """
        arguments = {
            "Elements": Elements,
        }

        out_params = self.proxy_call_action("CreateRecordSchedule", arguments=arguments)

        (RecordScheduleID, Result, UpdateID,) = out_params

        return RecordScheduleID, Result, UpdateID


    def action_DeleteRecordSchedule(self, RecordScheduleID):
        """
            Calls the DeleteRecordSchedule action.
        """
        arguments = {
            "RecordScheduleID": RecordScheduleID,
        }

        out_params = self.proxy_call_action("DeleteRecordSchedule", arguments=arguments)

        (result,) = out_params

        return result


    def action_DeleteRecordTask(self, RecordTaskID):
        """
            Calls the DeleteRecordTask action.
        """
        arguments = {
            "RecordTaskID": RecordTaskID,
        }

        out_params = self.proxy_call_action("DeleteRecordTask", arguments=arguments)

        (result,) = out_params

        return result


    def action_DisableRecordSchedule(self, RecordScheduleID):
        """
            Calls the DisableRecordSchedule action.
        """
        arguments = {
            "RecordScheduleID": RecordScheduleID,
        }

        out_params = self.proxy_call_action("DisableRecordSchedule", arguments=arguments)

        (result,) = out_params

        return result


    def action_DisableRecordTask(self, RecordTaskID):
        """
            Calls the DisableRecordTask action.
        """
        arguments = {
            "RecordTaskID": RecordTaskID,
        }

        out_params = self.proxy_call_action("DisableRecordTask", arguments=arguments)

        (result,) = out_params

        return result


    def action_EnableRecordSchedule(self, RecordScheduleID):
        """
            Calls the EnableRecordSchedule action.
        """
        arguments = {
            "RecordScheduleID": RecordScheduleID,
        }

        out_params = self.proxy_call_action("EnableRecordSchedule", arguments=arguments)

        (result,) = out_params

        return result


    def action_EnableRecordTask(self, RecordTaskID):
        """
            Calls the EnableRecordTask action.
        """
        arguments = {
            "RecordTaskID": RecordTaskID,
        }

        out_params = self.proxy_call_action("EnableRecordTask", arguments=arguments)

        (result,) = out_params

        return result


    def action_GetAllowedValues(self, DataTypeID, Filter):
        """
            Calls the GetAllowedValues action.
        """
        arguments = {
            "DataTypeID": DataTypeID,
            "Filter": Filter,
        }

        out_params = self.proxy_call_action("GetAllowedValues", arguments=arguments)

        (PropertyInfo,) = out_params

        return PropertyInfo


    def action_GetPropertyList(self, DataTypeID):
        """
            Calls the GetPropertyList action.
        """
        arguments = {
            "DataTypeID": DataTypeID,
        }

        out_params = self.proxy_call_action("GetPropertyList", arguments=arguments)

        (PropertyList,) = out_params

        return PropertyList


    def action_GetRecordSchedule(self, RecordScheduleID, Filter):
        """
            Calls the GetRecordSchedule action.
        """
        arguments = {
            "RecordScheduleID": RecordScheduleID,
            "Filter": Filter,
        }

        out_params = self.proxy_call_action("GetRecordSchedule", arguments=arguments)

        (Result, UpdateID,) = out_params

        return Result, UpdateID


    def action_GetRecordScheduleConflicts(self, RecordScheduleID):
        """
            Calls the GetRecordScheduleConflicts action.
        """
        arguments = {
            "RecordScheduleID": RecordScheduleID,
        }

        out_params = self.proxy_call_action("GetRecordScheduleConflicts", arguments=arguments)

        (RecordScheduleConflictIDList, UpdateID,) = out_params

        return RecordScheduleConflictIDList, UpdateID


    def action_GetRecordTask(self, RecordTaskID, Filter):
        """
            Calls the GetRecordTask action.
        """
        arguments = {
            "RecordTaskID": RecordTaskID,
            "Filter": Filter,
        }

        out_params = self.proxy_call_action("GetRecordTask", arguments=arguments)

        (Result, UpdateID,) = out_params

        return Result, UpdateID


    def action_GetRecordTaskConflicts(self, RecordTaskID):
        """
            Calls the GetRecordTaskConflicts action.
        """
        arguments = {
            "RecordTaskID": RecordTaskID,
        }

        out_params = self.proxy_call_action("GetRecordTaskConflicts", arguments=arguments)

        (RecordTaskConflictIDList, UpdateID,) = out_params

        return RecordTaskConflictIDList, UpdateID


    def action_GetSortCapabilities(self):
        """
            Calls the GetSortCapabilities action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetSortCapabilities", arguments=arguments)

        (SortCaps, SortLevelCap,) = out_params

        return SortCaps, SortLevelCap


    def action_GetStateUpdateID(self):
        """
            Calls the GetStateUpdateID action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetStateUpdateID", arguments=arguments)

        (Id,) = out_params

        return Id


    def action_ResetRecordTask(self, RecordTaskID):
        """
            Calls the ResetRecordTask action.
        """
        arguments = {
            "RecordTaskID": RecordTaskID,
        }

        out_params = self.proxy_call_action("ResetRecordTask", arguments=arguments)

        (result,) = out_params

        return result

