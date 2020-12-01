"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class QPlay1ServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'QPlay1' service.
    """

    SERVICE_MANUFACTURER = 'SonosInc'
    SERVICE_TYPE = 'urn:schemas-tencent-com:service:QPlay:1'

    SERVICE_EVENT_VARIABLES = {}

    def action_QPlayAuth(self, Seed, extract_returns=True):
        """
            Calls the QPlayAuth action.

            :returns: "Code", "MID", "DID"
        """
        arguments = {
            "Seed": Seed,
        }

        out_params = self._proxy_call_action("QPlayAuth", arguments=arguments)

        rtn_args = out_params
        if extract_returns:
            rtn_args = [out_params[k] for k in ("Code", "MID", "DID",)]
            if len(rtn_args) == 1:
                rtn_args = rtn_args[0]

        return rtn_args
