"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class GroupManagement1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'GroupManagement1' service.
    """

    SERVICE_MANUFACTURER = 'SonosInc'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:GroupManagement:1'

    SERVICE_EVENT_VARIABLES = {
        "GroupCoordinatorIsLocal": { "data_type": "boolean", "default": None, "allowed_list": None},
        "LocalGroupUUID": { "data_type": "string", "default": None, "allowed_list": None},
        "ResetVolumeAfter": { "data_type": "boolean", "default": None, "allowed_list": None},
        "VirtualLineInGroupID": { "data_type": "string", "default": None, "allowed_list": None},
        "VolumeAVTransportURI": { "data_type": "string", "default": None, "allowed_list": None},
    }


    def action_AddMember(self, MemberID, BootSeq, extract_returns=True):
        """
            Calls the AddMember action.

            :returns: "CurrentTransportSettings", "CurrentURI", "GroupUUIDJoined", "ResetVolumeAfter", "VolumeAVTransportURI"
        """
        arguments = {
            "MemberID": MemberID,
            "BootSeq": BootSeq,
        }

        out_params = self._proxy_call_action("AddMember", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentTransportSettings", "CurrentURI", "GroupUUIDJoined", "ResetVolumeAfter", "VolumeAVTransportURI",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_RemoveMember(self, MemberID, extract_returns=True):
        """
            Calls the RemoveMember action.

            :returns: "result"
        """
        arguments = {
            "MemberID": MemberID,
        }

        out_params = self._proxy_call_action("RemoveMember", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_ReportTrackBufferingResult(self, MemberID, ResultCode, extract_returns=True):
        """
            Calls the ReportTrackBufferingResult action.

            :returns: "result"
        """
        arguments = {
            "MemberID": MemberID,
            "ResultCode": ResultCode,
        }

        out_params = self._proxy_call_action("ReportTrackBufferingResult", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetSourceAreaIds(self, DesiredSourceAreaIds, extract_returns=True):
        """
            Calls the SetSourceAreaIds action.

            :returns: "result"
        """
        arguments = {
            "DesiredSourceAreaIds": DesiredSourceAreaIds,
        }

        out_params = self._proxy_call_action("SetSourceAreaIds", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

