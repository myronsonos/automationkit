"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class ContentDirectory2ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'ContentDirectory2' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:ContentDirectory:2'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:ContentDirectory'


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


    def action_GetFeatureList(self):
        """
            Calls the GetFeatureList action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetFeatureList", arguments=arguments)

        (FeatureList,) = out_params

        return FeatureList


    def action_GetSearchCapabilities(self):
        """
            Calls the GetSearchCapabilities action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetSearchCapabilities", arguments=arguments)

        (SearchCaps,) = out_params

        return SearchCaps


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

