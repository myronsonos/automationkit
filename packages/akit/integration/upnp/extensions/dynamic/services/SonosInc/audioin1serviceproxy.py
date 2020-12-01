"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class AudioIn1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'AudioIn1' service.
    """

    SERVICE_MANUFACTURER = 'SonosInc'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:AudioIn:1'

    SERVICE_EVENT_VARIABLES = {
        "AudioInputName": { "data_type": "string", "default": None, "allowed_list": None},
        "Icon": { "data_type": "string", "default": None, "allowed_list": None},
        "LeftLineInLevel": { "data_type": "i4", "default": None, "allowed_list": None},
        "LineInConnected": { "data_type": "boolean", "default": None, "allowed_list": None},
        "Playing": { "data_type": "boolean", "default": None, "allowed_list": None},
        "RightLineInLevel": { "data_type": "i4", "default": None, "allowed_list": None},
    }

    def action_GetAudioInputAttributes(self, extract_returns=True):
        """
            Calls the GetAudioInputAttributes action.

            :returns: "CurrentName", "CurrentIcon"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetAudioInputAttributes", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentName", "CurrentIcon",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetLineInLevel(self, extract_returns=True):
        """
            Calls the GetLineInLevel action.

            :returns: "CurrentLeftLineInLevel", "CurrentRightLineInLevel"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetLineInLevel", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentLeftLineInLevel", "CurrentRightLineInLevel",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SelectAudio(self, ObjectID, extract_returns=True):
        """
            Calls the SelectAudio action.

            :returns: "result"
        """
        arguments = {
            "ObjectID": ObjectID,
        }

        out_params = self._proxy_call_action("SelectAudio", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetAudioInputAttributes(self, DesiredName, DesiredIcon, extract_returns=True):
        """
            Calls the SetAudioInputAttributes action.

            :returns: "result"
        """
        arguments = {
            "DesiredName": DesiredName,
            "DesiredIcon": DesiredIcon,
        }

        out_params = self._proxy_call_action("SetAudioInputAttributes", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetLineInLevel(self, DesiredLeftLineInLevel, DesiredRightLineInLevel, extract_returns=True):
        """
            Calls the SetLineInLevel action.

            :returns: "result"
        """
        arguments = {
            "DesiredLeftLineInLevel": DesiredLeftLineInLevel,
            "DesiredRightLineInLevel": DesiredRightLineInLevel,
        }

        out_params = self._proxy_call_action("SetLineInLevel", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_StartTransmissionToGroup(self, CoordinatorID, extract_returns=True):
        """
            Calls the StartTransmissionToGroup action.

            :returns: "CurrentTransportSettings"
        """
        arguments = {
            "CoordinatorID": CoordinatorID,
        }

        out_params = self._proxy_call_action("StartTransmissionToGroup", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("CurrentTransportSettings",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_StopTransmissionToGroup(self, CoordinatorID, extract_returns=True):
        """
            Calls the StopTransmissionToGroup action.

            :returns: "result"
        """
        arguments = {
            "CoordinatorID": CoordinatorID,
        }

        out_params = self._proxy_call_action("StopTransmissionToGroup", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args
