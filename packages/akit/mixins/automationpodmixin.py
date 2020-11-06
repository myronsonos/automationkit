"""
.. module:: automationpodmixin
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Contains a ClusterMixIn object to use for working with the nodes of a cluster

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

from akit.integration.landscaping import Landscape
from akit.integration.coordinators.upnpcoordinator import UpnpCoordinator
from akit.integration.upnp.upnpprotocol import inline_msearch

from akit.mixins.integration import IntegrationMixIn

class AutomationPodMixIn(IntegrationMixIn):
    """
        This is a mock automation pod device.
    """

    pathbase = None

    landscape = Landscape()

    upnp_devices_expected = None
    upnp_devices_found = None
    upnp_devices_pool = None
    upnp_devices_inuse = None

    upnp_coord = None

    def __init__(self, *args, **kwargs):
        """
            The default contructor for an :class:`AutomationPodMixIn`.
        """
        if self.pathbase is None:
            raise ValueError("The 'pathbase' class member variable must be set to a unique name for each integration class type.")

        self.context.insert(self.pathbase, self)
        return

    def checkout_upnp_device(self, usn):
        """
            Checkout a device from the device pool by USN.
        """
        codev = None

        if usn in self.upnp_devices_pool:
            codev = self.upnp_devices_pool.pop(usn)
            self.upnp_devices_inuse[usn] = codev

        return codev

    def checkin_upnp_device(self, codev):
        """
            Checkin a device to the device pool.
        """
        usn = codev["USN"]
        
        if usn in self.upnp_devices_inuse:
            codev = self.upnp_devices_inuse.pop(usn)
            self.upnp_devices_pool[usn] = codev

        return

    @classmethod
    def attach_to_environment(cls):
        """
            This API is called so that the IntegrationMixIn can process configuration information.  The :class:`IntegrationMixIn`
            will verify that it has a valid environment and configuration to run in.

            :raises :class:`akit.exceptions.AKitMissingConfigError`, :class:`akit.exceptions.AKitInvalidConfigError`:
        """
        cls.upnp_devices_expected = cls.landscape.get_upnp_devices()

        # First do an inline search for devices with a timeout to make sure all the expected
        # devices are visible.
        found_devices, matching_devices = inline_msearch(cls.upnp_devices_expected)

        # If the inline m-search was successful, then go ahead and startup the UpnpAgent
        cls.upnp_coord = UpnpCoordinator()
        return

    @classmethod
    def collect_resources(cls):
        """
            This API is called so the `IntegrationMixIn` can connect with a resource management
            system and gain access to the resources required for the automation run.

            :raises :class:`akit.exceptions.AKitResourceError`:
        """
        
        return

    @classmethod
    def diagnostic(cls, diag_level, diag_folder):
        """
            The API is called by the :class:`akit.sequencer.Sequencer` object when the automation sequencer is 
            building out a diagnostic package at a diagnostic point in the automation sequence.  Example diagnostic
            points are:

            * pre-run
            * post-run

            Each diagnostic package has its own storage location so derived :class:`akit.scope.ScopeMixIn` objects
            can simply write to their specified output folder.

            :param diag_level: The maximum diagnostic level to run dianostics for.
            :type diag_level: int
            :param diag_folder: The output folder path where the diagnostic information should be written.
            :type diag_folder: str
        """
        
        return

    @classmethod
    def establish_connectivity(cls):
        """
            This API is called so the `IntegrationMixIn` can establish connectivity with any compute or storage
            resources.

            :raises :class:`akit.exceptins.AKitInitialConnectivityError`:
        """
        
        return