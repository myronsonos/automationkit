"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class DigitalSecurityCameraMotionImage1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'DigitalSecurityCameraMotionImage1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:DigitalSecurityCameraMotionImage:1'

    SERVICE_EVENT_VARIABLES = {
        "DefaultCompressionLevel": { "data_type": "string", "default": None, "allowed_list": None},
        "DefaultEncoding": { "data_type": "string", "default": None, "allowed_list": None},
        "DefaultResolution": { "data_type": "string", "default": None, "allowed_list": None},
        "MaxBandwidth": { "data_type": "ui4", "default": "100", "allowed_list": None},
        "TargetFrameRate": { "data_type": "ui4", "default": "1500", "allowed_list": None},
    }

    def action_GetAvailableCompressionLevels(self, extract_returns=True):
        """
            Calls the GetAvailableCompressionLevels action.

            :returns: "RetAvailableCompressionLevels"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetAvailableCompressionLevels", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RetAvailableCompressionLevels",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetAvailableEncodings(self, extract_returns=True):
        """
            Calls the GetAvailableEncodings action.

            :returns: "RetAvailableEncodings"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetAvailableEncodings", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RetAvailableEncodings",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetAvailableResolutions(self, extract_returns=True):
        """
            Calls the GetAvailableResolutions action.

            :returns: "RetAvailableResolutions"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetAvailableResolutions", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RetAvailableResolutions",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetDefaultCompressionLevel(self, extract_returns=True):
        """
            Calls the GetDefaultCompressionLevel action.

            :returns: "RetCompressionLevel"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetDefaultCompressionLevel", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RetCompressionLevel",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetDefaultEncoding(self, extract_returns=True):
        """
            Calls the GetDefaultEncoding action.

            :returns: "RetEncoding"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetDefaultEncoding", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RetEncoding",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetDefaultResolution(self, extract_returns=True):
        """
            Calls the GetDefaultResolution action.

            :returns: "RetResolution"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetDefaultResolution", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RetResolution",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetDefaultVideoPresentationURL(self, extract_returns=True):
        """
            Calls the GetDefaultVideoPresentationURL action.

            :returns: "RetVideoPresentationURL"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetDefaultVideoPresentationURL", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RetVideoPresentationURL",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetDefaultVideoURL(self, extract_returns=True):
        """
            Calls the GetDefaultVideoURL action.

            :returns: "RetVideoURL"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetDefaultVideoURL", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RetVideoURL",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetMaxBandwidth(self, extract_returns=True):
        """
            Calls the GetMaxBandwidth action.

            :returns: "RetMaxBandwidth"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetMaxBandwidth", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RetMaxBandwidth",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetTargetFrameRate(self, extract_returns=True):
        """
            Calls the GetTargetFrameRate action.

            :returns: "RetTargetFrameRate"
        """
        arguments = { }

        out_params = self._proxy_call_action("GetTargetFrameRate", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RetTargetFrameRate",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetVideoPresentationURL(self, ReqEncoding, ReqCompression, ReqResolution, extract_returns=True):
        """
            Calls the GetVideoPresentationURL action.

            :returns: "RetVideoPresentationURL"
        """
        arguments = {
            "ReqEncoding": ReqEncoding,
            "ReqCompression": ReqCompression,
            "ReqResolution": ReqResolution,
        }

        out_params = self._proxy_call_action("GetVideoPresentationURL", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RetVideoPresentationURL",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetVideoURL(self, ReqEncoding, ReqCompression, ReqResolution, extract_returns=True):
        """
            Calls the GetVideoURL action.

            :returns: "RetVideoURL"
        """
        arguments = {
            "ReqEncoding": ReqEncoding,
            "ReqCompression": ReqCompression,
            "ReqResolution": ReqResolution,
        }

        out_params = self._proxy_call_action("GetVideoURL", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("RetVideoURL",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetDefaultCompressionLevel(self, ReqCompressionLevel, extract_returns=True):
        """
            Calls the SetDefaultCompressionLevel action.

            :returns: "result"
        """
        arguments = {
            "ReqCompressionLevel": ReqCompressionLevel,
        }

        out_params = self._proxy_call_action("SetDefaultCompressionLevel", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetDefaultEncoding(self, ReqEncoding, extract_returns=True):
        """
            Calls the SetDefaultEncoding action.

            :returns: "result"
        """
        arguments = {
            "ReqEncoding": ReqEncoding,
        }

        out_params = self._proxy_call_action("SetDefaultEncoding", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetDefaultResolution(self, ReqResolution, extract_returns=True):
        """
            Calls the SetDefaultResolution action.

            :returns: "result"
        """
        arguments = {
            "ReqResolution": ReqResolution,
        }

        out_params = self._proxy_call_action("SetDefaultResolution", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetMaxBandwidth(self, ReqMaxBandwidth, extract_returns=True):
        """
            Calls the SetMaxBandwidth action.

            :returns: "result"
        """
        arguments = {
            "ReqMaxBandwidth": ReqMaxBandwidth,
        }

        out_params = self._proxy_call_action("SetMaxBandwidth", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_SetTargetFrameRate(self, ReqTargetFrameRate, extract_returns=True):
        """
            Calls the SetTargetFrameRate action.

            :returns: "result"
        """
        arguments = {
            "ReqTargetFrameRate": ReqTargetFrameRate,
        }

        out_params = self._proxy_call_action("SetTargetFrameRate", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args
