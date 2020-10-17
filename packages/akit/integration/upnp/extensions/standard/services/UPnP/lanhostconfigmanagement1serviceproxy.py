"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class LANHostConfigManagement1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'LANHostConfigManagement1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:LANHostConfigManagement:1'


    def action_DeleteDNSServer(self, NewDNSServers, extract_returns=True):
        """
            Calls the DeleteDNSServer action.

            :returns: "result"
        """
        arguments = {
            "NewDNSServers": NewDNSServers,
        }

        out_params = self.proxy_call_action("DeleteDNSServer", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_DeleteIPRouter(self, NewIPRouters, extract_returns=True):
        """
            Calls the DeleteIPRouter action.

            :returns: "result"
        """
        arguments = {
            "NewIPRouters": NewIPRouters,
        }

        out_params = self.proxy_call_action("DeleteIPRouter", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_DeleteReservedAddress(self, NewReservedAddresses, extract_returns=True):
        """
            Calls the DeleteReservedAddress action.

            :returns: "result"
        """
        arguments = {
            "NewReservedAddresses": NewReservedAddresses,
        }

        out_params = self.proxy_call_action("DeleteReservedAddress", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetAddressRange(self, extract_returns=True):
        """
            Calls the GetAddressRange action.

            :returns: "NewMinAddress", "NewMaxAddress"
        """
        arguments = { }

        out_params = self.proxy_call_action("GetAddressRange", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewMinAddress", "NewMaxAddress",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetDHCPRelay(self, extract_returns=True):
        """
            Calls the GetDHCPRelay action.

            :returns: "NewDHCPRelay"
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDHCPRelay", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewDHCPRelay",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetDHCPServerConfigurable(self, extract_returns=True):
        """
            Calls the GetDHCPServerConfigurable action.

            :returns: "NewDHCPServerConfigurable"
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDHCPServerConfigurable", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewDHCPServerConfigurable",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetDNSServers(self, extract_returns=True):
        """
            Calls the GetDNSServers action.

            :returns: "NewDNSServers"
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDNSServers", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewDNSServers",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetDomainName(self, extract_returns=True):
        """
            Calls the GetDomainName action.

            :returns: "NewDomainName"
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDomainName", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewDomainName",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetIPRoutersList(self, extract_returns=True):
        """
            Calls the GetIPRoutersList action.

            :returns: "NewIPRouters"
        """
        arguments = { }

        out_params = self.proxy_call_action("GetIPRoutersList", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewIPRouters",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetReservedAddresses(self, extract_returns=True):
        """
            Calls the GetReservedAddresses action.

            :returns: "NewReservedAddresses"
        """
        arguments = { }

        out_params = self.proxy_call_action("GetReservedAddresses", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewReservedAddresses",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_GetSubnetMask(self, extract_returns=True):
        """
            Calls the GetSubnetMask action.

            :returns: "NewSubnetMask"
        """
        arguments = { }

        out_params = self.proxy_call_action("GetSubnetMask", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewSubnetMask",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetAddressRange(self, NewMinAddress, NewMaxAddress, extract_returns=True):
        """
            Calls the SetAddressRange action.

            :returns: "result"
        """
        arguments = {
            "NewMinAddress": NewMinAddress,
            "NewMaxAddress": NewMaxAddress,
        }

        out_params = self.proxy_call_action("SetAddressRange", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetDHCPRelay(self, NewDHCPRelay, extract_returns=True):
        """
            Calls the SetDHCPRelay action.

            :returns: "result"
        """
        arguments = {
            "NewDHCPRelay": NewDHCPRelay,
        }

        out_params = self.proxy_call_action("SetDHCPRelay", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetDHCPServerConfigurable(self, NewDHCPServerConfigurable, extract_returns=True):
        """
            Calls the SetDHCPServerConfigurable action.

            :returns: "result"
        """
        arguments = {
            "NewDHCPServerConfigurable": NewDHCPServerConfigurable,
        }

        out_params = self.proxy_call_action("SetDHCPServerConfigurable", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetDNSServer(self, NewDNSServers, extract_returns=True):
        """
            Calls the SetDNSServer action.

            :returns: "result"
        """
        arguments = {
            "NewDNSServers": NewDNSServers,
        }

        out_params = self.proxy_call_action("SetDNSServer", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetDomainName(self, NewDomainName, extract_returns=True):
        """
            Calls the SetDomainName action.

            :returns: "result"
        """
        arguments = {
            "NewDomainName": NewDomainName,
        }

        out_params = self.proxy_call_action("SetDomainName", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetIPRouter(self, NewIPRouters, extract_returns=True):
        """
            Calls the SetIPRouter action.

            :returns: "result"
        """
        arguments = {
            "NewIPRouters": NewIPRouters,
        }

        out_params = self.proxy_call_action("SetIPRouter", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetReservedAddress(self, NewReservedAddresses, extract_returns=True):
        """
            Calls the SetReservedAddress action.

            :returns: "result"
        """
        arguments = {
            "NewReservedAddresses": NewReservedAddresses,
        }

        out_params = self.proxy_call_action("SetReservedAddress", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SetSubnetMask(self, NewSubnetMask, extract_returns=True):
        """
            Calls the SetSubnetMask action.

            :returns: "result"
        """
        arguments = {
            "NewSubnetMask": NewSubnetMask,
        }

        out_params = self.proxy_call_action("SetSubnetMask", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

