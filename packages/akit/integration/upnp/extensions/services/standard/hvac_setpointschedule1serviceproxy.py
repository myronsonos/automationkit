"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class HVAC_SetpointSchedule1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'HVAC_SetpointSchedule1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:HVAC_SetpointSchedule:1'
    SERVICE_ID = 'urn:schemas-upnp-org:service:HVAC_SetpointSchedule'


    def get_EventsPerDay(self):
        """
            Gets the "EventsPerDay" variable.
        """
        rval = self.proxy_get_variable_value("EventsPerDay")
        return rval


    def set_EventsPerDay(self, val):
        """
            Sets the "EventsPerDay" variable.
        """
        self.proxy_set_variable_value("EventsPerDay", val)
        return


    def action_GetEventsPerDay(self, SubmittedDayOfWeek):
        """
            Calls the GetEventsPerDay action.
        """
        arguments = {
            "SubmittedDayOfWeek": SubmittedDayOfWeek,
        }

        out_params = self.proxy_call_action("GetEventsPerDay", arguments=arguments)

        (CurrentEventsPerDay,) = out_params

        return CurrentEventsPerDay


    def action_SetEventParameters(self, SubmittedDayOfWeek, SubmittedEventName, NewStartTime, NewHeatingSetpoint, NewCoolingSetpoint):
        """
            Calls the SetEventParameters action.
        """
        arguments = {
            "SubmittedDayOfWeek": SubmittedDayOfWeek,
            "SubmittedEventName": SubmittedEventName,
            "NewStartTime": NewStartTime,
            "NewHeatingSetpoint": NewHeatingSetpoint,
            "NewCoolingSetpoint": NewCoolingSetpoint,
        }

        out_params = self.proxy_call_action("SetEventParameters", arguments=arguments)

        (result,) = out_params

        return result

