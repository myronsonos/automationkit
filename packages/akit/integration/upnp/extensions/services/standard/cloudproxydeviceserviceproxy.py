"""

    NOTE: This is a code generated file.  This file should not be edited directly.
"""



from akit.extensible import LoadableExtension
from akit.integration.upnp.services.upnpserviceproxy import UpnpServiceProxy

class CloudProxyDeviceServiceProxy(UpnpServiceProxy, LoadableExtension):
    """
        This is a code generated proxy class to the 'CloudProxyDevice' service.
    """

    SERVICE_TYPE = 'urn:schemas-upnp-org:service:CloudProxyDevice:1'
    SERVICE_NAME = 'urn:schemas-upnp-org:service:CloudProxyDevice'

