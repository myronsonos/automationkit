"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class PrintBasic1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'PrintBasic1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:PrintBasic:1'


    def action_CancelJob(self, JobId, extract_returns=True):
        """
            Calls the CancelJob action.

            :returns: "result"
        """
        arguments = {
            "JobId": JobId,
        }

        out_params = self.proxy_call_action("CancelJob", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_CreateJob(self, JobName, JobOriginatingUserName, DocumentFormat, Copies, Sides, NumberUp, OrientationRequested, MediaSize, MediaType, PrintQuality, extract_returns=True):
        """
            Calls the CreateJob action.

            :returns: "JobId", "DataSink"
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

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("JobId", "DataSink",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetJobAttributes(self, JobId, extract_returns=True):
        """
            Calls the GetJobAttributes action.

            :returns: "JobName", "JobOriginatingUserName", "JobMediaSheetsCompleted"
        """
        arguments = {
            "JobId": JobId,
        }

        out_params = self.proxy_call_action("GetJobAttributes", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("JobName", "JobOriginatingUserName", "JobMediaSheetsCompleted",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetPrinterAttributes(self, extract_returns=True):
        """
            Calls the GetPrinterAttributes action.

            :returns: "PrinterState", "PrinterStateReasons", "JobIdList", "JobId"
        """
        arguments = { }

        out_params = self.proxy_call_action("GetPrinterAttributes", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("PrinterState", "PrinterStateReasons", "JobIdList", "JobId",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

