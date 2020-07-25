"""
.. module:: akit.mixins.integration
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the :class:`IntegrationMixIn` class and associated reflection methods.

    The :class:`IntegrationMixIn` derived classes can be used to integraton automation resources and roles
    into the test environment.

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

from akit.exceptions import AKitInvalidConfigError, AKitMissingConfigError, AKitResourceError, AKitInitialConnectivityError

from akit.environment.context import ContextUser
from akit.integration.landscaping import Landscape

from akit.xlogging import getAutomatonKitLogger

class IntegrationMixIn(ContextUser):
    """
        The :class:`IntegrationMixIn` object serves as the base object for the declaration of an automation integration
        requirement.  The :class:`akit.testing.testsequencer.Sequencer` queries the class hierarchies of the tests that
        are included in an automation run.
    """

    logger = None
    landscape = None
    pathname = None

    def __init__(self, *args, role=None, **kwargs):
        """
            The default contructor for an :class:`IntegrationMixIn`.
        """
        self._role = role

        if self.pathname is None:
            raise ValueError("The 'pathname' class member variable must be set to a unique name for each integration class type.")

        self.context.insert(self.pathname, self)
        return

    @property
    def mode(self):
        """
            Returns the current mode any associated resource is operating in.
        """
        return self._mode

    @mode.setter
    def mode(self, value):
        """
            Sets the current mode any associated resource is operating in.
        """
        old_value = self._mode
        self._mode = value
        self.on_mode_changed(old_value, value)
        return

    @property
    def role(self):
        """
            Returns the current automation role assigned to the integration mixin.
        """
        return self._role

    def on_mode_changed(self, prev_mode, new_mode):
        """
            Implemented by derived classes in order to perform the changeover of modes.
        """
        return

    @classmethod
    def declare_precedence(cls):
        """
            This API is called so that the IntegrationMixIn can declare an ordinal precedence that should be
            utilized for bringing up its integration state.
        """
        return
    
    @classmethod
    def declare_options(cls):
        """
            This API is called so that the IntegrationMixIn can declare any command line options that are required
            for it to be able to function.
        """
        return

    @classmethod
    def attach_to_environment(cls):
        """
            This API is called so that the IntegrationMixIn can process configuration information.  The :class:`IntegrationMixIn`
            will verify that it has a valid environment and configuration to run in.

            :raises :class:`akit.exceptions.AKitMissingConfigError`, :class:`akit.exceptions.AKitInvalidConfigError`:
        """
        cls.logger = getAutomatonKitLogger()
        cls.landscape = Landscape()
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


def is_integration_mixin(cls):
    is_integmi = False
    if inspect.isclass(cls) and cls is not IntegrationMixIn and issubclass(cls, IntegrationMixIn):
        is_integmi = True
    return is_integmi