"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class SoftwareManagement1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'SoftwareManagement1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:SoftwareManagement:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:SoftwareManagement'


    def get_ActiveEUIDs(self):
        """
            Gets the "ActiveEUIDs" variable.
        """
        rval = self.proxy_get_variable_value("ActiveEUIDs")
        return rval


    def set_ActiveEUIDs(self, val):
        """
            Sets the "ActiveEUIDs" variable.
        """
        self.proxy_set_variable_value("ActiveEUIDs", val)
        return


    def get_DUIDs(self):
        """
            Gets the "DUIDs" variable.
        """
        rval = self.proxy_get_variable_value("DUIDs")
        return rval


    def set_DUIDs(self, val):
        """
            Sets the "DUIDs" variable.
        """
        self.proxy_set_variable_value("DUIDs", val)
        return


    def get_EUIDs(self):
        """
            Gets the "EUIDs" variable.
        """
        rval = self.proxy_get_variable_value("EUIDs")
        return rval


    def set_EUIDs(self, val):
        """
            Sets the "EUIDs" variable.
        """
        self.proxy_set_variable_value("EUIDs", val)
        return


    def get_ErrorEUIDs(self):
        """
            Gets the "ErrorEUIDs" variable.
        """
        rval = self.proxy_get_variable_value("ErrorEUIDs")
        return rval


    def set_ErrorEUIDs(self, val):
        """
            Sets the "ErrorEUIDs" variable.
        """
        self.proxy_set_variable_value("ErrorEUIDs", val)
        return


    def get_OperationIDs(self):
        """
            Gets the "OperationIDs" variable.
        """
        rval = self.proxy_get_variable_value("OperationIDs")
        return rval


    def set_OperationIDs(self, val):
        """
            Sets the "OperationIDs" variable.
        """
        self.proxy_set_variable_value("OperationIDs", val)
        return


    def get_RunningEUIDs(self):
        """
            Gets the "RunningEUIDs" variable.
        """
        rval = self.proxy_get_variable_value("RunningEUIDs")
        return rval


    def set_RunningEUIDs(self, val):
        """
            Sets the "RunningEUIDs" variable.
        """
        self.proxy_set_variable_value("RunningEUIDs", val)
        return


    def action_GetActiveEUIDs(self):
        """
            Calls the GetActiveEUIDs action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetActiveEUIDs", arguments=arguments)

        (ActiveEUIDs,) = out_params

        return ActiveEUIDs


    def action_GetDUIDs(self):
        """
            Calls the GetDUIDs action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDUIDs", arguments=arguments)

        (DUIDs,) = out_params

        return DUIDs


    def action_GetDUInfo(self, DUID):
        """
            Calls the GetDUInfo action.
        """
        arguments = {
            "DUID": DUID,
        }

        out_params = self.proxy_call_action("GetDUInfo", arguments=arguments)

        (DUName, DUVersion, DUType, DUState, DUURI,) = out_params

        return DUName, DUVersion, DUType, DUState, DUURI


    def action_GetEUIDs(self):
        """
            Calls the GetEUIDs action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetEUIDs", arguments=arguments)

        (EUIDs,) = out_params

        return EUIDs


    def action_GetEUInfo(self, EUID):
        """
            Calls the GetEUInfo action.
        """
        arguments = {
            "EUID": EUID,
        }

        out_params = self.proxy_call_action("GetEUInfo", arguments=arguments)

        (EUName, EUVersion, EURequestedState, EUExecutionState,) = out_params

        return EUName, EUVersion, EURequestedState, EUExecutionState


    def action_GetErrorEUIDs(self):
        """
            Calls the GetErrorEUIDs action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetErrorEUIDs", arguments=arguments)

        (ErrorEUIDs,) = out_params

        return ErrorEUIDs


    def action_GetOperationIDs(self):
        """
            Calls the GetOperationIDs action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetOperationIDs", arguments=arguments)

        (OperationIDs,) = out_params

        return OperationIDs


    def action_GetOperationInfo(self, OperationID):
        """
            Calls the GetOperationInfo action.
        """
        arguments = {
            "OperationID": OperationID,
        }

        out_params = self.proxy_call_action("GetOperationInfo", arguments=arguments)

        (OperationState, TargetedIDs, Action, ErrorDescription, AdditionalInfo,) = out_params

        return OperationState, TargetedIDs, Action, ErrorDescription, AdditionalInfo


    def action_GetRunningEUIDs(self):
        """
            Calls the GetRunningEUIDs action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetRunningEUIDs", arguments=arguments)

        (RunningEUIDs,) = out_params

        return RunningEUIDs


    def action_Install(self, DUURI, DUType, HandleDependencies):
        """
            Calls the Install action.
        """
        arguments = {
            "DUURI": DUURI,
            "DUType": DUType,
            "HandleDependencies": HandleDependencies,
        }

        out_params = self.proxy_call_action("Install", arguments=arguments)

        (OperationID,) = out_params

        return OperationID


    def action_Start(self, EUID, HandleDependencies):
        """
            Calls the Start action.
        """
        arguments = {
            "EUID": EUID,
            "HandleDependencies": HandleDependencies,
        }

        out_params = self.proxy_call_action("Start", arguments=arguments)

        (OperationID,) = out_params

        return OperationID


    def action_Stop(self, EUID, HandleDependencies):
        """
            Calls the Stop action.
        """
        arguments = {
            "EUID": EUID,
            "HandleDependencies": HandleDependencies,
        }

        out_params = self.proxy_call_action("Stop", arguments=arguments)

        (OperationID,) = out_params

        return OperationID


    def action_Uninstall(self, DUID, HandleDependencies):
        """
            Calls the Uninstall action.
        """
        arguments = {
            "DUID": DUID,
            "HandleDependencies": HandleDependencies,
        }

        out_params = self.proxy_call_action("Uninstall", arguments=arguments)

        (OperationID,) = out_params

        return OperationID


    def action_Update(self, DUID, NewDUURI, HandleDependencies):
        """
            Calls the Update action.
        """
        arguments = {
            "DUID": DUID,
            "NewDUURI": NewDUURI,
            "HandleDependencies": HandleDependencies,
        }

        out_params = self.proxy_call_action("Update", arguments=arguments)

        (OperationID,) = out_params

        return OperationID

