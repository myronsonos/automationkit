"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class RADAConfig2ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'RADAConfig2' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:RADAConfig:2'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:RADAConfig'


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


    def get_SystemInfoUpdateID(self):
        """
            Gets the "SystemInfoUpdateID" variable.
        """
        rval = self.proxy_get_variable_value("SystemInfoUpdateID")
        return rval


    def set_SystemInfoUpdateID(self, val):
        """
            Sets the "SystemInfoUpdateID" variable.
        """
        self.proxy_set_variable_value("SystemInfoUpdateID", val)
        return


    def action_CreateVirtualDevice(self, VirtualDeviceDescr):
        """
            Calls the CreateVirtualDevice action.
        """
        arguments = {
            "VirtualDeviceDescr": VirtualDeviceDescr,
        }

        out_params = self.proxy_call_action("CreateVirtualDevice", arguments=arguments)

        (VirtualDeviceID,) = out_params

        return VirtualDeviceID


    def action_DestroyVirtualDevice(self, VirtualDeviceID):
        """
            Calls the DestroyVirtualDevice action.
        """
        arguments = {
            "VirtualDeviceID": VirtualDeviceID,
        }

        out_params = self.proxy_call_action("DestroyVirtualDevice", arguments=arguments)

        (result,) = out_params

        return result


    def action_EditFilter(self, Filter):
        """
            Calls the EditFilter action.
        """
        arguments = {
            "Filter": Filter,
        }

        out_params = self.proxy_call_action("EditFilter", arguments=arguments)

        (result,) = out_params

        return result


    def action_GetSystemInfo(self, ID):
        """
            Calls the GetSystemInfo action.
        """
        arguments = {
            "ID": ID,
        }

        out_params = self.proxy_call_action("GetSystemInfo", arguments=arguments)

        (SystemInfo,) = out_params

        return SystemInfo


    def action_GetVirtualDevices(self):
        """
            Calls the GetVirtualDevices action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetVirtualDevices", arguments=arguments)

        (VirtualDeviceList,) = out_params

        return VirtualDeviceList
