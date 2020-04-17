"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class PrintEnhancedServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'PrintEnhanced' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:PrintEnhanced:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:PrintEnhanced'


    def get_CharRepSupported(self):
        """
            Gets the "CharRepSupported" variable.
        """
        rval = self.proxy_get_variable_value("CharRepSupported")
        return rval


    def set_CharRepSupported(self, val):
        """
            Sets the "CharRepSupported" variable.
        """
        self.proxy_set_variable_value("CharRepSupported", val)
        return


    def get_ColorSupported(self):
        """
            Gets the "ColorSupported" variable.
        """
        rval = self.proxy_get_variable_value("ColorSupported")
        return rval


    def set_ColorSupported(self, val):
        """
            Sets the "ColorSupported" variable.
        """
        self.proxy_set_variable_value("ColorSupported", val)
        return


    def get_ContentCompleteList(self):
        """
            Gets the "ContentCompleteList" variable.
        """
        rval = self.proxy_get_variable_value("ContentCompleteList")
        return rval


    def set_ContentCompleteList(self, val):
        """
            Sets the "ContentCompleteList" variable.
        """
        self.proxy_set_variable_value("ContentCompleteList", val)
        return


    def get_Copies(self):
        """
            Gets the "Copies" variable.
        """
        rval = self.proxy_get_variable_value("Copies")
        return rval


    def set_Copies(self, val):
        """
            Sets the "Copies" variable.
        """
        self.proxy_set_variable_value("Copies", val)
        return


    def get_CriticalAttributesSupported(self):
        """
            Gets the "CriticalAttributesSupported" variable.
        """
        rval = self.proxy_get_variable_value("CriticalAttributesSupported")
        return rval


    def set_CriticalAttributesSupported(self, val):
        """
            Sets the "CriticalAttributesSupported" variable.
        """
        self.proxy_set_variable_value("CriticalAttributesSupported", val)
        return


    def get_DataSink(self):
        """
            Gets the "DataSink" variable.
        """
        rval = self.proxy_get_variable_value("DataSink")
        return rval


    def set_DataSink(self, val):
        """
            Sets the "DataSink" variable.
        """
        self.proxy_set_variable_value("DataSink", val)
        return


    def get_DeviceId(self):
        """
            Gets the "DeviceId" variable.
        """
        rval = self.proxy_get_variable_value("DeviceId")
        return rval


    def set_DeviceId(self, val):
        """
            Sets the "DeviceId" variable.
        """
        self.proxy_set_variable_value("DeviceId", val)
        return


    def get_DocumentFormat(self):
        """
            Gets the "DocumentFormat" variable.
        """
        rval = self.proxy_get_variable_value("DocumentFormat")
        return rval


    def set_DocumentFormat(self, val):
        """
            Sets the "DocumentFormat" variable.
        """
        self.proxy_set_variable_value("DocumentFormat", val)
        return


    def get_DocumentUTF16Supported(self):
        """
            Gets the "DocumentUTF16Supported" variable.
        """
        rval = self.proxy_get_variable_value("DocumentUTF16Supported")
        return rval


    def set_DocumentUTF16Supported(self, val):
        """
            Sets the "DocumentUTF16Supported" variable.
        """
        self.proxy_set_variable_value("DocumentUTF16Supported", val)
        return


    def get_FullBleedSupported(self):
        """
            Gets the "FullBleedSupported" variable.
        """
        rval = self.proxy_get_variable_value("FullBleedSupported")
        return rval


    def set_FullBleedSupported(self, val):
        """
            Sets the "FullBleedSupported" variable.
        """
        self.proxy_set_variable_value("FullBleedSupported", val)
        return


    def get_InternetConnectState(self):
        """
            Gets the "InternetConnectState" variable.
        """
        rval = self.proxy_get_variable_value("InternetConnectState")
        return rval


    def set_InternetConnectState(self, val):
        """
            Sets the "InternetConnectState" variable.
        """
        self.proxy_set_variable_value("InternetConnectState", val)
        return


    def get_JobAbortState(self):
        """
            Gets the "JobAbortState" variable.
        """
        rval = self.proxy_get_variable_value("JobAbortState")
        return rval


    def set_JobAbortState(self, val):
        """
            Sets the "JobAbortState" variable.
        """
        self.proxy_set_variable_value("JobAbortState", val)
        return


    def get_JobEndState(self):
        """
            Gets the "JobEndState" variable.
        """
        rval = self.proxy_get_variable_value("JobEndState")
        return rval


    def set_JobEndState(self, val):
        """
            Sets the "JobEndState" variable.
        """
        self.proxy_set_variable_value("JobEndState", val)
        return


    def get_JobId(self):
        """
            Gets the "JobId" variable.
        """
        rval = self.proxy_get_variable_value("JobId")
        return rval


    def set_JobId(self, val):
        """
            Sets the "JobId" variable.
        """
        self.proxy_set_variable_value("JobId", val)
        return


    def get_JobIdList(self):
        """
            Gets the "JobIdList" variable.
        """
        rval = self.proxy_get_variable_value("JobIdList")
        return rval


    def set_JobIdList(self, val):
        """
            Sets the "JobIdList" variable.
        """
        self.proxy_set_variable_value("JobIdList", val)
        return


    def get_JobMediaSheetsCompleted(self):
        """
            Gets the "JobMediaSheetsCompleted" variable.
        """
        rval = self.proxy_get_variable_value("JobMediaSheetsCompleted")
        return rval


    def set_JobMediaSheetsCompleted(self, val):
        """
            Sets the "JobMediaSheetsCompleted" variable.
        """
        self.proxy_set_variable_value("JobMediaSheetsCompleted", val)
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


    def get_JobOriginatingUserName(self):
        """
            Gets the "JobOriginatingUserName" variable.
        """
        rval = self.proxy_get_variable_value("JobOriginatingUserName")
        return rval


    def set_JobOriginatingUserName(self, val):
        """
            Sets the "JobOriginatingUserName" variable.
        """
        self.proxy_set_variable_value("JobOriginatingUserName", val)
        return


    def get_MediaSize(self):
        """
            Gets the "MediaSize" variable.
        """
        rval = self.proxy_get_variable_value("MediaSize")
        return rval


    def set_MediaSize(self, val):
        """
            Sets the "MediaSize" variable.
        """
        self.proxy_set_variable_value("MediaSize", val)
        return


    def get_MediaType(self):
        """
            Gets the "MediaType" variable.
        """
        rval = self.proxy_get_variable_value("MediaType")
        return rval


    def set_MediaType(self, val):
        """
            Sets the "MediaType" variable.
        """
        self.proxy_set_variable_value("MediaType", val)
        return


    def get_NumberUp(self):
        """
            Gets the "NumberUp" variable.
        """
        rval = self.proxy_get_variable_value("NumberUp")
        return rval


    def set_NumberUp(self, val):
        """
            Sets the "NumberUp" variable.
        """
        self.proxy_set_variable_value("NumberUp", val)
        return


    def get_OrientationRequested(self):
        """
            Gets the "OrientationRequested" variable.
        """
        rval = self.proxy_get_variable_value("OrientationRequested")
        return rval


    def set_OrientationRequested(self, val):
        """
            Sets the "OrientationRequested" variable.
        """
        self.proxy_set_variable_value("OrientationRequested", val)
        return


    def get_PageMargins(self):
        """
            Gets the "PageMargins" variable.
        """
        rval = self.proxy_get_variable_value("PageMargins")
        return rval


    def set_PageMargins(self, val):
        """
            Sets the "PageMargins" variable.
        """
        self.proxy_set_variable_value("PageMargins", val)
        return


    def get_PrintQuality(self):
        """
            Gets the "PrintQuality" variable.
        """
        rval = self.proxy_get_variable_value("PrintQuality")
        return rval


    def set_PrintQuality(self, val):
        """
            Sets the "PrintQuality" variable.
        """
        self.proxy_set_variable_value("PrintQuality", val)
        return


    def get_PrinterLocation(self):
        """
            Gets the "PrinterLocation" variable.
        """
        rval = self.proxy_get_variable_value("PrinterLocation")
        return rval


    def set_PrinterLocation(self, val):
        """
            Sets the "PrinterLocation" variable.
        """
        self.proxy_set_variable_value("PrinterLocation", val)
        return


    def get_PrinterName(self):
        """
            Gets the "PrinterName" variable.
        """
        rval = self.proxy_get_variable_value("PrinterName")
        return rval


    def set_PrinterName(self, val):
        """
            Sets the "PrinterName" variable.
        """
        self.proxy_set_variable_value("PrinterName", val)
        return


    def get_PrinterState(self):
        """
            Gets the "PrinterState" variable.
        """
        rval = self.proxy_get_variable_value("PrinterState")
        return rval


    def set_PrinterState(self, val):
        """
            Sets the "PrinterState" variable.
        """
        self.proxy_set_variable_value("PrinterState", val)
        return


    def get_PrinterStateReasons(self):
        """
            Gets the "PrinterStateReasons" variable.
        """
        rval = self.proxy_get_variable_value("PrinterStateReasons")
        return rval


    def set_PrinterStateReasons(self, val):
        """
            Sets the "PrinterStateReasons" variable.
        """
        self.proxy_set_variable_value("PrinterStateReasons", val)
        return


    def get_Sides(self):
        """
            Gets the "Sides" variable.
        """
        rval = self.proxy_get_variable_value("Sides")
        return rval


    def set_Sides(self, val):
        """
            Sets the "Sides" variable.
        """
        self.proxy_set_variable_value("Sides", val)
        return


    def get_SourceURI(self):
        """
            Gets the "SourceURI" variable.
        """
        rval = self.proxy_get_variable_value("SourceURI")
        return rval


    def set_SourceURI(self, val):
        """
            Sets the "SourceURI" variable.
        """
        self.proxy_set_variable_value("SourceURI", val)
        return


    def get_XHTMLImageSupported(self):
        """
            Gets the "XHTMLImageSupported" variable.
        """
        rval = self.proxy_get_variable_value("XHTMLImageSupported")
        return rval


    def set_XHTMLImageSupported(self, val):
        """
            Sets the "XHTMLImageSupported" variable.
        """
        self.proxy_set_variable_value("XHTMLImageSupported", val)
        return


    def action_CancelJob(self, JobId):
        """
            Calls the CancelJob action.
        """
        arguments = {
            "JobId": JobId,
        }

        out_params = self.proxy_call_action("CancelJob", arguments=arguments)

        (result,) = out_params

        return result


    def action_CreateJob(self, JobName, JobOriginatingUserName, DocumentFormat, Copies, Sides, NumberUp, OrientationRequested, MediaSize, MediaType, PrintQuality):
        """
            Calls the CreateJob action.
        """
        arguments = {
            "JobName": JobName,
            "JobOriginatingUserName": JobOriginatingUserName,
            "DocumentFormat": DocumentFormat,
            "Copies": Copies,
            "Sides": Sides,
            "NumberUp": NumberUp,
            "OrientationRequested": OrientationRequested,
            "MediaSize": MediaSize,
            "MediaType": MediaType,
            "PrintQuality": PrintQuality,
        }

        out_params = self.proxy_call_action("CreateJob", arguments=arguments)

        (JobId, DataSink,) = out_params

        return JobId, DataSink


    def action_CreateJobV2(self, JobName, JobOriginatingUserName, DocumentFormat, Copies, Sides, NumberUp, OrientationRequested, MediaSize, MediaType, PrintQuality, CriticalAttributesList):
        """
            Calls the CreateJobV2 action.
        """
        arguments = {
            "JobName": JobName,
            "JobOriginatingUserName": JobOriginatingUserName,
            "DocumentFormat": DocumentFormat,
            "Copies": Copies,
            "Sides": Sides,
            "NumberUp": NumberUp,
            "OrientationRequested": OrientationRequested,
            "MediaSize": MediaSize,
            "MediaType": MediaType,
            "PrintQuality": PrintQuality,
            "CriticalAttributesList": CriticalAttributesList,
        }

        out_params = self.proxy_call_action("CreateJobV2", arguments=arguments)

        (JobId, DataSink,) = out_params

        return JobId, DataSink


    def action_CreateURIJob(self, JobName, JobOriginatingUserName, DocumentFormat, Copies, Sides, NumberUp, OrientationRequested, MediaSize, MediaType, PrintQuality, CriticalAttributesList, SourceURI):
        """
            Calls the CreateURIJob action.
        """
        arguments = {
            "JobName": JobName,
            "JobOriginatingUserName": JobOriginatingUserName,
            "DocumentFormat": DocumentFormat,
            "Copies": Copies,
            "Sides": Sides,
            "NumberUp": NumberUp,
            "OrientationRequested": OrientationRequested,
            "MediaSize": MediaSize,
            "MediaType": MediaType,
            "PrintQuality": PrintQuality,
            "CriticalAttributesList": CriticalAttributesList,
            "SourceURI": SourceURI,
        }

        out_params = self.proxy_call_action("CreateURIJob", arguments=arguments)

        (JobId,) = out_params

        return JobId


    def action_GetJobAttributes(self, JobId):
        """
            Calls the GetJobAttributes action.
        """
        arguments = {
            "JobId": JobId,
        }

        out_params = self.proxy_call_action("GetJobAttributes", arguments=arguments)

        (JobName, JobOriginatingUserName, JobMediaSheetsCompleted,) = out_params

        return JobName, JobOriginatingUserName, JobMediaSheetsCompleted


    def action_GetMargins(self, MediaSize, MediaType):
        """
            Calls the GetMargins action.
        """
        arguments = {
            "MediaSize": MediaSize,
            "MediaType": MediaType,
        }

        out_params = self.proxy_call_action("GetMargins", arguments=arguments)

        (PageMargins, FullBleedSupported,) = out_params

        return PageMargins, FullBleedSupported


    def action_GetMediaList(self, MediaSize, MediaType):
        """
            Calls the GetMediaList action.
        """
        arguments = {
            "MediaSize": MediaSize,
            "MediaType": MediaType,
        }

        out_params = self.proxy_call_action("GetMediaList", arguments=arguments)

        (MediaList,) = out_params

        return MediaList


    def action_GetPrinterAttributes(self):
        """
            Calls the GetPrinterAttributes action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetPrinterAttributes", arguments=arguments)

        (PrinterState, PrinterStateReasons, JobIdList, JobId,) = out_params

        return PrinterState, PrinterStateReasons, JobIdList, JobId


    def action_GetPrinterAttributesV2(self):
        """
            Calls the GetPrinterAttributesV2 action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetPrinterAttributesV2", arguments=arguments)

        (PrinterState, PrinterStateReasons, JobIdList, JobId, InternetConnectState,) = out_params

        return PrinterState, PrinterStateReasons, JobIdList, JobId, InternetConnectState

