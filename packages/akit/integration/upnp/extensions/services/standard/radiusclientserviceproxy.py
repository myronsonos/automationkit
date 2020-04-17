"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class RadiusClientServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'RadiusClient' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:RadiusClient:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:RadiusClient'


    def get_AuthenticationServerIPAddress(self):
        """
            Gets the "AuthenticationServerIPAddress" variable.
        """
        rval = self.proxy_get_variable_value("AuthenticationServerIPAddress")
        return rval


    def set_AuthenticationServerIPAddress(self, val):
        """
            Sets the "AuthenticationServerIPAddress" variable.
        """
        self.proxy_set_variable_value("AuthenticationServerIPAddress", val)
        return


    def get_AuthenticationServerPortNumber(self):
        """
            Gets the "AuthenticationServerPortNumber" variable.
        """
        rval = self.proxy_get_variable_value("AuthenticationServerPortNumber")
        return rval


    def set_AuthenticationServerPortNumber(self, val):
        """
            Sets the "AuthenticationServerPortNumber" variable.
        """
        self.proxy_set_variable_value("AuthenticationServerPortNumber", val)
        return


    def get_AuthenticationServerSharedSecret(self):
        """
            Gets the "AuthenticationServerSharedSecret" variable.
        """
        rval = self.proxy_get_variable_value("AuthenticationServerSharedSecret")
        return rval


    def set_AuthenticationServerSharedSecret(self, val):
        """
            Sets the "AuthenticationServerSharedSecret" variable.
        """
        self.proxy_set_variable_value("AuthenticationServerSharedSecret", val)
        return


    def get_NumberOfAuthenticationServerEntries(self):
        """
            Gets the "NumberOfAuthenticationServerEntries" variable.
        """
        rval = self.proxy_get_variable_value("NumberOfAuthenticationServerEntries")
        return rval


    def set_NumberOfAuthenticationServerEntries(self, val):
        """
            Sets the "NumberOfAuthenticationServerEntries" variable.
        """
        self.proxy_set_variable_value("NumberOfAuthenticationServerEntries", val)
        return


    def action_AddAuthenticationServerEntry(self, NewAuthenticationServerIPAddress, NewAuthenticationServerPortNumber, NewAuthenticationServerSharedSecret):
        """
            Calls the AddAuthenticationServerEntry action.
        """
        arguments = {
            "NewAuthenticationServerIPAddress": NewAuthenticationServerIPAddress,
            "NewAuthenticationServerPortNumber": NewAuthenticationServerPortNumber,
            "NewAuthenticationServerSharedSecret": NewAuthenticationServerSharedSecret,
        }

        out_params = self.proxy_call_action("AddAuthenticationServerEntry", arguments=arguments)

        (result,) = out_params

        return result


    def action_DeleteAuthenticationServerEntry(self, NewAuthenticationServerIPAddress, NewAuthenticationServerPortNumber):
        """
            Calls the DeleteAuthenticationServerEntry action.
        """
        arguments = {
            "NewAuthenticationServerIPAddress": NewAuthenticationServerIPAddress,
            "NewAuthenticationServerPortNumber": NewAuthenticationServerPortNumber,
        }

        out_params = self.proxy_call_action("DeleteAuthenticationServerEntry", arguments=arguments)

        (result,) = out_params

        return result


    def action_FactoryDefaultReset(self, NewAuthenticationServerIPAddress, NewAuthenticationServerPortNumber):
        """
            Calls the FactoryDefaultReset action.
        """
        arguments = {
            "NewAuthenticationServerIPAddress": NewAuthenticationServerIPAddress,
            "NewAuthenticationServerPortNumber": NewAuthenticationServerPortNumber,
        }

        out_params = self.proxy_call_action("FactoryDefaultReset", arguments=arguments)

        (result,) = out_params

        return result


    def action_GetGenericAuthenticationServerEntry(self, NewAuthenticationServerIndex):
        """
            Calls the GetGenericAuthenticationServerEntry action.
        """
        arguments = {
            "NewAuthenticationServerIndex": NewAuthenticationServerIndex,
        }

        out_params = self.proxy_call_action("GetGenericAuthenticationServerEntry", arguments=arguments)

        (NewAuthenticationServerIPAddress, NewAuthenticationServerPortNumber, NewAuthenticationServerSharedSecret,) = out_params

        return NewAuthenticationServerIPAddress, NewAuthenticationServerPortNumber, NewAuthenticationServerSharedSecret


    def action_GetSpecificAuthenticationServerEntry(self, NewAuthenticationServerIPAddress, NewAuthenticationServerPortNumber):
        """
            Calls the GetSpecificAuthenticationServerEntry action.
        """
        arguments = {
            "NewAuthenticationServerIPAddress": NewAuthenticationServerIPAddress,
            "NewAuthenticationServerPortNumber": NewAuthenticationServerPortNumber,
        }

        out_params = self.proxy_call_action("GetSpecificAuthenticationServerEntry", arguments=arguments)

        (NewAuthenticationServerSharedSecret,) = out_params

        return NewAuthenticationServerSharedSecret


    def action_ResetAuthentication(self, NewAuthenticationServerIPAddress, NewAuthenticationServerPortNumber):
        """
            Calls the ResetAuthentication action.
        """
        arguments = {
            "NewAuthenticationServerIPAddress": NewAuthenticationServerIPAddress,
            "NewAuthenticationServerPortNumber": NewAuthenticationServerPortNumber,
        }

        out_params = self.proxy_call_action("ResetAuthentication", arguments=arguments)

        (result,) = out_params

        return result

