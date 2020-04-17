"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class WANIPConnection2ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'WANIPConnection2' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:WANIPConnection:2'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:WANIPConnection'


    def get_AutoDisconnectTime(self):
        """
            Gets the "AutoDisconnectTime" variable.
        """
        rval = self.proxy_get_variable_value("AutoDisconnectTime")
        return rval


    def set_AutoDisconnectTime(self, val):
        """
            Sets the "AutoDisconnectTime" variable.
        """
        self.proxy_set_variable_value("AutoDisconnectTime", val)
        return


    def get_ConnectionStatus(self):
        """
            Gets the "ConnectionStatus" variable.
        """
        rval = self.proxy_get_variable_value("ConnectionStatus")
        return rval


    def set_ConnectionStatus(self, val):
        """
            Sets the "ConnectionStatus" variable.
        """
        self.proxy_set_variable_value("ConnectionStatus", val)
        return


    def get_ConnectionType(self):
        """
            Gets the "ConnectionType" variable.
        """
        rval = self.proxy_get_variable_value("ConnectionType")
        return rval


    def set_ConnectionType(self, val):
        """
            Sets the "ConnectionType" variable.
        """
        self.proxy_set_variable_value("ConnectionType", val)
        return


    def get_ExternalIPAddress(self):
        """
            Gets the "ExternalIPAddress" variable.
        """
        rval = self.proxy_get_variable_value("ExternalIPAddress")
        return rval


    def set_ExternalIPAddress(self, val):
        """
            Sets the "ExternalIPAddress" variable.
        """
        self.proxy_set_variable_value("ExternalIPAddress", val)
        return


    def get_ExternalPort(self):
        """
            Gets the "ExternalPort" variable.
        """
        rval = self.proxy_get_variable_value("ExternalPort")
        return rval


    def set_ExternalPort(self, val):
        """
            Sets the "ExternalPort" variable.
        """
        self.proxy_set_variable_value("ExternalPort", val)
        return


    def get_IdleDisconnectTime(self):
        """
            Gets the "IdleDisconnectTime" variable.
        """
        rval = self.proxy_get_variable_value("IdleDisconnectTime")
        return rval


    def set_IdleDisconnectTime(self, val):
        """
            Sets the "IdleDisconnectTime" variable.
        """
        self.proxy_set_variable_value("IdleDisconnectTime", val)
        return


    def get_InternalClient(self):
        """
            Gets the "InternalClient" variable.
        """
        rval = self.proxy_get_variable_value("InternalClient")
        return rval


    def set_InternalClient(self, val):
        """
            Sets the "InternalClient" variable.
        """
        self.proxy_set_variable_value("InternalClient", val)
        return


    def get_InternalPort(self):
        """
            Gets the "InternalPort" variable.
        """
        rval = self.proxy_get_variable_value("InternalPort")
        return rval


    def set_InternalPort(self, val):
        """
            Sets the "InternalPort" variable.
        """
        self.proxy_set_variable_value("InternalPort", val)
        return


    def get_LastConnectionError(self):
        """
            Gets the "LastConnectionError" variable.
        """
        rval = self.proxy_get_variable_value("LastConnectionError")
        return rval


    def set_LastConnectionError(self, val):
        """
            Sets the "LastConnectionError" variable.
        """
        self.proxy_set_variable_value("LastConnectionError", val)
        return


    def get_NATEnabled(self):
        """
            Gets the "NATEnabled" variable.
        """
        rval = self.proxy_get_variable_value("NATEnabled")
        return rval


    def set_NATEnabled(self, val):
        """
            Sets the "NATEnabled" variable.
        """
        self.proxy_set_variable_value("NATEnabled", val)
        return


    def get_PortMappingDescription(self):
        """
            Gets the "PortMappingDescription" variable.
        """
        rval = self.proxy_get_variable_value("PortMappingDescription")
        return rval


    def set_PortMappingDescription(self, val):
        """
            Sets the "PortMappingDescription" variable.
        """
        self.proxy_set_variable_value("PortMappingDescription", val)
        return


    def get_PortMappingEnabled(self):
        """
            Gets the "PortMappingEnabled" variable.
        """
        rval = self.proxy_get_variable_value("PortMappingEnabled")
        return rval


    def set_PortMappingEnabled(self, val):
        """
            Sets the "PortMappingEnabled" variable.
        """
        self.proxy_set_variable_value("PortMappingEnabled", val)
        return


    def get_PortMappingLeaseDuration(self):
        """
            Gets the "PortMappingLeaseDuration" variable.
        """
        rval = self.proxy_get_variable_value("PortMappingLeaseDuration")
        return rval


    def set_PortMappingLeaseDuration(self, val):
        """
            Sets the "PortMappingLeaseDuration" variable.
        """
        self.proxy_set_variable_value("PortMappingLeaseDuration", val)
        return


    def get_PortMappingNumberOfEntries(self):
        """
            Gets the "PortMappingNumberOfEntries" variable.
        """
        rval = self.proxy_get_variable_value("PortMappingNumberOfEntries")
        return rval


    def set_PortMappingNumberOfEntries(self, val):
        """
            Sets the "PortMappingNumberOfEntries" variable.
        """
        self.proxy_set_variable_value("PortMappingNumberOfEntries", val)
        return


    def get_PortMappingProtocol(self):
        """
            Gets the "PortMappingProtocol" variable.
        """
        rval = self.proxy_get_variable_value("PortMappingProtocol")
        return rval


    def set_PortMappingProtocol(self, val):
        """
            Sets the "PortMappingProtocol" variable.
        """
        self.proxy_set_variable_value("PortMappingProtocol", val)
        return


    def get_PossibleConnectionTypes(self):
        """
            Gets the "PossibleConnectionTypes" variable.
        """
        rval = self.proxy_get_variable_value("PossibleConnectionTypes")
        return rval


    def set_PossibleConnectionTypes(self, val):
        """
            Sets the "PossibleConnectionTypes" variable.
        """
        self.proxy_set_variable_value("PossibleConnectionTypes", val)
        return


    def get_RSIPAvailable(self):
        """
            Gets the "RSIPAvailable" variable.
        """
        rval = self.proxy_get_variable_value("RSIPAvailable")
        return rval


    def set_RSIPAvailable(self, val):
        """
            Sets the "RSIPAvailable" variable.
        """
        self.proxy_set_variable_value("RSIPAvailable", val)
        return


    def get_RemoteHost(self):
        """
            Gets the "RemoteHost" variable.
        """
        rval = self.proxy_get_variable_value("RemoteHost")
        return rval


    def set_RemoteHost(self, val):
        """
            Sets the "RemoteHost" variable.
        """
        self.proxy_set_variable_value("RemoteHost", val)
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


    def get_Uptime(self):
        """
            Gets the "Uptime" variable.
        """
        rval = self.proxy_get_variable_value("Uptime")
        return rval


    def set_Uptime(self, val):
        """
            Sets the "Uptime" variable.
        """
        self.proxy_set_variable_value("Uptime", val)
        return


    def get_WarnDisconnectDelay(self):
        """
            Gets the "WarnDisconnectDelay" variable.
        """
        rval = self.proxy_get_variable_value("WarnDisconnectDelay")
        return rval


    def set_WarnDisconnectDelay(self, val):
        """
            Sets the "WarnDisconnectDelay" variable.
        """
        self.proxy_set_variable_value("WarnDisconnectDelay", val)
        return


    def action_AddAnyPortMapping(self, NewRemoteHost, NewExternalPort, NewProtocol, NewInternalPort, NewInternalClient, NewEnabled, NewPortMappingDescription, NewLeaseDuration):
        """
            Calls the AddAnyPortMapping action.
        """
        arguments = {
            "NewRemoteHost": NewRemoteHost,
            "NewExternalPort": NewExternalPort,
            "NewProtocol": NewProtocol,
            "NewInternalPort": NewInternalPort,
            "NewInternalClient": NewInternalClient,
            "NewEnabled": NewEnabled,
            "NewPortMappingDescription": NewPortMappingDescription,
            "NewLeaseDuration": NewLeaseDuration,
        }

        out_params = self.proxy_call_action("AddAnyPortMapping", arguments=arguments)

        (NewReservedPort,) = out_params

        return NewReservedPort


    def action_AddPortMapping(self, NewRemoteHost, NewExternalPort, NewProtocol, NewInternalPort, NewInternalClient, NewEnabled, NewPortMappingDescription, NewLeaseDuration):
        """
            Calls the AddPortMapping action.
        """
        arguments = {
            "NewRemoteHost": NewRemoteHost,
            "NewExternalPort": NewExternalPort,
            "NewProtocol": NewProtocol,
            "NewInternalPort": NewInternalPort,
            "NewInternalClient": NewInternalClient,
            "NewEnabled": NewEnabled,
            "NewPortMappingDescription": NewPortMappingDescription,
            "NewLeaseDuration": NewLeaseDuration,
        }

        out_params = self.proxy_call_action("AddPortMapping", arguments=arguments)

        (result,) = out_params

        return result


    def action_DeletePortMapping(self, NewRemoteHost, NewExternalPort, NewProtocol):
        """
            Calls the DeletePortMapping action.
        """
        arguments = {
            "NewRemoteHost": NewRemoteHost,
            "NewExternalPort": NewExternalPort,
            "NewProtocol": NewProtocol,
        }

        out_params = self.proxy_call_action("DeletePortMapping", arguments=arguments)

        (result,) = out_params

        return result


    def action_DeletePortMappingRange(self, NewStartPort, NewEndPort, NewProtocol, NewManage):
        """
            Calls the DeletePortMappingRange action.
        """
        arguments = {
            "NewStartPort": NewStartPort,
            "NewEndPort": NewEndPort,
            "NewProtocol": NewProtocol,
            "NewManage": NewManage,
        }

        out_params = self.proxy_call_action("DeletePortMappingRange", arguments=arguments)

        (result,) = out_params

        return result


    def action_ForceTermination(self):
        """
            Calls the ForceTermination action.
        """
        arguments = { }

        out_params = self.proxy_call_action("ForceTermination", arguments=arguments)

        (NewConnectionType, NewPossibleConnectionTypes,) = out_params

        return NewConnectionType, NewPossibleConnectionTypes


    def action_GetAutoDisconnectTime(self):
        """
            Calls the GetAutoDisconnectTime action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetAutoDisconnectTime", arguments=arguments)

        (NewAutoDisconnectTime,) = out_params

        return NewAutoDisconnectTime


    def action_GetConnectionTypeInfo(self):
        """
            Calls the GetConnectionTypeInfo action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetConnectionTypeInfo", arguments=arguments)

        (NewConnectionType, NewPossibleConnectionTypes,) = out_params

        return NewConnectionType, NewPossibleConnectionTypes


    def action_GetExternalIPAddress(self):
        """
            Calls the GetExternalIPAddress action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetExternalIPAddress", arguments=arguments)

        (NewExternalIPAddress,) = out_params

        return NewExternalIPAddress


    def action_GetGenericPortMappingEntry(self, NewPortMappingIndex):
        """
            Calls the GetGenericPortMappingEntry action.
        """
        arguments = {
            "NewPortMappingIndex": NewPortMappingIndex,
        }

        out_params = self.proxy_call_action("GetGenericPortMappingEntry", arguments=arguments)

        (NewRemoteHost, NewExternalPort, NewProtocol, NewInternalPort, NewInternalClient, NewEnabled, NewPortMappingDescription, NewLeaseDuration,) = out_params

        return NewRemoteHost, NewExternalPort, NewProtocol, NewInternalPort, NewInternalClient, NewEnabled, NewPortMappingDescription, NewLeaseDuration


    def action_GetIdleDisconnectTime(self):
        """
            Calls the GetIdleDisconnectTime action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetIdleDisconnectTime", arguments=arguments)

        (NewIdleDisconnectTime,) = out_params

        return NewIdleDisconnectTime


    def action_GetListOfPortMappings(self, NewStartPort, NewEndPort, NewProtocol, NewManage, NewNumberOfPorts):
        """
            Calls the GetListOfPortMappings action.
        """
        arguments = {
            "NewStartPort": NewStartPort,
            "NewEndPort": NewEndPort,
            "NewProtocol": NewProtocol,
            "NewManage": NewManage,
            "NewNumberOfPorts": NewNumberOfPorts,
        }

        out_params = self.proxy_call_action("GetListOfPortMappings", arguments=arguments)

        (NewPortListing,) = out_params

        return NewPortListing


    def action_GetNATRSIPStatus(self):
        """
            Calls the GetNATRSIPStatus action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetNATRSIPStatus", arguments=arguments)

        (NewRSIPAvailable, NewNATEnabled,) = out_params

        return NewRSIPAvailable, NewNATEnabled


    def action_GetSpecificPortMappingEntry(self, NewRemoteHost, NewExternalPort, NewProtocol):
        """
            Calls the GetSpecificPortMappingEntry action.
        """
        arguments = {
            "NewRemoteHost": NewRemoteHost,
            "NewExternalPort": NewExternalPort,
            "NewProtocol": NewProtocol,
        }

        out_params = self.proxy_call_action("GetSpecificPortMappingEntry", arguments=arguments)

        (NewInternalPort, NewInternalClient, NewEnabled, NewPortMappingDescription, NewLeaseDuration,) = out_params

        return NewInternalPort, NewInternalClient, NewEnabled, NewPortMappingDescription, NewLeaseDuration


    def action_GetStatusInfo(self):
        """
            Calls the GetStatusInfo action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetStatusInfo", arguments=arguments)

        (NewConnectionStatus, NewLastConnectionError, NewUptime,) = out_params

        return NewConnectionStatus, NewLastConnectionError, NewUptime


    def action_GetWarnDisconnectDelay(self):
        """
            Calls the GetWarnDisconnectDelay action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetWarnDisconnectDelay", arguments=arguments)

        (NewWarnDisconnectDelay,) = out_params

        return NewWarnDisconnectDelay


    def action_RequestConnection(self):
        """
            Calls the RequestConnection action.
        """
        arguments = { }

        out_params = self.proxy_call_action("RequestConnection", arguments=arguments)

        (NewConnectionType, NewPossibleConnectionTypes,) = out_params

        return NewConnectionType, NewPossibleConnectionTypes


    def action_RequestTermination(self):
        """
            Calls the RequestTermination action.
        """
        arguments = { }

        out_params = self.proxy_call_action("RequestTermination", arguments=arguments)

        (NewConnectionType, NewPossibleConnectionTypes,) = out_params

        return NewConnectionType, NewPossibleConnectionTypes


    def action_SetAutoDisconnectTime(self, NewAutoDisconnectTime):
        """
            Calls the SetAutoDisconnectTime action.
        """
        arguments = {
            "NewAutoDisconnectTime": NewAutoDisconnectTime,
        }

        out_params = self.proxy_call_action("SetAutoDisconnectTime", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetConnectionType(self, NewConnectionType):
        """
            Calls the SetConnectionType action.
        """
        arguments = {
            "NewConnectionType": NewConnectionType,
        }

        out_params = self.proxy_call_action("SetConnectionType", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetIdleDisconnectTime(self, NewIdleDisconnectTime):
        """
            Calls the SetIdleDisconnectTime action.
        """
        arguments = {
            "NewIdleDisconnectTime": NewIdleDisconnectTime,
        }

        out_params = self.proxy_call_action("SetIdleDisconnectTime", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetWarnDisconnectDelay(self, NewWarnDisconnectDelay):
        """
            Calls the SetWarnDisconnectDelay action.
        """
        arguments = {
            "NewWarnDisconnectDelay": NewWarnDisconnectDelay,
        }

        out_params = self.proxy_call_action("SetWarnDisconnectDelay", arguments=arguments)

        (result,) = out_params

        return result

