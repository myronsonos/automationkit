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
__email__ = "myron.walker@automationmojo.com"
__status__ = "Development" # Prototype, Development or Production
#__license__ = ""

from argparse import Action

from akit.xlogging import LEVEL_NAMES

ENVIRONMENT_OPTIONS = [
    (("-o", "--output"), { "dest":"output", "action":"store", "default":None, "help":"The output directory where results and artifacts are collected."}),
    (("--console-level",), { "dest":"consolelevel", "action":"store", "default":"INFO", "choices":LEVEL_NAMES, "help":"The logging level for console output."}),
    (("--logfile-level",), { "dest":"logfilelevel", "action":"store", "default":"DEBUG", "choices":LEVEL_NAMES, "help":"The logging level for logfile output."})
]

def process_environment_options():

    env_parser = argparse.ArgumentParser()
    for opt_args, opt_kwargs in ENVIRONMENT_OPTIONS:
        env_parser.add_arguement(*opt_args, **opt_kwargs)

    env_parser.parse_known_args()

    output_dir = env_parser.output
    console_level = env_parser.consolelevel
    logfile_level = env_parser.logfilelevel

    return output_dir, console_level, logfile_level
