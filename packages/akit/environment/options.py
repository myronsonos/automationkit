"""
.. module:: akit.environment.options
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the :class:`Context` object and :class:`ContextCursor` that
               are used to maintain the shared automation context.

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

import argparse

from akit.environment.variables import LOG_LEVEL_NAMES

ENVIRONMENT_OPTIONS = [
    (("-o", "--output"), { "dest":"output", "action":"store", "default":None, "help":"The output directory where results and artifacts are collected."}),
    (("--console-level",), { "dest":"consolelevel", "action":"store", "default":None, "choices":LOG_LEVEL_NAMES, "help":"The logging level for console output."}),
    (("--logfile-level",), { "dest":"logfilelevel", "action":"store", "default":None, "choices":LOG_LEVEL_NAMES, "help":"The logging level for logfile output."}),
    (("--branch",), { "dest": "branch", "action": "store", "default": None, "help": "The name of the branch to associate with the test run results."}),
    (("--build",), { "dest": "build", "action": "store", "default": None, "help": "The name of the build to associate with the test run results."}),
    (("--flavor",), { "dest": "flavor", "action": "store", "default": None, "help": "The name of the flavor to associate with the test run results."}),
    (("--start",), { "dest": "start", "action": "store", "default": None, "help": r"A time stamp to associate with the start of the run. Example: 2020-10-17T15:30:11.989120  Bash: date +%Y-%m-%dT%H:%M:%S.%N"})
]

def process_environment_options():
    """
        Processes the basic automation kit environment commandline options which
        are used to configure the base automation functionality such as:

        * output directory
        * console log level
        * logfile log level
        * branch
        * build
        * flavor
    """
    env_parser = argparse.ArgumentParser()
    for opt_args, opt_kwargs in ENVIRONMENT_OPTIONS:
        env_parser.add_argument(*opt_args, **opt_kwargs)

    args, _ = env_parser.parse_known_args()

    output_dir = args.output
    console_level = args.consolelevel
    logfile_level = args.logfilelevel
    branch = args.branch
    build = args.build
    flavor = args.flavor
    start_time = args.start

    return output_dir, console_level, logfile_level, branch, build, flavor, start_time
