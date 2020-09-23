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
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

# Step 1 - Force the default configuration to load if it is not already loaded
from akit.environment.configuration import RUNTIME_CONFIGURATION

# Step 2 - Process the environment variables that are used to overwride the
# default configuration
from akit.environment.variables import VARIABLES

# Step 3 - Load the user configuration and add it to the RUNTIME_CONFIGURATION 'ChainMap' so
# the user settings take precedence over the runtime default settings.
from akit.environment.userconfig import load_user_configuration
user_config = load_user_configuration()
RUNTIME_CONFIGURATION.maps.insert(0, user_config)

# Step 4 - Process environment options
from akit.environment.options import process_environment_options
output_dir, console_level, logfile_level, branch, build, flavor = process_environment_options()

# Step 5 - Force the context to load with defaults if it is not already loaded
# and setup the run type if not already set
from akit.environment.context import Context

ctx = Context()

# The environment element holds the resulting variables that are a result of the
# startup process
env = ctx.lookup("/environment")

if branch is not None:
    env["branch"] = branch
else:
    env["branch"] = VARIABLES.AKIT_BRANCH

if build is not None:
    env["build"] = build
else:
    env["build"] = VARIABLES.AKIT_BUILD

if flavor is not None:
    env["flavor"] = flavor
else:
    env["flavor"] = VARIABLES.AKIT_FLAVOR

conf = ctx.lookup("/environment/configuration")

if env["jobtype"] == "unkownjob":
    env["jobtype"] = "testrun"
    env["output_directory"] = conf.lookup("/paths/testresults")

if output_dir is not None:
    env["output_directory"] = output_dir

loglevels = conf.lookup("/logging/levels")
loglevels["console"] = console_level
loglevels["logfile"] = logfile_level

# Step 5 - Import the logging module so we get an initial configuration that
# points to standard out
import akit.xlogging

