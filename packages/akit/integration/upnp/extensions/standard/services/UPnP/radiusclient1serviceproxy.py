"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class RadiusClient1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'RadiusClient1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:RadiusClient:1'

    SERVICE_EVENT_VARIABLES = {
        "NumberOfAuthenticationServerEntries": { "data_type": "ui2", "default": None, "allowed_list": None},
    }

    def action_AddAuthenticationServerEntry(self, NewAuthenticationServerIPAddress, NewAuthenticationServerPortNumber, NewAuthenticationServerSharedSecret, extract_returns=True):
        """
            Calls the AddAuthenticationServerEntry action.

            :returns: "result"
        """
        arguments = {
            "NewAuthenticationServerIPAddress": NewAuthenticationServerIPAddress,
            "NewAuthenticationServerPortNumber": NewAuthenticationServerPortNumber,
            "NewAuthenticationServerSharedSecret": NewAuthenticationServerSharedSecret,
        }

        out_params = self._proxy_call_action("AddAuthenticationServerEntry", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_DeleteAuthenticationServerEntry(self, NewAuthenticationServerIPAddress, NewAuthenticationServerPortNumber, extract_returns=True):
        """
            Calls the DeleteAuthenticationServerEntry action.

            :returns: "result"
        """
        arguments = {
            "NewAuthenticationServerIPAddress": NewAuthenticationServerIPAddress,
            "NewAuthenticationServerPortNumber": NewAuthenticationServerPortNumber,
        }

        out_params = self._proxy_call_action("DeleteAuthenticationServerEntry", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_FactoryDefaultReset(self, extract_returns=True):
        """
            Calls the FactoryDefaultReset action.

            :returns: "result"
        """
        arguments = { }

        out_params = self._proxy_call_action("FactoryDefaultReset", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetGenericAuthenticationServerEntry(self, NewAuthenticationServerIndex, extract_returns=True):
        """
            Calls the GetGenericAuthenticationServerEntry action.

            :returns: "NewAuthenticationServerIPAddress", "NewAuthenticationServerPortNumber", "NewAuthenticationServerSharedSecret"
        """
        arguments = {
            "NewAuthenticationServerIndex": NewAuthenticationServerIndex,
        }

        out_params = self._proxy_call_action("GetGenericAuthenticationServerEntry", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewAuthenticationServerIPAddress", "NewAuthenticationServerPortNumber", "NewAuthenticationServerSharedSecret",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_GetSpecificAuthenticationServerEntry(self, NewAuthenticationServerIPAddress, NewAuthenticationServerPortNumber, extract_returns=True):
        """
            Calls the GetSpecificAuthenticationServerEntry action.

            :returns: "NewAuthenticationServerSharedSecret"
        """
        arguments = {
            "NewAuthenticationServerIPAddress": NewAuthenticationServerIPAddress,
            "NewAuthenticationServerPortNumber": NewAuthenticationServerPortNumber,
        }

        out_params = self._proxy_call_action("GetSpecificAuthenticationServerEntry", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("NewAuthenticationServerSharedSecret",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

    def action_ResetAuthentication(self, extract_returns=True):
        """
            Calls the ResetAuthentication action.

            :returns: "result"
        """
        arguments = { }

        out_params = self._proxy_call_action("ResetAuthentication", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args
