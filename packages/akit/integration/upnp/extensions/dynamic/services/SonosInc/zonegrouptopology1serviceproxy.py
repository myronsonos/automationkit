"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class ZoneGroupTopology1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'ZoneGroupTopology1' service.
    """

    SERVICE_MANUFACTURER = 'SonosInc'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:ZoneGroupTopology:1'

    SERVICE_EVENT_VARIABLES = {
        "AlarmRunSequence": { "data_type": "string", "default": None, "allowed_list": None},
        "AreasUpdateID": { "data_type": "string", "default": None, "allowed_list": None},
        "AvailableSoftwareUpdate": { "data_type": "string", "default": None, "allowed_list": None},
        "MuseHouseholdId": { "data_type": "string", "default": None, "allowed_list": None},
        "NetsettingsUpdateID": { "data_type": "string", "default": None, "allowed_list": None},
        "SourceAreasUpdateID": { "data_type": "string", "default": None, "allowed_list": None},
        "ThirdPartyMediaServersX": { "data_type": "string", "default": None, "allowed_list": None},
        "ZoneGroupID": { "data_type": "string", "default": None, "allowed_list": None},
        "ZoneGroupName": { "data_type": "string", "default": None, "allowed_list": None},
        "ZoneGroupState": { "data_type": "string", "default": None, "allowed_list": None},
        "ZonePlayerUUIDsInGroup": { "data_type": "string", "default": None, "allowed_list": None},
    }


    def action_BeginSoftwareUpdate(self, UpdateURL, Flags, ExtraOptions, extract_returns=True):
        """
            Calls the BeginSoftwareUpdate action.

            :returns: "result"
        """
        arguments = {
            "UpdateURL": UpdateURL,
            "Flags": Flags,
            "ExtraOptions": ExtraOptions,
        }

        out_params = self._proxy_call_action("BeginSoftwareUpdate", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_CheckForUpdate(self, UpdateType, CachedOnly, Version, extract_returns=True):
        """
            Calls the CheckForUpdate action.

            :returns: "UpdateItem"
        """
        arguments = {
            "UpdateType": UpdateType,
            "CachedOnly": CachedOnly,
            "Version": Version,
        }

        out_params = self._proxy_call_action("CheckForUpdate", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("UpdateItem",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetZoneGroupAttributes(self, extract_returns=True):
        """
            Calls the GetZoneGroupAttributes action.

            :returns: "CurrentZoneGroupName", "CurrentZoneGroupID", "CurrentZonePlayerUUIDsInGroup", "CurrentMuseHouseholdId"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetZoneGroupAttributes", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentZoneGroupName", "CurrentZoneGroupID", "CurrentZonePlayerUUIDsInGroup", "CurrentMuseHouseholdId",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetZoneGroupState(self, extract_returns=True):
        """
            Calls the GetZoneGroupState action.

            :returns: "ZoneGroupState"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetZoneGroupState", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("ZoneGroupState",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_RegisterMobileDevice(self, MobileDeviceName, MobileDeviceUDN, MobileIPAndPort, extract_returns=True):
        """
            Calls the RegisterMobileDevice action.

            :returns: "result"
        """
        arguments = {
            "MobileDeviceName": MobileDeviceName,
            "MobileDeviceUDN": MobileDeviceUDN,
            "MobileIPAndPort": MobileIPAndPort,
        }

        out_params = self._proxy_call_action("RegisterMobileDevice", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_ReportAlarmStartedRunning(self, extract_returns=True):
        """
            Calls the ReportAlarmStartedRunning action.

            :returns: "result"
        """
        arguments = { }

        out_params = self._proxy_call_action("ReportAlarmStartedRunning", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_ReportUnresponsiveDevice(self, DeviceUUID, DesiredAction, extract_returns=True):
        """
            Calls the ReportUnresponsiveDevice action.

            :returns: "result"
        """
        arguments = {
            "DeviceUUID": DeviceUUID,
            "DesiredAction": DesiredAction,
        }

        out_params = self._proxy_call_action("ReportUnresponsiveDevice", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SubmitDiagnostics(self, IncludeControllers, Type, extract_returns=True):
        """
            Calls the SubmitDiagnostics action.

            :returns: "DiagnosticID"
        """
        arguments = {
            "IncludeControllers": IncludeControllers,
            "Type": Type,
        }

        out_params = self._proxy_call_action("SubmitDiagnostics", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("DiagnosticID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

