"""
    .. module:: akit.mixins.integration

    A scope represents a predefined state that is reached by the execution of code.  The state represents a
    requirement that is needed to be met in order for a task to be able to run.

    Scopes have a name that is like a file system path /environment/configuration

    Scopes can contain state and they are deposited into the context in a leaf just like other nodes.


"""

import inspect

from akit.environment.context import ContextUser
from akit.exceptions import AKitInvalidConfigError, AKitMissingConfigError, AKitResourceError, AKitInitialConnectivityError

class IntegrationMixIn(ContextUser):
    """
        The :class:`IntegrationMixIn` object serves as the base object for the declaration of an automation integration
        requirement.  The :class:`akit.testing.testsequencer.Sequencer` queries the class hierarchies of the tests that
        are included in an automation run.
    """

    pathname = None

    def __init__(self, *args, **kwargs):
        """
            The default contructor for an :class:`IntegrationMixIn`.
        """
        if self.pathname is None:
            raise ValueError("The 'pathname' class member variable must be set to a unique name for each integration class type.")

        self.context.insert(self.pathname, self)
        return

    @classmethod
    def attach_to_environment(cls):
        """
            This API is called so that the IntegrationMixIn can process configuration information.  The :class:`IntegrationMixIn`
            will verify that it has a valid environment and configuration to run in.

            :raises :class:`akit.exceptions.AKitMissingConfigError`, :class:`akit.exceptions.AKitInvalidConfigError`:
        """
        
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