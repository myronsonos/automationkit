"""
.. module:: activate
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

import os

from datetime import datetime

from akit.xtime import parse_datetime

# =======================================================================================
# The way we start up the test framework and the order which things come up in is a very
# important part of the automation process.  It effects whether or not logging is brought
# up consistently before all modules start using it.  It ensures that no matter how we
# enter into an automation process, whether via a test runner, terminal, or debugging a single
# file that we properly parse arguments and settings and launch the automation process
# consistently.
#
# Because of these necessities, we setup the activate module so it is the first thing
# scripts and tests files that consume the test framework will import to ensure the
# startup process is always consistent
#
# The framework has a special activation module :module:`akit.environment.console` that is
# used when bringing up the test framework in a console.  This special method redirects

# Step 1 - Force the default configuration to load if it is not already loaded
from akit.environment.configuration import RUNTIME_CONFIGURATION

# Step 2 - Process the environment variables that are used to overwride the
# default configuration
from akit.environment.variables import VARIABLES, LOG_LEVEL_NAMES

# Step 3 - Load the user configuration and add it to the RUNTIME_CONFIGURATION 'ChainMap' so
# the user settings take precedence over the runtime default settings.
from akit.environment.userconfig import load_user_configuration
user_config = load_user_configuration()
RUNTIME_CONFIGURATION.maps.insert(0, user_config)

# Step 4 - Process environment options
from akit.environment.options import process_environment_options
output_dir, console_level, logfile_level, branch, build, flavor, start_time = process_environment_options()

if console_level is None:
    if VARIABLES.AKIT_CONSOLE_LOG_LEVEL is not None and VARIABLES.AKIT_CONSOLE_LOG_LEVEL in LOG_LEVEL_NAMES:
        console_level = VARIABLES.AKIT_CONSOLE_LOG_LEVEL
    else:
        console_level = "INFO"

if logfile_level is None:
    if VARIABLES.AKIT_FILE_LOG_LEVEL is not None and VARIABLES.AKIT_FILE_LOG_LEVEL in LOG_LEVEL_NAMES:
        logfile_level = VARIABLES.AKIT_FILE_LOG_LEVEL
    else:
        logfile_level = "DEBUG"

# Step 5 - Force the context to load with defaults ifz it is not already loaded
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

if start_time is not None:
    starttime = parse_datetime(start_time)
    env["starttime"] = starttime
elif VARIABLES.AKIT_STARTTIME is not None:
    starttime = parse_datetime(start_time)
    env["starttime"] = starttime
else:
    env["starttime"] = datetime.now()

conf = ctx.lookup("/environment/configuration")

fill_dict = {
    "starttime": str(env["starttime"]).replace(" ", "T")
}

jobtype = env["jobtype"]
if jobtype == "unkownjob" or jobtype == "testrun":
    env["jobtype"] = "testrun"
    outdir_template = conf.lookup("/paths/testresults")
    outdir_full = os.path.abspath(os.path.expandvars(os.path.expanduser(outdir_template % fill_dict)))
    env["output_directory"] = outdir_full
elif jobtype == "console":
    outdir_template = conf.lookup("/paths/consoleresults")
    outdir_full = os.path.abspath(os.path.expandvars(os.path.expanduser(outdir_template % fill_dict)))
    env["output_directory"] = outdir_full

if output_dir is not None:
    env["output_directory"] = output_dir

loglevels = conf.lookup("/logging/levels")
loglevels["console"] = console_level
loglevels["logfile"] = logfile_level

# Step 5 - Import the logging module so we get an initial configuration that
# points to standard out
import akit.xlogging

