"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class RemoteUIServerServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'RemoteUIServer' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:RemoteUIServer:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:RemoteUIServer'

