

import requests
import traceback

from xml.etree.ElementTree import fromstring as parsefromstring
from xml.etree.ElementTree import ElementTree

from akit.integration.upnp.protocols.msearch import MSearchKeys
from akit.integration.upnp.devices.upnpdevice import UpnpDevice
from akit.integration.upnp.xml.upnpdevice1 import UPNP_DEVICE1_NAMESPACE
from akit.integration.upnp.xml.upnpdevice1 import UpnpDevice1Device, UpnpDevice1SpecVersion

class UpnpRootDevice(UpnpDevice):
    """
        The UPNP Root device is the base device for the hierarchy that is
        associated with a unique network devices location.  The :class:`RootDevice`
        and its subdevices are linked by thier location url. 

        http://www.upnp.org/specs/arch/UPnP-arch-DeviceArchitecture-v1.0.pdf
    """

    def __init__(self):
        """
            Creates a root device object.
        """
        super(UpnpRootDevice, self).__init__()

        self._description = None
        self._specVersion = None
        self._urlBase = None
        return

    @property
    def description(self):
        return self._description

    @property
    def specVersion(self):
        return self._specVersion

    @property
    def URLBase(self):
        return self._urlBase

    def refresh_description(self):
        """
        """
        try:
            resp = requests.get(self._location)
            if resp.status_code == 200:
                xmlcontent = resp.content
                docNode = parsefromstring(xmlcontent)

                # {urn:schemas-upnp-org:device-1-0}root
                defaultns = {"": UPNP_DEVICE1_NAMESPACE}
                docTree = ElementTree(docNode)

                specVerNode = docTree.find("specVersion", namespaces=defaultns)
                if specVerNode is not None:
                    self._process_version_node(specVerNode, namespaces=defaultns)

                baseURLNode = docTree.find("URLBase", namespaces=defaultns)
                if baseURLNode is not None:
                    self._process_urlbase_node(baseURLNode, namespaces=defaultns)

                devNode = docTree.find("device", namespaces=defaultns)
                if devNode is not None:
                    self._process_device_node(devNode, namespaces=defaultns)
        except Exception as xcpt:
            err_msg = traceback.format_exc()
            print(err_msg)
            raise

        return

    def _process_device_node(self, devNode, namespaces=None):
        self._description = UpnpDevice1Device(devNode, namespaces=namespaces)
        return

    def _process_urlbase_node(self, urlBaseNode, namespaces=None):
        self._urlBase = urlBaseNode.text
        return

    def _process_version_node(self, verNode, namespaces=None):
        self._specVersion = UpnpDevice1SpecVersion(verNode, namespaces=namespaces)
        return