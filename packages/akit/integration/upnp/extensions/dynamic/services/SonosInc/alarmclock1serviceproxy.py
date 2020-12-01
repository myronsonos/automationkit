"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class AlarmClock1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'AlarmClock1' service.
    """

    SERVICE_MANUFACTURER = 'SonosInc'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:AlarmClock:1'

    SERVICE_EVENT_VARIABLES = {
        "AlarmListVersion": { "data_type": "string", "default": None, "allowed_list": None},
        "DailyIndexRefreshTime": { "data_type": "string", "default": None, "allowed_list": None},
        "DateFormat": { "data_type": "string", "default": None, "allowed_list": None},
        "TimeFormat": { "data_type": "string", "default": None, "allowed_list": None},
        "TimeGeneration": { "data_type": "ui4", "default": None, "allowed_list": None},
        "TimeServer": { "data_type": "string", "default": None, "allowed_list": None},
        "TimeZone": { "data_type": "string", "default": None, "allowed_list": None},
    }

    def action_CreateAlarm(self, StartLocalTime, Duration, Recurrence, Enabled, RoomUUID, ProgramURI, ProgramMetaData, PlayMode, Volume, IncludeLinkedZones, extract_returns=True):
        """
            Calls the CreateAlarm action.

            :returns: "AssignedID"
        """
        arguments = {
            "StartLocalTime": StartLocalTime,
            "Duration": Duration,
            "Recurrence": Recurrence,
            "Enabled": Enabled,
            "RoomUUID": RoomUUID,
            "ProgramURI": ProgramURI,
            "ProgramMetaData": ProgramMetaData,
            "PlayMode": PlayMode,
            "Volume": Volume,
            "IncludeLinkedZones": IncludeLinkedZones,
        }

        out_params = self._proxy_call_action("CreateAlarm", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("AssignedID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_DestroyAlarm(self, ID, extract_returns=True):
        """
            Calls the DestroyAlarm action.

            :returns: "result"
        """
        arguments = {
            "ID": ID,
        }

        out_params = self._proxy_call_action("DestroyAlarm", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetDailyIndexRefreshTime(self, extract_returns=True):
        """
            Calls the GetDailyIndexRefreshTime action.

            :returns: "CurrentDailyIndexRefreshTime"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetDailyIndexRefreshTime", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentDailyIndexRefreshTime",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetFormat(self, extract_returns=True):
        """
            Calls the GetFormat action.

            :returns: "CurrentTimeFormat", "CurrentDateFormat"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetFormat", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentTimeFormat", "CurrentDateFormat",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetHouseholdTimeAtStamp(self, TimeStamp, extract_returns=True):
        """
            Calls the GetHouseholdTimeAtStamp action.

            :returns: "HouseholdUTCTime"
        """
        arguments = {
            "TimeStamp": TimeStamp,
        }

        out_params = self._proxy_call_action("GetHouseholdTimeAtStamp", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("HouseholdUTCTime",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetTimeNow(self, extract_returns=True):
        """
            Calls the GetTimeNow action.

            :returns: "CurrentUTCTime", "CurrentLocalTime", "CurrentTimeZone", "CurrentTimeGeneration"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetTimeNow", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentUTCTime", "CurrentLocalTime", "CurrentTimeZone", "CurrentTimeGeneration",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetTimeServer(self, extract_returns=True):
        """
            Calls the GetTimeServer action.

            :returns: "CurrentTimeServer"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetTimeServer", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentTimeServer",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetTimeZone(self, extract_returns=True):
        """
            Calls the GetTimeZone action.

            :returns: "Index", "AutoAdjustDst"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetTimeZone", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("Index", "AutoAdjustDst",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetTimeZoneAndRule(self, extract_returns=True):
        """
            Calls the GetTimeZoneAndRule action.

            :returns: "Index", "AutoAdjustDst", "CurrentTimeZone"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetTimeZoneAndRule", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("Index", "AutoAdjustDst", "CurrentTimeZone",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetTimeZoneRule(self, Index, extract_returns=True):
        """
            Calls the GetTimeZoneRule action.

            :returns: "TimeZone"
        """
        arguments = {
            "Index": Index,
        }

        out_params = self._proxy_call_action("GetTimeZoneRule", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("TimeZone",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_ListAlarms(self, extract_returns=True):
        """
            Calls the ListAlarms action.

            :returns: "CurrentAlarmList", "CurrentAlarmListVersion"
        """
        arguments = { }

        out_params = self._proxy_call_action("ListAlarms", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentAlarmList", "CurrentAlarmListVersion",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetDailyIndexRefreshTime(self, DesiredDailyIndexRefreshTime, extract_returns=True):
        """
            Calls the SetDailyIndexRefreshTime action.

            :returns: "result"
        """
        arguments = {
            "DesiredDailyIndexRefreshTime": DesiredDailyIndexRefreshTime,
        }

        out_params = self._proxy_call_action("SetDailyIndexRefreshTime", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetFormat(self, DesiredTimeFormat, DesiredDateFormat, extract_returns=True):
        """
            Calls the SetFormat action.

            :returns: "result"
        """
        arguments = {
            "DesiredTimeFormat": DesiredTimeFormat,
            "DesiredDateFormat": DesiredDateFormat,
        }

        out_params = self._proxy_call_action("SetFormat", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetTimeNow(self, DesiredTime, TimeZoneForDesiredTime, extract_returns=True):
        """
            Calls the SetTimeNow action.

            :returns: "result"
        """
        arguments = {
            "DesiredTime": DesiredTime,
            "TimeZoneForDesiredTime": TimeZoneForDesiredTime,
        }

        out_params = self._proxy_call_action("SetTimeNow", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetTimeServer(self, DesiredTimeServer, extract_returns=True):
        """
            Calls the SetTimeServer action.

            :returns: "result"
        """
        arguments = {
            "DesiredTimeServer": DesiredTimeServer,
        }

        out_params = self._proxy_call_action("SetTimeServer", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetTimeZone(self, Index, AutoAdjustDst, extract_returns=True):
        """
            Calls the SetTimeZone action.

            :returns: "result"
        """
        arguments = {
            "Index": Index,
            "AutoAdjustDst": AutoAdjustDst,
        }

        out_params = self._proxy_call_action("SetTimeZone", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_UpdateAlarm(self, ID, StartLocalTime, Duration, Recurrence, Enabled, RoomUUID, ProgramURI, ProgramMetaData, PlayMode, Volume, IncludeLinkedZones, extract_returns=True):
        """
            Calls the UpdateAlarm action.

            :returns: "result"
        """
        arguments = {
            "ID": ID,
            "StartLocalTime": StartLocalTime,
            "Duration": Duration,
            "Recurrence": Recurrence,
            "Enabled": Enabled,
            "RoomUUID": RoomUUID,
            "ProgramURI": ProgramURI,
            "ProgramMetaData": ProgramMetaData,
            "PlayMode": PlayMode,
            "Volume": Volume,
            "IncludeLinkedZones": IncludeLinkedZones,
        }

        out_params = self._proxy_call_action("UpdateAlarm", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args
