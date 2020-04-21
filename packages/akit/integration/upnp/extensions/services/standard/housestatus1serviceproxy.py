"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class HouseStatus1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'HouseStatus1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:HouseStatus:1'
    SERVICE_ID = 'urn:schemas-upnp-org:service:HouseStatus'


    def get_ActivityLevel(self):
        """
            Gets the "ActivityLevel" variable.
        """
        rval = self.proxy_get_variable_value("ActivityLevel")
        return rval


    def set_ActivityLevel(self, val):
        """
            Sets the "ActivityLevel" variable.
        """
        self.proxy_set_variable_value("ActivityLevel", val)
        return


    def get_DormancyLevel(self):
        """
            Gets the "DormancyLevel" variable.
        """
        rval = self.proxy_get_variable_value("DormancyLevel")
        return rval


    def set_DormancyLevel(self, val):
        """
            Sets the "DormancyLevel" variable.
        """
        self.proxy_set_variable_value("DormancyLevel", val)
        return


    def get_OccupancyState(self):
        """
            Gets the "OccupancyState" variable.
        """
        rval = self.proxy_get_variable_value("OccupancyState")
        return rval


    def set_OccupancyState(self, val):
        """
            Sets the "OccupancyState" variable.
        """
        self.proxy_set_variable_value("OccupancyState", val)
        return


    def action_GetActivityLevel(self):
        """
            Calls the GetActivityLevel action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetActivityLevel", arguments=arguments)

        (CurrentActivityLevel,) = out_params

        return CurrentActivityLevel


    def action_GetDormancyLevel(self):
        """
            Calls the GetDormancyLevel action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDormancyLevel", arguments=arguments)

        (CurrentDormancyLevel,) = out_params

        return CurrentDormancyLevel


    def action_GetOccupancyState(self):
        """
            Calls the GetOccupancyState action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetOccupancyState", arguments=arguments)

        (CurrentOccupancyState,) = out_params

        return CurrentOccupancyState


    def action_SetActivityLevel(self, NewActivityLevel):
        """
            Calls the SetActivityLevel action.
        """
        arguments = {
            "NewActivityLevel": NewActivityLevel,
        }

        out_params = self.proxy_call_action("SetActivityLevel", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetDormancyLevel(self, NewDormancyLevel):
        """
            Calls the SetDormancyLevel action.
        """
        arguments = {
            "NewDormancyLevel": NewDormancyLevel,
        }

        out_params = self.proxy_call_action("SetDormancyLevel", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetOccupancyState(self, NewOccupancyState):
        """
            Calls the SetOccupancyState action.
        """
        arguments = {
            "NewOccupancyState": NewOccupancyState,
        }

        out_params = self.proxy_call_action("SetOccupancyState", arguments=arguments)

        (result,) = out_params

        return result

