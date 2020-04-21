"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class LinkAuthentication1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'LinkAuthentication1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:LinkAuthentication:1'
    SERVICE_ID = 'urn:schemas-upnp-org:service:LinkAuthentication'


    def get_AuthState(self):
        """
            Gets the "AuthState" variable.
        """
        rval = self.proxy_get_variable_value("AuthState")
        return rval


    def set_AuthState(self, val):
        """
            Sets the "AuthState" variable.
        """
        self.proxy_set_variable_value("AuthState", val)
        return


    def get_AuthType(self):
        """
            Gets the "AuthType" variable.
        """
        rval = self.proxy_get_variable_value("AuthType")
        return rval


    def set_AuthType(self, val):
        """
            Sets the "AuthType" variable.
        """
        self.proxy_set_variable_value("AuthType", val)
        return


    def get_CredentialDuration(self):
        """
            Gets the "CredentialDuration" variable.
        """
        rval = self.proxy_get_variable_value("CredentialDuration")
        return rval


    def set_CredentialDuration(self, val):
        """
            Sets the "CredentialDuration" variable.
        """
        self.proxy_set_variable_value("CredentialDuration", val)
        return


    def get_CredentialState(self):
        """
            Gets the "CredentialState" variable.
        """
        rval = self.proxy_get_variable_value("CredentialState")
        return rval


    def set_CredentialState(self, val):
        """
            Sets the "CredentialState" variable.
        """
        self.proxy_set_variable_value("CredentialState", val)
        return


    def get_Description(self):
        """
            Gets the "Description" variable.
        """
        rval = self.proxy_get_variable_value("Description")
        return rval


    def set_Description(self, val):
        """
            Sets the "Description" variable.
        """
        self.proxy_set_variable_value("Description", val)
        return


    def get_Identifier(self):
        """
            Gets the "Identifier" variable.
        """
        rval = self.proxy_get_variable_value("Identifier")
        return rval


    def set_Identifier(self, val):
        """
            Sets the "Identifier" variable.
        """
        self.proxy_set_variable_value("Identifier", val)
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


    def get_LastError(self):
        """
            Gets the "LastError" variable.
        """
        rval = self.proxy_get_variable_value("LastError")
        return rval


    def set_LastError(self, val):
        """
            Sets the "LastError" variable.
        """
        self.proxy_set_variable_value("LastError", val)
        return


    def get_LinkedIdentifier(self):
        """
            Gets the "LinkedIdentifier" variable.
        """
        rval = self.proxy_get_variable_value("LinkedIdentifier")
        return rval


    def set_LinkedIdentifier(self, val):
        """
            Sets the "LinkedIdentifier" variable.
        """
        self.proxy_set_variable_value("LinkedIdentifier", val)
        return


    def get_MACAddress(self):
        """
            Gets the "MACAddress" variable.
        """
        rval = self.proxy_get_variable_value("MACAddress")
        return rval


    def set_MACAddress(self, val):
        """
            Sets the "MACAddress" variable.
        """
        self.proxy_set_variable_value("MACAddress", val)
        return


    def get_NumberOfEntries(self):
        """
            Gets the "NumberOfEntries" variable.
        """
        rval = self.proxy_get_variable_value("NumberOfEntries")
        return rval


    def set_NumberOfEntries(self, val):
        """
            Sets the "NumberOfEntries" variable.
        """
        self.proxy_set_variable_value("NumberOfEntries", val)
        return


    def get_Secret(self):
        """
            Gets the "Secret" variable.
        """
        rval = self.proxy_get_variable_value("Secret")
        return rval


    def set_Secret(self, val):
        """
            Sets the "Secret" variable.
        """
        self.proxy_set_variable_value("Secret", val)
        return


    def get_SecretType(self):
        """
            Gets the "SecretType" variable.
        """
        rval = self.proxy_get_variable_value("SecretType")
        return rval


    def set_SecretType(self, val):
        """
            Sets the "SecretType" variable.
        """
        self.proxy_set_variable_value("SecretType", val)
        return


    def action_AddEntry(self, NewIdentifier, NewSecret, NewSecretType, NewAuthType, NewAuthState, NewCredentialState, NewDescription, NewMACAddress, NewCredentialDuration, NewLinkedIdentifier):
        """
            Calls the AddEntry action.
        """
        arguments = {
            "NewIdentifier": NewIdentifier,
            "NewSecret": NewSecret,
            "NewSecretType": NewSecretType,
            "NewAuthType": NewAuthType,
            "NewAuthState": NewAuthState,
            "NewCredentialState": NewCredentialState,
            "NewDescription": NewDescription,
            "NewMACAddress": NewMACAddress,
            "NewCredentialDuration": NewCredentialDuration,
            "NewLinkedIdentifier": NewLinkedIdentifier,
        }

        out_params = self.proxy_call_action("AddEntry", arguments=arguments)

        (NewNumberOfEntries,) = out_params

        return NewNumberOfEntries


    def action_DeleteEntry(self, NewIdentifier):
        """
            Calls the DeleteEntry action.
        """
        arguments = {
            "NewIdentifier": NewIdentifier,
        }

        out_params = self.proxy_call_action("DeleteEntry", arguments=arguments)

        (NewNumberOfEntries,) = out_params

        return NewNumberOfEntries


    def action_FactoryDefaultReset(self):
        """
            Calls the FactoryDefaultReset action.
        """
        arguments = { }

        out_params = self.proxy_call_action("FactoryDefaultReset", arguments=arguments)

        (NewNumberOfEntries,) = out_params

        return NewNumberOfEntries


    def action_GetGenericEntry(self, NewIndex):
        """
            Calls the GetGenericEntry action.
        """
        arguments = {
            "NewIndex": NewIndex,
        }

        out_params = self.proxy_call_action("GetGenericEntry", arguments=arguments)

        (NewIdentifier, NewSecret, NewSecretType, NewAuthType, NewAuthState, NewCredentialState, NewDescription, NewMACAddress, NewCredentialDuration, NewLinkedIdentifier,) = out_params

        return NewIdentifier, NewSecret, NewSecretType, NewAuthType, NewAuthState, NewCredentialState, NewDescription, NewMACAddress, NewCredentialDuration, NewLinkedIdentifier


    def action_GetNumberOfEntries(self):
        """
            Calls the GetNumberOfEntries action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetNumberOfEntries", arguments=arguments)

        (NewNumberOfEntries,) = out_params

        return NewNumberOfEntries


    def action_GetSpecificEntry(self, NewIdentifierKey):
        """
            Calls the GetSpecificEntry action.
        """
        arguments = {
            "NewIdentifierKey": NewIdentifierKey,
        }

        out_params = self.proxy_call_action("GetSpecificEntry", arguments=arguments)

        (NewIdentifier, NewSecret, NewSecretType, NewAuthType, NewAuthState, NewCredentialState, NewDescription, NewMACAddress, NewCredentialDuration, NewLinkedIdentifier,) = out_params

        return NewIdentifier, NewSecret, NewSecretType, NewAuthType, NewAuthState, NewCredentialState, NewDescription, NewMACAddress, NewCredentialDuration, NewLinkedIdentifier


    def action_ResetAuthentication(self):
        """
            Calls the ResetAuthentication action.
        """
        arguments = { }

        out_params = self.proxy_call_action("ResetAuthentication", arguments=arguments)

        (NewNumberOfEntries,) = out_params

        return NewNumberOfEntries


    def action_UpdateEntry(self, NewIdentifier, NewSecret, NewSecretType, NewAuthType, NewAuthState, NewCredentialState, NewDescription, NewMACAddress, NewCredentialDuration, NewLinkedIdentifier):
        """
            Calls the UpdateEntry action.
        """
        arguments = {
            "NewIdentifier": NewIdentifier,
            "NewSecret": NewSecret,
            "NewSecretType": NewSecretType,
            "NewAuthType": NewAuthType,
            "NewAuthState": NewAuthState,
            "NewCredentialState": NewCredentialState,
            "NewDescription": NewDescription,
            "NewMACAddress": NewMACAddress,
            "NewCredentialDuration": NewCredentialDuration,
            "NewLinkedIdentifier": NewLinkedIdentifier,
        }

        out_params = self.proxy_call_action("UpdateEntry", arguments=arguments)

        (NewNumberOfEntries,) = out_params

        return NewNumberOfEntries

