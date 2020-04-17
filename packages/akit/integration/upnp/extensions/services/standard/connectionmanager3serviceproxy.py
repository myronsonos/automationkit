"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class ConnectionManager3ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'ConnectionManager3' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:ConnectionManager:3'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:ConnectionManager'


    def get_ClockUpdateID(self):
        """
            Gets the "ClockUpdateID" variable.
        """
        rval = self.proxy_get_variable_value("ClockUpdateID")
        return rval


    def set_ClockUpdateID(self, val):
        """
            Sets the "ClockUpdateID" variable.
        """
        self.proxy_set_variable_value("ClockUpdateID", val)
        return


    def get_CurrentConnectionIDs(self):
        """
            Gets the "CurrentConnectionIDs" variable.
        """
        rval = self.proxy_get_variable_value("CurrentConnectionIDs")
        return rval


    def set_CurrentConnectionIDs(self, val):
        """
            Sets the "CurrentConnectionIDs" variable.
        """
        self.proxy_set_variable_value("CurrentConnectionIDs", val)
        return


    def get_DeviceClockInfoUpdates(self):
        """
            Gets the "DeviceClockInfoUpdates" variable.
        """
        rval = self.proxy_get_variable_value("DeviceClockInfoUpdates")
        return rval


    def set_DeviceClockInfoUpdates(self, val):
        """
            Sets the "DeviceClockInfoUpdates" variable.
        """
        self.proxy_set_variable_value("DeviceClockInfoUpdates", val)
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


    def get_SinkProtocolInfo(self):
        """
            Gets the "SinkProtocolInfo" variable.
        """
        rval = self.proxy_get_variable_value("SinkProtocolInfo")
        return rval


    def set_SinkProtocolInfo(self, val):
        """
            Sets the "SinkProtocolInfo" variable.
        """
        self.proxy_set_variable_value("SinkProtocolInfo", val)
        return


    def get_SourceProtocolInfo(self):
        """
            Gets the "SourceProtocolInfo" variable.
        """
        rval = self.proxy_get_variable_value("SourceProtocolInfo")
        return rval


    def set_SourceProtocolInfo(self, val):
        """
            Sets the "SourceProtocolInfo" variable.
        """
        self.proxy_set_variable_value("SourceProtocolInfo", val)
        return


    def action_ConnectionComplete(self, ConnectionID):
        """
            Calls the ConnectionComplete action.
        """
        arguments = {
            "ConnectionID": ConnectionID,
        }

        out_params = self.proxy_call_action("ConnectionComplete", arguments=arguments)

        (result,) = out_params

        return result


    def action_GetCurrentConnectionIDs(self):
        """
            Calls the GetCurrentConnectionIDs action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetCurrentConnectionIDs", arguments=arguments)

        (ConnectionIDs,) = out_params

        return ConnectionIDs


    def action_GetCurrentConnectionInfo(self, ConnectionID):
        """
            Calls the GetCurrentConnectionInfo action.
        """
        arguments = {
            "ConnectionID": ConnectionID,
        }

        out_params = self.proxy_call_action("GetCurrentConnectionInfo", arguments=arguments)

        (RcsID, AVTransportID, ProtocolInfo, PeerConnectionManager, PeerConnectionID, Direction, Status,) = out_params

        return RcsID, AVTransportID, ProtocolInfo, PeerConnectionManager, PeerConnectionID, Direction, Status


    def action_GetFeatureList(self):
        """
            Calls the GetFeatureList action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetFeatureList", arguments=arguments)

        (FeatureList,) = out_params

        return FeatureList


    def action_GetProtocolInfo(self):
        """
            Calls the GetProtocolInfo action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetProtocolInfo", arguments=arguments)

        (Source, Sink,) = out_params

        return Source, Sink


    def action_GetRendererItemInfo(self, ItemInfoFilter, ItemMetadataList):
        """
            Calls the GetRendererItemInfo action.
        """
        arguments = {
            "ItemInfoFilter": ItemInfoFilter,
            "ItemMetadataList": ItemMetadataList,
        }

        out_params = self.proxy_call_action("GetRendererItemInfo", arguments=arguments)

        (ItemRenderingInfoList,) = out_params

        return ItemRenderingInfoList


    def action_PrepareForConnection(self, RemoteProtocolInfo, PeerConnectionManager, PeerConnectionID, Direction):
        """
            Calls the PrepareForConnection action.
        """
        arguments = {
            "RemoteProtocolInfo": RemoteProtocolInfo,
            "PeerConnectionManager": PeerConnectionManager,
            "PeerConnectionID": PeerConnectionID,
            "Direction": Direction,
        }

        out_params = self.proxy_call_action("PrepareForConnection", arguments=arguments)

        (ConnectionID, AVTransportID, RcsID,) = out_params

        return ConnectionID, AVTransportID, RcsID

