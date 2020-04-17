"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class RATAConfig1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'RATAConfig1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:RATAConfig:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:RATAConfig'


    def get_CredentialDelivery(self):
        """
            Gets the "CredentialDelivery" variable.
        """
        rval = self.proxy_get_variable_value("CredentialDelivery")
        return rval


    def set_CredentialDelivery(self, val):
        """
            Sets the "CredentialDelivery" variable.
        """
        self.proxy_set_variable_value("CredentialDelivery", val)
        return


    def get_CredentialsList(self):
        """
            Gets the "CredentialsList" variable.
        """
        rval = self.proxy_get_variable_value("CredentialsList")
        return rval


    def set_CredentialsList(self, val):
        """
            Sets the "CredentialsList" variable.
        """
        self.proxy_set_variable_value("CredentialsList", val)
        return


    def get_ProfileList(self):
        """
            Gets the "ProfileList" variable.
        """
        rval = self.proxy_get_variable_value("ProfileList")
        return rval


    def set_ProfileList(self, val):
        """
            Sets the "ProfileList" variable.
        """
        self.proxy_set_variable_value("ProfileList", val)
        return


    def get_SystemInfo(self):
        """
            Gets the "SystemInfo" variable.
        """
        rval = self.proxy_get_variable_value("SystemInfo")
        return rval


    def set_SystemInfo(self, val):
        """
            Sets the "SystemInfo" variable.
        """
        self.proxy_set_variable_value("SystemInfo", val)
        return


    def get_TransportAgentCapabilities(self):
        """
            Gets the "TransportAgentCapabilities" variable.
        """
        rval = self.proxy_get_variable_value("TransportAgentCapabilities")
        return rval


    def set_TransportAgentCapabilities(self, val):
        """
            Sets the "TransportAgentCapabilities" variable.
        """
        self.proxy_set_variable_value("TransportAgentCapabilities", val)
        return


    def action_AddProfile(self, NewProfileConfigInfo):
        """
            Calls the AddProfile action.
        """
        arguments = {
            "NewProfileConfigInfo": NewProfileConfigInfo,
        }

        out_params = self.proxy_call_action("AddProfile", arguments=arguments)

        (result,) = out_params

        return result


    def action_DeleteProfile(self, ProfileID):
        """
            Calls the DeleteProfile action.
        """
        arguments = {
            "ProfileID": ProfileID,
        }

        out_params = self.proxy_call_action("DeleteProfile", arguments=arguments)

        (result,) = out_params

        return result


    def action_EditProfile(self, ProfileID, UpdatedProfileConfigInfo):
        """
            Calls the EditProfile action.
        """
        arguments = {
            "ProfileID": ProfileID,
            "UpdatedProfileConfigInfo": UpdatedProfileConfigInfo,
        }

        out_params = self.proxy_call_action("EditProfile", arguments=arguments)

        (result,) = out_params

        return result


    def action_GetCredentialsList(self):
        """
            Calls the GetCredentialsList action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetCredentialsList", arguments=arguments)

        (CurrentCredentialsList,) = out_params

        return CurrentCredentialsList


    def action_GetProfileConfigInfo(self, ProfileID):
        """
            Calls the GetProfileConfigInfo action.
        """
        arguments = {
            "ProfileID": ProfileID,
        }

        out_params = self.proxy_call_action("GetProfileConfigInfo", arguments=arguments)

        (ProfileConfigInfo,) = out_params

        return ProfileConfigInfo


    def action_GetProfileList(self):
        """
            Calls the GetProfileList action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetProfileList", arguments=arguments)

        (ProfileList,) = out_params

        return ProfileList


    def action_GetSupportedCredentialDelivery(self):
        """
            Calls the GetSupportedCredentialDelivery action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetSupportedCredentialDelivery", arguments=arguments)

        (SupportedCredentialDelivery,) = out_params

        return SupportedCredentialDelivery


    def action_GetTransportAgentCapabilities(self):
        """
            Calls the GetTransportAgentCapabilities action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetTransportAgentCapabilities", arguments=arguments)

        (TransportAgentCapabilities,) = out_params

        return TransportAgentCapabilities

