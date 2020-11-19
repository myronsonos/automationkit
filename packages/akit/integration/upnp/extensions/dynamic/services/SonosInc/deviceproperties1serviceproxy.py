"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class DeviceProperties1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'DeviceProperties1' service.
    """

    SERVICE_MANUFACTURER = 'SonosInc'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:DeviceProperties:1'
    
    SERVICE_EVENT_VARIABLES = {
        "AirPlayEnabled": { "data_type": "boolean", "default": None, "allowed_list": None},
        "AvailableRoomCalibration": { "data_type": "string", "default": None, "allowed_list": None},
        "BehindWifiExtender": { "data_type": "ui4", "default": None, "allowed_list": None},
        "ChannelFreq": { "data_type": "ui4", "default": None, "allowed_list": None},
        "ChannelMapSet": { "data_type": "string", "default": None, "allowed_list": None},
        "ConfigMode": { "data_type": "string", "default": None, "allowed_list": None},
        "Configuration": { "data_type": "string", "default": None, "allowed_list": None},
        "HTBondedZoneCommitState": { "data_type": "ui4", "default": None, "allowed_list": None},
        "HTFreq": { "data_type": "ui4", "default": None, "allowed_list": None},
        "HTSatChanMapSet": { "data_type": "string", "default": None, "allowed_list": None},
        "HasConfiguredSSID": { "data_type": "boolean", "default": None, "allowed_list": None},
        "HdmiCecAvailable": { "data_type": "boolean", "default": None, "allowed_list": None},
        "Icon": { "data_type": "string", "default": None, "allowed_list": None},
        "Invisible": { "data_type": "boolean", "default": None, "allowed_list": None},
        "IsIdle": { "data_type": "boolean", "default": None, "allowed_list": None},
        "IsZoneBridge": { "data_type": "boolean", "default": None, "allowed_list": None},
        "LastChangedPlayState": { "data_type": "string", "default": None, "allowed_list": None},
        "MicEnabled": { "data_type": "ui4", "default": None, "allowed_list": None},
        "MoreInfo": { "data_type": "string", "default": None, "allowed_list": None},
        "Orientation": { "data_type": "i4", "default": None, "allowed_list": None},
        "RoomCalibrationState": { "data_type": "i4", "default": None, "allowed_list": None},
        "SecureRegState": { "data_type": "ui4", "default": None, "allowed_list": None},
        "SettingsReplicationState": { "data_type": "string", "default": None, "allowed_list": None},
        "SupportsAudioClip": { "data_type": "boolean", "default": None, "allowed_list": None},
        "SupportsAudioIn": { "data_type": "boolean", "default": None, "allowed_list": None},
        "TVConfigurationError": { "data_type": "boolean", "default": None, "allowed_list": None},
        "VoiceConfigState": { "data_type": "ui4", "default": None, "allowed_list": None},
        "WifiEnabled": { "data_type": "boolean", "default": None, "allowed_list": None},
        "WirelessLeafOnly": { "data_type": "boolean", "default": None, "allowed_list": None},
        "WirelessMode": { "data_type": "ui4", "default": None, "allowed_list": None},
        "ZoneName": { "data_type": "string", "default": None, "allowed_list": None},
    }


    def action_AddBondedZones(self, ChannelMapSet, extract_returns=True):
        """
            Calls the AddBondedZones action.

            :returns: "result"
        """
        arguments = {
            "ChannelMapSet": ChannelMapSet,
        }

        out_params = self._proxy_call_action("AddBondedZones", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_AddHTSatellite(self, HTSatChanMapSet, extract_returns=True):
        """
            Calls the AddHTSatellite action.

            :returns: "result"
        """
        arguments = {
            "HTSatChanMapSet": HTSatChanMapSet,
        }

        out_params = self._proxy_call_action("AddHTSatellite", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_CreateStereoPair(self, ChannelMapSet, extract_returns=True):
        """
            Calls the CreateStereoPair action.

            :returns: "result"
        """
        arguments = {
            "ChannelMapSet": ChannelMapSet,
        }

        out_params = self._proxy_call_action("CreateStereoPair", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_EnterConfigMode(self, Mode, Options, extract_returns=True):
        """
            Calls the EnterConfigMode action.

            :returns: "State"
        """
        arguments = {
            "Mode": Mode,
            "Options": Options,
        }

        out_params = self._proxy_call_action("EnterConfigMode", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("State",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_ExitConfigMode(self, Options, extract_returns=True):
        """
            Calls the ExitConfigMode action.

            :returns: "result"
        """
        arguments = {
            "Options": Options,
        }

        out_params = self._proxy_call_action("ExitConfigMode", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetAutoplayLinkedZones(self, Source, extract_returns=True):
        """
            Calls the GetAutoplayLinkedZones action.

            :returns: "IncludeLinkedZones"
        """
        arguments = {
            "Source": Source,
        }

        out_params = self._proxy_call_action("GetAutoplayLinkedZones", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("IncludeLinkedZones",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetAutoplayRoomUUID(self, Source, extract_returns=True):
        """
            Calls the GetAutoplayRoomUUID action.

            :returns: "RoomUUID"
        """
        arguments = {
            "Source": Source,
        }

        out_params = self._proxy_call_action("GetAutoplayRoomUUID", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RoomUUID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetAutoplayVolume(self, Source, extract_returns=True):
        """
            Calls the GetAutoplayVolume action.

            :returns: "CurrentVolume"
        """
        arguments = {
            "Source": Source,
        }

        out_params = self._proxy_call_action("GetAutoplayVolume", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentVolume",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetButtonLockState(self, extract_returns=True):
        """
            Calls the GetButtonLockState action.

            :returns: "CurrentButtonLockState"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetButtonLockState", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentButtonLockState",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetButtonState(self, extract_returns=True):
        """
            Calls the GetButtonState action.

            :returns: "State"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetButtonState", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("State",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetHouseholdID(self, extract_returns=True):
        """
            Calls the GetHouseholdID action.

            :returns: "CurrentHouseholdID"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetHouseholdID", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentHouseholdID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetLEDState(self, extract_returns=True):
        """
            Calls the GetLEDState action.

            :returns: "CurrentLEDState"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetLEDState", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentLEDState",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetUseAutoplayVolume(self, Source, extract_returns=True):
        """
            Calls the GetUseAutoplayVolume action.

            :returns: "UseVolume"
        """
        arguments = {
            "Source": Source,
        }

        out_params = self._proxy_call_action("GetUseAutoplayVolume", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("UseVolume",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetZoneAttributes(self, extract_returns=True):
        """
            Calls the GetZoneAttributes action.

            :returns: "CurrentZoneName", "CurrentIcon", "CurrentConfiguration", "CurrentTargetRoomName"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetZoneAttributes", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentZoneName", "CurrentIcon", "CurrentConfiguration", "CurrentTargetRoomName",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetZoneInfo(self, extract_returns=True):
        """
            Calls the GetZoneInfo action.

            :returns: "SerialNumber", "SoftwareVersion", "DisplaySoftwareVersion", "HardwareVersion", "IPAddress", "MACAddress", "CopyrightInfo", "ExtraInfo", "HTAudioIn", "Flags"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetZoneInfo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("SerialNumber", "SoftwareVersion", "DisplaySoftwareVersion", "HardwareVersion", "IPAddress", "MACAddress", "CopyrightInfo", "ExtraInfo", "HTAudioIn", "Flags",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_RemoveBondedZones(self, ChannelMapSet, KeepGrouped, extract_returns=True):
        """
            Calls the RemoveBondedZones action.

            :returns: "result"
        """
        arguments = {
            "ChannelMapSet": ChannelMapSet,
            "KeepGrouped": KeepGrouped,
        }

        out_params = self._proxy_call_action("RemoveBondedZones", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_RemoveHTSatellite(self, SatRoomUUID, extract_returns=True):
        """
            Calls the RemoveHTSatellite action.

            :returns: "result"
        """
        arguments = {
            "SatRoomUUID": SatRoomUUID,
        }

        out_params = self._proxy_call_action("RemoveHTSatellite", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SeparateStereoPair(self, ChannelMapSet, extract_returns=True):
        """
            Calls the SeparateStereoPair action.

            :returns: "result"
        """
        arguments = {
            "ChannelMapSet": ChannelMapSet,
        }

        out_params = self._proxy_call_action("SeparateStereoPair", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetAutoplayLinkedZones(self, IncludeLinkedZones, Source, extract_returns=True):
        """
            Calls the SetAutoplayLinkedZones action.

            :returns: "result"
        """
        arguments = {
            "IncludeLinkedZones": IncludeLinkedZones,
            "Source": Source,
        }

        out_params = self._proxy_call_action("SetAutoplayLinkedZones", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetAutoplayRoomUUID(self, RoomUUID, Source, extract_returns=True):
        """
            Calls the SetAutoplayRoomUUID action.

            :returns: "result"
        """
        arguments = {
            "RoomUUID": RoomUUID,
            "Source": Source,
        }

        out_params = self._proxy_call_action("SetAutoplayRoomUUID", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetAutoplayVolume(self, Volume, Source, extract_returns=True):
        """
            Calls the SetAutoplayVolume action.

            :returns: "result"
        """
        arguments = {
            "Volume": Volume,
            "Source": Source,
        }

        out_params = self._proxy_call_action("SetAutoplayVolume", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetButtonLockState(self, DesiredButtonLockState, extract_returns=True):
        """
            Calls the SetButtonLockState action.

            :returns: "result"
        """
        arguments = {
            "DesiredButtonLockState": DesiredButtonLockState,
        }

        out_params = self._proxy_call_action("SetButtonLockState", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetLEDState(self, DesiredLEDState, extract_returns=True):
        """
            Calls the SetLEDState action.

            :returns: "result"
        """
        arguments = {
            "DesiredLEDState": DesiredLEDState,
        }

        out_params = self._proxy_call_action("SetLEDState", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetUseAutoplayVolume(self, UseVolume, Source, extract_returns=True):
        """
            Calls the SetUseAutoplayVolume action.

            :returns: "result"
        """
        arguments = {
            "UseVolume": UseVolume,
            "Source": Source,
        }

        out_params = self._proxy_call_action("SetUseAutoplayVolume", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetZoneAttributes(self, DesiredZoneName, DesiredIcon, DesiredConfiguration, DesiredTargetRoomName, extract_returns=True):
        """
            Calls the SetZoneAttributes action.

            :returns: "result"
        """
        arguments = {
            "DesiredZoneName": DesiredZoneName,
            "DesiredIcon": DesiredIcon,
            "DesiredConfiguration": DesiredConfiguration,
            "DesiredTargetRoomName": DesiredTargetRoomName,
        }

        out_params = self._proxy_call_action("SetZoneAttributes", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

