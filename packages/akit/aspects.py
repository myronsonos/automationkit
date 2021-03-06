"""
.. module:: aspects
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the :class:`Aspects` class and the constants used to provide aspect behaviors.

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

class RunPattern:
    """
        A run pattern to use when running commands.
    """
    SINGLE_RUN = 0
    RUN_UNTIL_SUCCESS = 1
    RUN_WHILE_SUCCESS = 2

class LoggingPattern:
    """
        A logging pattern to use when logging commands.
    """
    ALL_RESULTS = 0
    FAILURE_ONLY = 1
    SUCCESS_ONLY = 2


DEFAULT_COMPLETION_TIMEOUT = 600
DEFAULT_COMPLETION_INTERVAL = 10

DEFAULT_INACTIVITY_TIMEOUT = 600
DEFAULT_INACTIVITY_INTERVAL = .5

DEFAULT_MONITOR_DELAY = 30

DEFAULT_LOGGING_PATTERN = LoggingPattern.ALL_RESULTS

class Aspects:
    """
        Aspects are utilized with the interop APIs and agents such as the :class:`SSHAgent` class in order
        to modify the behavior of APIs with respect to retry parameter such as timeout, interval, looping patterns
        logging, etc.  The aspects object provides a way to package this common criteria into a single parameter
        or constant you can  pass to multiple APIs
    """

    def __init__(self, run_pattern: RunPattern = RunPattern.SINGLE_RUN, completion_timeout: float = DEFAULT_COMPLETION_TIMEOUT, completion_interval: float = DEFAULT_COMPLETION_INTERVAL,
                       inactivity_timeout: float = DEFAULT_INACTIVITY_TIMEOUT, inactivity_interval: float = DEFAULT_INACTIVITY_INTERVAL, monitor_delay: float = DEFAULT_MONITOR_DELAY,
                       logging_pattern: LoggingPattern = DEFAULT_LOGGING_PATTERN):
        """
            Creates an :class:`Aspects` package.

            :param run_pattern: The :class:`RunPattern` that the API should exhibit such as SINGLE_RUN, RUN_UNTIL_SUCCESS, RUN_WHILE_SUCCESS
            :param completion_timeout: The time in seconds as a float that is the max time before timeout for the activity to complete.
            :param completion_interval: The time in seconds as a float that is waited before reattempting an activity.
            :param inactivity_timeout: The time in seconds as a float that is the max time before timeout that is waited before a :class:`TimeoutError`
                                       is raised due to inactivity.
            :param inactivity_interval: The time in seconds as a float that is waited before reattempting an activity.
        """
        self.run_pattern = run_pattern
        self.completion_timeout = completion_timeout
        self.completion_interval = completion_interval
        self.inactivity_timeout = inactivity_timeout
        self.inactivity_interval = inactivity_interval
        self.monitor_delay = monitor_delay
        self.logging_pattern = logging_pattern

        return

DEFAULT_ASPECTS = Aspects()
