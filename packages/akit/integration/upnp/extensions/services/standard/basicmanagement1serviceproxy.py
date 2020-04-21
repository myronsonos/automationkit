"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class BasicManagement1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'BasicManagement1' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:BasicManagement:1'
    SERVICE_ID = 'urn:schemas-upnp-org:service:BasicManagement'


    def get_ActiveTestIDs(self):
        """
            Gets the "ActiveTestIDs" variable.
        """
        rval = self.proxy_get_variable_value("ActiveTestIDs")
        return rval


    def set_ActiveTestIDs(self, val):
        """
            Sets the "ActiveTestIDs" variable.
        """
        self.proxy_set_variable_value("ActiveTestIDs", val)
        return


    def get_DeviceStatus(self):
        """
            Gets the "DeviceStatus" variable.
        """
        rval = self.proxy_get_variable_value("DeviceStatus")
        return rval


    def set_DeviceStatus(self, val):
        """
            Sets the "DeviceStatus" variable.
        """
        self.proxy_set_variable_value("DeviceStatus", val)
        return


    def get_LogURIs(self):
        """
            Gets the "LogURIs" variable.
        """
        rval = self.proxy_get_variable_value("LogURIs")
        return rval


    def set_LogURIs(self, val):
        """
            Sets the "LogURIs" variable.
        """
        self.proxy_set_variable_value("LogURIs", val)
        return


    def get_SequenceMode(self):
        """
            Gets the "SequenceMode" variable.
        """
        rval = self.proxy_get_variable_value("SequenceMode")
        return rval


    def set_SequenceMode(self, val):
        """
            Sets the "SequenceMode" variable.
        """
        self.proxy_set_variable_value("SequenceMode", val)
        return


    def action_BaselineReset(self):
        """
            Calls the BaselineReset action.
        """
        arguments = { }

        out_params = self.proxy_call_action("BaselineReset", arguments=arguments)

        (RebootStatus,) = out_params

        return RebootStatus


    def action_CancelTest(self, TestID):
        """
            Calls the CancelTest action.
        """
        arguments = {
            "TestID": TestID,
        }

        out_params = self.proxy_call_action("CancelTest", arguments=arguments)

        (result,) = out_params

        return result


    def action_GetActiveTestIDs(self):
        """
            Calls the GetActiveTestIDs action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetActiveTestIDs", arguments=arguments)

        (TestIDs,) = out_params

        return TestIDs


    def action_GetDeviceStatus(self):
        """
            Calls the GetDeviceStatus action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetDeviceStatus", arguments=arguments)

        (DeviceStatus,) = out_params

        return DeviceStatus


    def action_GetInterfaceResetResult(self, TestID):
        """
            Calls the GetInterfaceResetResult action.
        """
        arguments = {
            "TestID": TestID,
        }

        out_params = self.proxy_call_action("GetInterfaceResetResult", arguments=arguments)

        (Status, AdditionalInfo, NumberOfSuccesses, NumberOfFailures,) = out_params

        return Status, AdditionalInfo, NumberOfSuccesses, NumberOfFailures


    def action_GetLogInfo(self, LogURI):
        """
            Calls the GetLogInfo action.
        """
        arguments = {
            "LogURI": LogURI,
        }

        out_params = self.proxy_call_action("GetLogInfo", arguments=arguments)

        (Configurable, Enabled, LogLevel, LogURL, MaxSize, LastChange,) = out_params

        return Configurable, Enabled, LogLevel, LogURL, MaxSize, LastChange


    def action_GetLogURIs(self):
        """
            Calls the GetLogURIs action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetLogURIs", arguments=arguments)

        (LogURIs,) = out_params

        return LogURIs


    def action_GetNSLookupResult(self, TestID):
        """
            Calls the GetNSLookupResult action.
        """
        arguments = {
            "TestID": TestID,
        }

        out_params = self.proxy_call_action("GetNSLookupResult", arguments=arguments)

        (Status, AdditionalInfo, SuccessCount, Result,) = out_params

        return Status, AdditionalInfo, SuccessCount, Result


    def action_GetPingResult(self, TestID):
        """
            Calls the GetPingResult action.
        """
        arguments = {
            "TestID": TestID,
        }

        out_params = self.proxy_call_action("GetPingResult", arguments=arguments)

        (Status, AdditionalInfo, SuccessCount, FailureCount, AverageResponseTime, MinimumResponseTime, MaximumResponseTime,) = out_params

        return Status, AdditionalInfo, SuccessCount, FailureCount, AverageResponseTime, MinimumResponseTime, MaximumResponseTime


    def action_GetSelfTestResult(self, TestID):
        """
            Calls the GetSelfTestResult action.
        """
        arguments = {
            "TestID": TestID,
        }

        out_params = self.proxy_call_action("GetSelfTestResult", arguments=arguments)

        (Status, AdditionalInfo,) = out_params

        return Status, AdditionalInfo


    def action_GetSequenceMode(self):
        """
            Calls the GetSequenceMode action.
        """
        arguments = { }

        out_params = self.proxy_call_action("GetSequenceMode", arguments=arguments)

        (SequenceMode,) = out_params

        return SequenceMode


    def action_GetTestInfo(self, TestID):
        """
            Calls the GetTestInfo action.
        """
        arguments = {
            "TestID": TestID,
        }

        out_params = self.proxy_call_action("GetTestInfo", arguments=arguments)

        (Type, State,) = out_params

        return Type, State


    def action_GetTracerouteResult(self, TestID):
        """
            Calls the GetTracerouteResult action.
        """
        arguments = {
            "TestID": TestID,
        }

        out_params = self.proxy_call_action("GetTracerouteResult", arguments=arguments)

        (Status, AdditionalInfo, ResponseTime, HopHosts,) = out_params

        return Status, AdditionalInfo, ResponseTime, HopHosts


    def action_InterfaceReset(self, Interfaces):
        """
            Calls the InterfaceReset action.
        """
        arguments = {
            "Interfaces": Interfaces,
        }

        out_params = self.proxy_call_action("InterfaceReset", arguments=arguments)

        (TestID,) = out_params

        return TestID


    def action_NSLookup(self, HostName, DNSServer, NumberOfRepetitions, Timeout):
        """
            Calls the NSLookup action.
        """
        arguments = {
            "HostName": HostName,
            "DNSServer": DNSServer,
            "NumberOfRepetitions": NumberOfRepetitions,
            "Timeout": Timeout,
        }

        out_params = self.proxy_call_action("NSLookup", arguments=arguments)

        (TestID,) = out_params

        return TestID


    def action_Ping(self, Host, NumberOfRepetitions, Timeout, DataBlockSize, DSCP):
        """
            Calls the Ping action.
        """
        arguments = {
            "Host": Host,
            "NumberOfRepetitions": NumberOfRepetitions,
            "Timeout": Timeout,
            "DataBlockSize": DataBlockSize,
            "DSCP": DSCP,
        }

        out_params = self.proxy_call_action("Ping", arguments=arguments)

        (TestID,) = out_params

        return TestID


    def action_Reboot(self):
        """
            Calls the Reboot action.
        """
        arguments = { }

        out_params = self.proxy_call_action("Reboot", arguments=arguments)

        (RebootStatus,) = out_params

        return RebootStatus


    def action_SelfTest(self):
        """
            Calls the SelfTest action.
        """
        arguments = { }

        out_params = self.proxy_call_action("SelfTest", arguments=arguments)

        (TestID,) = out_params

        return TestID


    def action_SetLogInfo(self, LogURI, Enabled, LogLevel):
        """
            Calls the SetLogInfo action.
        """
        arguments = {
            "LogURI": LogURI,
            "Enabled": Enabled,
            "LogLevel": LogLevel,
        }

        out_params = self.proxy_call_action("SetLogInfo", arguments=arguments)

        (result,) = out_params

        return result


    def action_SetSequenceMode(self, NewSequenceMode):
        """
            Calls the SetSequenceMode action.
        """
        arguments = {
            "NewSequenceMode": NewSequenceMode,
        }

        out_params = self.proxy_call_action("SetSequenceMode", arguments=arguments)

        (OldSequenceMode,) = out_params

        return OldSequenceMode


    def action_Traceroute(self, Host, Timeout, DataBlockSize, MaxHopCount, DSCP):
        """
            Calls the Traceroute action.
        """
        arguments = {
            "Host": Host,
            "Timeout": Timeout,
            "DataBlockSize": DataBlockSize,
            "MaxHopCount": MaxHopCount,
            "DSCP": DSCP,
        }

        out_params = self.proxy_call_action("Traceroute", arguments=arguments)

        (TestID,) = out_params

        return TestID

