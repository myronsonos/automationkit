"""
.. module:: akit.exceptions
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the exceptions that are raised by the code in the Automation Kit

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@automationmojo.com"
__status__ = "Development" # Prototype, Development or Production
#__license__ = ""
class AKitError(Exception):
    """
        The base error object for Automation Kit errors.
    """

class AKitInitialConnectivityError(AKitError):
    """
        This error is raised when an IntegrationMixIn object is unable to establish an initial level of
        connectivity with a connected resource.
    """

class AKitInvalidConfigError(AKitError):
    """
        This error is raised when an IntegrationMixIn object has been passed invalid configuration parameters.
    """

class AKitMissingConfigError(AKitError):
    """
        This error is raised when an IntegrationMixIn object is missing required configuration parameters.
    """

class AKitOutOfScopeError(AttributeError):
    """
        This error is raised when a method is called on a ScopeMixIn that is not in scope.  A test can have,
        multiple ScopeMixIn(s) and can run in multiple scopes but the test must be instantiated and run in
        each scope individually.
    """

class AKitResourceError(AKitError):
    """
        This error is raised when an IntegrationMixIn object was unable to obtain a required resource.
    """

class AKitScopeEntryError(AKitError):
    """
        This error is raised when a ScopeMixIn was unable to complete the entry of a scope.
    """

class AKitRequestStopError(AKitError):
    """
        This error is raised when a test indicates it wants to stop an automation run.  The `TestSequencer`
        may or may not stop the automation run as a result of a test or scope raising this error.  The
        `TestSequencer` looks at the current runtime context which was set by the commandline arguements
        and will stop the test run if the runtime context indicates that stopping is allowed.
    """

class AKitSkipError(AKitError):
    """
        This error is raised when a test indicates it wants to be skipped while being run
    """
    def __init__(self, reason):
        AKitError.__init__(self, reason)
        self.reason = reason
        return


