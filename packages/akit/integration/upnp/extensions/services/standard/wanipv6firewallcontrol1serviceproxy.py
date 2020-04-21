"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class WANIPv6FirewallControl1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'WANIPv6FirewallControl1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:WANIPv6FirewallControl:1'
    SERVICE_ID = 'urn:schemas-upnp-org:service:WANIPv6FirewallControl'


    def get_FirewallEnabled(self):
        """
            Gets the "FirewallEnabled" variable.
        """
        rval = self.proxy_get_variable_value("FirewallEnabled")
        return rval


    def set_FirewallEnabled(self, val):
        """
            Sets the "FirewallEnabled" variable.
        """
        self.proxy_set_variable_value("FirewallEnabled", val)
        return


    def get_InboundPinholeAllowed(self):
        """
            Gets the "InboundPinholeAllowed" variable.
        """
        rval = self.proxy_get_variable_value("InboundPinholeAllowed")
        return rval


    def set_InboundPinholeAllowed(self, val):
        """
            Sets the "InboundPinholeAllowed" variable.
        """
        self.proxy_set_variable_value("InboundPinholeAllowed", val)
        return


    def action_AddPinhole(self, RemoteHost, RemotePort, InternalClient, InternalPort, Protocol, LeaseTime):
        """
            Calls the AddPinhole action.
        """
        arguments = {
            "RemoteHost": RemoteHost,
            "RemotePort": RemotePort,
            "InternalClient": InternalClient,
            "InternalPort": InternalPort,
            "Protocol": Protocol,
            "LeaseTime": LeaseTime,
        }

        out_params = self.proxy_call_action("AddPinhole", arguments=arguments)

        (UniqueID,) = out_params

        return UniqueID


    def action_CheckPinholeWorking(self, UniqueID):
        """
            Calls the CheckPinholeWorking action.
        """
        arguments = {
            "UniqueID": UniqueID,
        }

        out_params = self.proxy_call_action("CheckPinholeWorking", arguments=arguments)

        (IsWorking,) = out_params

        return IsWorking


    def action_DeletePinhole(self, UniqueID):
        """
            Calls the DeletePinhole action.
        """
        arguments = {
            "UniqueID": UniqueID,
        }

        out_params = self.proxy_call_action("DeletePinhole", arguments=arguments)

        (result,) = out_params

        return result


    def action_GetFirewallStatus(self):
        """
            Calls the GetFirewallStatus action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetFirewallStatus", arguments=arguments)

        (FirewallEnabled, InboundPinholeAllowed,) = out_params

        return FirewallEnabled, InboundPinholeAllowed


    def action_GetOutboundPinholeTimeout(self, RemoteHost, RemotePort, InternalClient, InternalPort, Protocol):
        """
            Calls the GetOutboundPinholeTimeout action.
        """
        arguments = {
            "RemoteHost": RemoteHost,
            "RemotePort": RemotePort,
            "InternalClient": InternalClient,
            "InternalPort": InternalPort,
            "Protocol": Protocol,
        }

        out_params = self.proxy_call_action("GetOutboundPinholeTimeout", arguments=arguments)

        (OutboundPinholeTimeout,) = out_params

        return OutboundPinholeTimeout


    def action_GetPinholePackets(self, UniqueID):
        """
            Calls the GetPinholePackets action.
        """
        arguments = {
            "UniqueID": UniqueID,
        }

        out_params = self.proxy_call_action("GetPinholePackets", arguments=arguments)

        (PinholePackets,) = out_params

        return PinholePackets


    def action_UpdatePinhole(self, UniqueID, NewLeaseTime):
        """
            Calls the UpdatePinhole action.
        """
        arguments = {
            "UniqueID": UniqueID,
            "NewLeaseTime": NewLeaseTime,
        }

        out_params = self.proxy_call_action("UpdatePinhole", arguments=arguments)

        (result,) = out_params

        return result

