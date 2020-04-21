"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class WLANConfiguration1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'WLANConfiguration1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:WLANConfiguration:1'
    SERVICE_ID = 'urn:schemas-upnp-org:service:WLANConfiguration'


    def get_AssociatedDeviceAuthenticationState(self):
        """
            Gets the "AssociatedDeviceAuthenticationState" variable.
        """
        rval = self.proxy_get_variable_value("AssociatedDeviceAuthenticationState")
        return rval


    def set_AssociatedDeviceAuthenticationState(self, val):
        """
            Sets the "AssociatedDeviceAuthenticationState" variable.
        """
        self.proxy_set_variable_value("AssociatedDeviceAuthenticationState", val)
        return


    def get_AssociatedDeviceIPAddress(self):
        """
            Gets the "AssociatedDeviceIPAddress" variable.
        """
        rval = self.proxy_get_variable_value("AssociatedDeviceIPAddress")
        return rval


    def set_AssociatedDeviceIPAddress(self, val):
        """
            Sets the "AssociatedDeviceIPAddress" variable.
        """
        self.proxy_set_variable_value("AssociatedDeviceIPAddress", val)
        return


    def get_AssociatedDeviceMACAddress(self):
        """
            Gets the "AssociatedDeviceMACAddress" variable.
        """
        rval = self.proxy_get_variable_value("AssociatedDeviceMACAddress")
        return rval


    def set_AssociatedDeviceMACAddress(self, val):
        """
            Sets the "AssociatedDeviceMACAddress" variable.
        """
        self.proxy_set_variable_value("AssociatedDeviceMACAddress", val)
        return


    def get_AuthenticationServiceMode(self):
        """
            Gets the "AuthenticationServiceMode" variable.
        """
        rval = self.proxy_get_variable_value("AuthenticationServiceMode")
        return rval


    def set_AuthenticationServiceMode(self, val):
        """
            Sets the "AuthenticationServiceMode" variable.
        """
        self.proxy_set_variable_value("AuthenticationServiceMode", val)
        return


    def get_AutoRateFallBackEnabled(self):
        """
            Gets the "AutoRateFallBackEnabled" variable.
        """
        rval = self.proxy_get_variable_value("AutoRateFallBackEnabled")
        return rval


    def set_AutoRateFallBackEnabled(self, val):
        """
            Sets the "AutoRateFallBackEnabled" variable.
        """
        self.proxy_set_variable_value("AutoRateFallBackEnabled", val)
        return


    def get_BSSID(self):
        """
            Gets the "BSSID" variable.
        """
        rval = self.proxy_get_variable_value("BSSID")
        return rval


    def set_BSSID(self, val):
        """
            Sets the "BSSID" variable.
        """
        self.proxy_set_variable_value("BSSID", val)
        return


    def get_BasicAuthenticationMode(self):
        """
            Gets the "BasicAuthenticationMode" variable.
        """
        rval = self.proxy_get_variable_value("BasicAuthenticationMode")
        return rval


    def set_BasicAuthenticationMode(self, val):
        """
            Sets the "BasicAuthenticationMode" variable.
        """
        self.proxy_set_variable_value("BasicAuthenticationMode", val)
        return


    def get_BasicDataTransmissionRates(self):
        """
            Gets the "BasicDataTransmissionRates" variable.
        """
        rval = self.proxy_get_variable_value("BasicDataTransmissionRates")
        return rval


    def set_BasicDataTransmissionRates(self, val):
        """
            Sets the "BasicDataTransmissionRates" variable.
        """
        self.proxy_set_variable_value("BasicDataTransmissionRates", val)
        return


    def get_BasicEncryptionModes(self):
        """
            Gets the "BasicEncryptionModes" variable.
        """
        rval = self.proxy_get_variable_value("BasicEncryptionModes")
        return rval


    def set_BasicEncryptionModes(self, val):
        """
            Sets the "BasicEncryptionModes" variable.
        """
        self.proxy_set_variable_value("BasicEncryptionModes", val)
        return


    def get_BeaconAdvertisementEnabled(self):
        """
            Gets the "BeaconAdvertisementEnabled" variable.
        """
        rval = self.proxy_get_variable_value("BeaconAdvertisementEnabled")
        return rval


    def set_BeaconAdvertisementEnabled(self, val):
        """
            Sets the "BeaconAdvertisementEnabled" variable.
        """
        self.proxy_set_variable_value("BeaconAdvertisementEnabled", val)
        return


    def get_BeaconType(self):
        """
            Gets the "BeaconType" variable.
        """
        rval = self.proxy_get_variable_value("BeaconType")
        return rval


    def set_BeaconType(self, val):
        """
            Sets the "BeaconType" variable.
        """
        self.proxy_set_variable_value("BeaconType", val)
        return


    def get_Channel(self):
        """
            Gets the "Channel" variable.
        """
        rval = self.proxy_get_variable_value("Channel")
        return rval


    def set_Channel(self, val):
        """
            Sets the "Channel" variable.
        """
        self.proxy_set_variable_value("Channel", val)
        return


    def get_ChannelsInUse(self):
        """
            Gets the "ChannelsInUse" variable.
        """
        rval = self.proxy_get_variable_value("ChannelsInUse")
        return rval


    def set_ChannelsInUse(self, val):
        """
            Sets the "ChannelsInUse" variable.
        """
        self.proxy_set_variable_value("ChannelsInUse", val)
        return


    def get_DeviceOperationMode(self):
        """
            Gets the "DeviceOperationMode" variable.
        """
        rval = self.proxy_get_variable_value("DeviceOperationMode")
        return rval


    def set_DeviceOperationMode(self, val):
        """
            Sets the "DeviceOperationMode" variable.
        """
        self.proxy_set_variable_value("DeviceOperationMode", val)
        return


    def get_DistanceFromRoot(self):
        """
            Gets the "DistanceFromRoot" variable.
        """
        rval = self.proxy_get_variable_value("DistanceFromRoot")
        return rval


    def set_DistanceFromRoot(self, val):
        """
            Sets the "DistanceFromRoot" variable.
        """
        self.proxy_set_variable_value("DistanceFromRoot", val)
        return


    def get_IEEE11iAuthenticationMode(self):
        """
            Gets the "IEEE11iAuthenticationMode" variable.
        """
        rval = self.proxy_get_variable_value("IEEE11iAuthenticationMode")
        return rval


    def set_IEEE11iAuthenticationMode(self, val):
        """
            Sets the "IEEE11iAuthenticationMode" variable.
        """
        self.proxy_set_variable_value("IEEE11iAuthenticationMode", val)
        return


    def get_IEEE11iEncryptionModes(self):
        """
            Gets the "IEEE11iEncryptionModes" variable.
        """
        rval = self.proxy_get_variable_value("IEEE11iEncryptionModes")
        return rval


    def set_IEEE11iEncryptionModes(self, val):
        """
            Sets the "IEEE11iEncryptionModes" variable.
        """
        self.proxy_set_variable_value("IEEE11iEncryptionModes", val)
        return


    def get_InsecureOutOfBandAccessEnabled(self):
        """
            Gets the "InsecureOutOfBandAccessEnabled" variable.
        """
        rval = self.proxy_get_variable_value("InsecureOutOfBandAccessEnabled")
        return rval


    def set_InsecureOutOfBandAccessEnabled(self, val):
        """
            Sets the "InsecureOutOfBandAccessEnabled" variable.
        """
        self.proxy_set_variable_value("InsecureOutOfBandAccessEnabled", val)
        return


    def get_KeyPassphrase(self):
        """
            Gets the "KeyPassphrase" variable.
        """
        rval = self.proxy_get_variable_value("KeyPassphrase")
        return rval


    def set_KeyPassphrase(self, val):
        """
            Sets the "KeyPassphrase" variable.
        """
        self.proxy_set_variable_value("KeyPassphrase", val)
        return


    def get_LocationDescription(self):
        """
            Gets the "LocationDescription" variable.
        """
        rval = self.proxy_get_variable_value("LocationDescription")
        return rval


    def set_LocationDescription(self, val):
        """
            Sets the "LocationDescription" variable.
        """
        self.proxy_set_variable_value("LocationDescription", val)
        return


    def get_OperationalDataTransmissionRates(self):
        """
            Gets the "OperationalDataTransmissionRates" variable.
        """
        rval = self.proxy_get_variable_value("OperationalDataTransmissionRates")
        return rval


    def set_OperationalDataTransmissionRates(self, val):
        """
            Sets the "OperationalDataTransmissionRates" variable.
        """
        self.proxy_set_variable_value("OperationalDataTransmissionRates", val)
        return


    def get_PeerBSSID(self):
        """
            Gets the "PeerBSSID" variable.
        """
        rval = self.proxy_get_variable_value("PeerBSSID")
        return rval


    def set_PeerBSSID(self, val):
        """
            Sets the "PeerBSSID" variable.
        """
        self.proxy_set_variable_value("PeerBSSID", val)
        return


    def get_PossibleChannels(self):
        """
            Gets the "PossibleChannels" variable.
        """
        rval = self.proxy_get_variable_value("PossibleChannels")
        return rval


    def set_PossibleChannels(self, val):
        """
            Sets the "PossibleChannels" variable.
        """
        self.proxy_set_variable_value("PossibleChannels", val)
        return


    def get_PossibleDataTransmissionRates(self):
        """
            Gets the "PossibleDataTransmissionRates" variable.
        """
        rval = self.proxy_get_variable_value("PossibleDataTransmissionRates")
        return rval


    def set_PossibleDataTransmissionRates(self, val):
        """
            Sets the "PossibleDataTransmissionRates" variable.
        """
        self.proxy_set_variable_value("PossibleDataTransmissionRates", val)
        return


    def get_PreSharedKey(self):
        """
            Gets the "PreSharedKey" variable.
        """
        rval = self.proxy_get_variable_value("PreSharedKey")
        return rval


    def set_PreSharedKey(self, val):
        """
            Sets the "PreSharedKey" variable.
        """
        self.proxy_set_variable_value("PreSharedKey", val)
        return


    def get_PreSharedKeyIndex(self):
        """
            Gets the "PreSharedKeyIndex" variable.
        """
        rval = self.proxy_get_variable_value("PreSharedKeyIndex")
        return rval


    def set_PreSharedKeyIndex(self, val):
        """
            Sets the "PreSharedKeyIndex" variable.
        """
        self.proxy_set_variable_value("PreSharedKeyIndex", val)
        return


    def get_RadioEnabled(self):
        """
            Gets the "RadioEnabled" variable.
        """
        rval = self.proxy_get_variable_value("RadioEnabled")
        return rval


    def set_RadioEnabled(self, val):
        """
            Sets the "RadioEnabled" variable.
        """
        self.proxy_set_variable_value("RadioEnabled", val)
        return


    def get_RegulatoryDomain(self):
        """
            Gets the "RegulatoryDomain" variable.
        """
        rval = self.proxy_get_variable_value("RegulatoryDomain")
        return rval


    def set_RegulatoryDomain(self, val):
        """
            Sets the "RegulatoryDomain" variable.
        """
        self.proxy_set_variable_value("RegulatoryDomain", val)
        return


    def get_SSID(self):
        """
            Gets the "SSID" variable.
        """
        rval = self.proxy_get_variable_value("SSID")
        return rval


    def set_SSID(self, val):
        """
            Sets the "SSID" variable.
        """
        self.proxy_set_variable_value("SSID", val)
        return


    def get_TotalAssociations(self):
        """
            Gets the "TotalAssociations" variable.
        """
        rval = self.proxy_get_variable_value("TotalAssociations")
        return rval


    def set_TotalAssociations(self, val):
        """
            Sets the "TotalAssociations" variable.
        """
        self.proxy_set_variable_value("TotalAssociations", val)
        return


    def get_TotalBytesReceived(self):
        """
            Gets the "TotalBytesReceived" variable.
        """
        rval = self.proxy_get_variable_value("TotalBytesReceived")
        return rval


    def set_TotalBytesReceived(self, val):
        """
            Sets the "TotalBytesReceived" variable.
        """
        self.proxy_set_variable_value("TotalBytesReceived", val)
        return


    def get_TotalBytesSent(self):
        """
            Gets the "TotalBytesSent" variable.
        """
        rval = self.proxy_get_variable_value("TotalBytesSent")
        return rval


    def set_TotalBytesSent(self, val):
        """
            Sets the "TotalBytesSent" variable.
        """
        self.proxy_set_variable_value("TotalBytesSent", val)
        return


    def get_TotalIntegrityFailures(self):
        """
            Gets the "TotalIntegrityFailures" variable.
        """
        rval = self.proxy_get_variable_value("TotalIntegrityFailures")
        return rval


    def set_TotalIntegrityFailures(self, val):
        """
            Sets the "TotalIntegrityFailures" variable.
        """
        self.proxy_set_variable_value("TotalIntegrityFailures", val)
        return


    def get_TotalPSKFailures(self):
        """
            Gets the "TotalPSKFailures" variable.
        """
        rval = self.proxy_get_variable_value("TotalPSKFailures")
        return rval


    def set_TotalPSKFailures(self, val):
        """
            Sets the "TotalPSKFailures" variable.
        """
        self.proxy_set_variable_value("TotalPSKFailures", val)
        return


    def get_TotalPacketsReceived(self):
        """
            Gets the "TotalPacketsReceived" variable.
        """
        rval = self.proxy_get_variable_value("TotalPacketsReceived")
        return rval


    def set_TotalPacketsReceived(self, val):
        """
            Sets the "TotalPacketsReceived" variable.
        """
        self.proxy_set_variable_value("TotalPacketsReceived", val)
        return


    def get_TotalPacketsSent(self):
        """
            Gets the "TotalPacketsSent" variable.
        """
        rval = self.proxy_get_variable_value("TotalPacketsSent")
        return rval


    def set_TotalPacketsSent(self, val):
        """
            Sets the "TotalPacketsSent" variable.
        """
        self.proxy_set_variable_value("TotalPacketsSent", val)
        return


    def get_WEPEncryptionLevel(self):
        """
            Gets the "WEPEncryptionLevel" variable.
        """
        rval = self.proxy_get_variable_value("WEPEncryptionLevel")
        return rval


    def set_WEPEncryptionLevel(self, val):
        """
            Sets the "WEPEncryptionLevel" variable.
        """
        self.proxy_set_variable_value("WEPEncryptionLevel", val)
        return


    def get_WEPKey(self):
        """
            Gets the "WEPKey" variable.
        """
        rval = self.proxy_get_variable_value("WEPKey")
        return rval


    def set_WEPKey(self, val):
        """
            Sets the "WEPKey" variable.
        """
        self.proxy_set_variable_value("WEPKey", val)
        return


    def get_WEPKeyIndex(self):
        """
            Gets the "WEPKeyIndex" variable.
        """
        rval = self.proxy_get_variable_value("WEPKeyIndex")
        return rval


    def set_WEPKeyIndex(self, val):
        """
            Sets the "WEPKeyIndex" variable.
        """
        self.proxy_set_variable_value("WEPKeyIndex", val)
        return


    def get_WPAAuthenticationMode(self):
        """
            Gets the "WPAAuthenticationMode" variable.
        """
        rval = self.proxy_get_variable_value("WPAAuthenticationMode")
        return rval


    def set_WPAAuthenticationMode(self, val):
        """
            Sets the "WPAAuthenticationMode" variable.
        """
        self.proxy_set_variable_value("WPAAuthenticationMode", val)
        return


    def get_WPAEncryptionModes(self):
        """
            Gets the "WPAEncryptionModes" variable.
        """
        rval = self.proxy_get_variable_value("WPAEncryptionModes")
        return rval


    def set_WPAEncryptionModes(self, val):
        """
            Sets the "WPAEncryptionModes" variable.
        """
        self.proxy_set_variable_value("WPAEncryptionModes", val)
        return


    def action_FactoryDefaultReset(self):
        """
            Calls the FactoryDefaultReset action.
        """
        arguments = { }

        out_params = self.proxy_call_action("FactoryDefaultReset", arguments=arguments)

        (NewIEEE11iEncryptionModes, NewIEEE11iAuthenticationMode,) = out_params

        return NewIEEE11iEncryptionModes, NewIEEE11iAuthenticationMode


    def action_Get11iBeaconSecurityProperties(self):
        """
            Calls the Get11iBeaconSecurityProperties action.
        """
        arguments = { }

        out_params = self.proxy_call_action("Get11iBeaconSecurityProperties", arguments=arguments)

        (NewIEEE11iEncryptionModes, NewIEEE11iAuthenticationMode,) = out_params

        return NewIEEE11iEncryptionModes, NewIEEE11iAuthenticationMode


    def action_GetAuthenticationServiceMode(self):
        """
            Calls the GetAuthenticationServiceMode action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetAuthenticationServiceMode", arguments=arguments)

        (NewAuthenticationServiceMode,) = out_params

        return NewAuthenticationServiceMode


    def action_GetAutoRateFallBackMode(self):
        """
            Calls the GetAutoRateFallBackMode action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetAutoRateFallBackMode", arguments=arguments)

        (NewAutoRateFallBackEnabled,) = out_params

        return NewAutoRateFallBackEnabled


    def action_GetBSSID(self):
        """
            Calls the GetBSSID action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetBSSID", arguments=arguments)

        (NewBSSID,) = out_params

        return NewBSSID


    def action_GetBasicBeaconSecurityProperties(self):
        """
            Calls the GetBasicBeaconSecurityProperties action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetBasicBeaconSecurityProperties", arguments=arguments)

        (NewBasicEncryptionModes, NewBasicAuthenticationMode,) = out_params

        return NewBasicEncryptionModes, NewBasicAuthenticationMode


    def action_GetBeaconAdvertisement(self):
        """
            Calls the GetBeaconAdvertisement action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetBeaconAdvertisement", arguments=arguments)

        (NewBeaconAdvertisementEnabled,) = out_params

        return NewBeaconAdvertisementEnabled


    def action_GetBeaconType(self):
        """
            Calls the GetBeaconType action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetBeaconType", arguments=arguments)

        (NewBeaconType,) = out_params

        return NewBeaconType


    def action_GetByteStatistics(self):
        """
            Calls the GetByteStatistics action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetByteStatistics", arguments=arguments)

        (NewTotalBytesSent, NewTotalBytesReceived,) = out_params

        return NewTotalBytesSent, NewTotalBytesReceived


    def action_GetChannelInfo(self):
        """
            Calls the GetChannelInfo action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetChannelInfo", arguments=arguments)

        (NewChannel, NewPossibleChannels,) = out_params

        return NewChannel, NewPossibleChannels


    def action_GetChannelsInUse(self):
        """
            Calls the GetChannelsInUse action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetChannelsInUse", arguments=arguments)

        (NewChannelsInUse,) = out_params

        return NewChannelsInUse


    def action_GetDataTransmissionRateInfo(self):
        """
            Calls the GetDataTransmissionRateInfo action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDataTransmissionRateInfo", arguments=arguments)

        (NewBasicDataTransmissionRates, NewOperationalDataTransmissionRates, NewPossibleDataTransmissionRates,) = out_params

        return NewBasicDataTransmissionRates, NewOperationalDataTransmissionRates, NewPossibleDataTransmissionRates


    def action_GetDefaultWEPKeyIndex(self):
        """
            Calls the GetDefaultWEPKeyIndex action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDefaultWEPKeyIndex", arguments=arguments)

        (NewDefaultWEPKeyIndex,) = out_params

        return NewDefaultWEPKeyIndex


    def action_GetDeviceOperationMode(self):
        """
            Calls the GetDeviceOperationMode action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDeviceOperationMode", arguments=arguments)

        (NewDeviceOperationMode, NewSSID, NewBSSID, NewChannel, NewBasicDataTransmissionRates, NewOperationalDataTransmissionRates, NewDistanceFromRoot,) = out_params

        return NewDeviceOperationMode, NewSSID, NewBSSID, NewChannel, NewBasicDataTransmissionRates, NewOperationalDataTransmissionRates, NewDistanceFromRoot


    def action_GetFailureStatusInfo(self):
        """
            Calls the GetFailureStatusInfo action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetFailureStatusInfo", arguments=arguments)

        (NewTotalIntegrityFailures, NewTotalPSKFailures,) = out_params

        return NewTotalIntegrityFailures, NewTotalPSKFailures


    def action_GetGenericAssociatedDeviceInfo(self, NewAssociatedDeviceIndex):
        """
            Calls the GetGenericAssociatedDeviceInfo action.
        """
        arguments = {
            "NewAssociatedDeviceIndex": NewAssociatedDeviceIndex,
        }

        out_params = self.proxy_call_action("GetGenericAssociatedDeviceInfo", arguments=arguments)

        (NewAssociatedDeviceMACAddress, NewAssociatedDeviceIPAddress, NewAssociatedDeviceAuthenticationState,) = out_params

        return NewAssociatedDeviceMACAddress, NewAssociatedDeviceIPAddress, NewAssociatedDeviceAuthenticationState


    def action_GetInsecureOutOfBandAccessMode(self):
        """
            Calls the GetInsecureOutOfBandAccessMode action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetInsecureOutOfBandAccessMode", arguments=arguments)

        (NewInsecureOutOfBandAccessEnabled,) = out_params

        return NewInsecureOutOfBandAccessEnabled


    def action_GetLocationDescription(self):
        """
            Calls the GetLocationDescription action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetLocationDescription", arguments=arguments)

        (NewLocationDescription,) = out_params

        return NewLocationDescription


    def action_GetPacketStatistics(self):
        """
            Calls the GetPacketStatistics action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetPacketStatistics", arguments=arguments)

        (NewTotalPacketsSent, NewTotalPacketsReceived,) = out_params

        return NewTotalPacketsSent, NewTotalPacketsReceived


    def action_GetPreSharedKey(self, NewPreSharedKeyIndex):
        """
            Calls the GetPreSharedKey action.
        """
        arguments = {
            "NewPreSharedKeyIndex": NewPreSharedKeyIndex,
        }

        out_params = self.proxy_call_action("GetPreSharedKey", arguments=arguments)

        (NewPreSharedKey, NewPSKPassphrase,) = out_params

        return NewPreSharedKey, NewPSKPassphrase


    def action_GetRadioMode(self):
        """
            Calls the GetRadioMode action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetRadioMode", arguments=arguments)

        (NewRadioEnabled,) = out_params

        return NewRadioEnabled


    def action_GetRegulatoryDomain(self):
        """
            Calls the GetRegulatoryDomain action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetRegulatoryDomain", arguments=arguments)

        (NewRegulatoryDomain,) = out_params

        return NewRegulatoryDomain


    def action_GetSSID(self):
        """
            Calls the GetSSID action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetSSID", arguments=arguments)

        (NewSSID,) = out_params

        return NewSSID


    def action_GetSecurityKeys(self):
        """
            Calls the GetSecurityKeys action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetSecurityKeys", arguments=arguments)

        (NewWEPKey0, NewWEPKey1, NewWEPKey2, NewWEPKey3, NewPreSharedKey, NewKeyPassphrase,) = out_params

        return NewWEPKey0, NewWEPKey1, NewWEPKey2, NewWEPKey3, NewPreSharedKey, NewKeyPassphrase


    def action_GetSpecificAssociatedDeviceInfo(self, NewAssociatedDeviceMACAddress):
        """
            Calls the GetSpecificAssociatedDeviceInfo action.
        """
        arguments = {
            "NewAssociatedDeviceMACAddress": NewAssociatedDeviceMACAddress,
        }

        out_params = self.proxy_call_action("GetSpecificAssociatedDeviceInfo", arguments=arguments)

        (NewAssociatedDeviceIPAddress, NewAssociatedDeviceAuthenticationState,) = out_params

        return NewAssociatedDeviceIPAddress, NewAssociatedDeviceAuthenticationState


    def action_GetTotalAssociations(self):
        """
            Calls the GetTotalAssociations action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetTotalAssociations", arguments=arguments)

        (NewTotalAssociations,) = out_params

        return NewTotalAssociations


    def action_GetWPABeaconSecurityProperties(self):
        """
            Calls the GetWPABeaconSecurityProperties action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetWPABeaconSecurityProperties", arguments=arguments)

        (NewWPAEncryptionModes, NewWPAAuthenticationMode,) = out_params

        return NewWPAEncryptionModes, NewWPAAuthenticationMode


    def action_ResetAuthentication(self):
        """
            Calls the ResetAuthentication action.
        """
        arguments = { }

        out_params = self.proxy_call_action("ResetAuthentication", arguments=arguments)

        (NewIEEE11iEncryptionModes, NewIEEE11iAuthenticationMode,) = out_params

        return NewIEEE11iEncryptionModes, NewIEEE11iAuthenticationMode


    def action_Set11iBeaconSecurityProperties(self, NewIEEE11iEncryptionModes, NewIEEE11iAuthenticationMode):
        """
            Calls the Set11iBeaconSecurityProperties action.
        """
        arguments = {
            "NewIEEE11iEncryptionModes": NewIEEE11iEncryptionModes,
            "NewIEEE11iAuthenticationMode": NewIEEE11iAuthenticationMode,
        }

        out_params = self.proxy_call_action("Set11iBeaconSecurityProperties", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetAuthenticationServiceMode(self, NewAuthenticationServiceMode):
        """
            Calls the SetAuthenticationServiceMode action.
        """
        arguments = {
            "NewAuthenticationServiceMode": NewAuthenticationServiceMode,
        }

        out_params = self.proxy_call_action("SetAuthenticationServiceMode", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetAutoRateFallBackMode(self, NewAutoRateFallBackEnabled):
        """
            Calls the SetAutoRateFallBackMode action.
        """
        arguments = {
            "NewAutoRateFallBackEnabled": NewAutoRateFallBackEnabled,
        }

        out_params = self.proxy_call_action("SetAutoRateFallBackMode", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetBasicBeaconSecurityProperties(self, NewBasicEncryptionModes, NewBasicAuthenticationMode):
        """
            Calls the SetBasicBeaconSecurityProperties action.
        """
        arguments = {
            "NewBasicEncryptionModes": NewBasicEncryptionModes,
            "NewBasicAuthenticationMode": NewBasicAuthenticationMode,
        }

        out_params = self.proxy_call_action("SetBasicBeaconSecurityProperties", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetBeaconAdvertisement(self, NewBeaconAdvertisementEnabled):
        """
            Calls the SetBeaconAdvertisement action.
        """
        arguments = {
            "NewBeaconAdvertisementEnabled": NewBeaconAdvertisementEnabled,
        }

        out_params = self.proxy_call_action("SetBeaconAdvertisement", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetBeaconType(self, NewBeaconType):
        """
            Calls the SetBeaconType action.
        """
        arguments = {
            "NewBeaconType": NewBeaconType,
        }

        out_params = self.proxy_call_action("SetBeaconType", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetChannel(self, NewChannel):
        """
            Calls the SetChannel action.
        """
        arguments = {
            "NewChannel": NewChannel,
        }

        out_params = self.proxy_call_action("SetChannel", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetDataTransmissionRates(self, NewBasicDataTransmissionRates, NewOperationalDataTransmissionRates):
        """
            Calls the SetDataTransmissionRates action.
        """
        arguments = {
            "NewBasicDataTransmissionRates": NewBasicDataTransmissionRates,
            "NewOperationalDataTransmissionRates": NewOperationalDataTransmissionRates,
        }

        out_params = self.proxy_call_action("SetDataTransmissionRates", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetDefaultWEPKeyIndex(self, NewDefaultWEPKeyIndex):
        """
            Calls the SetDefaultWEPKeyIndex action.
        """
        arguments = {
            "NewDefaultWEPKeyIndex": NewDefaultWEPKeyIndex,
        }

        out_params = self.proxy_call_action("SetDefaultWEPKeyIndex", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetDeviceOperationMode(self, NewDeviceOperationMode, NewSSID, NewBSSID, NewChannel, NewBasicDataTransmissionRates, NewOperationalDataTransmissionRates, NewDistanceFromRoot):
        """
            Calls the SetDeviceOperationMode action.
        """
        arguments = {
            "NewDeviceOperationMode": NewDeviceOperationMode,
            "NewSSID": NewSSID,
            "NewBSSID": NewBSSID,
            "NewChannel": NewChannel,
            "NewBasicDataTransmissionRates": NewBasicDataTransmissionRates,
            "NewOperationalDataTransmissionRates": NewOperationalDataTransmissionRates,
            "NewDistanceFromRoot": NewDistanceFromRoot,
        }

        out_params = self.proxy_call_action("SetDeviceOperationMode", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetInsecureOutOfBandAccessMode(self, NewInsecureOutOfBandAccessEnabled):
        """
            Calls the SetInsecureOutOfBandAccessMode action.
        """
        arguments = {
            "NewInsecureOutOfBandAccessEnabled": NewInsecureOutOfBandAccessEnabled,
        }

        out_params = self.proxy_call_action("SetInsecureOutOfBandAccessMode", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetLocationDescription(self, NewLocationDescription):
        """
            Calls the SetLocationDescription action.
        """
        arguments = {
            "NewLocationDescription": NewLocationDescription,
        }

        out_params = self.proxy_call_action("SetLocationDescription", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetPreSharedKey(self, NewPreSharedKeyIndex, NewPreSharedKey, NewPSKPassphrase):
        """
            Calls the SetPreSharedKey action.
        """
        arguments = {
            "NewPreSharedKeyIndex": NewPreSharedKeyIndex,
            "NewPreSharedKey": NewPreSharedKey,
            "NewPSKPassphrase": NewPSKPassphrase,
        }

        out_params = self.proxy_call_action("SetPreSharedKey", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetRadioMode(self, NewRadioEnabled):
        """
            Calls the SetRadioMode action.
        """
        arguments = {
            "NewRadioEnabled": NewRadioEnabled,
        }

        out_params = self.proxy_call_action("SetRadioMode", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetRegulatoryDomain(self, NewRegulatoryDomain):
        """
            Calls the SetRegulatoryDomain action.
        """
        arguments = {
            "NewRegulatoryDomain": NewRegulatoryDomain,
        }

        out_params = self.proxy_call_action("SetRegulatoryDomain", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetSSID(self, NewSSID):
        """
            Calls the SetSSID action.
        """
        arguments = {
            "NewSSID": NewSSID,
        }

        out_params = self.proxy_call_action("SetSSID", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetSecurityKeys(self, NewWEPKey0, NewWEPKey1, NewWEPKey2, NewWEPKey3, NewPreSharedKey, NewKeyPassphrase):
        """
            Calls the SetSecurityKeys action.
        """
        arguments = {
            "NewWEPKey0": NewWEPKey0,
            "NewWEPKey1": NewWEPKey1,
            "NewWEPKey2": NewWEPKey2,
            "NewWEPKey3": NewWEPKey3,
            "NewPreSharedKey": NewPreSharedKey,
            "NewKeyPassphrase": NewKeyPassphrase,
        }

        out_params = self.proxy_call_action("SetSecurityKeys", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetWPABeaconSecurityProperties(self, NewWPAEncryptionModes, NewWPAAuthenticationMode):
        """
            Calls the SetWPABeaconSecurityProperties action.
        """
        arguments = {
            "NewWPAEncryptionModes": NewWPAEncryptionModes,
            "NewWPAAuthenticationMode": NewWPAAuthenticationMode,
        }

        out_params = self.proxy_call_action("SetWPABeaconSecurityProperties", arguments=arguments)

        (result,) = out_params

        return result

