"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class ScanServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'Scan' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:Scan:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:Scan'


    def get_AppendSideNumber(self):
        """
            Gets the "AppendSideNumber" variable.
        """
        rval = self.proxy_get_variable_value("AppendSideNumber")
        return rval


    def set_AppendSideNumber(self, val):
        """
            Sets the "AppendSideNumber" variable.
        """
        self.proxy_set_variable_value("AppendSideNumber", val)
        return


    def get_BaseName(self):
        """
            Gets the "BaseName" variable.
        """
        rval = self.proxy_get_variable_value("BaseName")
        return rval


    def set_BaseName(self, val):
        """
            Sets the "BaseName" variable.
        """
        self.proxy_set_variable_value("BaseName", val)
        return


    def get_BitDepth(self):
        """
            Gets the "BitDepth" variable.
        """
        rval = self.proxy_get_variable_value("BitDepth")
        return rval


    def set_BitDepth(self, val):
        """
            Sets the "BitDepth" variable.
        """
        self.proxy_set_variable_value("BitDepth", val)
        return


    def get_ColorSpace(self):
        """
            Gets the "ColorSpace" variable.
        """
        rval = self.proxy_get_variable_value("ColorSpace")
        return rval


    def set_ColorSpace(self, val):
        """
            Sets the "ColorSpace" variable.
        """
        self.proxy_set_variable_value("ColorSpace", val)
        return


    def get_ColorType(self):
        """
            Gets the "ColorType" variable.
        """
        rval = self.proxy_get_variable_value("ColorType")
        return rval


    def set_ColorType(self, val):
        """
            Sets the "ColorType" variable.
        """
        self.proxy_set_variable_value("ColorType", val)
        return


    def get_CompressionFactor(self):
        """
            Gets the "CompressionFactor" variable.
        """
        rval = self.proxy_get_variable_value("CompressionFactor")
        return rval


    def set_CompressionFactor(self, val):
        """
            Sets the "CompressionFactor" variable.
        """
        self.proxy_set_variable_value("CompressionFactor", val)
        return


    def get_Destination(self):
        """
            Gets the "Destination" variable.
        """
        rval = self.proxy_get_variable_value("Destination")
        return rval


    def set_Destination(self, val):
        """
            Sets the "Destination" variable.
        """
        self.proxy_set_variable_value("Destination", val)
        return


    def get_DestinationID(self):
        """
            Gets the "DestinationID" variable.
        """
        rval = self.proxy_get_variable_value("DestinationID")
        return rval


    def set_DestinationID(self, val):
        """
            Sets the "DestinationID" variable.
        """
        self.proxy_set_variable_value("DestinationID", val)
        return


    def get_DeviceID(self):
        """
            Gets the "DeviceID" variable.
        """
        rval = self.proxy_get_variable_value("DeviceID")
        return rval


    def set_DeviceID(self, val):
        """
            Sets the "DeviceID" variable.
        """
        self.proxy_set_variable_value("DeviceID", val)
        return


    def get_ErrorTimeout(self):
        """
            Gets the "ErrorTimeout" variable.
        """
        rval = self.proxy_get_variable_value("ErrorTimeout")
        return rval


    def set_ErrorTimeout(self, val):
        """
            Sets the "ErrorTimeout" variable.
        """
        self.proxy_set_variable_value("ErrorTimeout", val)
        return


    def get_FailureCode(self):
        """
            Gets the "FailureCode" variable.
        """
        rval = self.proxy_get_variable_value("FailureCode")
        return rval


    def set_FailureCode(self, val):
        """
            Sets the "FailureCode" variable.
        """
        self.proxy_set_variable_value("FailureCode", val)
        return


    def get_HeightLimit(self):
        """
            Gets the "HeightLimit" variable.
        """
        rval = self.proxy_get_variable_value("HeightLimit")
        return rval


    def set_HeightLimit(self, val):
        """
            Sets the "HeightLimit" variable.
        """
        self.proxy_set_variable_value("HeightLimit", val)
        return


    def get_ImageFormat(self):
        """
            Gets the "ImageFormat" variable.
        """
        rval = self.proxy_get_variable_value("ImageFormat")
        return rval


    def set_ImageFormat(self, val):
        """
            Sets the "ImageFormat" variable.
        """
        self.proxy_set_variable_value("ImageFormat", val)
        return


    def get_ImageType(self):
        """
            Gets the "ImageType" variable.
        """
        rval = self.proxy_get_variable_value("ImageType")
        return rval


    def set_ImageType(self, val):
        """
            Sets the "ImageType" variable.
        """
        self.proxy_set_variable_value("ImageType", val)
        return


    def get_JobID(self):
        """
            Gets the "JobID" variable.
        """
        rval = self.proxy_get_variable_value("JobID")
        return rval


    def set_JobID(self, val):
        """
            Sets the "JobID" variable.
        """
        self.proxy_set_variable_value("JobID", val)
        return


    def get_JobName(self):
        """
            Gets the "JobName" variable.
        """
        rval = self.proxy_get_variable_value("JobName")
        return rval


    def set_JobName(self, val):
        """
            Sets the "JobName" variable.
        """
        self.proxy_set_variable_value("JobName", val)
        return


    def get_RegistrationID(self):
        """
            Gets the "RegistrationID" variable.
        """
        rval = self.proxy_get_variable_value("RegistrationID")
        return rval


    def set_RegistrationID(self, val):
        """
            Sets the "RegistrationID" variable.
        """
        self.proxy_set_variable_value("RegistrationID", val)
        return


    def get_Resolution(self):
        """
            Gets the "Resolution" variable.
        """
        rval = self.proxy_get_variable_value("Resolution")
        return rval


    def set_Resolution(self, val):
        """
            Sets the "Resolution" variable.
        """
        self.proxy_set_variable_value("Resolution", val)
        return


    def get_ScanLength(self):
        """
            Gets the "ScanLength" variable.
        """
        rval = self.proxy_get_variable_value("ScanLength")
        return rval


    def set_ScanLength(self, val):
        """
            Sets the "ScanLength" variable.
        """
        self.proxy_set_variable_value("ScanLength", val)
        return


    def get_SideCount(self):
        """
            Gets the "SideCount" variable.
        """
        rval = self.proxy_get_variable_value("SideCount")
        return rval


    def set_SideCount(self, val):
        """
            Sets the "SideCount" variable.
        """
        self.proxy_set_variable_value("SideCount", val)
        return


    def get_SideNumber(self):
        """
            Gets the "SideNumber" variable.
        """
        rval = self.proxy_get_variable_value("SideNumber")
        return rval


    def set_SideNumber(self, val):
        """
            Sets the "SideNumber" variable.
        """
        self.proxy_set_variable_value("SideNumber", val)
        return


    def get_State(self):
        """
            Gets the "State" variable.
        """
        rval = self.proxy_get_variable_value("State")
        return rval


    def set_State(self, val):
        """
            Sets the "State" variable.
        """
        self.proxy_set_variable_value("State", val)
        return


    def get_StateReason(self):
        """
            Gets the "StateReason" variable.
        """
        rval = self.proxy_get_variable_value("StateReason")
        return rval


    def set_StateReason(self, val):
        """
            Sets the "StateReason" variable.
        """
        self.proxy_set_variable_value("StateReason", val)
        return


    def get_Timeout(self):
        """
            Gets the "Timeout" variable.
        """
        rval = self.proxy_get_variable_value("Timeout")
        return rval


    def set_Timeout(self, val):
        """
            Sets the "Timeout" variable.
        """
        self.proxy_set_variable_value("Timeout", val)
        return


    def get_UseFeeder(self):
        """
            Gets the "UseFeeder" variable.
        """
        rval = self.proxy_get_variable_value("UseFeeder")
        return rval


    def set_UseFeeder(self, val):
        """
            Sets the "UseFeeder" variable.
        """
        self.proxy_set_variable_value("UseFeeder", val)
        return


    def get_WidthLimit(self):
        """
            Gets the "WidthLimit" variable.
        """
        rval = self.proxy_get_variable_value("WidthLimit")
        return rval


    def set_WidthLimit(self, val):
        """
            Sets the "WidthLimit" variable.
        """
        self.proxy_set_variable_value("WidthLimit", val)
        return


    def get_XValueLimit(self):
        """
            Gets the "XValueLimit" variable.
        """
        rval = self.proxy_get_variable_value("XValueLimit")
        return rval


    def set_XValueLimit(self, val):
        """
            Sets the "XValueLimit" variable.
        """
        self.proxy_set_variable_value("XValueLimit", val)
        return


    def get_YValueLimit(self):
        """
            Gets the "YValueLimit" variable.
        """
        rval = self.proxy_get_variable_value("YValueLimit")
        return rval


    def set_YValueLimit(self, val):
        """
            Sets the "YValueLimit" variable.
        """
        self.proxy_set_variable_value("YValueLimit", val)
        return


    def action_GetConfiguration(self):
        """
            Calls the GetConfiguration action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetConfiguration", arguments=arguments)

        (JobNameOut, ResolutionOut, ImageXOffsetOut, ImageYOffsetOut, ImageWidthOut, ImageHeightOut, ImageFormatOut, CompressionFactorOut, ImageTypeOut, ColorTypeOut, BitDepthOut, ColorSpaceOut, BaseNameOut, AppendSideNumberOut, TimeoutOut,) = out_params

        return JobNameOut, ResolutionOut, ImageXOffsetOut, ImageYOffsetOut, ImageWidthOut, ImageHeightOut, ImageFormatOut, CompressionFactorOut, ImageTypeOut, ColorTypeOut, BitDepthOut, ColorSpaceOut, BaseNameOut, AppendSideNumberOut, TimeoutOut


    def action_GetSideInformation(self):
        """
            Calls the GetSideInformation action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetSideInformation", arguments=arguments)

        (SideNumberOut, SideCountOut, ScanLengthOut,) = out_params

        return SideNumberOut, SideCountOut, ScanLengthOut


    def action_GetState(self):
        """
            Calls the GetState action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetState", arguments=arguments)

        (StateOut, StateReasonOut, FailureCodeOut,) = out_params

        return StateOut, StateReasonOut, FailureCodeOut


    def action_StartScan(self, RegistrationIDIn, UseFeederIn, SideCountIn, JobNameIn, ResolutionIn, ImageXOffsetIn, ImageYOffsetIn, ImageWidthIn, ImageHeightIn, ImageFormatIn, CompressionFactorIn, ImageTypeIn, ColorTypeIn, BitDepthIn, ColorSpaceIn, BaseNameIn, AppendSideNumberIn, TimeoutIn):
        """
            Calls the StartScan action.
        """
        arguments = {
            "RegistrationIDIn": RegistrationIDIn,
            "UseFeederIn": UseFeederIn,
            "SideCountIn": SideCountIn,
            "JobNameIn": JobNameIn,
            "ResolutionIn": ResolutionIn,
            "ImageXOffsetIn": ImageXOffsetIn,
            "ImageYOffsetIn": ImageYOffsetIn,
            "ImageWidthIn": ImageWidthIn,
            "ImageHeightIn": ImageHeightIn,
            "ImageFormatIn": ImageFormatIn,
            "CompressionFactorIn": CompressionFactorIn,
            "ImageTypeIn": ImageTypeIn,
            "ColorTypeIn": ColorTypeIn,
            "BitDepthIn": BitDepthIn,
            "ColorSpaceIn": ColorSpaceIn,
            "BaseNameIn": BaseNameIn,
            "AppendSideNumberIn": AppendSideNumberIn,
            "TimeoutIn": TimeoutIn,
        }

        out_params = self.proxy_call_action("StartScan", arguments=arguments)

        (ActualTimeoutOut, JobIDOut, ActualWidthOut, ActualHeightOut,) = out_params

        return ActualTimeoutOut, JobIDOut, ActualWidthOut, ActualHeightOut

