"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class AVTransport3ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'AVTransport3' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:AVTransport:3'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:AVTransport'


    def get_AVTransportURI(self):
        """
            Gets the "AVTransportURI" variable.
        """
        rval = self.proxy_get_variable_value("AVTransportURI")
        return rval


    def set_AVTransportURI(self, val):
        """
            Sets the "AVTransportURI" variable.
        """
        self.proxy_set_variable_value("AVTransportURI", val)
        return


    def get_AVTransportURIMetaData(self):
        """
            Gets the "AVTransportURIMetaData" variable.
        """
        rval = self.proxy_get_variable_value("AVTransportURIMetaData")
        return rval


    def set_AVTransportURIMetaData(self, val):
        """
            Sets the "AVTransportURIMetaData" variable.
        """
        self.proxy_set_variable_value("AVTransportURIMetaData", val)
        return


    def get_AbsoluteCounterPosition(self):
        """
            Gets the "AbsoluteCounterPosition" variable.
        """
        rval = self.proxy_get_variable_value("AbsoluteCounterPosition")
        return rval


    def set_AbsoluteCounterPosition(self, val):
        """
            Sets the "AbsoluteCounterPosition" variable.
        """
        self.proxy_set_variable_value("AbsoluteCounterPosition", val)
        return


    def get_AbsoluteTimePosition(self):
        """
            Gets the "AbsoluteTimePosition" variable.
        """
        rval = self.proxy_get_variable_value("AbsoluteTimePosition")
        return rval


    def set_AbsoluteTimePosition(self, val):
        """
            Sets the "AbsoluteTimePosition" variable.
        """
        self.proxy_set_variable_value("AbsoluteTimePosition", val)
        return


    def get_CurrentMediaCategory(self):
        """
            Gets the "CurrentMediaCategory" variable.
        """
        rval = self.proxy_get_variable_value("CurrentMediaCategory")
        return rval


    def set_CurrentMediaCategory(self, val):
        """
            Sets the "CurrentMediaCategory" variable.
        """
        self.proxy_set_variable_value("CurrentMediaCategory", val)
        return


    def get_CurrentMediaDuration(self):
        """
            Gets the "CurrentMediaDuration" variable.
        """
        rval = self.proxy_get_variable_value("CurrentMediaDuration")
        return rval


    def set_CurrentMediaDuration(self, val):
        """
            Sets the "CurrentMediaDuration" variable.
        """
        self.proxy_set_variable_value("CurrentMediaDuration", val)
        return


    def get_CurrentPlayMode(self):
        """
            Gets the "CurrentPlayMode" variable.
        """
        rval = self.proxy_get_variable_value("CurrentPlayMode")
        return rval


    def set_CurrentPlayMode(self, val):
        """
            Sets the "CurrentPlayMode" variable.
        """
        self.proxy_set_variable_value("CurrentPlayMode", val)
        return


    def get_CurrentRecordQualityMode(self):
        """
            Gets the "CurrentRecordQualityMode" variable.
        """
        rval = self.proxy_get_variable_value("CurrentRecordQualityMode")
        return rval


    def set_CurrentRecordQualityMode(self, val):
        """
            Sets the "CurrentRecordQualityMode" variable.
        """
        self.proxy_set_variable_value("CurrentRecordQualityMode", val)
        return


    def get_CurrentTrack(self):
        """
            Gets the "CurrentTrack" variable.
        """
        rval = self.proxy_get_variable_value("CurrentTrack")
        return rval


    def set_CurrentTrack(self, val):
        """
            Sets the "CurrentTrack" variable.
        """
        self.proxy_set_variable_value("CurrentTrack", val)
        return


    def get_CurrentTrackDuration(self):
        """
            Gets the "CurrentTrackDuration" variable.
        """
        rval = self.proxy_get_variable_value("CurrentTrackDuration")
        return rval


    def set_CurrentTrackDuration(self, val):
        """
            Sets the "CurrentTrackDuration" variable.
        """
        self.proxy_set_variable_value("CurrentTrackDuration", val)
        return


    def get_CurrentTrackMetaData(self):
        """
            Gets the "CurrentTrackMetaData" variable.
        """
        rval = self.proxy_get_variable_value("CurrentTrackMetaData")
        return rval


    def set_CurrentTrackMetaData(self, val):
        """
            Sets the "CurrentTrackMetaData" variable.
        """
        self.proxy_set_variable_value("CurrentTrackMetaData", val)
        return


    def get_CurrentTrackURI(self):
        """
            Gets the "CurrentTrackURI" variable.
        """
        rval = self.proxy_get_variable_value("CurrentTrackURI")
        return rval


    def set_CurrentTrackURI(self, val):
        """
            Sets the "CurrentTrackURI" variable.
        """
        self.proxy_set_variable_value("CurrentTrackURI", val)
        return


    def get_CurrentTransportActions(self):
        """
            Gets the "CurrentTransportActions" variable.
        """
        rval = self.proxy_get_variable_value("CurrentTransportActions")
        return rval


    def set_CurrentTransportActions(self, val):
        """
            Sets the "CurrentTransportActions" variable.
        """
        self.proxy_set_variable_value("CurrentTransportActions", val)
        return


    def get_DRMState(self):
        """
            Gets the "DRMState" variable.
        """
        rval = self.proxy_get_variable_value("DRMState")
        return rval


    def set_DRMState(self, val):
        """
            Sets the "DRMState" variable.
        """
        self.proxy_set_variable_value("DRMState", val)
        return


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


    def get_NextAVTransportURI(self):
        """
            Gets the "NextAVTransportURI" variable.
        """
        rval = self.proxy_get_variable_value("NextAVTransportURI")
        return rval


    def set_NextAVTransportURI(self, val):
        """
            Sets the "NextAVTransportURI" variable.
        """
        self.proxy_set_variable_value("NextAVTransportURI", val)
        return


    def get_NextAVTransportURIMetaData(self):
        """
            Gets the "NextAVTransportURIMetaData" variable.
        """
        rval = self.proxy_get_variable_value("NextAVTransportURIMetaData")
        return rval


    def set_NextAVTransportURIMetaData(self, val):
        """
            Sets the "NextAVTransportURIMetaData" variable.
        """
        self.proxy_set_variable_value("NextAVTransportURIMetaData", val)
        return


    def get_NumberOfTracks(self):
        """
            Gets the "NumberOfTracks" variable.
        """
        rval = self.proxy_get_variable_value("NumberOfTracks")
        return rval


    def set_NumberOfTracks(self, val):
        """
            Sets the "NumberOfTracks" variable.
        """
        self.proxy_set_variable_value("NumberOfTracks", val)
        return


    def get_PlaybackStorageMedium(self):
        """
            Gets the "PlaybackStorageMedium" variable.
        """
        rval = self.proxy_get_variable_value("PlaybackStorageMedium")
        return rval


    def set_PlaybackStorageMedium(self, val):
        """
            Sets the "PlaybackStorageMedium" variable.
        """
        self.proxy_set_variable_value("PlaybackStorageMedium", val)
        return


    def get_PossiblePlaybackStorageMedia(self):
        """
            Gets the "PossiblePlaybackStorageMedia" variable.
        """
        rval = self.proxy_get_variable_value("PossiblePlaybackStorageMedia")
        return rval


    def set_PossiblePlaybackStorageMedia(self, val):
        """
            Sets the "PossiblePlaybackStorageMedia" variable.
        """
        self.proxy_set_variable_value("PossiblePlaybackStorageMedia", val)
        return


    def get_PossibleRecordQualityModes(self):
        """
            Gets the "PossibleRecordQualityModes" variable.
        """
        rval = self.proxy_get_variable_value("PossibleRecordQualityModes")
        return rval


    def set_PossibleRecordQualityModes(self, val):
        """
            Sets the "PossibleRecordQualityModes" variable.
        """
        self.proxy_set_variable_value("PossibleRecordQualityModes", val)
        return


    def get_PossibleRecordStorageMedia(self):
        """
            Gets the "PossibleRecordStorageMedia" variable.
        """
        rval = self.proxy_get_variable_value("PossibleRecordStorageMedia")
        return rval


    def set_PossibleRecordStorageMedia(self, val):
        """
            Sets the "PossibleRecordStorageMedia" variable.
        """
        self.proxy_set_variable_value("PossibleRecordStorageMedia", val)
        return


    def get_RecordMediumWriteStatus(self):
        """
            Gets the "RecordMediumWriteStatus" variable.
        """
        rval = self.proxy_get_variable_value("RecordMediumWriteStatus")
        return rval


    def set_RecordMediumWriteStatus(self, val):
        """
            Sets the "RecordMediumWriteStatus" variable.
        """
        self.proxy_set_variable_value("RecordMediumWriteStatus", val)
        return


    def get_RecordStorageMedium(self):
        """
            Gets the "RecordStorageMedium" variable.
        """
        rval = self.proxy_get_variable_value("RecordStorageMedium")
        return rval


    def set_RecordStorageMedium(self, val):
        """
            Sets the "RecordStorageMedium" variable.
        """
        self.proxy_set_variable_value("RecordStorageMedium", val)
        return


    def get_RelativeCounterPosition(self):
        """
            Gets the "RelativeCounterPosition" variable.
        """
        rval = self.proxy_get_variable_value("RelativeCounterPosition")
        return rval


    def set_RelativeCounterPosition(self, val):
        """
            Sets the "RelativeCounterPosition" variable.
        """
        self.proxy_set_variable_value("RelativeCounterPosition", val)
        return


    def get_RelativeTimePosition(self):
        """
            Gets the "RelativeTimePosition" variable.
        """
        rval = self.proxy_get_variable_value("RelativeTimePosition")
        return rval


    def set_RelativeTimePosition(self, val):
        """
            Sets the "RelativeTimePosition" variable.
        """
        self.proxy_set_variable_value("RelativeTimePosition", val)
        return


    def get_SyncOffset(self):
        """
            Gets the "SyncOffset" variable.
        """
        rval = self.proxy_get_variable_value("SyncOffset")
        return rval


    def set_SyncOffset(self, val):
        """
            Sets the "SyncOffset" variable.
        """
        self.proxy_set_variable_value("SyncOffset", val)
        return


    def get_TransportPlaySpeed(self):
        """
            Gets the "TransportPlaySpeed" variable.
        """
        rval = self.proxy_get_variable_value("TransportPlaySpeed")
        return rval


    def set_TransportPlaySpeed(self, val):
        """
            Sets the "TransportPlaySpeed" variable.
        """
        self.proxy_set_variable_value("TransportPlaySpeed", val)
        return


    def get_TransportState(self):
        """
            Gets the "TransportState" variable.
        """
        rval = self.proxy_get_variable_value("TransportState")
        return rval


    def set_TransportState(self, val):
        """
            Sets the "TransportState" variable.
        """
        self.proxy_set_variable_value("TransportState", val)
        return


    def get_TransportStatus(self):
        """
            Gets the "TransportStatus" variable.
        """
        rval = self.proxy_get_variable_value("TransportStatus")
        return rval


    def set_TransportStatus(self, val):
        """
            Sets the "TransportStatus" variable.
        """
        self.proxy_set_variable_value("TransportStatus", val)
        return


    def action_AdjustSyncOffset(self, InstanceID, Adjustment):
        """
            Calls the AdjustSyncOffset action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "Adjustment": Adjustment,
        }

        out_params = self.proxy_call_action("AdjustSyncOffset", arguments=arguments)

        (result,) = out_params

        return result


    def action_GetCurrentTransportActions(self, InstanceID):
        """
            Calls the GetCurrentTransportActions action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetCurrentTransportActions", arguments=arguments)

        (Actions,) = out_params

        return Actions


    def action_GetDRMState(self, InstanceID):
        """
            Calls the GetDRMState action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetDRMState", arguments=arguments)

        (CurrentDRMState,) = out_params

        return CurrentDRMState


    def action_GetDeviceCapabilities(self, InstanceID):
        """
            Calls the GetDeviceCapabilities action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetDeviceCapabilities", arguments=arguments)

        (PlayMedia, RecMedia, RecQualityModes,) = out_params

        return PlayMedia, RecMedia, RecQualityModes


    def action_GetMediaInfo(self, InstanceID):
        """
            Calls the GetMediaInfo action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetMediaInfo", arguments=arguments)

        (NrTracks, MediaDuration, CurrentURI, CurrentURIMetaData, NextURI, NextURIMetaData, PlayMedium, RecordMedium, WriteStatus,) = out_params

        return NrTracks, MediaDuration, CurrentURI, CurrentURIMetaData, NextURI, NextURIMetaData, PlayMedium, RecordMedium, WriteStatus


    def action_GetMediaInfo_Ext(self, InstanceID):
        """
            Calls the GetMediaInfo_Ext action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetMediaInfo_Ext", arguments=arguments)

        (CurrentType, NrTracks, MediaDuration, CurrentURI, CurrentURIMetaData, NextURI, NextURIMetaData, PlayMedium, RecordMedium, WriteStatus,) = out_params

        return CurrentType, NrTracks, MediaDuration, CurrentURI, CurrentURIMetaData, NextURI, NextURIMetaData, PlayMedium, RecordMedium, WriteStatus


    def action_GetPlaylistInfo(self, InstanceID, PlaylistType):
        """
            Calls the GetPlaylistInfo action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "PlaylistType": PlaylistType,
        }

        out_params = self.proxy_call_action("GetPlaylistInfo", arguments=arguments)

        (PlaylistInfo,) = out_params

        return PlaylistInfo


    def action_GetPositionInfo(self, InstanceID):
        """
            Calls the GetPositionInfo action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetPositionInfo", arguments=arguments)

        (Track, TrackDuration, TrackMetaData, TrackURI, RelTime, AbsTime, RelCount, AbsCount,) = out_params

        return Track, TrackDuration, TrackMetaData, TrackURI, RelTime, AbsTime, RelCount, AbsCount


    def action_GetStateVariables(self, InstanceID, StateVariableList):
        """
            Calls the GetStateVariables action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "StateVariableList": StateVariableList,
        }

        out_params = self.proxy_call_action("GetStateVariables", arguments=arguments)

        (StateVariableValuePairs,) = out_params

        return StateVariableValuePairs


    def action_GetSyncOffset(self, InstanceID):
        """
            Calls the GetSyncOffset action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetSyncOffset", arguments=arguments)

        (CurrentSyncOffset,) = out_params

        return CurrentSyncOffset


    def action_GetTransportInfo(self, InstanceID):
        """
            Calls the GetTransportInfo action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetTransportInfo", arguments=arguments)

        (CurrentTransportState, CurrentTransportStatus, CurrentSpeed,) = out_params

        return CurrentTransportState, CurrentTransportStatus, CurrentSpeed


    def action_GetTransportSettings(self, InstanceID):
        """
            Calls the GetTransportSettings action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetTransportSettings", arguments=arguments)

        (PlayMode, RecQualityMode,) = out_params

        return PlayMode, RecQualityMode


    def action_Next(self, InstanceID):
        """
            Calls the Next action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("Next", arguments=arguments)

        (result,) = out_params

        return result


    def action_Pause(self, InstanceID):
        """
            Calls the Pause action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("Pause", arguments=arguments)

        (result,) = out_params

        return result


    def action_Play(self, InstanceID, Speed):
        """
            Calls the Play action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "Speed": Speed,
        }

        out_params = self.proxy_call_action("Play", arguments=arguments)

        (result,) = out_params

        return result


    def action_Previous(self, InstanceID):
        """
            Calls the Previous action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("Previous", arguments=arguments)

        (result,) = out_params

        return result


    def action_Record(self, InstanceID):
        """
            Calls the Record action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("Record", arguments=arguments)

        (result,) = out_params

        return result


    def action_Seek(self, InstanceID, Unit, Target):
        """
            Calls the Seek action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "Unit": Unit,
            "Target": Target,
        }

        out_params = self.proxy_call_action("Seek", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetAVTransportURI(self, InstanceID, CurrentURI, CurrentURIMetaData):
        """
            Calls the SetAVTransportURI action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "CurrentURI": CurrentURI,
            "CurrentURIMetaData": CurrentURIMetaData,
        }

        out_params = self.proxy_call_action("SetAVTransportURI", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetNextAVTransportURI(self, InstanceID, NextURI, NextURIMetaData):
        """
            Calls the SetNextAVTransportURI action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "NextURI": NextURI,
            "NextURIMetaData": NextURIMetaData,
        }

        out_params = self.proxy_call_action("SetNextAVTransportURI", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetPlayMode(self, InstanceID, NewPlayMode):
        """
            Calls the SetPlayMode action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "NewPlayMode": NewPlayMode,
        }

        out_params = self.proxy_call_action("SetPlayMode", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetRecordQualityMode(self, InstanceID, NewRecordQualityMode):
        """
            Calls the SetRecordQualityMode action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "NewRecordQualityMode": NewRecordQualityMode,
        }

        out_params = self.proxy_call_action("SetRecordQualityMode", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetStateVariables(self, InstanceID, AVTransportUDN, ServiceType, ServiceId, StateVariableValuePairs):
        """
            Calls the SetStateVariables action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "AVTransportUDN": AVTransportUDN,
            "ServiceType": ServiceType,
            "ServiceId": ServiceId,
            "StateVariableValuePairs": StateVariableValuePairs,
        }

        out_params = self.proxy_call_action("SetStateVariables", arguments=arguments)

        (StateVariableList,) = out_params

        return StateVariableList


    def action_SetStaticPlaylist(self, InstanceID, PlaylistData, PlaylistDataLength, PlaylistOffset, PlaylistTotalLength, PlaylistMIMEType, PlaylistExtendedType, PlaylistStartObj, PlaylistStartGroup):
        """
            Calls the SetStaticPlaylist action.
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

        out_params = self.proxy_call_action("SetStaticPlaylist", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetStreamingPlaylist(self, InstanceID, PlaylistData, PlaylistDataLength, PlaylistMIMEType, PlaylistExtendedType, PlaylistStep):
        """
            Calls the SetStreamingPlaylist action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "PlaylistData": PlaylistData,
            "PlaylistDataLength": PlaylistDataLength,
            "PlaylistMIMEType": PlaylistMIMEType,
            "PlaylistExtendedType": PlaylistExtendedType,
            "PlaylistStep": PlaylistStep,
        }

        out_params = self.proxy_call_action("SetStreamingPlaylist", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetSyncOffset(self, InstanceID, NewSyncOffset):
        """
            Calls the SetSyncOffset action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "NewSyncOffset": NewSyncOffset,
        }

        out_params = self.proxy_call_action("SetSyncOffset", arguments=arguments)

        (result,) = out_params

        return result


    def action_Stop(self, InstanceID):
        """
            Calls the Stop action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("Stop", arguments=arguments)

        (result,) = out_params

        return result


    def action_SyncPause(self, InstanceID, PauseTime, ReferenceClockId):
        """
            Calls the SyncPause action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "PauseTime": PauseTime,
            "ReferenceClockId": ReferenceClockId,
        }

        out_params = self.proxy_call_action("SyncPause", arguments=arguments)

        (result,) = out_params

        return result


    def action_SyncPlay(self, InstanceID, Speed, ReferencePositionUnits, ReferencePosition, ReferencePresentationTime, ReferenceClockId):
        """
            Calls the SyncPlay action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "Speed": Speed,
            "ReferencePositionUnits": ReferencePositionUnits,
            "ReferencePosition": ReferencePosition,
            "ReferencePresentationTime": ReferencePresentationTime,
            "ReferenceClockId": ReferenceClockId,
        }

        out_params = self.proxy_call_action("SyncPlay", arguments=arguments)

        (result,) = out_params

        return result


    def action_SyncStop(self, InstanceID, StopTime, ReferenceClockId):
        """
            Calls the SyncStop action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "StopTime": StopTime,
            "ReferenceClockId": ReferenceClockId,
        }

        out_params = self.proxy_call_action("SyncStop", arguments=arguments)

        (result,) = out_params

        return result
