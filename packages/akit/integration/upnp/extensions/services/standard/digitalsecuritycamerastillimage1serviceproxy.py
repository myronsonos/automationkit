"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class DigitalSecurityCameraStillImage1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'DigitalSecurityCameraStillImage1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:DigitalSecurityCameraStillImage:1'
    SERVICE_ID = 'urn:schemas-upnp-org:service:DigitalSecurityCameraStillImage'


    def get_AvailableCompressionLevels(self):
        """
            Gets the "AvailableCompressionLevels" variable.
        """
        rval = self.proxy_get_variable_value("AvailableCompressionLevels")
        return rval


    def set_AvailableCompressionLevels(self, val):
        """
            Sets the "AvailableCompressionLevels" variable.
        """
        self.proxy_set_variable_value("AvailableCompressionLevels", val)
        return


    def get_AvailableEncodings(self):
        """
            Gets the "AvailableEncodings" variable.
        """
        rval = self.proxy_get_variable_value("AvailableEncodings")
        return rval


    def set_AvailableEncodings(self, val):
        """
            Sets the "AvailableEncodings" variable.
        """
        self.proxy_set_variable_value("AvailableEncodings", val)
        return


    def get_AvailableResolutions(self):
        """
            Gets the "AvailableResolutions" variable.
        """
        rval = self.proxy_get_variable_value("AvailableResolutions")
        return rval


    def set_AvailableResolutions(self, val):
        """
            Sets the "AvailableResolutions" variable.
        """
        self.proxy_set_variable_value("AvailableResolutions", val)
        return


    def get_DefaultCompressionLevel(self):
        """
            Gets the "DefaultCompressionLevel" variable.
        """
        rval = self.proxy_get_variable_value("DefaultCompressionLevel")
        return rval


    def set_DefaultCompressionLevel(self, val):
        """
            Sets the "DefaultCompressionLevel" variable.
        """
        self.proxy_set_variable_value("DefaultCompressionLevel", val)
        return


    def get_DefaultEncoding(self):
        """
            Gets the "DefaultEncoding" variable.
        """
        rval = self.proxy_get_variable_value("DefaultEncoding")
        return rval


    def set_DefaultEncoding(self, val):
        """
            Sets the "DefaultEncoding" variable.
        """
        self.proxy_set_variable_value("DefaultEncoding", val)
        return


    def get_DefaultResolution(self):
        """
            Gets the "DefaultResolution" variable.
        """
        rval = self.proxy_get_variable_value("DefaultResolution")
        return rval


    def set_DefaultResolution(self, val):
        """
            Sets the "DefaultResolution" variable.
        """
        self.proxy_set_variable_value("DefaultResolution", val)
        return


    def get_ImagePresentationURL(self):
        """
            Gets the "ImagePresentationURL" variable.
        """
        rval = self.proxy_get_variable_value("ImagePresentationURL")
        return rval


    def set_ImagePresentationURL(self, val):
        """
            Sets the "ImagePresentationURL" variable.
        """
        self.proxy_set_variable_value("ImagePresentationURL", val)
        return


    def get_ImageURL(self):
        """
            Gets the "ImageURL" variable.
        """
        rval = self.proxy_get_variable_value("ImageURL")
        return rval


    def set_ImageURL(self, val):
        """
            Sets the "ImageURL" variable.
        """
        self.proxy_set_variable_value("ImageURL", val)
        return


    def action_GetAvailableCompressionLevels(self):
        """
            Calls the GetAvailableCompressionLevels action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetAvailableCompressionLevels", arguments=arguments)

        (RetAvailableCompressionLevels,) = out_params

        return RetAvailableCompressionLevels


    def action_GetAvailableEncodings(self):
        """
            Calls the GetAvailableEncodings action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetAvailableEncodings", arguments=arguments)

        (RetAvailableEncodings,) = out_params

        return RetAvailableEncodings


    def action_GetAvailableResolutions(self):
        """
            Calls the GetAvailableResolutions action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetAvailableResolutions", arguments=arguments)

        (RetAvailableResolutions,) = out_params

        return RetAvailableResolutions


    def action_GetDefaultCompressionLevel(self):
        """
            Calls the GetDefaultCompressionLevel action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDefaultCompressionLevel", arguments=arguments)

        (RetCompressionLevel,) = out_params

        return RetCompressionLevel


    def action_GetDefaultEncoding(self):
        """
            Calls the GetDefaultEncoding action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDefaultEncoding", arguments=arguments)

        (RetEncoding,) = out_params

        return RetEncoding


    def action_GetDefaultImagePresentationURL(self):
        """
            Calls the GetDefaultImagePresentationURL action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDefaultImagePresentationURL", arguments=arguments)

        (RetImagePresentationURL,) = out_params

        return RetImagePresentationURL


    def action_GetDefaultImageURL(self):
        """
            Calls the GetDefaultImageURL action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDefaultImageURL", arguments=arguments)

        (RetImageURL,) = out_params

        return RetImageURL


    def action_GetDefaultResolution(self):
        """
            Calls the GetDefaultResolution action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDefaultResolution", arguments=arguments)

        (RetResolution,) = out_params

        return RetResolution


    def action_GetImagePresentationURL(self, ReqEncoding, ReqCompression, ReqResolution):
        """
            Calls the GetImagePresentationURL action.
        """
        arguments = {
            "ReqEncoding": ReqEncoding,
            "ReqCompression": ReqCompression,
            "ReqResolution": ReqResolution,
        }

        out_params = self.proxy_call_action("GetImagePresentationURL", arguments=arguments)

        (RetImagePresentationURL,) = out_params

        return RetImagePresentationURL


    def action_GetImageURL(self, ReqEncoding, ReqCompression, ReqResolution):
        """
            Calls the GetImageURL action.
        """
        arguments = {
            "ReqEncoding": ReqEncoding,
            "ReqCompression": ReqCompression,
            "ReqResolution": ReqResolution,
        }

        out_params = self.proxy_call_action("GetImageURL", arguments=arguments)

        (RetImageURL,) = out_params

        return RetImageURL


    def action_SetDefaultCompressionLevel(self, ReqCompressionLevel):
        """
            Calls the SetDefaultCompressionLevel action.
        """
        arguments = {
            "ReqCompressionLevel": ReqCompressionLevel,
        }

        out_params = self.proxy_call_action("SetDefaultCompressionLevel", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetDefaultEncoding(self, ReqEncoding):
        """
            Calls the SetDefaultEncoding action.
        """
        arguments = {
            "ReqEncoding": ReqEncoding,
        }

        out_params = self.proxy_call_action("SetDefaultEncoding", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetDefaultResolution(self, ReqResolution):
        """
            Calls the SetDefaultResolution action.
        """
        arguments = {
            "ReqResolution": ReqResolution,
        }

        out_params = self.proxy_call_action("SetDefaultResolution", arguments=arguments)

        (result,) = out_params

        return result

