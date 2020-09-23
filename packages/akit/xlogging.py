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

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import fnmatch
import logging
import os
import sys

from akit.environment.context import Context

# Start Logging to Standard Out.  We need to make sure it is initialized to something as early as possible,
# but we may not have a file to write to yet until logging_initialize is called by a proper entry point 
logging.basicConfig(level=logging.NOTSET)

LOGGER_NAME = "AKIT"

LOGGING_SECTION_MARKER = "="
LOGGING_SECTION_MARKER_LENGTH = 80


def format_log_section_header(title):
    title_upper = " %s " % title.strip().upper()
    marker_count = LOGGING_SECTION_MARKER_LENGTH - len(title_upper)
    marker_half = marker_count >> 1
    marker_prefix = LOGGING_SECTION_MARKER * marker_half
    marker_suffix = LOGGING_SECTION_MARKER * (marker_count - marker_half)
    header = "\n%s%s%s\n" % (marker_prefix, title_upper, marker_suffix)
    return header

akit_logger = None

def getAutomatonKitLogger():
    global akit_logger
    if akit_logger is None:
        akit_logger = TestKitLoggerWrapper(logging.getLogger(LOGGER_NAME))
    return akit_logger

OTHER_LOGGER_FILTERS = []

LEVEL_NAMES = [
    "NOTSET",
    "DEBUG",
    "INFO",
    "WARNING",
    "ERROR",
    "CRITICAL"
]

class TestKitLoggerWrapper:

    def __init__(self, logger):
        self._logger = logger
        return

    def debug(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'DEBUG'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.debug("Houston, we have a %s", "thorny problem", exc_info=1)
        """
        self._logger.debug(msg, *args, **kwargs)
        return

    def info(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'INFO'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.info("Houston, we have a %s", "interesting problem", exc_info=1)
        """
        self._logger.info(msg, *args, **kwargs)
        return


    def warning(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'WARNING'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.warning("Houston, we have a %s", "bit of a problem", exc_info=1)
        """
        self._logger.warning(msg, *args, **kwargs)
        return

    def warn(self, msg, *args, **kwargs):
        self._logger.warning(msg, *args, **kwargs)
        return

    def error(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'ERROR'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.error("Houston, we have a %s", "major problem", exc_info=1)
        """
        self._logger.error(msg, *args, **kwargs)
        return

    def exception(self, msg, *args, exc_info=True, **kwargs):
        """
        Convenience method for logging an ERROR with exception information.
        """
        self._logger.exception(msg, *args, exc_info=exc_info, **kwargs)
        return

    def critical(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'CRITICAL'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.critical("Houston, we have a %s", "major disaster", exc_info=1)
        """
        self._logger.critical(msg, *args, **kwargs)
        return

    fatal = critical

    def section(self, title):
        """
            Logs a log section marker
        """
        self._logger.info(format_log_section_header(title))
        return

class WarningFilter(logging.Filter):
    def filter(self, rec):
        process_rec = rec.levelno < logging.WARNING
        return process_rec

class OtherFilter:
    def __init__(self, prefix):
        self.prefix = prefix
        return

    def filter(self, rec):
        rec.is_other = fnmatch.fnmatch(rec.name, self.prefix)
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
    """
        Method used to configure the automation kit logging based on the environmental parameters
        specified and then reinitialize the logging.
    """
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

def logging_create_branch_logger(logger_name, logfilename, log_level):
    """
        Method that allows for the creation of a separate logfile for specific loggers in order
        to reduce the noise in the main logfile.  A common use for this would be to redirect
        logging from specific modules such as 'paramiko' and 'httplib' to thier own log files.

        :param logger_name: The name of the logger to create a branch log for.
    """
    target_logger = logging.getLogger(logger_name)

    # Setup the relevant log file which will get all the
    # log entries from loggers that satisified a relevant
    # logger name prefix match
    handler = logging.FileHandler(logfilename)
    handler.setLevel(log_level)
    for handler in target_logger.handlers:
        target_logger.removeHandler(handler)
    target_logger.addHandler(handler)
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

    # Setup the other log handler and other filter, we
    # need to add the other log handler before adding
    # the relevant log handler
    other_handler = logging.FileHandler(other_logfilename)
    other_handler.setLevel(logfilelevel)
    for other_expr in OTHER_LOGGER_FILTERS:
        other_handler.addFilter(OtherFilter(other_expr))
    root_logger.addHandler(other_handler)

    # Setup the relevant log file which will get all the
    # log entries from loggers that satisified a relevant
    # logger name prefix match
    rel_handler = logging.FileHandler(rel_logfilename)
    rel_handler.setLevel(logging.NOTSET)
    rel_handler.addFilter(RelevantFilter())
    root_logger.addHandler(rel_handler)

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

    root_logger.info(format_log_section_header("Logging Initiaized"))

    return

