"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class ContentDirectory4ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'ContentDirectory4' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:ContentDirectory:4'
    SERVICE_ID = 'urn:schemas-upnp-org:service:ContentDirectory'


    def get_ContainerUpdateIDs(self):
        """
            Gets the "ContainerUpdateIDs" variable.
        """
        rval = self.proxy_get_variable_value("ContainerUpdateIDs")
        return rval


    def set_ContainerUpdateIDs(self, val):
        """
            Sets the "ContainerUpdateIDs" variable.
        """
        self.proxy_set_variable_value("ContainerUpdateIDs", val)
        return


    def get_DeviceMode(self):
        """
            Gets the "DeviceMode" variable.
        """
        rval = self.proxy_get_variable_value("DeviceMode")
        return rval


    def set_DeviceMode(self, val):
        """
            Sets the "DeviceMode" variable.
        """
        self.proxy_set_variable_value("DeviceMode", val)
        return


    def get_DeviceModeStatus(self):
        """
            Gets the "DeviceModeStatus" variable.
        """
        rval = self.proxy_get_variable_value("DeviceModeStatus")
        return rval


    def set_DeviceModeStatus(self, val):
        """
            Sets the "DeviceModeStatus" variable.
        """
        self.proxy_set_variable_value("DeviceModeStatus", val)
        return


    def get_FeatureList(self):
        """
            Gets the "FeatureList" variable.
        """
        rval = self.proxy_get_variable_value("FeatureList")
        return rval


    def set_FeatureList(self, val):
        """
            Sets the "FeatureList" variable.
        """
        self.proxy_set_variable_value("FeatureList", val)
        return


    def get_LastChange(self):
        """
            Gets the "LastChange" variable.
        """
        rval = self.proxy_get_variable_value("LastChange")
        return rval


    def set_LastChange(self, val):
        """
            Sets the "LastChange" variable.
        """
        self.proxy_set_variable_value("LastChange", val)
        return


    def get_PermissionsInfo(self):
        """
            Gets the "PermissionsInfo" variable.
        """
        rval = self.proxy_get_variable_value("PermissionsInfo")
        return rval


    def set_PermissionsInfo(self, val):
        """
            Sets the "PermissionsInfo" variable.
        """
        self.proxy_set_variable_value("PermissionsInfo", val)
        return


    def get_SearchCapabilities(self):
        """
            Gets the "SearchCapabilities" variable.
        """
        rval = self.proxy_get_variable_value("SearchCapabilities")
        return rval


    def set_SearchCapabilities(self, val):
        """
            Sets the "SearchCapabilities" variable.
        """
        self.proxy_set_variable_value("SearchCapabilities", val)
        return


    def get_ServiceResetToken(self):
        """
            Gets the "ServiceResetToken" variable.
        """
        rval = self.proxy_get_variable_value("ServiceResetToken")
        return rval


    def set_ServiceResetToken(self, val):
        """
            Sets the "ServiceResetToken" variable.
        """
        self.proxy_set_variable_value("ServiceResetToken", val)
        return


    def get_SortCapabilities(self):
        """
            Gets the "SortCapabilities" variable.
        """
        rval = self.proxy_get_variable_value("SortCapabilities")
        return rval


    def set_SortCapabilities(self, val):
        """
            Sets the "SortCapabilities" variable.
        """
        self.proxy_set_variable_value("SortCapabilities", val)
        return


    def get_SortExtensionCapabilities(self):
        """
            Gets the "SortExtensionCapabilities" variable.
        """
        rval = self.proxy_get_variable_value("SortExtensionCapabilities")
        return rval


    def set_SortExtensionCapabilities(self, val):
        """
            Sets the "SortExtensionCapabilities" variable.
        """
        self.proxy_set_variable_value("SortExtensionCapabilities", val)
        return


    def get_SystemUpdateID(self):
        """
            Gets the "SystemUpdateID" variable.
        """
        rval = self.proxy_get_variable_value("SystemUpdateID")
        return rval


    def set_SystemUpdateID(self, val):
        """
            Sets the "SystemUpdateID" variable.
        """
        self.proxy_set_variable_value("SystemUpdateID", val)
        return


    def get_TransferIDs(self):
        """
            Gets the "TransferIDs" variable.
        """
        rval = self.proxy_get_variable_value("TransferIDs")
        return rval


    def set_TransferIDs(self, val):
        """
            Sets the "TransferIDs" variable.
        """
        self.proxy_set_variable_value("TransferIDs", val)
        return


    def get_TransformStatus(self):
        """
            Gets the "TransformStatus" variable.
        """
        rval = self.proxy_get_variable_value("TransformStatus")
        return rval


    def set_TransformStatus(self, val):
        """
            Sets the "TransformStatus" variable.
        """
        self.proxy_set_variable_value("TransformStatus", val)
        return


    def action_Browse(self, ObjectID, BrowseFlag, Filter, StartingIndex, RequestedCount, SortCriteria):
        """
            Calls the Browse action.
        """
        arguments = {
            "ObjectID": ObjectID,
            "BrowseFlag": BrowseFlag,
            "Filter": Filter,
            "StartingIndex": StartingIndex,
            "RequestedCount": RequestedCount,
            "SortCriteria": SortCriteria,
        }

        out_params = self.proxy_call_action("Browse", arguments=arguments)

        (Result, NumberReturned, TotalMatches, UpdateID,) = out_params

        return Result, NumberReturned, TotalMatches, UpdateID


    def action_CancelDeviceMode(self, DeviceModeID):
        """
            Calls the CancelDeviceMode action.
        """
        arguments = {
            "DeviceModeID": DeviceModeID,
        }

        out_params = self.proxy_call_action("CancelDeviceMode", arguments=arguments)

        (result,) = out_params

        return result


    def action_CancelTransformTask(self, TransformTaskID):
        """
            Calls the CancelTransformTask action.
        """
        arguments = {
            "TransformTaskID": TransformTaskID,
        }

        out_params = self.proxy_call_action("CancelTransformTask", arguments=arguments)

        (result,) = out_params

        return result


    def action_CreateObject(self, ContainerID, Elements):
        """
            Calls the CreateObject action.
        """
        arguments = {
            "ContainerID": ContainerID,
            "Elements": Elements,
        }

        out_params = self.proxy_call_action("CreateObject", arguments=arguments)

        (ObjectID, Result,) = out_params

        return ObjectID, Result


    def action_CreateReference(self, ContainerID, ObjectID):
        """
            Calls the CreateReference action.
        """
        arguments = {
            "ContainerID": ContainerID,
            "ObjectID": ObjectID,
        }

        out_params = self.proxy_call_action("CreateReference", arguments=arguments)

        (NewID,) = out_params

        return NewID


    def action_DeleteResource(self, ResourceURI):
        """
            Calls the DeleteResource action.
        """
        arguments = {
            "ResourceURI": ResourceURI,
        }

        out_params = self.proxy_call_action("DeleteResource", arguments=arguments)

        (result,) = out_params

        return result


    def action_DestroyObject(self, ObjectID):
        """
            Calls the DestroyObject action.
        """
        arguments = {
            "ObjectID": ObjectID,
        }

        out_params = self.proxy_call_action("DestroyObject", arguments=arguments)

        (result,) = out_params

        return result


    def action_EvaluateTransforms(self, TransformResourceDesc, TransformSettings):
        """
            Calls the EvaluateTransforms action.
        """
        arguments = {
            "TransformResourceDesc": TransformResourceDesc,
            "TransformSettings": TransformSettings,
        }

        out_params = self.proxy_call_action("EvaluateTransforms", arguments=arguments)

        (EvaluationResult,) = out_params

        return EvaluationResult


    def action_ExportResource(self, SourceURI, DestinationURI):
        """
            Calls the ExportResource action.
        """
        arguments = {
            "SourceURI": SourceURI,
            "DestinationURI": DestinationURI,
        }

        out_params = self.proxy_call_action("ExportResource", arguments=arguments)

        (TransferID,) = out_params

        return TransferID


    def action_ExtendDeviceMode(self, DeviceModeID, DeviceModeRequest):
        """
            Calls the ExtendDeviceMode action.
        """
        arguments = {
            "DeviceModeID": DeviceModeID,
            "DeviceModeRequest": DeviceModeRequest,
        }

        out_params = self.proxy_call_action("ExtendDeviceMode", arguments=arguments)

        (DeviceModeStatus,) = out_params

        return DeviceModeStatus


    def action_FreeFormQuery(self, ContainerID, CDSView, QueryRequest):
        """
            Calls the FreeFormQuery action.
        """
        arguments = {
            "ContainerID": ContainerID,
            "CDSView": CDSView,
            "QueryRequest": QueryRequest,
        }

        out_params = self.proxy_call_action("FreeFormQuery", arguments=arguments)

        (QueryResult, UpdateID,) = out_params

        return QueryResult, UpdateID


    def action_GetAllAvailableTransforms(self):
        """
            Calls the GetAllAvailableTransforms action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetAllAvailableTransforms", arguments=arguments)

        (AllAvailableTransforms,) = out_params

        return AllAvailableTransforms


    def action_GetAllowedTransforms(self, TransformResourceObjectDesc):
        """
            Calls the GetAllowedTransforms action.
        """
        arguments = {
            "TransformResourceObjectDesc": TransformResourceObjectDesc,
        }

        out_params = self.proxy_call_action("GetAllowedTransforms", arguments=arguments)

        (AllowedTransforms,) = out_params

        return AllowedTransforms


    def action_GetCurrentTransformStatusList(self):
        """
            Calls the GetCurrentTransformStatusList action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetCurrentTransformStatusList", arguments=arguments)

        (TransformStatus,) = out_params

        return TransformStatus


    def action_GetDeviceMode(self):
        """
            Calls the GetDeviceMode action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDeviceMode", arguments=arguments)

        (DeviceMode,) = out_params

        return DeviceMode


    def action_GetDeviceModeStatus(self):
        """
            Calls the GetDeviceModeStatus action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDeviceModeStatus", arguments=arguments)

        (DeviceModeStatus,) = out_params

        return DeviceModeStatus


    def action_GetFeatureList(self):
        """
            Calls the GetFeatureList action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetFeatureList", arguments=arguments)

        (FeatureList,) = out_params

        return FeatureList


    def action_GetFreeFormQueryCapabilities(self):
        """
            Calls the GetFreeFormQueryCapabilities action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetFreeFormQueryCapabilities", arguments=arguments)

        (FFQCapabilities,) = out_params

        return FFQCapabilities


    def action_GetPermissionsInfo(self):
        """
            Calls the GetPermissionsInfo action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetPermissionsInfo", arguments=arguments)

        (PermissionsInfo,) = out_params

        return PermissionsInfo


    def action_GetSearchCapabilities(self):
        """
            Calls the GetSearchCapabilities action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetSearchCapabilities", arguments=arguments)

        (SearchCaps,) = out_params

        return SearchCaps


    def action_GetServiceResetToken(self):
        """
            Calls the GetServiceResetToken action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetServiceResetToken", arguments=arguments)

        (ResetToken,) = out_params

        return ResetToken


    def action_GetSortCapabilities(self):
        """
            Calls the GetSortCapabilities action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetSortCapabilities", arguments=arguments)

        (SortCaps,) = out_params

        return SortCaps


    def action_GetSortExtensionCapabilities(self):
        """
            Calls the GetSortExtensionCapabilities action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetSortExtensionCapabilities", arguments=arguments)

        (SortExtensionCaps,) = out_params

        return SortExtensionCaps


    def action_GetSystemUpdateID(self):
        """
            Calls the GetSystemUpdateID action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetSystemUpdateID", arguments=arguments)

        (Id,) = out_params

        return Id


    def action_GetTransferProgress(self, TransferID):
        """
            Calls the GetTransferProgress action.
        """
        arguments = {
            "TransferID": TransferID,
        }

        out_params = self.proxy_call_action("GetTransferProgress", arguments=arguments)

        (TransferStatus, TransferLength, TransferTotal,) = out_params

        return TransferStatus, TransferLength, TransferTotal


    def action_GetTransformTaskResult(self, TransformTaskID, TransformTaskResultFilter):
        """
            Calls the GetTransformTaskResult action.
        """
        arguments = {
            "TransformTaskID": TransformTaskID,
            "TransformTaskResultFilter": TransformTaskResultFilter,
        }

        out_params = self.proxy_call_action("GetTransformTaskResult", arguments=arguments)

        (TransformTaskResult,) = out_params

        return TransformTaskResult


    def action_GetTransforms(self, TransformTaskID):
        """
            Calls the GetTransforms action.
        """
        arguments = {
            "TransformTaskID": TransformTaskID,
        }

        out_params = self.proxy_call_action("GetTransforms", arguments=arguments)

        (CurrentTransformSettings,) = out_params

        return CurrentTransformSettings


    def action_ImportResource(self, SourceURI, DestinationURI):
        """
            Calls the ImportResource action.
        """
        arguments = {
            "SourceURI": SourceURI,
            "DestinationURI": DestinationURI,
        }

        out_params = self.proxy_call_action("ImportResource", arguments=arguments)

        (TransferID,) = out_params

        return TransferID


    def action_MoveObject(self, ObjectID, NewParentID):
        """
            Calls the MoveObject action.
        """
        arguments = {
            "ObjectID": ObjectID,
            "NewParentID": NewParentID,
        }

        out_params = self.proxy_call_action("MoveObject", arguments=arguments)

        (NewObjectID,) = out_params

        return NewObjectID


    def action_PauseTransformTask(self, TransformTaskID):
        """
            Calls the PauseTransformTask action.
        """
        arguments = {
            "TransformTaskID": TransformTaskID,
        }

        out_params = self.proxy_call_action("PauseTransformTask", arguments=arguments)

        (result,) = out_params

        return result


    def action_RequestDeviceMode(self, CPID, DeviceModeRequest):
        """
            Calls the RequestDeviceMode action.
        """
        arguments = {
            "CPID": CPID,
            "DeviceModeRequest": DeviceModeRequest,
        }

        out_params = self.proxy_call_action("RequestDeviceMode", arguments=arguments)

        (DeviceModeID, DeviceModeStatus,) = out_params

        return DeviceModeID, DeviceModeStatus


    def action_ResumeTransformTask(self, TransformTaskID):
        """
            Calls the ResumeTransformTask action.
        """
        arguments = {
            "TransformTaskID": TransformTaskID,
        }

        out_params = self.proxy_call_action("ResumeTransformTask", arguments=arguments)

        (result,) = out_params

        return result


    def action_RollbackTransformTask(self, TransformTaskID):
        """
            Calls the RollbackTransformTask action.
        """
        arguments = {
            "TransformTaskID": TransformTaskID,
        }

        out_params = self.proxy_call_action("RollbackTransformTask", arguments=arguments)

        (result,) = out_params

        return result


    def action_Search(self, ContainerID, SearchCriteria, Filter, StartingIndex, RequestedCount, SortCriteria):
        """
            Calls the Search action.
        """
        arguments = {
            "ContainerID": ContainerID,
            "SearchCriteria": SearchCriteria,
            "Filter": Filter,
            "StartingIndex": StartingIndex,
            "RequestedCount": RequestedCount,
            "SortCriteria": SortCriteria,
        }

        out_params = self.proxy_call_action("Search", arguments=arguments)

        (Result, NumberReturned, TotalMatches, UpdateID,) = out_params

        return Result, NumberReturned, TotalMatches, UpdateID


    def action_StartTransformTask(self, TransformResourceDesc, TransformSettings, TransformOverwrite, TransformRollback):
        """
            Calls the StartTransformTask action.
        """
        arguments = {
            "TransformResourceDesc": TransformResourceDesc,
            "TransformSettings": TransformSettings,
            "TransformOverwrite": TransformOverwrite,
            "TransformRollback": TransformRollback,
        }

        out_params = self.proxy_call_action("StartTransformTask", arguments=arguments)

        (TransformTaskID,) = out_params

        return TransformTaskID


    def action_StopTransferResource(self, TransferID):
        """
            Calls the StopTransferResource action.
        """
        arguments = {
            "TransferID": TransferID,
        }

        out_params = self.proxy_call_action("StopTransferResource", arguments=arguments)

        (result,) = out_params

        return result


    def action_UpdateObject(self, ObjectID, CurrentTagValue, NewTagValue):
        """
            Calls the UpdateObject action.
        """
        arguments = {
            "ObjectID": ObjectID,
            "CurrentTagValue": CurrentTagValue,
            "NewTagValue": NewTagValue,
        }

        out_params = self.proxy_call_action("UpdateObject", arguments=arguments)

        (result,) = out_params

        return result

