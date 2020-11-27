"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class WLANConfiguration1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'WLANConfiguration1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:WLANConfiguration:1'

    SERVICE_EVENT_VARIABLES = {
        "TotalAssociations": { "data_type": "ui2", "default": None, "allowed_list": None},
    }


    def action_FactoryDefaultReset(self, extract_returns=True):
        """
            Calls the FactoryDefaultReset action.

            :returns: "result"
        """
        arguments = { }

        out_params = self._proxy_call_action("FactoryDefaultReset", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_Get11iBeaconSecurityProperties(self, extract_returns=True):
        """
            Calls the Get11iBeaconSecurityProperties action.

            :returns: "NewIEEE11iEncryptionModes", "NewIEEE11iAuthenticationMode"
        """
        arguments = { }

        out_params = self._proxy_call_action("Get11iBeaconSecurityProperties", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewIEEE11iEncryptionModes", "NewIEEE11iAuthenticationMode",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetAuthenticationServiceMode(self, extract_returns=True):
        """
            Calls the GetAuthenticationServiceMode action.

            :returns: "NewAuthenticationServiceMode"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetAuthenticationServiceMode", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewAuthenticationServiceMode",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetAutoRateFallBackMode(self, extract_returns=True):
        """
            Calls the GetAutoRateFallBackMode action.

            :returns: "NewAutoRateFallBackEnabled"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetAutoRateFallBackMode", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewAutoRateFallBackEnabled",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetBSSID(self, extract_returns=True):
        """
            Calls the GetBSSID action.

            :returns: "NewBSSID"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetBSSID", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewBSSID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetBasicBeaconSecurityProperties(self, extract_returns=True):
        """
            Calls the GetBasicBeaconSecurityProperties action.

            :returns: "NewBasicEncryptionModes", "NewBasicAuthenticationMode"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetBasicBeaconSecurityProperties", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewBasicEncryptionModes", "NewBasicAuthenticationMode",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetBeaconAdvertisement(self, extract_returns=True):
        """
            Calls the GetBeaconAdvertisement action.

            :returns: "NewBeaconAdvertisementEnabled"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetBeaconAdvertisement", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewBeaconAdvertisementEnabled",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetBeaconType(self, extract_returns=True):
        """
            Calls the GetBeaconType action.

            :returns: "NewBeaconType"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetBeaconType", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewBeaconType",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetByteStatistics(self, extract_returns=True):
        """
            Calls the GetByteStatistics action.

            :returns: "NewTotalBytesSent", "NewTotalBytesReceived"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetByteStatistics", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewTotalBytesSent", "NewTotalBytesReceived",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetChannelInfo(self, extract_returns=True):
        """
            Calls the GetChannelInfo action.

            :returns: "NewChannel", "NewPossibleChannels"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetChannelInfo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewChannel", "NewPossibleChannels",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetChannelsInUse(self, extract_returns=True):
        """
            Calls the GetChannelsInUse action.

            :returns: "NewChannelsInUse"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetChannelsInUse", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewChannelsInUse",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetDataTransmissionRateInfo(self, extract_returns=True):
        """
            Calls the GetDataTransmissionRateInfo action.

            :returns: "NewBasicDataTransmissionRates", "NewOperationalDataTransmissionRates", "NewPossibleDataTransmissionRates"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetDataTransmissionRateInfo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewBasicDataTransmissionRates", "NewOperationalDataTransmissionRates", "NewPossibleDataTransmissionRates",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetDefaultWEPKeyIndex(self, extract_returns=True):
        """
            Calls the GetDefaultWEPKeyIndex action.

            :returns: "NewDefaultWEPKeyIndex"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetDefaultWEPKeyIndex", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewDefaultWEPKeyIndex",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetDeviceOperationMode(self, extract_returns=True):
        """
            Calls the GetDeviceOperationMode action.

            :returns: "NewDeviceOperationMode", "NewSSID", "NewBSSID", "NewChannel", "NewBasicDataTransmissionRates", "NewOperationalDataTransmissionRates", "NewDistanceFromRoot"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetDeviceOperationMode", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewDeviceOperationMode", "NewSSID", "NewBSSID", "NewChannel", "NewBasicDataTransmissionRates", "NewOperationalDataTransmissionRates", "NewDistanceFromRoot",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetFailureStatusInfo(self, extract_returns=True):
        """
            Calls the GetFailureStatusInfo action.

            :returns: "NewTotalIntegrityFailures", "NewTotalPSKFailures"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetFailureStatusInfo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewTotalIntegrityFailures", "NewTotalPSKFailures",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetGenericAssociatedDeviceInfo(self, NewAssociatedDeviceIndex, extract_returns=True):
        """
            Calls the GetGenericAssociatedDeviceInfo action.

            :returns: "NewAssociatedDeviceMACAddress", "NewAssociatedDeviceIPAddress", "NewAssociatedDeviceAuthenticationState"
        """
        arguments = {
            "NewAssociatedDeviceIndex": NewAssociatedDeviceIndex,
        }

        out_params = self._proxy_call_action("GetGenericAssociatedDeviceInfo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewAssociatedDeviceMACAddress", "NewAssociatedDeviceIPAddress", "NewAssociatedDeviceAuthenticationState",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetInsecureOutOfBandAccessMode(self, extract_returns=True):
        """
            Calls the GetInsecureOutOfBandAccessMode action.

            :returns: "NewInsecureOutOfBandAccessEnabled"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetInsecureOutOfBandAccessMode", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewInsecureOutOfBandAccessEnabled",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetLocationDescription(self, extract_returns=True):
        """
            Calls the GetLocationDescription action.

            :returns: "NewLocationDescription"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetLocationDescription", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewLocationDescription",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetPacketStatistics(self, extract_returns=True):
        """
            Calls the GetPacketStatistics action.

            :returns: "NewTotalPacketsSent", "NewTotalPacketsReceived"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetPacketStatistics", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewTotalPacketsSent", "NewTotalPacketsReceived",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetPreSharedKey(self, NewPreSharedKeyIndex, extract_returns=True):
        """
            Calls the GetPreSharedKey action.

            :returns: "NewPreSharedKey", "NewPSKPassphrase"
        """
        arguments = {
            "NewPreSharedKeyIndex": NewPreSharedKeyIndex,
        }

        out_params = self._proxy_call_action("GetPreSharedKey", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewPreSharedKey", "NewPSKPassphrase",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetRadioMode(self, extract_returns=True):
        """
            Calls the GetRadioMode action.

            :returns: "NewRadioEnabled"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetRadioMode", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewRadioEnabled",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetRegulatoryDomain(self, extract_returns=True):
        """
            Calls the GetRegulatoryDomain action.

            :returns: "NewRegulatoryDomain"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetRegulatoryDomain", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewRegulatoryDomain",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetSSID(self, extract_returns=True):
        """
            Calls the GetSSID action.

            :returns: "NewSSID"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetSSID", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewSSID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetSecurityKeys(self, extract_returns=True):
        """
            Calls the GetSecurityKeys action.

            :returns: "NewWEPKey0", "NewWEPKey1", "NewWEPKey2", "NewWEPKey3", "NewPreSharedKey", "NewKeyPassphrase"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetSecurityKeys", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewWEPKey0", "NewWEPKey1", "NewWEPKey2", "NewWEPKey3", "NewPreSharedKey", "NewKeyPassphrase",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetSpecificAssociatedDeviceInfo(self, NewAssociatedDeviceMACAddress, extract_returns=True):
        """
            Calls the GetSpecificAssociatedDeviceInfo action.

            :returns: "NewAssociatedDeviceIPAddress", "NewAssociatedDeviceAuthenticationState"
        """
        arguments = {
            "NewAssociatedDeviceMACAddress": NewAssociatedDeviceMACAddress,
        }

        out_params = self._proxy_call_action("GetSpecificAssociatedDeviceInfo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewAssociatedDeviceIPAddress", "NewAssociatedDeviceAuthenticationState",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetTotalAssociations(self, extract_returns=True):
        """
            Calls the GetTotalAssociations action.

            :returns: "NewTotalAssociations"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetTotalAssociations", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewTotalAssociations",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetWPABeaconSecurityProperties(self, extract_returns=True):
        """
            Calls the GetWPABeaconSecurityProperties action.

            :returns: "NewWPAEncryptionModes", "NewWPAAuthenticationMode"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetWPABeaconSecurityProperties", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewWPAEncryptionModes", "NewWPAAuthenticationMode",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_ResetAuthentication(self, extract_returns=True):
        """
            Calls the ResetAuthentication action.

            :returns: "result"
        """
        arguments = { }

        out_params = self._proxy_call_action("ResetAuthentication", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_Set11iBeaconSecurityProperties(self, NewIEEE11iEncryptionModes, NewIEEE11iAuthenticationMode, extract_returns=True):
        """
            Calls the Set11iBeaconSecurityProperties action.

            :returns: "result"
        """
        arguments = {
            "NewIEEE11iEncryptionModes": NewIEEE11iEncryptionModes,
            "NewIEEE11iAuthenticationMode": NewIEEE11iAuthenticationMode,
        }

        out_params = self._proxy_call_action("Set11iBeaconSecurityProperties", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetAuthenticationServiceMode(self, NewAuthenticationServiceMode, extract_returns=True):
        """
            Calls the SetAuthenticationServiceMode action.

            :returns: "result"
        """
        arguments = {
            "NewAuthenticationServiceMode": NewAuthenticationServiceMode,
        }

        out_params = self._proxy_call_action("SetAuthenticationServiceMode", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetAutoRateFallBackMode(self, NewAutoRateFallBackEnabled, extract_returns=True):
        """
            Calls the SetAutoRateFallBackMode action.

            :returns: "result"
        """
        arguments = {
            "NewAutoRateFallBackEnabled": NewAutoRateFallBackEnabled,
        }

        out_params = self._proxy_call_action("SetAutoRateFallBackMode", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetBasicBeaconSecurityProperties(self, NewBasicEncryptionModes, NewBasicAuthenticationMode, extract_returns=True):
        """
            Calls the SetBasicBeaconSecurityProperties action.

            :returns: "result"
        """
        arguments = {
            "NewBasicEncryptionModes": NewBasicEncryptionModes,
            "NewBasicAuthenticationMode": NewBasicAuthenticationMode,
        }

        out_params = self._proxy_call_action("SetBasicBeaconSecurityProperties", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetBeaconAdvertisement(self, NewBeaconAdvertisementEnabled, extract_returns=True):
        """
            Calls the SetBeaconAdvertisement action.

            :returns: "result"
        """
        arguments = {
            "NewBeaconAdvertisementEnabled": NewBeaconAdvertisementEnabled,
        }

        out_params = self._proxy_call_action("SetBeaconAdvertisement", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetBeaconType(self, NewBeaconType, extract_returns=True):
        """
            Calls the SetBeaconType action.

            :returns: "result"
        """
        arguments = {
            "NewBeaconType": NewBeaconType,
        }

        out_params = self._proxy_call_action("SetBeaconType", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetChannel(self, NewChannel, extract_returns=True):
        """
            Calls the SetChannel action.

            :returns: "result"
        """
        arguments = {
            "NewChannel": NewChannel,
        }

        out_params = self._proxy_call_action("SetChannel", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetDataTransmissionRates(self, NewBasicDataTransmissionRates, NewOperationalDataTransmissionRates, extract_returns=True):
        """
            Calls the SetDataTransmissionRates action.

            :returns: "result"
        """
        arguments = {
            "NewBasicDataTransmissionRates": NewBasicDataTransmissionRates,
            "NewOperationalDataTransmissionRates": NewOperationalDataTransmissionRates,
        }

        out_params = self._proxy_call_action("SetDataTransmissionRates", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetDefaultWEPKeyIndex(self, NewDefaultWEPKeyIndex, extract_returns=True):
        """
            Calls the SetDefaultWEPKeyIndex action.

            :returns: "result"
        """
        arguments = {
            "NewDefaultWEPKeyIndex": NewDefaultWEPKeyIndex,
        }

        out_params = self._proxy_call_action("SetDefaultWEPKeyIndex", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetDeviceOperationMode(self, NewDeviceOperationMode, NewSSID, NewBSSID, NewChannel, NewBasicDataTransmissionRates, NewOperationalDataTransmissionRates, NewDistanceFromRoot, extract_returns=True):
        """
            Calls the SetDeviceOperationMode action.

            :returns: "result"
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

        out_params = self._proxy_call_action("SetDeviceOperationMode", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetInsecureOutOfBandAccessMode(self, NewInsecureOutOfBandAccessEnabled, extract_returns=True):
        """
            Calls the SetInsecureOutOfBandAccessMode action.

            :returns: "result"
        """
        arguments = {
            "NewInsecureOutOfBandAccessEnabled": NewInsecureOutOfBandAccessEnabled,
        }

        out_params = self._proxy_call_action("SetInsecureOutOfBandAccessMode", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetLocationDescription(self, NewLocationDescription, extract_returns=True):
        """
            Calls the SetLocationDescription action.

            :returns: "result"
        """
        arguments = {
            "NewLocationDescription": NewLocationDescription,
        }

        out_params = self._proxy_call_action("SetLocationDescription", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetPreSharedKey(self, NewPreSharedKeyIndex, NewPreSharedKey, NewPSKPassphrase, extract_returns=True):
        """
            Calls the SetPreSharedKey action.

            :returns: "result"
        """
        arguments = {
            "NewPreSharedKeyIndex": NewPreSharedKeyIndex,
            "NewPreSharedKey": NewPreSharedKey,
            "NewPSKPassphrase": NewPSKPassphrase,
        }

        out_params = self._proxy_call_action("SetPreSharedKey", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetRadioMode(self, NewRadioEnabled, extract_returns=True):
        """
            Calls the SetRadioMode action.

            :returns: "result"
        """
        arguments = {
            "NewRadioEnabled": NewRadioEnabled,
        }

        out_params = self._proxy_call_action("SetRadioMode", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetRegulatoryDomain(self, NewRegulatoryDomain, extract_returns=True):
        """
            Calls the SetRegulatoryDomain action.

            :returns: "result"
        """
        arguments = {
            "NewRegulatoryDomain": NewRegulatoryDomain,
        }

        out_params = self._proxy_call_action("SetRegulatoryDomain", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetSSID(self, NewSSID, extract_returns=True):
        """
            Calls the SetSSID action.

            :returns: "result"
        """
        arguments = {
            "NewSSID": NewSSID,
        }

        out_params = self._proxy_call_action("SetSSID", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetSecurityKeys(self, NewWEPKey0, NewWEPKey1, NewWEPKey2, NewWEPKey3, NewPreSharedKey, NewKeyPassphrase, extract_returns=True):
        """
            Calls the SetSecurityKeys action.

            :returns: "result"
        """
        arguments = {
            "NewWEPKey0": NewWEPKey0,
            "NewWEPKey1": NewWEPKey1,
            "NewWEPKey2": NewWEPKey2,
            "NewWEPKey3": NewWEPKey3,
            "NewPreSharedKey": NewPreSharedKey,
            "NewKeyPassphrase": NewKeyPassphrase,
        }

        out_params = self._proxy_call_action("SetSecurityKeys", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetWPABeaconSecurityProperties(self, NewWPAEncryptionModes, NewWPAAuthenticationMode, extract_returns=True):
        """
            Calls the SetWPABeaconSecurityProperties action.

            :returns: "result"
        """
        arguments = {
            "NewWPAEncryptionModes": NewWPAEncryptionModes,
            "NewWPAAuthenticationMode": NewWPAAuthenticationMode,
        }

        out_params = self._proxy_call_action("SetWPABeaconSecurityProperties", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

