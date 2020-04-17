"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class LANHostConfigManagement1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'LANHostConfigManagement1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:LANHostConfigManagement:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:LANHostConfigManagement'


    def get_DHCPRelay(self):
        """
            Gets the "DHCPRelay" variable.
        """
        rval = self.proxy_get_variable_value("DHCPRelay")
        return rval


    def set_DHCPRelay(self, val):
        """
            Sets the "DHCPRelay" variable.
        """
        self.proxy_set_variable_value("DHCPRelay", val)
        return


    def get_DHCPServerConfigurable(self):
        """
            Gets the "DHCPServerConfigurable" variable.
        """
        rval = self.proxy_get_variable_value("DHCPServerConfigurable")
        return rval


    def set_DHCPServerConfigurable(self, val):
        """
            Sets the "DHCPServerConfigurable" variable.
        """
        self.proxy_set_variable_value("DHCPServerConfigurable", val)
        return


    def get_DNSServers(self):
        """
            Gets the "DNSServers" variable.
        """
        rval = self.proxy_get_variable_value("DNSServers")
        return rval


    def set_DNSServers(self, val):
        """
            Sets the "DNSServers" variable.
        """
        self.proxy_set_variable_value("DNSServers", val)
        return


    def get_DomainName(self):
        """
            Gets the "DomainName" variable.
        """
        rval = self.proxy_get_variable_value("DomainName")
        return rval


    def set_DomainName(self, val):
        """
            Sets the "DomainName" variable.
        """
        self.proxy_set_variable_value("DomainName", val)
        return


    def get_IPRouters(self):
        """
            Gets the "IPRouters" variable.
        """
        rval = self.proxy_get_variable_value("IPRouters")
        return rval


    def set_IPRouters(self, val):
        """
            Sets the "IPRouters" variable.
        """
        self.proxy_set_variable_value("IPRouters", val)
        return


    def get_MaxAddress(self):
        """
            Gets the "MaxAddress" variable.
        """
        rval = self.proxy_get_variable_value("MaxAddress")
        return rval


    def set_MaxAddress(self, val):
        """
            Sets the "MaxAddress" variable.
        """
        self.proxy_set_variable_value("MaxAddress", val)
        return


    def get_MinAddress(self):
        """
            Gets the "MinAddress" variable.
        """
        rval = self.proxy_get_variable_value("MinAddress")
        return rval


    def set_MinAddress(self, val):
        """
            Sets the "MinAddress" variable.
        """
        self.proxy_set_variable_value("MinAddress", val)
        return


    def get_ReservedAddresses(self):
        """
            Gets the "ReservedAddresses" variable.
        """
        rval = self.proxy_get_variable_value("ReservedAddresses")
        return rval


    def set_ReservedAddresses(self, val):
        """
            Sets the "ReservedAddresses" variable.
        """
        self.proxy_set_variable_value("ReservedAddresses", val)
        return


    def get_SubnetMask(self):
        """
            Gets the "SubnetMask" variable.
        """
        rval = self.proxy_get_variable_value("SubnetMask")
        return rval


    def set_SubnetMask(self, val):
        """
            Sets the "SubnetMask" variable.
        """
        self.proxy_set_variable_value("SubnetMask", val)
        return


    def action_DeleteDNSServer(self, NewDNSServers):
        """
            Calls the DeleteDNSServer action.
        """
        arguments = {
            "NewDNSServers": NewDNSServers,
        }

        out_params = self.proxy_call_action("DeleteDNSServer", arguments=arguments)

        (result,) = out_params

        return result


    def action_DeleteIPRouter(self, NewIPRouters):
        """
            Calls the DeleteIPRouter action.
        """
        arguments = {
            "NewIPRouters": NewIPRouters,
        }

        out_params = self.proxy_call_action("DeleteIPRouter", arguments=arguments)

        (result,) = out_params

        return result


    def action_DeleteReservedAddress(self, NewReservedAddresses):
        """
            Calls the DeleteReservedAddress action.
        """
        arguments = {
            "NewReservedAddresses": NewReservedAddresses,
        }

        out_params = self.proxy_call_action("DeleteReservedAddress", arguments=arguments)

        (result,) = out_params

        return result


    def action_GetAddressRange(self):
        """
            Calls the GetAddressRange action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetAddressRange", arguments=arguments)

        (NewMinAddress, NewMaxAddress,) = out_params

        return NewMinAddress, NewMaxAddress


    def action_GetDHCPRelay(self):
        """
            Calls the GetDHCPRelay action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDHCPRelay", arguments=arguments)

        (NewDHCPRelay,) = out_params

        return NewDHCPRelay


    def action_GetDHCPServerConfigurable(self):
        """
            Calls the GetDHCPServerConfigurable action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDHCPServerConfigurable", arguments=arguments)

        (NewDHCPServerConfigurable,) = out_params

        return NewDHCPServerConfigurable


    def action_GetDNSServers(self):
        """
            Calls the GetDNSServers action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDNSServers", arguments=arguments)

        (NewDNSServers,) = out_params

        return NewDNSServers


    def action_GetDomainName(self):
        """
            Calls the GetDomainName action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDomainName", arguments=arguments)

        (NewDomainName,) = out_params

        return NewDomainName


    def action_GetIPRoutersList(self):
        """
            Calls the GetIPRoutersList action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetIPRoutersList", arguments=arguments)

        (NewIPRouters,) = out_params

        return NewIPRouters


    def action_GetReservedAddresses(self):
        """
            Calls the GetReservedAddresses action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetReservedAddresses", arguments=arguments)

        (NewReservedAddresses,) = out_params

        return NewReservedAddresses


    def action_GetSubnetMask(self):
        """
            Calls the GetSubnetMask action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetSubnetMask", arguments=arguments)

        (NewSubnetMask,) = out_params

        return NewSubnetMask


    def action_SetAddressRange(self, NewMinAddress, NewMaxAddress):
        """
            Calls the SetAddressRange action.
        """
        arguments = {
            "NewMinAddress": NewMinAddress,
            "NewMaxAddress": NewMaxAddress,
        }

        out_params = self.proxy_call_action("SetAddressRange", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetDHCPRelay(self, NewDHCPRelay):
        """
            Calls the SetDHCPRelay action.
        """
        arguments = {
            "NewDHCPRelay": NewDHCPRelay,
        }

        out_params = self.proxy_call_action("SetDHCPRelay", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetDHCPServerConfigurable(self, NewDHCPServerConfigurable):
        """
            Calls the SetDHCPServerConfigurable action.
        """
        arguments = {
            "NewDHCPServerConfigurable": NewDHCPServerConfigurable,
        }

        out_params = self.proxy_call_action("SetDHCPServerConfigurable", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetDNSServer(self, NewDNSServers):
        """
            Calls the SetDNSServer action.
        """
        arguments = {
            "NewDNSServers": NewDNSServers,
        }

        out_params = self.proxy_call_action("SetDNSServer", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetDomainName(self, NewDomainName):
        """
            Calls the SetDomainName action.
        """
        arguments = {
            "NewDomainName": NewDomainName,
        }

        out_params = self.proxy_call_action("SetDomainName", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetIPRouter(self, NewIPRouters):
        """
            Calls the SetIPRouter action.
        """
        arguments = {
            "NewIPRouters": NewIPRouters,
        }

        out_params = self.proxy_call_action("SetIPRouter", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetReservedAddress(self, NewReservedAddresses):
        """
            Calls the SetReservedAddress action.
        """
        arguments = {
            "NewReservedAddresses": NewReservedAddresses,
        }

        out_params = self.proxy_call_action("SetReservedAddress", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetSubnetMask(self, NewSubnetMask):
        """
            Calls the SetSubnetMask action.
        """
        arguments = {
            "NewSubnetMask": NewSubnetMask,
        }

        out_params = self.proxy_call_action("SetSubnetMask", arguments=arguments)

        (result,) = out_params

        return result

