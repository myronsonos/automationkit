"""
.. module:: akit.environment.activate
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that is utilized by test files to ensure the test environment is initialized in
               the correct order.

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

# Force the default configuration to load if it is not already loaded
import akit.environment.configuration

# Process the environment variables that are used to overwride the default configuration
import akit.environment.variables

from akit.environment.options import process_environment_options

# Force the context to load with defaults if it is not already loaded and setup the run type if not already set
from akit.environment.context import Context

ctx = Context()
env = ctx.lookup("/environment")
conf = ctx.lookup("/environment/configuration")

if env["jobtype"] == "unkownjob":
    env["jobtype"] = "testrun"
    env["output_directory"] = conf.lookup("/paths/testresults")

# Import the logging module so we get an initial configuration that points
# to standard out 
import akit.xlogging
