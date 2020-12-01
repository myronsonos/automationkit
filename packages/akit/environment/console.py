"""
.. module:: console
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that is utilized by interactive consoles to activate the environment
               with logging to the console minimized in order to provide a good interactive
               console work experience.

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
from logging.handlers import RotatingFileHandler

# For console activation we don't want to log to the console and we want
# to point the logs to a different output folder
os.environ["AKIT_CONSOLE_LOG_LEVEL"] = "QUIET"
os.environ["AKIT_JOBTYPE"] = "console"

import akit.environment.activate # pylint: disable=unused-import,wrong-import-position

from akit.xlogging.foundations import logging_initialize, LoggingDefaults # pylint: disable=wrong-import-position

LoggingDefaults.DefaultFileLoggingHandler = RotatingFileHandler
logging_initialize()

def showlog():
    """
        Opens up another terminal and shows the output of the console log in the terminal.  This way we don't
        need to clutter the interactive terminal with logging based output.
    """
    import subprocess # pylint: disable=import-outside-toplevel

    from akit.environment.context import context # pylint: disable=import-outside-toplevel
    targetlog = context.lookup("/environment/logfile_debug")

    terminal_exec = "gnome-terminal"

    tail_exec = subprocess.check_output(["which","tail"]).strip().decode("utf-8")
    terminal_args = ['--', tail_exec, "-f", targetlog]

    proc_args = [terminal_exec]
    proc_args.extend(terminal_args)

    subprocess.call(proc_args)

    return
