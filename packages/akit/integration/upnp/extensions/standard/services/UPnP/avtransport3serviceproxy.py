"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class AVTransport3ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'AVTransport3' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:AVTransport:3'
    
    SERVICE_EVENT_VARIABLES = {
        "LastChange": { "data_type": "string", "default": None, "allowed_list": None},
    }


    def action_AdjustSyncOffset(self, InstanceID, Adjustment, extract_returns=True):
        """
            Calls the AdjustSyncOffset action.

            :returns: "result"
        """
        arguments = {
            "InstanceID": InstanceID,
            "Adjustment": Adjustment,
        }

        out_params = self._proxy_call_action("AdjustSyncOffset", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetCurrentTransportActions(self, InstanceID, extract_returns=True):
        """
            Calls the GetCurrentTransportActions action.

            :returns: "Actions"
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self._proxy_call_action("GetCurrentTransportActions", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("Actions",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetDRMState(self, InstanceID, extract_returns=True):
        """
            Calls the GetDRMState action.

            :returns: "CurrentDRMState"
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self._proxy_call_action("GetDRMState", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentDRMState",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetDeviceCapabilities(self, InstanceID, extract_returns=True):
        """
            Calls the GetDeviceCapabilities action.

            :returns: "PlayMedia", "RecMedia", "RecQualityModes"
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self._proxy_call_action("GetDeviceCapabilities", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("PlayMedia", "RecMedia", "RecQualityModes",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetMediaInfo(self, InstanceID, extract_returns=True):
        """
            Calls the GetMediaInfo action.

            :returns: "NrTracks", "MediaDuration", "CurrentURI", "CurrentURIMetaData", "NextURI", "NextURIMetaData", "PlayMedium", "RecordMedium", "WriteStatus"
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self._proxy_call_action("GetMediaInfo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NrTracks", "MediaDuration", "CurrentURI", "CurrentURIMetaData", "NextURI", "NextURIMetaData", "PlayMedium", "RecordMedium", "WriteStatus",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetMediaInfo_Ext(self, InstanceID, extract_returns=True):
        """
            Calls the GetMediaInfo_Ext action.

            :returns: "CurrentType", "NrTracks", "MediaDuration", "CurrentURI", "CurrentURIMetaData", "NextURI", "NextURIMetaData", "PlayMedium", "RecordMedium", "WriteStatus"
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self._proxy_call_action("GetMediaInfo_Ext", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentType", "NrTracks", "MediaDuration", "CurrentURI", "CurrentURIMetaData", "NextURI", "NextURIMetaData", "PlayMedium", "RecordMedium", "WriteStatus",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetPlaylistInfo(self, InstanceID, PlaylistType, extract_returns=True):
        """
            Calls the GetPlaylistInfo action.

            :returns: "PlaylistInfo"
        """
        arguments = {
            "InstanceID": InstanceID,
            "PlaylistType": PlaylistType,
        }

        out_params = self._proxy_call_action("GetPlaylistInfo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("PlaylistInfo",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetPositionInfo(self, InstanceID, extract_returns=True):
        """
            Calls the GetPositionInfo action.

            :returns: "Track", "TrackDuration", "TrackMetaData", "TrackURI", "RelTime", "AbsTime", "RelCount", "AbsCount"
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self._proxy_call_action("GetPositionInfo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("Track", "TrackDuration", "TrackMetaData", "TrackURI", "RelTime", "AbsTime", "RelCount", "AbsCount",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetStateVariables(self, InstanceID, StateVariableList, extract_returns=True):
        """
            Calls the GetStateVariables action.

            :returns: "StateVariableValuePairs"
        """
        arguments = {
            "InstanceID": InstanceID,
            "StateVariableList": StateVariableList,
        }

        out_params = self._proxy_call_action("GetStateVariables", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("StateVariableValuePairs",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetSyncOffset(self, InstanceID, extract_returns=True):
        """
            Calls the GetSyncOffset action.

            :returns: "CurrentSyncOffset"
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self._proxy_call_action("GetSyncOffset", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentSyncOffset",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetTransportInfo(self, InstanceID, extract_returns=True):
        """
            Calls the GetTransportInfo action.

            :returns: "CurrentTransportState", "CurrentTransportStatus", "CurrentSpeed"
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self._proxy_call_action("GetTransportInfo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentTransportState", "CurrentTransportStatus", "CurrentSpeed",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetTransportSettings(self, InstanceID, extract_returns=True):
        """
            Calls the GetTransportSettings action.

            :returns: "PlayMode", "RecQualityMode"
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self._proxy_call_action("GetTransportSettings", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("PlayMode", "RecQualityMode",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_Next(self, InstanceID, extract_returns=True):
        """
            Calls the Next action.

            :returns: "result"
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self._proxy_call_action("Next", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_Pause(self, InstanceID, extract_returns=True):
        """
            Calls the Pause action.

            :returns: "result"
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self._proxy_call_action("Pause", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_Play(self, InstanceID, Speed, extract_returns=True):
        """
            Calls the Play action.

            :returns: "result"
        """
        arguments = {
            "InstanceID": InstanceID,
            "Speed": Speed,
        }

        out_params = self._proxy_call_action("Play", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_Previous(self, InstanceID, extract_returns=True):
        """
            Calls the Previous action.

            :returns: "result"
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self._proxy_call_action("Previous", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_Record(self, InstanceID, extract_returns=True):
        """
            Calls the Record action.

            :returns: "result"
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self._proxy_call_action("Record", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_Seek(self, InstanceID, Unit, Target, extract_returns=True):
        """
            Calls the Seek action.

            :returns: "result"
        """
        arguments = {
            "InstanceID": InstanceID,
            "Unit": Unit,
            "Target": Target,
        }

        out_params = self._proxy_call_action("Seek", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetAVTransportURI(self, InstanceID, CurrentURI, CurrentURIMetaData, extract_returns=True):
        """
            Calls the SetAVTransportURI action.

            :returns: "result"
        """
        arguments = {
            "InstanceID": InstanceID,
            "CurrentURI": CurrentURI,
            "CurrentURIMetaData": CurrentURIMetaData,
        }

        out_params = self._proxy_call_action("SetAVTransportURI", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetNextAVTransportURI(self, InstanceID, NextURI, NextURIMetaData, extract_returns=True):
        """
            Calls the SetNextAVTransportURI action.

            :returns: "result"
        """
        arguments = {
            "InstanceID": InstanceID,
            "NextURI": NextURI,
            "NextURIMetaData": NextURIMetaData,
        }

        out_params = self._proxy_call_action("SetNextAVTransportURI", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetPlayMode(self, InstanceID, NewPlayMode, extract_returns=True):
        """
            Calls the SetPlayMode action.

            :returns: "result"
        """
        arguments = {
            "InstanceID": InstanceID,
            "NewPlayMode": NewPlayMode,
        }

        out_params = self._proxy_call_action("SetPlayMode", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetRecordQualityMode(self, InstanceID, NewRecordQualityMode, extract_returns=True):
        """
            Calls the SetRecordQualityMode action.

            :returns: "result"
        """
        arguments = {
            "InstanceID": InstanceID,
            "NewRecordQualityMode": NewRecordQualityMode,
        }

        out_params = self._proxy_call_action("SetRecordQualityMode", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetStateVariables(self, InstanceID, AVTransportUDN, ServiceType, ServiceId, StateVariableValuePairs, extract_returns=True):
        """
            Calls the SetStateVariables action.

            :returns: "StateVariableList"
        """
        arguments = {
            "InstanceID": InstanceID,
            "AVTransportUDN": AVTransportUDN,
            "ServiceType": ServiceType,
            "ServiceId": ServiceId,
            "StateVariableValuePairs": StateVariableValuePairs,
        }

        out_params = self._proxy_call_action("SetStateVariables", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("StateVariableList",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetStaticPlaylist(self, InstanceID, PlaylistData, PlaylistDataLength, PlaylistOffset, PlaylistTotalLength, PlaylistMIMEType, PlaylistExtendedType, PlaylistStartObj, PlaylistStartGroup, extract_returns=True):
        """
            Calls the SetStaticPlaylist action.

            :returns: "result"
        """
        arguments = {
            "InstanceID": InstanceID,
            "PlaylistData": PlaylistData,
            "PlaylistDataLength": PlaylistDataLength,
            "PlaylistOffset": PlaylistOffset,
            "PlaylistTotalLength": PlaylistTotalLength,
            "PlaylistMIMEType": PlaylistMIMEType,
            "PlaylistExtendedType": PlaylistExtendedType,
            "PlaylistStartObj": PlaylistStartObj,
            "PlaylistStartGroup": PlaylistStartGroup,
        }

        out_params = self._proxy_call_action("SetStaticPlaylist", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetStreamingPlaylist(self, InstanceID, PlaylistData, PlaylistDataLength, PlaylistMIMEType, PlaylistExtendedType, PlaylistStep, extract_returns=True):
        """
            Calls the SetStreamingPlaylist action.

            :returns: "result"
        """
        arguments = {
            "InstanceID": InstanceID,
            "PlaylistData": PlaylistData,
            "PlaylistDataLength": PlaylistDataLength,
            "PlaylistMIMEType": PlaylistMIMEType,
            "PlaylistExtendedType": PlaylistExtendedType,
            "PlaylistStep": PlaylistStep,
        }

        out_params = self._proxy_call_action("SetStreamingPlaylist", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetSyncOffset(self, InstanceID, NewSyncOffset, extract_returns=True):
        """
            Calls the SetSyncOffset action.

            :returns: "result"
        """
        arguments = {
            "InstanceID": InstanceID,
            "NewSyncOffset": NewSyncOffset,
        }

        out_params = self._proxy_call_action("SetSyncOffset", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_Stop(self, InstanceID, extract_returns=True):
        """
            Calls the Stop action.

            :returns: "result"
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self._proxy_call_action("Stop", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SyncPause(self, InstanceID, PauseTime, ReferenceClockId, extract_returns=True):
        """
            Calls the SyncPause action.

            :returns: "result"
        """
        arguments = {
            "InstanceID": InstanceID,
            "PauseTime": PauseTime,
            "ReferenceClockId": ReferenceClockId,
        }

        out_params = self._proxy_call_action("SyncPause", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SyncPlay(self, InstanceID, Speed, ReferencePositionUnits, ReferencePosition, ReferencePresentationTime, ReferenceClockId, extract_returns=True):
        """
            Calls the SyncPlay action.

            :returns: "result"
        """
        arguments = {
            "InstanceID": InstanceID,
            "Speed": Speed,
            "ReferencePositionUnits": ReferencePositionUnits,
            "ReferencePosition": ReferencePosition,
            "ReferencePresentationTime": ReferencePresentationTime,
            "ReferenceClockId": ReferenceClockId,
        }

        out_params = self._proxy_call_action("SyncPlay", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SyncStop(self, InstanceID, StopTime, ReferenceClockId, extract_returns=True):
        """
            Calls the SyncStop action.

            :returns: "result"
        """
        arguments = {
            "InstanceID": InstanceID,
            "StopTime": StopTime,
            "ReferenceClockId": ReferenceClockId,
        }

        out_params = self._proxy_call_action("SyncStop", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

