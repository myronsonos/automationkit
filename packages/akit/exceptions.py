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
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"
class AKitError(Exception):
    """
        The base error object for Automation Kit errors.
    """

# ==================================================================================
#                            BASE ERROR CLASSIFICATIONS
# ==================================================================================

class AKitConfigurationError(AKitError):
    """
        The base error object for errors that indicate that there is an issue related
        to improper configuration.
    """

class AKitLandscapeError(AKitError):
    """
        The base error object for errors that indicate that there is an issue related
        to the interaction usage or consumption of an environmental resources.
    """

class AKitRuntimeError(AKitError):
    """
        The base error object for errors that indicate that an error was produced during
        the execution of task or test code and the error was not able to be classified
        as Configuration, Landscape, or Semantic related.
    """

class AKitSemanticError(AKitError):
    """
        The base error object for errors that indicate that there is an issue with
        a piece of automation code and with the way the Automation Kit code is being
        utilized.  
    """

# ==================================================================================
#                         CONFIGURATION RELATED ERRORS
# ==================================================================================

class AKitInvalidConfigError(AKitConfigurationError):
    """
        This error is raised when an IntegrationMixIn object has been passed invalid configuration parameters.
    """

class AKitMissingConfigError(AKitConfigurationError):
    """
        This error is raised when an IntegrationMixIn object is missing required configuration parameters.
    """


# ==================================================================================
#                           LANDSCAPE RELATED ERRORS
# ==================================================================================
class AKitInitialConnectivityError(AKitLandscapeError):
    """
        This error is raised when an IntegrationMixIn object is unable to establish an initial level of
        connectivity with a connected resource.
    """

class AKitMissingResourceError(AKitLandscapeError):
    """
        This error is raised when an device or resources was declared in the landscape.json file
        but was not able to be found during device or resource discovery.
    """

class AKitResourceError(AKitLandscapeError):
    """
        This error is raised when an IntegrationMixIn object was unable to obtain a required resource.
    """

# ==================================================================================
#                           RUNTIME RELATED ERRORS
# ==================================================================================

class AKitCommunicationsProtocolError(AKitRuntimeError):
    """
        This is the base error for exceptions that are related to communciations protocols
    """

class AKitOutOfScopeError(AKitRuntimeError):
    """
        This error is raised when a method is called on a ScopeMixIn that is not in scope.  A test can have,
        multiple ScopeMixIn(s) and can run in multiple scopes but the test must be instantiated and run in
        each scope individually.
    """

class AKitRequestStopError(AKitRuntimeError):
    """
        This error is raised when a test indicates it wants to stop an automation run.  The `TestSequencer`
        may or may not stop the automation run as a result of a test or scope raising this error.  The
        `TestSequencer` looks at the current runtime context which was set by the commandline arguements
        and will stop the test run if the runtime context indicates that stopping is allowed.
    """

class AKitScopeEntryError(AKitRuntimeError):
    """
        This error is raised when a ScopeMixIn was unable to complete the entry of a scope.
    """

class AKitSkipError(AKitRuntimeError):
    """
        This error is raised when a test indicates it wants to be skipped while being run
    """

class AKitTimeoutError(AKitRuntimeError):
    """
        This error is raised when a timeout occurs
    """

# ==================================================================================
#                           SEMANTIC RELATED ERRORS
# ==================================================================================

class AKitAbstractMethodError(AKitSemanticError):
    """
        This error is raised when an abstract method has been called. 
    """

class AKitNotImplementedError(AKitSemanticError):
    """
        This error is raised when a method is called that has not yet been implemented. 
    """

class AKitNotOverloadedError(AKitSemanticError):
    """
        This error is raised when a method that must be overloaded has not been overridden. 
    """

