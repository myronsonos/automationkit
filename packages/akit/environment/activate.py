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
__license__ = "MIT"

# Step 1 - Force the default configuration to load if it is not already loaded
import akit.environment.configuration

# Step 2 - Process the environment variables that are used to overwride the
# default configuration
import akit.environment.variables

# Step 3 - Process environment options
from akit.environment.options import process_environment_options
output_dir, console_level, logfile_level = process_environment_options()

# Step 4 - Force the context to load with defaults if it is not already loaded
# and setup the run type if not already set
from akit.environment.context import Context

ctx = Context()

# The environment element holds the resulting variables that are a result of the
# startup process
env = ctx.lookup("/environment")

if env["jobtype"] == "unkownjob":
    env["jobtype"] = "testrun"
    env["output_directory"] = conf.lookup("/paths/testresults")

if output_dir is not None:
    env["output_directory"] = output_dir

conf = ctx.lookup("/environment/configuration")

loglevels = conf.lookup("/logging/levels")
loglevels["console"] = console_level
loglevels["logfile"] = logfile_level

# Step 5 - Import the logging module so we get an initial configuration that
# points to standard out
import akit.xlogging

