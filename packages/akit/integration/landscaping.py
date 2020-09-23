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

from akit.xformatting import indent_lines
from akit.xlogging import getAutomatonKitLogger

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

    def load(self, landscapefile):
        return
    

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

    def get_ssh_devices(self):
        """
            Returns a list of devices that support ssh.
        """
        ssh_device_list = []

        for devinfo in self.get_devices():
            if "ssh" in devinfo:
                ssh_device_list.append(devinfo)

        return ssh_device_list

    def get_upnp_devices(self):
        """
            Returns a list of UPNP device information dictionaries.
        """
        upnp_device_list = []

        for devinfo in self.get_devices():
            dev_type = devinfo["deviceType"]
            if dev_type == "network/upnp":
                upnp_device_list.append(devinfo)

        return upnp_device_list

    def get_upnp_device_lookup_table(self):
        """
            Returns a USN lookup table for upnp devices.
        """
        upnp_device_list = self.get_upnp_devices()

        upnp_device_table = {}
        for device in upnp_device_list:
            usn = device["USN"]
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
            with open(landscape_file, 'r') as lf:
                lfcontent = lf.read()
                self._landscape_info = json.loads(lfcontent)
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

        for devinfo in self.get_devices():
            dev_type = devinfo["deviceType"]
            if dev_type == "network/upnp":
                usn = devinfo["USN"]
                if "ssh" in devinfo:
                    agent = self._ssh_coord.lookup_agent_by_usn(usn)
                    if not agent.verify_connectivity():
                        error_lists.append(devinfo)
            elif dev_type == "network/ssh":
                sshinfo = devinfo["ssh"]
                host = sshinfo["host"]
                agent = self._ssh_coord.lookup_agent_by_host(host)
                if not agent.verify_connectivity():
                    error_lists.append(devinfo)
            else:
                error_lists.append(devinfo)

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
                errmsg = "Unknown device type %r in configuration file.\n" % dev_type
                errmsg += "DEVICE INFO:\n"
                errmsg += indent_lines(pprint.pformat(devinfo, indent=4), level=1)
                self._logger.error(errmsg)

        if len(upnp_device_list) > 0:
            self._has_upnp_devices = True
            upnp_hint_list = [devinfo["USN"] for devinfo in upnp_device_list]
            self._upnp_coord = UpnpCoordinator()
            self._upnp_coord.startup_scan(upnp_hint_list, watchlist=upnp_hint_list, exclude_interfaces=["lo"])

        if len(ssh_device_list) > 0:
            self._has_ssh_devices = True
            self._ssh_coord = SshPoolCoordinator()
            self._ssh_coord.attach_to_devices(ssh_device_list)

        return

    def _validate_landscape(self):
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
