"""
.. module:: akit.integration.upnp.device.upnprootdevice
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the :class:`UpnpRootDevice` class and associated diagnostic.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>

"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@automationmojo.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = ""

import requests
import traceback

from akit.integration.upnp.protocols.msearch import MSearchKeys
from akit.integration.upnp.devices.upnpdevice import UpnpDevice
from akit.integration.upnp.xml.upnpdevice1 import UpnpDevice1Device, UpnpDevice1SpecVersion

class UpnpRootDevice(UpnpDevice):
    """
        The UPNP Root device is the base device for the hierarchy that is
        associated with a unique network devices location.  The :class:`UpnpRootDevice`
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

    def refresh_description(self, docNode, namespaces=None):
        """
        """
        try:
            specVerNode = docNode.find("specVersion", namespaces=namespaces)
            if specVerNode is not None:
                self._process_version_node(specVerNode, namespaces=namespaces)

            baseURLNode = docNode.find("URLBase", namespaces=namespaces)
            if baseURLNode is not None:
                self._process_urlbase_node(baseURLNode, namespaces=namespaces)

            devNode = docNode.find("device", namespaces=namespaces)
            if devNode is not None:
                self._process_device_node(devNode, namespaces=namespaces)
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