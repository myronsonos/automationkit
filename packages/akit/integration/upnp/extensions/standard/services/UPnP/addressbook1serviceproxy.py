"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class AddressBook1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'AddressBook1' service.
    """

    SERVICE_MANUFACTURER = 'UPnP'
    SERVICE_TYPE = 'urn:schemas-upnp-org:service:AddressBook:1'


    def action_Accept(self, RequestID, extract_returns=True):
        """
            Calls the Accept action.

            :returns: "result"
        """
        arguments = {
            "RequestID": RequestID,
        }

        out_params = self.proxy_call_action("Accept", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_FetchcontactInfo(self, Targetcontacts, ShareInfo, extract_returns=True):
        """
            Calls the FetchcontactInfo action.

            :returns: "result"
        """
        arguments = {
            "Targetcontacts": Targetcontacts,
            "ShareInfo": ShareInfo,
        }

        out_params = self.proxy_call_action("FetchcontactInfo", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_ImportContacts(self, NetworkAddressBookID, extract_returns=True):
        """
            Calls the ImportContacts action.

            :returns: "result"
        """
        arguments = {
            "NetworkAddressBookID": NetworkAddressBookID,
        }

        out_params = self.proxy_call_action("ImportContacts", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_Reject(self, RequestID, extract_returns=True):
        """
            Calls the Reject action.

            :returns: "result"
        """
        arguments = {
            "RequestID": RequestID,
        }

        out_params = self.proxy_call_action("Reject", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_RetrieveIncomingRequests(self, extract_returns=True):
        """
            Calls the RetrieveIncomingRequests action.

            :returns: "ActiveIncomingRequests"
        """
        arguments = { }

        out_params = self.proxy_call_action("RetrieveIncomingRequests", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("ActiveIncomingRequests",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_ShareContacts(self, SharedContacts, SharedInfo, TargetContacts, extract_returns=True):
        """
            Calls the ShareContacts action.

            :returns: "result"
        """
        arguments = {
            "SharedContacts": SharedContacts,
            "SharedInfo": SharedInfo,
            "TargetContacts": TargetContacts,
        }

        out_params = self.proxy_call_action("ShareContacts", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args


    def action_SharePCC(self, TargetContacts, ShareInfo, extract_returns=True):
        """
            Calls the SharePCC action.

            :returns: "result"
        """
        arguments = {
            "TargetContacts": TargetContacts,
            "ShareInfo": ShareInfo,
        }

        out_params = self.proxy_call_action("SharePCC", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("result",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args

