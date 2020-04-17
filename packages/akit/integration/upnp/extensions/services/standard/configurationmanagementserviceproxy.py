"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class ConfigurationManagementServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'ConfigurationManagement' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:ConfigurationManagement:2'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:ConfigurationManagement'


    def get_AlarmsEnabled(self):
        """
            Gets the "AlarmsEnabled" variable.
        """
        rval = self.proxy_get_variable_value("AlarmsEnabled")
        return rval


    def set_AlarmsEnabled(self, val):
        """
            Sets the "AlarmsEnabled" variable.
        """
        self.proxy_set_variable_value("AlarmsEnabled", val)
        return


    def get_AttributeValuesUpdate(self):
        """
            Gets the "AttributeValuesUpdate" variable.
        """
        rval = self.proxy_get_variable_value("AttributeValuesUpdate")
        return rval


    def set_AttributeValuesUpdate(self, val):
        """
            Sets the "AttributeValuesUpdate" variable.
        """
        self.proxy_set_variable_value("AttributeValuesUpdate", val)
        return


    def get_ConfigurationUpdate(self):
        """
            Gets the "ConfigurationUpdate" variable.
        """
        rval = self.proxy_get_variable_value("ConfigurationUpdate")
        return rval


    def set_ConfigurationUpdate(self, val):
        """
            Sets the "ConfigurationUpdate" variable.
        """
        self.proxy_set_variable_value("ConfigurationUpdate", val)
        return


    def get_CurrentConfigurationVersion(self):
        """
            Gets the "CurrentConfigurationVersion" variable.
        """
        rval = self.proxy_get_variable_value("CurrentConfigurationVersion")
        return rval


    def set_CurrentConfigurationVersion(self, val):
        """
            Sets the "CurrentConfigurationVersion" variable.
        """
        self.proxy_set_variable_value("CurrentConfigurationVersion", val)
        return


    def get_InconsistentStatus(self):
        """
            Gets the "InconsistentStatus" variable.
        """
        rval = self.proxy_get_variable_value("InconsistentStatus")
        return rval


    def set_InconsistentStatus(self, val):
        """
            Sets the "InconsistentStatus" variable.
        """
        self.proxy_set_variable_value("InconsistentStatus", val)
        return


    def get_SupportedDataModelsUpdate(self):
        """
            Gets the "SupportedDataModelsUpdate" variable.
        """
        rval = self.proxy_get_variable_value("SupportedDataModelsUpdate")
        return rval


    def set_SupportedDataModelsUpdate(self, val):
        """
            Sets the "SupportedDataModelsUpdate" variable.
        """
        self.proxy_set_variable_value("SupportedDataModelsUpdate", val)
        return


    def get_SupportedParametersUpdate(self):
        """
            Gets the "SupportedParametersUpdate" variable.
        """
        rval = self.proxy_get_variable_value("SupportedParametersUpdate")
        return rval


    def set_SupportedParametersUpdate(self, val):
        """
            Sets the "SupportedParametersUpdate" variable.
        """
        self.proxy_set_variable_value("SupportedParametersUpdate", val)
        return


    def action_CreateInstance(self, MultiInstanceName, ChildrenInitialization):
        """
            Calls the CreateInstance action.
        """
        arguments = {
            "MultiInstanceName": MultiInstanceName,
            "ChildrenInitialization": ChildrenInitialization,
        }

        out_params = self.proxy_call_action("CreateInstance", arguments=arguments)

        (InstanceIdentifier, Status,) = out_params

        return InstanceIdentifier, Status


    def action_DeleteInstance(self, InstanceIdentifier):
        """
            Calls the DeleteInstance action.
        """
        arguments = {
            "InstanceIdentifier": InstanceIdentifier,
        }

        out_params = self.proxy_call_action("DeleteInstance", arguments=arguments)

        (Status,) = out_params

        return Status


    def action_GetACLData(self, StartingNodes):
        """
            Calls the GetACLData action.
        """
        arguments = {
            "StartingNodes": StartingNodes,
        }

        out_params = self.proxy_call_action("GetACLData", arguments=arguments)

        (ACL,) = out_params

        return ACL


    def action_GetAlarmsEnabled(self):
        """
            Calls the GetAlarmsEnabled action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetAlarmsEnabled", arguments=arguments)

        (StateVariableValue,) = out_params

        return StateVariableValue


    def action_GetAttributeValuesUpdate(self):
        """
            Calls the GetAttributeValuesUpdate action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetAttributeValuesUpdate", arguments=arguments)

        (StateVariableValue,) = out_params

        return StateVariableValue


    def action_GetAttributes(self, Parameters):
        """
            Calls the GetAttributes action.
        """
        arguments = {
            "Parameters": Parameters,
        }

        out_params = self.proxy_call_action("GetAttributes", arguments=arguments)

        (NodeAttributeValueList,) = out_params

        return NodeAttributeValueList


    def action_GetConfigurationUpdate(self):
        """
            Calls the GetConfigurationUpdate action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetConfigurationUpdate", arguments=arguments)

        (StateVariableValue,) = out_params

        return StateVariableValue


    def action_GetCurrentConfigurationVersion(self):
        """
            Calls the GetCurrentConfigurationVersion action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetCurrentConfigurationVersion", arguments=arguments)

        (StateVariableValue,) = out_params

        return StateVariableValue


    def action_GetInconsistentStatus(self):
        """
            Calls the GetInconsistentStatus action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetInconsistentStatus", arguments=arguments)

        (StateVariableValue,) = out_params

        return StateVariableValue


    def action_GetInstances(self, StartingNode, SearchDepth):
        """
            Calls the GetInstances action.
        """
        arguments = {
            "StartingNode": StartingNode,
            "SearchDepth": SearchDepth,
        }

        out_params = self.proxy_call_action("GetInstances", arguments=arguments)

        (Result,) = out_params

        return Result


    def action_GetSelectedValues(self, StartingNode, Filter):
        """
            Calls the GetSelectedValues action.
        """
        arguments = {
            "StartingNode": StartingNode,
            "Filter": Filter,
        }

        out_params = self.proxy_call_action("GetSelectedValues", arguments=arguments)

        (ParameterValueList,) = out_params

        return ParameterValueList


    def action_GetSupportedDataModels(self):
        """
            Calls the GetSupportedDataModels action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetSupportedDataModels", arguments=arguments)

        (SupportedDataModels,) = out_params

        return SupportedDataModels


    def action_GetSupportedDataModelsUpdate(self):
        """
            Calls the GetSupportedDataModelsUpdate action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetSupportedDataModelsUpdate", arguments=arguments)

        (StateVariableValue,) = out_params

        return StateVariableValue


    def action_GetSupportedParameters(self, StartingNode, SearchDepth):
        """
            Calls the GetSupportedParameters action.
        """
        arguments = {
            "StartingNode": StartingNode,
            "SearchDepth": SearchDepth,
        }

        out_params = self.proxy_call_action("GetSupportedParameters", arguments=arguments)

        (Result,) = out_params

        return Result


    def action_GetSupportedParametersUpdate(self):
        """
            Calls the GetSupportedParametersUpdate action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetSupportedParametersUpdate", arguments=arguments)

        (StateVariableValue,) = out_params

        return StateVariableValue


    def action_GetValues(self, Parameters):
        """
            Calls the GetValues action.
        """
        arguments = {
            "Parameters": Parameters,
        }

        out_params = self.proxy_call_action("GetValues", arguments=arguments)

        (ParameterValueList,) = out_params

        return ParameterValueList


    def action_SetAlarmsEnabled(self, StateVariableValue):
        """
            Calls the SetAlarmsEnabled action.
        """
        arguments = {
            "StateVariableValue": StateVariableValue,
        }

        out_params = self.proxy_call_action("SetAlarmsEnabled", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetAttributes(self, NodeAttributeValueList):
        """
            Calls the SetAttributes action.
        """
        arguments = {
            "NodeAttributeValueList": NodeAttributeValueList,
        }

        out_params = self.proxy_call_action("SetAttributes", arguments=arguments)

        (Status,) = out_params

        return Status


    def action_SetValues(self, ParameterValueList):
        """
            Calls the SetValues action.
        """
        arguments = {
            "ParameterValueList": ParameterValueList,
        }

        out_params = self.proxy_call_action("SetValues", arguments=arguments)

        (Status,) = out_params

        return Status

