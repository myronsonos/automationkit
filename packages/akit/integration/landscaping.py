"""
.. module:: akit.integration.landscape
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

import inspect
import json
import os
import traceback

import pprint

from akit.compat import import_by_name
from akit.environment.variables import VARIABLES
from akit.environment.context import Context
from akit.exceptions import AKitConfigurationError, AKitSemanticError
from akit.paths import get_expanded_path

from akit.integration.coordinators.sshpoolcoordinator import SshPoolCoordinator
from akit.integration.coordinators.upnpcoordinator import UpnpCoordinator

from akit.integration.clients.linuxclientmixin import LinuxClientMixIn
from akit.integration.clients.windowsclientmixin import WindowsClientMixIn
from akit.integration.cluster.clustermixin import ClusterMixIn

from akit.xformatting import split_and_indent_lines
from akit.xlogging.foundations import getAutomatonKitLogger


class LandscapeDescription:
    """
        The base class for all derived :class:`LandscapeDescription` objects.  The
        :class:`LandscapeDescription` is used to load a description of the entities
        and resources in the tests landscape that will be used by the tests.
    """

    @classmethod
    def register_integration_points(cls, landscape):
        landscape.register_integration_point("primary-linux", LinuxClientMixIn)
        landscape.register_integration_point("secondary-linux", LinuxClientMixIn)

        landscape.register_integration_point("primary-windows", WindowsClientMixIn)
        landscape.register_integration_point("secondary-windows", WindowsClientMixIn)

        landscape.register_integration_point("primary-cluster", ClusterMixIn)
        landscape.register_integration_point("secondary-cluster", ClusterMixIn)
        return

    def load(self, landscape_file):
        landscape_info = None

        with open(landscape_file, 'r') as lf:
            lfcontent = lf.read()
            landscape_info = json.loads(lfcontent)

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

    def validate_devices_list(self, devlist, prefix=""):
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
                    if "ssh" in devinfo:
                        sshinfo = devinfo["ssh"]
                        child_errors = self.validate_ssh_info(sshinfo, require_host=False, prefix=prefix + "/ssh")
                        errors.extend(child_errors)
                else:
                    errors.append([prefix + "upnp", "Device type 'network/upnp' must have a 'upnp' data member."])
            if deviceType == "network/ssh":
                if "ssh" in devinfo:
                    sshinfo = devinfo["ssh"]
                    child_errors = self.validate_ssh_info(sshinfo, prefix=prefix + "/ssh")
                    errors.extend(child_errors)
                else:
                    errors.append([prefix + "ssh", "Device type 'network/ssh' must have a 'ssh' data member."])
        else:
            errors.append([prefix + "deviceType", "Device information is missing the required 'deviceType' data member."])

        return errors

    def validate_ssh_info(self, sshinfo, require_host=True, prefix=""):
        """
            Verifies that a ssh info dictionary has valid data member combinations and can be used. Returns a
            list of errors found.
        """
        errors = []

        if require_host and "host" not in sshinfo:
            errors.append([prefix + "host", "SSH information is missing a 'host' data member."])
        if "username" not in sshinfo:
            errors.append([prefix + "username", "SSH information is missing a 'username' data member."])

        if not ("password" in sshinfo or "keyfile" in sshinfo):
            errors.append([prefix + "password", "SSH information is missing a 'password' or 'keyfile' data member."])

        return errors

    def validate_upnp_info(self, upnpinfo, prefix=""):
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
    

class Landscape:
    """
        The base class for all derived :class:`Landscape` objects.  The :class:`Landscape`
        object is a singleton object that provides access to the resources and test
        environment level methods.
    """
    landscape_description = LandscapeDescription

    _landscape_type = None
    _instance = None
    _initialized = False

    def __new__(cls):
        """
            Constructs new instances of the Landscape object from the :class:`Landscape`
            type or from a derived type that is found in the module specified in the
            :module:`akit.environment.variables` module or by setting the
            'AKIT_LANDSCAPE_MODULE' environment variable.
        """
        if cls._instance is None:
            if cls._landscape_type is None:
                cls._instance = super(Landscape, cls).__new__(cls)
            else:
                cls._instance = super(Landscape, cls._landscape_type).__new__(cls._landscape_type)
            # Put any initialization here.
        return cls._instance
        
    def __init__(self):
        """
            Initializes the Singleton initializer class
        """
        this_cls = type(self)
        if not this_cls._initialized:
            this_cls._initialized = True
            self._landscape_info = None
            self._logger = getAutomatonKitLogger()
            self._has_upnp_devices = False
            self._has_ssh_devices = False
            self._upnp_coord = None
            self._ssh_coord = None
            self.initialize()
        return

    @property
    def name(self):
        lname = None
        if "name" in self.landscape_info:
            lname = self.landscape_info["name"]
        return lname

    @property
    def has_ssh_devices(self):
        return self._has_ssh_devices

    @property
    def has_upnp_devices(self):
        return self._has_upnp_devices

    @property
    def landscape_info(self):
        return self._landscape_info

    @property
    def ssh_coord(self):
        return self._ssh_coord

    @property
    def upnp_coord(self):
        return self._upnp_coord

    @property
    def databases(self):
        """
            Returns the database configuration information from the landscape file.
        """
        db_info = self.landscape_info["databases"]
        return db_info

    def get_devices(self):
        """
            Returns the list of devices from the landscape.  This will
            skip any device that has a "skip": true member.
        """
        device_list = []

        pod_info = self.landscape_info["pod"]
        for devinfo in pod_info["devices"]:
            if "skip" in devinfo and devinfo["skip"]:
                continue
            device_list.append(devinfo)

        return device_list

    def get_ssh_devices(self, exclude_upnp=False):
        """
            Returns a list of devices that support ssh.
        """
        ssh_device_list = []

        for devinfo in self.get_devices():
            dev_type = devinfo["deviceType"]

            if exclude_upnp and dev_type == "network/upnp":
                continue

            if "ssh" in devinfo:
                ssh_device_list.append(devinfo)

        return ssh_device_list

    def get_upnp_devices(self, ssh_only=False):
        """
            Returns a list of UPNP device information dictionaries.
        """
        upnp_device_list = []

        for devinfo in self.get_devices():
            dev_type = devinfo["deviceType"]

            if dev_type != "network/upnp":
                continue

            if ssh_only and "ssh" in devinfo:
                upnp_device_list.append(devinfo)
            else:
                upnp_device_list.append(devinfo)

        return upnp_device_list

    def get_upnp_device_lookup_table(self):
        """
            Returns a USN lookup table for upnp devices.
        """
        upnp_device_list = self.get_upnp_devices()

        upnp_device_table = {}
        for device in upnp_device_list:
            usn = device["upnp"]["USN"]
            upnp_device_table[usn] = device

        return upnp_device_table

    def initialize(self):
        """
            Called by '__init__' once at the beginning of the lifetime of a Landscape derived
            type.  This allows the derived types to participate in a customized intialization
            process.
        """
        self._ordered_roles = []
        self._integrations = {}

        self.landscape_description.register_integration_points(self)

        context = Context()
        try:
            landscape_file = get_expanded_path(context.lookup("/environment/configuration/paths/landscape"))
            lscape_desc = self.landscape_description()
            self._landscape_info = lscape_desc.load(landscape_file)
        except Exception as xcpt:
            err_msg = "Error loading the landscape file from (%s)" % landscape_file
            raise AKitConfigurationError(err_msg) from xcpt

        return

    def diagnostic(self, diaglabel, diags):
        """
            Can be called in order to perform a diagnostic capture across the test landscape.

            :param diaglabel: The label to use for the diagnostic.
            :type diaglabel: str
            :param diags: A dictionary of diagnostics to run.
            :type diags: dict
        """
        return
    
    def first_contact(self):
        """
            This method should be called as early as possible in order to ensure the entities in the
            automation landscape exist and the authentication credentials provided for these entities
            are valid and usable to interact with these entities.

            :returns list: list of failing entities
        """

        error_lists = []

        self._initialize_device_coordinators()

        if self._has_upnp_devices and self._upnp_coord is None:
            raise AKitConfigurationError("UpnpCoordinator initialization failure.")

        if self._has_ssh_devices and self._ssh_coord is None:
            raise AKitConfigurationError("SshPoolCoordinator initialization failure.")

        available_upnp_devices = self.get_upnp_devices(ssh_only=True)
        available_ssh_devices = self.get_ssh_devices(exclude_upnp=True)

        self._logger.info("===================== Initiating SSH First Contact with Landscape Devices =====================")
        self._logger.info("")


        if len(available_upnp_devices) == 0 and len(available_ssh_devices) == 0:
            self._logger.info("No SSH Devices Found...")

        if len(available_upnp_devices) > 0:
            self._logger.info("UPNP DEVICES:")
            for devinfo in available_upnp_devices:
                usn = devinfo["upnp"]["USN"]
                agent = self._ssh_coord.lookup_agent_by_usn(usn)
                self._logger.info("    Verifying USN={} HOST={} IP={}".format(usn, agent.host, agent.ipaddr))
                if not agent.verify_connectivity():
                    error_lists.append(devinfo)
            self._logger.info("")

        if len(available_ssh_devices) > 0:
            self._logger.info("SSH DEVICES:")
            for devinfo in available_ssh_devices:
                sshinfo = devinfo["ssh"]
                host = sshinfo["host"]
                agent = self._ssh_coord.lookup_agent_by_host(host)
                self._logger.info("    Verifying HOST={} IP={}".format(agent.host, agent.ipaddr))
                if not agent.verify_connectivity():
                    error_lists.append(devinfo)
            self._logger.info("")

        return error_lists

    def register_integration_point(self, role, mixin):
        """
            This method should be called from the attach_to_environment methods from individual mixins
            in order to register the base level integrations.  Integrations can be hierarchical so it
            is only necessary to register the root level integration mixins, the descendant mixins can
            be called from the root level mixins.

            :param role: The name of a role to assign for a mixin.
            :type role: str
            :param mixin: The mixin to register for the associated role.
            :type mixin: MixIn
        """
        if role not in self._integrations:
            self._ordered_roles.append(role)
            self._integrations[role] = mixin
        else:
            raise AKitSemanticError("A mixin with the role %r was already registered." % role)

        return

    def _initialize_device_coordinators(self):
        """
            Initializes the device coordinators according the the information specified in the
            'devices' portion of the configuration file.
        """

        upnp_device_list = []
        ssh_device_list = []

        for devinfo in self.get_devices():
            dev_type = devinfo["deviceType"]
            if dev_type == "network/upnp":
                upnp_device_list.append(devinfo)
                if "ssh" in devinfo:
                    ssh_device_list.append(devinfo)
            elif dev_type == "network/ssh":
                ssh_device_list.append(devinfo)
            else:
                errmsg_lines = [
                    "Unknown device type %r in configuration file." % dev_type,
                    "DEVICE INFO:"
                ]
                errmsg_lines.extend(split_and_indent_lines(pprint.pformat(devinfo, indent=4), 1))
                
                errmsg = os.linesep.join(errmsg_lines)
                self._logger.error(errmsg)

        if len(upnp_device_list) > 0:
            self._has_upnp_devices = True
            upnp_hint_list = self.get_upnp_device_lookup_table()
            self._upnp_coord = UpnpCoordinator()
            self._upnp_coord.startup_scan(upnp_hint_list, watchlist=upnp_hint_list, exclude_interfaces=["lo"])

        if len(ssh_device_list) > 0:
            self._has_ssh_devices = True
            self._ssh_coord = SshPoolCoordinator()
            self._ssh_coord.attach_to_devices(ssh_device_list, upnp_coord=self._upnp_coord)

        return


def is_subclass_of_landscape(cand_type):
    """
        Returns a boolean value indicating if the candidate type is a subclass
        of :class:`Landscape`.
    """
    is_scol = False
    if inspect.isclass(cand_type) and issubclass(cand_type, Landscape):
        is_scol = True
    return is_scol

def load_and_set_landscape_type(lscape_module):
    """
        Scans the module provided for :class:`Landscape` derived classes and will
        take the first one and assign it as the current runtime landscape type.
    """
    class_items = inspect.getmembers(lscape_module, is_subclass_of_landscape)
    for _, cls_type in class_items:
        type_module_name = cls_type.__module__
        if type_module_name == lscape_module.__name__:
            Landscape._landscape_type = cls_type
            break
    return

if VARIABLES.AKIT_LANDSCAPE_MODULE is not None:
    lscape_module = import_by_name(VARIABLES.AKIT_LANDSCAPE_MODULE)
    load_and_set_landscape_type(lscape_module)
    check_landscape = Landscape()
    pass

if __name__ == "__main__":
    lscape = Landscape()
    lscape.first_contact()
