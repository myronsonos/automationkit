"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class RenderingControl2ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'RenderingControl2' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:RenderingControl:2'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:RenderingControl'


    def get_BlueVideoBlackLevel(self):
        """
            Gets the "BlueVideoBlackLevel" variable.
        """
        rval = self.proxy_get_variable_value("BlueVideoBlackLevel")
        return rval


    def set_BlueVideoBlackLevel(self, val):
        """
            Sets the "BlueVideoBlackLevel" variable.
        """
        self.proxy_set_variable_value("BlueVideoBlackLevel", val)
        return


    def get_BlueVideoGain(self):
        """
            Gets the "BlueVideoGain" variable.
        """
        rval = self.proxy_get_variable_value("BlueVideoGain")
        return rval


    def set_BlueVideoGain(self, val):
        """
            Sets the "BlueVideoGain" variable.
        """
        self.proxy_set_variable_value("BlueVideoGain", val)
        return


    def get_Brightness(self):
        """
            Gets the "Brightness" variable.
        """
        rval = self.proxy_get_variable_value("Brightness")
        return rval


    def set_Brightness(self, val):
        """
            Sets the "Brightness" variable.
        """
        self.proxy_set_variable_value("Brightness", val)
        return


    def get_ColorTemperature(self):
        """
            Gets the "ColorTemperature" variable.
        """
        rval = self.proxy_get_variable_value("ColorTemperature")
        return rval


    def set_ColorTemperature(self, val):
        """
            Sets the "ColorTemperature" variable.
        """
        self.proxy_set_variable_value("ColorTemperature", val)
        return


    def get_Contrast(self):
        """
            Gets the "Contrast" variable.
        """
        rval = self.proxy_get_variable_value("Contrast")
        return rval


    def set_Contrast(self, val):
        """
            Sets the "Contrast" variable.
        """
        self.proxy_set_variable_value("Contrast", val)
        return


    def get_GreenVideoBlackLevel(self):
        """
            Gets the "GreenVideoBlackLevel" variable.
        """
        rval = self.proxy_get_variable_value("GreenVideoBlackLevel")
        return rval


    def set_GreenVideoBlackLevel(self, val):
        """
            Sets the "GreenVideoBlackLevel" variable.
        """
        self.proxy_set_variable_value("GreenVideoBlackLevel", val)
        return


    def get_GreenVideoGain(self):
        """
            Gets the "GreenVideoGain" variable.
        """
        rval = self.proxy_get_variable_value("GreenVideoGain")
        return rval


    def set_GreenVideoGain(self, val):
        """
            Sets the "GreenVideoGain" variable.
        """
        self.proxy_set_variable_value("GreenVideoGain", val)
        return


    def get_HorizontalKeystone(self):
        """
            Gets the "HorizontalKeystone" variable.
        """
        rval = self.proxy_get_variable_value("HorizontalKeystone")
        return rval


    def set_HorizontalKeystone(self, val):
        """
            Sets the "HorizontalKeystone" variable.
        """
        self.proxy_set_variable_value("HorizontalKeystone", val)
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


    def get_Loudness(self):
        """
            Gets the "Loudness" variable.
        """
        rval = self.proxy_get_variable_value("Loudness")
        return rval


    def set_Loudness(self, val):
        """
            Sets the "Loudness" variable.
        """
        self.proxy_set_variable_value("Loudness", val)
        return


    def get_Mute(self):
        """
            Gets the "Mute" variable.
        """
        rval = self.proxy_get_variable_value("Mute")
        return rval


    def set_Mute(self, val):
        """
            Sets the "Mute" variable.
        """
        self.proxy_set_variable_value("Mute", val)
        return


    def get_PresetNameList(self):
        """
            Gets the "PresetNameList" variable.
        """
        rval = self.proxy_get_variable_value("PresetNameList")
        return rval


    def set_PresetNameList(self, val):
        """
            Sets the "PresetNameList" variable.
        """
        self.proxy_set_variable_value("PresetNameList", val)
        return


    def get_RedVideoBlackLevel(self):
        """
            Gets the "RedVideoBlackLevel" variable.
        """
        rval = self.proxy_get_variable_value("RedVideoBlackLevel")
        return rval


    def set_RedVideoBlackLevel(self, val):
        """
            Sets the "RedVideoBlackLevel" variable.
        """
        self.proxy_set_variable_value("RedVideoBlackLevel", val)
        return


    def get_RedVideoGain(self):
        """
            Gets the "RedVideoGain" variable.
        """
        rval = self.proxy_get_variable_value("RedVideoGain")
        return rval


    def set_RedVideoGain(self, val):
        """
            Sets the "RedVideoGain" variable.
        """
        self.proxy_set_variable_value("RedVideoGain", val)
        return


    def get_Sharpness(self):
        """
            Gets the "Sharpness" variable.
        """
        rval = self.proxy_get_variable_value("Sharpness")
        return rval


    def set_Sharpness(self, val):
        """
            Sets the "Sharpness" variable.
        """
        self.proxy_set_variable_value("Sharpness", val)
        return


    def get_VerticalKeystone(self):
        """
            Gets the "VerticalKeystone" variable.
        """
        rval = self.proxy_get_variable_value("VerticalKeystone")
        return rval


    def set_VerticalKeystone(self, val):
        """
            Sets the "VerticalKeystone" variable.
        """
        self.proxy_set_variable_value("VerticalKeystone", val)
        return


    def get_Volume(self):
        """
            Gets the "Volume" variable.
        """
        rval = self.proxy_get_variable_value("Volume")
        return rval


    def set_Volume(self, val):
        """
            Sets the "Volume" variable.
        """
        self.proxy_set_variable_value("Volume", val)
        return


    def get_VolumeDB(self):
        """
            Gets the "VolumeDB" variable.
        """
        rval = self.proxy_get_variable_value("VolumeDB")
        return rval


    def set_VolumeDB(self, val):
        """
            Sets the "VolumeDB" variable.
        """
        self.proxy_set_variable_value("VolumeDB", val)
        return


    def action_GetBlueVideoBlackLevel(self, InstanceID):
        """
            Calls the GetBlueVideoBlackLevel action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetBlueVideoBlackLevel", arguments=arguments)

        (CurrentBlueVideoBlackLevel,) = out_params

        return CurrentBlueVideoBlackLevel


    def action_GetBlueVideoGain(self, InstanceID):
        """
            Calls the GetBlueVideoGain action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetBlueVideoGain", arguments=arguments)

        (CurrentBlueVideoGain,) = out_params

        return CurrentBlueVideoGain


    def action_GetBrightness(self, InstanceID):
        """
            Calls the GetBrightness action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetBrightness", arguments=arguments)

        (CurrentBrightness,) = out_params

        return CurrentBrightness


    def action_GetColorTemperature(self, InstanceID):
        """
            Calls the GetColorTemperature action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetColorTemperature", arguments=arguments)

        (CurrentColorTemperature,) = out_params

        return CurrentColorTemperature


    def action_GetContrast(self, InstanceID):
        """
            Calls the GetContrast action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetContrast", arguments=arguments)

        (CurrentContrast,) = out_params

        return CurrentContrast


    def action_GetGreenVideoBlackLevel(self, InstanceID):
        """
            Calls the GetGreenVideoBlackLevel action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetGreenVideoBlackLevel", arguments=arguments)

        (CurrentGreenVideoBlackLevel,) = out_params

        return CurrentGreenVideoBlackLevel


    def action_GetGreenVideoGain(self, InstanceID):
        """
            Calls the GetGreenVideoGain action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetGreenVideoGain", arguments=arguments)

        (CurrentGreenVideoGain,) = out_params

        return CurrentGreenVideoGain


    def action_GetHorizontalKeystone(self, InstanceID):
        """
            Calls the GetHorizontalKeystone action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetHorizontalKeystone", arguments=arguments)

        (CurrentHorizontalKeystone,) = out_params

        return CurrentHorizontalKeystone


    def action_GetLoudness(self, InstanceID, Channel):
        """
            Calls the GetLoudness action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "Channel": Channel,
        }

        out_params = self.proxy_call_action("GetLoudness", arguments=arguments)

        (CurrentLoudness,) = out_params

        return CurrentLoudness


    def action_GetMute(self, InstanceID, Channel):
        """
            Calls the GetMute action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "Channel": Channel,
        }

        out_params = self.proxy_call_action("GetMute", arguments=arguments)

        (CurrentMute,) = out_params

        return CurrentMute


    def action_GetRedVideoBlackLevel(self, InstanceID):
        """
            Calls the GetRedVideoBlackLevel action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetRedVideoBlackLevel", arguments=arguments)

        (CurrentRedVideoBlackLevel,) = out_params

        return CurrentRedVideoBlackLevel


    def action_GetRedVideoGain(self, InstanceID):
        """
            Calls the GetRedVideoGain action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetRedVideoGain", arguments=arguments)

        (CurrentRedVideoGain,) = out_params

        return CurrentRedVideoGain


    def action_GetSharpness(self, InstanceID):
        """
            Calls the GetSharpness action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetSharpness", arguments=arguments)

        (CurrentSharpness,) = out_params

        return CurrentSharpness


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


    def action_GetVerticalKeystone(self, InstanceID):
        """
            Calls the GetVerticalKeystone action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("GetVerticalKeystone", arguments=arguments)

        (CurrentVerticalKeystone,) = out_params

        return CurrentVerticalKeystone


    def action_GetVolume(self, InstanceID, Channel):
        """
            Calls the GetVolume action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "Channel": Channel,
        }

        out_params = self.proxy_call_action("GetVolume", arguments=arguments)

        (CurrentVolume,) = out_params

        return CurrentVolume


    def action_GetVolumeDB(self, InstanceID, Channel):
        """
            Calls the GetVolumeDB action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "Channel": Channel,
        }

        out_params = self.proxy_call_action("GetVolumeDB", arguments=arguments)

        (CurrentVolume,) = out_params

        return CurrentVolume


    def action_GetVolumeDBRange(self, InstanceID, Channel):
        """
            Calls the GetVolumeDBRange action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "Channel": Channel,
        }

        out_params = self.proxy_call_action("GetVolumeDBRange", arguments=arguments)

        (MinValue, MaxValue,) = out_params

        return MinValue, MaxValue


    def action_ListPresets(self, InstanceID):
        """
            Calls the ListPresets action.
        """
        arguments = {
            "InstanceID": InstanceID,
        }

        out_params = self.proxy_call_action("ListPresets", arguments=arguments)

        (CurrentPresetNameList,) = out_params

        return CurrentPresetNameList


    def action_SelectPreset(self, InstanceID, PresetName):
        """
            Calls the SelectPreset action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "PresetName": PresetName,
        }

        out_params = self.proxy_call_action("SelectPreset", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetBlueVideoBlackLevel(self, InstanceID, DesiredBlueVideoBlackLevel):
        """
            Calls the SetBlueVideoBlackLevel action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "DesiredBlueVideoBlackLevel": DesiredBlueVideoBlackLevel,
        }

        out_params = self.proxy_call_action("SetBlueVideoBlackLevel", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetBlueVideoGain(self, InstanceID, DesiredBlueVideoGain):
        """
            Calls the SetBlueVideoGain action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "DesiredBlueVideoGain": DesiredBlueVideoGain,
        }

        out_params = self.proxy_call_action("SetBlueVideoGain", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetBrightness(self, InstanceID, DesiredBrightness):
        """
            Calls the SetBrightness action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "DesiredBrightness": DesiredBrightness,
        }

        out_params = self.proxy_call_action("SetBrightness", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetColorTemperature(self, InstanceID, DesiredColorTemperature):
        """
            Calls the SetColorTemperature action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "DesiredColorTemperature": DesiredColorTemperature,
        }

        out_params = self.proxy_call_action("SetColorTemperature", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetContrast(self, InstanceID, DesiredContrast):
        """
            Calls the SetContrast action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "DesiredContrast": DesiredContrast,
        }

        out_params = self.proxy_call_action("SetContrast", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetGreenVideoBlackLevel(self, InstanceID, DesiredGreenVideoBlackLevel):
        """
            Calls the SetGreenVideoBlackLevel action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "DesiredGreenVideoBlackLevel": DesiredGreenVideoBlackLevel,
        }

        out_params = self.proxy_call_action("SetGreenVideoBlackLevel", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetGreenVideoGain(self, InstanceID, DesiredGreenVideoGain):
        """
            Calls the SetGreenVideoGain action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "DesiredGreenVideoGain": DesiredGreenVideoGain,
        }

        out_params = self.proxy_call_action("SetGreenVideoGain", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetHorizontalKeystone(self, InstanceID, DesiredHorizontalKeystone):
        """
            Calls the SetHorizontalKeystone action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "DesiredHorizontalKeystone": DesiredHorizontalKeystone,
        }

        out_params = self.proxy_call_action("SetHorizontalKeystone", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetLoudness(self, InstanceID, Channel, DesiredLoudness):
        """
            Calls the SetLoudness action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "Channel": Channel,
            "DesiredLoudness": DesiredLoudness,
        }

        out_params = self.proxy_call_action("SetLoudness", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetMute(self, InstanceID, Channel, DesiredMute):
        """
            Calls the SetMute action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "Channel": Channel,
            "DesiredMute": DesiredMute,
        }

        out_params = self.proxy_call_action("SetMute", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetRedVideoBlackLevel(self, InstanceID, DesiredRedVideoBlackLevel):
        """
            Calls the SetRedVideoBlackLevel action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "DesiredRedVideoBlackLevel": DesiredRedVideoBlackLevel,
        }

        out_params = self.proxy_call_action("SetRedVideoBlackLevel", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetRedVideoGain(self, InstanceID, DesiredRedVideoGain):
        """
            Calls the SetRedVideoGain action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "DesiredRedVideoGain": DesiredRedVideoGain,
        }

        out_params = self.proxy_call_action("SetRedVideoGain", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetSharpness(self, InstanceID, DesiredSharpness):
        """
            Calls the SetSharpness action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "DesiredSharpness": DesiredSharpness,
        }

        out_params = self.proxy_call_action("SetSharpness", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetStateVariables(self, InstanceID, RenderingControlUDN, ServiceType, ServiceId, StateVariableValuePairs):
        """
            Calls the SetStateVariables action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "RenderingControlUDN": RenderingControlUDN,
            "ServiceType": ServiceType,
            "ServiceId": ServiceId,
            "StateVariableValuePairs": StateVariableValuePairs,
        }

        out_params = self.proxy_call_action("SetStateVariables", arguments=arguments)

        (StateVariableList,) = out_params

        return StateVariableList


    def action_SetVerticalKeystone(self, InstanceID, DesiredVerticalKeystone):
        """
            Calls the SetVerticalKeystone action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "DesiredVerticalKeystone": DesiredVerticalKeystone,
        }

        out_params = self.proxy_call_action("SetVerticalKeystone", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetVolume(self, InstanceID, Channel, DesiredVolume):
        """
            Calls the SetVolume action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "Channel": Channel,
            "DesiredVolume": DesiredVolume,
        }

        out_params = self.proxy_call_action("SetVolume", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetVolumeDB(self, InstanceID, Channel, DesiredVolume):
        """
            Calls the SetVolumeDB action.
        """
        arguments = {
            "InstanceID": InstanceID,
            "Channel": Channel,
            "DesiredVolume": DesiredVolume,
        }

        out_params = self.proxy_call_action("SetVolumeDB", arguments=arguments)

        (result,) = out_params

        return result

