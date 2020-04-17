"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class DeviceProtection1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'DeviceProtection1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:DeviceProtection:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:DeviceProtection'


    def get_SetupReady(self):
        """
            Gets the "SetupReady" variable.
        """
        rval = self.proxy_get_variable_value("SetupReady")
        return rval


    def set_SetupReady(self, val):
        """
            Sets the "SetupReady" variable.
        """
        self.proxy_set_variable_value("SetupReady", val)
        return


    def get_SupportedProtocols(self):
        """
            Gets the "SupportedProtocols" variable.
        """
        rval = self.proxy_get_variable_value("SupportedProtocols")
        return rval


    def set_SupportedProtocols(self, val):
        """
            Sets the "SupportedProtocols" variable.
        """
        self.proxy_set_variable_value("SupportedProtocols", val)
        return


    def action_AddIdentityList(self, IdentityList):
        """
            Calls the AddIdentityList action.
        """
        arguments = {
            "IdentityList": IdentityList,
        }

        out_params = self.proxy_call_action("AddIdentityList", arguments=arguments)

        (IdentityListResult,) = out_params

        return IdentityListResult


    def action_AddRolesForIdentity(self, Identity, RoleList):
        """
            Calls the AddRolesForIdentity action.
        """
        arguments = {
            "Identity": Identity,
            "RoleList": RoleList,
        }

        out_params = self.proxy_call_action("AddRolesForIdentity", arguments=arguments)

        (result,) = out_params

        return result


    def action_GetACLData(self):
        """
            Calls the GetACLData action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetACLData", arguments=arguments)

        (ACL,) = out_params

        return ACL


    def action_GetAssignedRoles(self):
        """
            Calls the GetAssignedRoles action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetAssignedRoles", arguments=arguments)

        (RoleList,) = out_params

        return RoleList


    def action_GetRolesForAction(self, DeviceUDN, ServiceId, ActionName):
        """
            Calls the GetRolesForAction action.
        """
        arguments = {
            "DeviceUDN": DeviceUDN,
            "ServiceId": ServiceId,
            "ActionName": ActionName,
        }

        out_params = self.proxy_call_action("GetRolesForAction", arguments=arguments)

        (RoleList, RestrictedRoleList,) = out_params

        return RoleList, RestrictedRoleList


    def action_GetSupportedProtocols(self):
        """
            Calls the GetSupportedProtocols action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetSupportedProtocols", arguments=arguments)

        (ProtocolList,) = out_params

        return ProtocolList


    def action_GetUserLoginChallenge(self, ProtocolType, Name):
        """
            Calls the GetUserLoginChallenge action.
        """
        arguments = {
            "ProtocolType": ProtocolType,
            "Name": Name,
        }

        out_params = self.proxy_call_action("GetUserLoginChallenge", arguments=arguments)

        (Salt, Challenge,) = out_params

        return Salt, Challenge


    def action_RemoveIdentity(self, Identity):
        """
            Calls the RemoveIdentity action.
        """
        arguments = {
            "Identity": Identity,
        }

        out_params = self.proxy_call_action("RemoveIdentity", arguments=arguments)

        (result,) = out_params

        return result


    def action_RemoveRolesForIdentity(self, Identity, RoleList):
        """
            Calls the RemoveRolesForIdentity action.
        """
        arguments = {
            "Identity": Identity,
            "RoleList": RoleList,
        }

        out_params = self.proxy_call_action("RemoveRolesForIdentity", arguments=arguments)

        (result,) = out_params

        return result


    def action_SendSetupMessage(self, ProtocolType, InMessage):
        """
            Calls the SendSetupMessage action.
        """
        arguments = {
            "ProtocolType": ProtocolType,
            "InMessage": InMessage,
        }

        out_params = self.proxy_call_action("SendSetupMessage", arguments=arguments)

        (OutMessage,) = out_params

        return OutMessage


    def action_SetUserLoginPassword(self, ProtocolType, Name, Stored, Salt):
        """
            Calls the SetUserLoginPassword action.
        """
        arguments = {
            "ProtocolType": ProtocolType,
            "Name": Name,
            "Stored": Stored,
            "Salt": Salt,
        }

        out_params = self.proxy_call_action("SetUserLoginPassword", arguments=arguments)

        (result,) = out_params

        return result


    def action_UserLogin(self, ProtocolType, Challenge, Authenticator):
        """
            Calls the UserLogin action.
        """
        arguments = {
            "ProtocolType": ProtocolType,
            "Challenge": Challenge,
            "Authenticator": Authenticator,
        }

        out_params = self.proxy_call_action("UserLogin", arguments=arguments)

        (result,) = out_params

        return result


    def action_UserLogout(self, ProtocolType, Challenge, Authenticator):
        """
            Calls the UserLogout action.
        """
        arguments = {
            "ProtocolType": ProtocolType,
            "Challenge": Challenge,
            "Authenticator": Authenticator,
        }

        out_params = self.proxy_call_action("UserLogout", arguments=arguments)

        (result,) = out_params

        return result

