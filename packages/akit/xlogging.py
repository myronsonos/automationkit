"""
.. module:: akit.xlogging
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module which contains framework logging functions which extend the functionality to
               the python :module:`logging` module.

.. note:: The modules that are named `xsomething` like this module are prefixed with an `x` character to
          indicate they extend the functionality of a base python module and the `x` is pre-pended to
          prevent module name collisions with python modules.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

import fnmatch
import logging
import os
import sys

from akit.environment.context import Context

# Start Logging to Standard Out.  We need to make sure it is initialized to something as early as possible,
# but we may not have a file to write to yet until logging_initialize is called by a proper entry point 
logging.basicConfig(level=logging.NOTSET)

LOGGER_NAME = "AKIT"

def getAutomatonKitLogger():
    logger = logging.getLogger(LOGGER_NAME)
    return logger

OTHER_LOGGER_FILTERS = []

LEVEL_NAMES = [
    "NOTSET",
    "DEBUG",
    "INFO",
    "WARNING",
    "ERROR",
    "CRITICAL"
]

class WarningFilter(logging.Filter):
    def filter(self, rec):
        process_rec = rec.levelno < logging.WARNING
        return process_rec

class OtherFilter:
    def __init__(self, prefix):
        self.prefix = prefix
        return

    def filter(self, rec):
        rec.is_other = fnmatch.fnmatch(rec.name, prefix)
        return rec.is_other

class RelevantFilter:

    def filter(self, rec):
        process_rec = True
        if hasattr(rec, "is_other"):
            if rec.is_other:
                process_rec = False
        return process_rec

logging_initialized = False

def logging_initialize():
    global logging_initialized

    if not logging_initialized:
        logging_initialized = True

        ctx = Context()
        env = ctx.lookup("/environment")
        conf = ctx.lookup("/environment/configuration")
        logging_conf = conf["logging"]

        log_levels = logging_conf["levels"]
        consolelevel = log_levels["console"]
        logfilelevel = log_levels["logfile"]

        logname_template = logging_conf["logname"]
        logname = env.fill_template(logname_template)

        output_directory = env["output_directory"]
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        # Setup the log files
        _reinitialize_logging(consolelevel, logfilelevel, output_directory, logname)

    return

def _reinitialize_logging(consolelevel, logfilelevel, output_dir, logfile_basename):
    
    basecomp, extcomp = os.path.splitext(logfile_basename)

    debug_logfilename = os.path.join(output_dir, basecomp + ".DEBUG" + extcomp)
    other_logfilename = os.path.join(output_dir, basecomp + ".OTHER" + extcomp)
    rel_logfilename = os.path.join(output_dir, basecomp + extcomp)

    # Remove all the log handlers from the root logger
    root_logger = logging.getLogger()
    for lhandler in root_logger.handlers:
        root_logger.removeHandler(lhandler)

    # Set the root logger to NOTSET, so we don't impose an effective log
    # level on child loggers
    root_logger.setLevel(logging.NOTSET)

    # Setup the debug logfile
    base_handler = logging.FileHandler(debug_logfilename)
    base_handler.setLevel(logging.NOTSET)
    root_logger.addHandler(base_handler)

    # Setup the relevant log file which will get all the
    # log entries from loggers that satisified a relevant
    # logger name prefix match
    rel_hanlder = logging.FileHandler(rel_logfilename)
    rel_hanlder.setLevel(logging.NOTSET)
    rel_hanlder.addFilter(RelevantFilter())
    root_logger.addHandler(rel_hanlder)

    # Setup the other log handler and other filter, we
    # need to add the other log handler before adding
    # the relevant log handler
    other_handler = logging.FileHandler(other_logfilename)
    other_handler.setLevel(logfilelevel)
    for other_expr in OTHER_LOGGER_FILTERS:
        other_handler.addFilter(OtherFilter(other_expr))
    root_logger.addHandler(other_handler)

    # Setup the stdout logger with the correct console level and
    # filter the log entries from the stdout handler that are
    # greater than Info level
    stdout_logger = logging.StreamHandler(sys.stdout)
    stdout_logger.setLevel(consolelevel)
    stdout_logger.addFilter(WarningFilter())

    stderr_logger = logging.StreamHandler(sys.stderr)
    stderr_logger.setLevel(logging.WARNING)

    root_logger.addHandler(stdout_logger)
    root_logger.addHandler(stderr_logger)

    root_logger.info("Logging Initiaized")

    return

    
