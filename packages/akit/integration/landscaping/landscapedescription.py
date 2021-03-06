"""
.. module:: landscapedescription
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the :class:`TestLandscape` class and associated diagnostic.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>

"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"


import os
import yaml

from akit.exceptions import AKitConfigurationError

from akit.integration.clients.linuxclientmixin import LinuxClientMixIn
from akit.integration.clients.windowsclientmixin import WindowsClientMixIn
from akit.integration.cluster.clustermixin import ClusterMixIn
from akit.integration.credentials.sshcredential import SshCredential

# Declare a literal UpnpFacotry type for use with typing
# to allow for typing without creating circular reference
LITERAL_LANDSCAPE_TYPE = 'akit.integration.landscaping.landscape.Landscape'

class LandscapeDescription:
    """
        The base class for all derived :class:`LandscapeDescription` objects.  The
        :class:`LandscapeDescription` is used to load a description of the entities
        and resources in the tests landscape that will be used by the tests.
    """

    @classmethod
    def register_integration_points(cls, landscape: LITERAL_LANDSCAPE_TYPE):
        """
            Method called during the test framework ininitalization in order to register integartion mixins and their
            associated roles with the test framework.

            :param landscape: A reference to the landscape singleton object.  We pass in the landscape parameter in order
                              to eliminate the need to import the landscape module which would cause a circular reference.
            :type landscape: Landscape
        """
        landscape.register_integration_point("primary-linux", LinuxClientMixIn)
        landscape.register_integration_point("secondary-linux", LinuxClientMixIn)

        landscape.register_integration_point("primary-windows", WindowsClientMixIn)
        landscape.register_integration_point("secondary-windows", WindowsClientMixIn)

        landscape.register_integration_point("primary-cluster", ClusterMixIn)
        landscape.register_integration_point("secondary-cluster", ClusterMixIn)
        return

    def load(self, landscape_file: str):
        """
            Loads and validates the landscape description file.
        """
        landscape_info = None

        with open(landscape_file, 'r') as lf:
            lfcontent = lf.read()
            landscape_info = yaml.safe_load(lfcontent)

        errors = self.validate_landscape(landscape_info)

        if len(errors) > 0:
            errmsg_lines = [
                "ERROR Landscape validation failures:"
            ]
            for err in errors:
                errmsg_lines.append("    %s" % err)

            errmsg = os.linesep.join(errmsg_lines)
            raise AKitConfigurationError(errmsg)

        return landscape_info

    def validate_landscape(self, landscape_info):
        """
            Validates the landscape description file.
        """
        errors = []

        if "pod" in landscape_info:
            podinfo = landscape_info["pod"]
            if "devices" in podinfo:
                devices_list = podinfo["devices"]
                child_errors = self.validate_devices_list(devices_list, prefix="")
                errors.extend(child_errors)
            else:
                errors.append(["/pod/devices", "A pod description requires a 'devices' list data member."])
        else:
            errors.append(["/pod", "A landscape description requires a 'pod' data member."])

        return errors

    def validate_devices_list(self, devlist, prefix=""): # pylint: disable=unused-argument
        """
            Verifies that all the devices in a device list are valid and returns a list of errors found.
        """
        errors = []

        for devidx, devinfo in enumerate(devlist):
            item_prefix = "/devices[%d]" % devidx
            child_errors = self.validate_device_info(devinfo, prefix=item_prefix)
            errors.extend(child_errors)

        return errors

    def validate_device_info(self, devinfo, prefix=""):
        """
            Verifies that a device info dictionary has the required common fields and also has valid
            information for the declared device type.  Returns a list of errors found.

            Required Common Fields:
                deviceType

            Valid Device Types:
                network/ssh
                network/upnp
        """
        errors = []

        if "deviceType" in devinfo:
            deviceType = devinfo["deviceType"]
            if deviceType == "network/upnp":
                if "upnp" in devinfo:
                    upnpinfo = devinfo["upnp"]
                    child_errors = self.validate_upnp_info(upnpinfo, prefix=prefix + "/upnp")
                    errors.extend(child_errors)
                else:
                    errors.append([prefix + "upnp", "Device type 'network/upnp' must have a 'upnp' data member."])
            if deviceType == "network/ssh":
                if "host" not in devinfo:
                    errors.append("SSH Devices must have a 'host' field.")
                if "credentials" not in devinfo:
                    errors.append("Device type 'network/ssh' must have a 'credentials' data member.")
        else:
            errors.append([prefix + "deviceType", "Device information is missing the required 'deviceType' data member."])

        return errors

    def validate_upnp_info(self, upnpinfo, prefix=""): # pylint: disable=no-self-use,unused-argument
        """
            Verifies that a upnp info dictionary has valid data member combinations and can be used. Returns a
            list of errors found.
        """
        errors = []

        if "USN" not in upnpinfo:
            errors.append([prefix + "USN", "UPnP information is missing a 'USN' data member."])
        if "modelNumber" not in upnpinfo:
            errors.append([prefix + "modelNumber", "UPnP information is missing a 'modelNumber' data member."])
        if "modelName" not in upnpinfo:
            errors.append([prefix + "modelName", "UPnP information is missing a 'modelName' data member."])

        return errors
