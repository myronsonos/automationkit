"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class FeederServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'Feeder' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:Feeder:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:Feeder'


    def get_EntireDocument(self):
        """
            Gets the "EntireDocument" variable.
        """
        rval = self.proxy_get_variable_value("EntireDocument")
        return rval


    def set_EntireDocument(self, val):
        """
            Sets the "EntireDocument" variable.
        """
        self.proxy_set_variable_value("EntireDocument", val)
        return


    def get_FailureCode(self):
        """
            Gets the "FailureCode" variable.
        """
        rval = self.proxy_get_variable_value("FailureCode")
        return rval


    def set_FailureCode(self, val):
        """
            Sets the "FailureCode" variable.
        """
        self.proxy_set_variable_value("FailureCode", val)
        return


    def get_FeederMode(self):
        """
            Gets the "FeederMode" variable.
        """
        rval = self.proxy_get_variable_value("FeederMode")
        return rval


    def set_FeederMode(self, val):
        """
            Sets the "FeederMode" variable.
        """
        self.proxy_set_variable_value("FeederMode", val)
        return


    def get_InputJustification(self):
        """
            Gets the "InputJustification" variable.
        """
        rval = self.proxy_get_variable_value("InputJustification")
        return rval


    def set_InputJustification(self, val):
        """
            Sets the "InputJustification" variable.
        """
        self.proxy_set_variable_value("InputJustification", val)
        return


    def get_JobID(self):
        """
            Gets the "JobID" variable.
        """
        rval = self.proxy_get_variable_value("JobID")
        return rval


    def set_JobID(self, val):
        """
            Sets the "JobID" variable.
        """
        self.proxy_set_variable_value("JobID", val)
        return


    def get_Model(self):
        """
            Gets the "Model" variable.
        """
        rval = self.proxy_get_variable_value("Model")
        return rval


    def set_Model(self, val):
        """
            Sets the "Model" variable.
        """
        self.proxy_set_variable_value("Model", val)
        return


    def get_MorePages(self):
        """
            Gets the "MorePages" variable.
        """
        rval = self.proxy_get_variable_value("MorePages")
        return rval


    def set_MorePages(self, val):
        """
            Sets the "MorePages" variable.
        """
        self.proxy_set_variable_value("MorePages", val)
        return


    def get_SheetHeight(self):
        """
            Gets the "SheetHeight" variable.
        """
        rval = self.proxy_get_variable_value("SheetHeight")
        return rval


    def set_SheetHeight(self, val):
        """
            Sets the "SheetHeight" variable.
        """
        self.proxy_set_variable_value("SheetHeight", val)
        return


    def get_SheetWidth(self):
        """
            Gets the "SheetWidth" variable.
        """
        rval = self.proxy_get_variable_value("SheetWidth")
        return rval


    def set_SheetWidth(self, val):
        """
            Sets the "SheetWidth" variable.
        """
        self.proxy_set_variable_value("SheetWidth", val)
        return


    def get_State(self):
        """
            Gets the "State" variable.
        """
        rval = self.proxy_get_variable_value("State")
        return rval


    def set_State(self, val):
        """
            Sets the "State" variable.
        """
        self.proxy_set_variable_value("State", val)
        return


    def get_Timeout(self):
        """
            Gets the "Timeout" variable.
        """
        rval = self.proxy_get_variable_value("Timeout")
        return rval


    def set_Timeout(self, val):
        """
            Sets the "Timeout" variable.
        """
        self.proxy_set_variable_value("Timeout", val)
        return


    def action_Eject(self, JobIDIn, EntireDocumentIn):
        """
            Calls the Eject action.
        """
        arguments = {
            "JobIDIn": JobIDIn,
            "EntireDocumentIn": EntireDocumentIn,
        }

        out_params = self.proxy_call_action("Eject", arguments=arguments)

        (StateOut,) = out_params

        return StateOut


    def action_GetFeederMode(self):
        """
            Calls the GetFeederMode action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetFeederMode", arguments=arguments)

        (FeederModeOut,) = out_params

        return FeederModeOut


    def action_GetState(self):
        """
            Calls the GetState action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetState", arguments=arguments)

        (StateOut, MorePagesOut, FailureCodeOut,) = out_params

        return StateOut, MorePagesOut, FailureCodeOut


    def action_Load(self, JobIDIn):
        """
            Calls the Load action.
        """
        arguments = {
            "JobIDIn": JobIDIn,
        }

        out_params = self.proxy_call_action("Load", arguments=arguments)

        (StateOut,) = out_params

        return StateOut


    def action_Reset(self, JobIDIn):
        """
            Calls the Reset action.
        """
        arguments = {
            "JobIDIn": JobIDIn,
        }

        out_params = self.proxy_call_action("Reset", arguments=arguments)

        (StateOut,) = out_params

        return StateOut


    def action_SetFeederMode(self, JobIDIn, FeederModeIn):
        """
            Calls the SetFeederMode action.
        """
        arguments = {
            "JobIDIn": JobIDIn,
            "FeederModeIn": FeederModeIn,
        }

        out_params = self.proxy_call_action("SetFeederMode", arguments=arguments)

        (result,) = out_params

        return result

