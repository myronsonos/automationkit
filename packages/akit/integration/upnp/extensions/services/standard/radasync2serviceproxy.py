"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class RADASync2ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'RADASync2' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:RADASync:2'
    SERVICE_ID = 'urn:schemas-upnp-org:service:RADASync'


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


    def action_AddRemoteDevices(self, DeviceList, ID):
        """
            Calls the AddRemoteDevices action.
        """
        arguments = {
            "DeviceList": DeviceList,
            "ID": ID,
        }

        out_params = self.proxy_call_action("AddRemoteDevices", arguments=arguments)

        (result,) = out_params

        return result


    def action_GetLocalNetworkAddressInfo(self):
        """
            Calls the GetLocalNetworkAddressInfo action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetLocalNetworkAddressInfo", arguments=arguments)

        (LocalNetworkAddress,) = out_params

        return LocalNetworkAddress


    def action_HeartbeatUpdate(self, ID):
        """
            Calls the HeartbeatUpdate action.
        """
        arguments = {
            "ID": ID,
        }

        out_params = self.proxy_call_action("HeartbeatUpdate", arguments=arguments)

        (result,) = out_params

        return result


    def action_RemoveRemoteDevices(self, DeviceList, ID):
        """
            Calls the RemoveRemoteDevices action.
        """
        arguments = {
            "DeviceList": DeviceList,
            "ID": ID,
        }

        out_params = self.proxy_call_action("RemoveRemoteDevices", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetDDDLocation(self, DDDLocation, ID):
        """
            Calls the SetDDDLocation action.
        """
        arguments = {
            "DDDLocation": DDDLocation,
            "ID": ID,
        }

        out_params = self.proxy_call_action("SetDDDLocation", arguments=arguments)

        (result,) = out_params

        return result

