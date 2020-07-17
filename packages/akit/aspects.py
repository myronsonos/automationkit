"""
.. module:: akit.aspects
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the :class:`Aspects` class and the constants used to provide aspect behaviors.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@automationmojo.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

DEFAULT_COMPLETION_TIMEOUT = 600
DEFAULT_COMPLETION_INTERVAL = 10

DEFAULT_INACTIVITY_TIMEOUT = 600
DEFAULT_INACTIVITY_INTERVAL = 5

class RunPattern:
    SINGLE_RUN = 0
    RUN_UNTIL_SUCCESS = 1
    RUN_WHILE_SUCCESS = 2

class Aspects:
    def __init__(self, run_pattern=RunPattern.SINGLE_RUN, completion_timeout=DEFAULT_COMPLETION_TIMEOUT, completion_interval=DEFAULT_COMPLETION_INTERVAL,
                       inactivity_timeout=DEFAULT_INACTIVITY_TIMEOUT, inactivity_interval=DEFAULT_INACTIVITY_INTERVAL):
        self.run_pattern = run_pattern
        self.completion_timeout = completion_timeout
        self.completion_interval = completion_interval
        self.inactivity_timeout = inactivity_timeout
        self.inactivity_interval = inactivity_interval
        return

DEFAULT_ASPECTS = Aspects()
