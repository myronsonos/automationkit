"""
.. module:: akit.xlogging.scopemonitor
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module which contains the :class:`ScopeMonitor` object which monitors thread entrapment
               withing a specified scope.

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

import os
import time
import traceback
import uuid

from akit.xformatting import split_and_indent_lines
from akit.xlogging.foundations import getAutomatonKitLogger

DEFAULT_MONITORED_SCOPE_TIMEOUT = 600

logger = getAutomatonKitLogger()

class ScopeMonitor:

    def __init__(self):
        return


class MonitoredScope:

    def __init__(self, label, message, timeout=DEFAULT_MONITORED_SCOPE_TIMEOUT):
        self._id = str(uuid.uuid4())
        self._label = label
        self._message = message
        self._timeout = timeout
        self._start_time = time.time()
        self._end_time = self._start_time + timeout


        self._diag_func = None
        self._diag_args = None
        self._diag_kwargs = None

        self._exited = False
        self._triggered = False
        return

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_inst, ex_tb):

        self._exited = True

        return False

    @property
    def exited(self):
        """
            Return true if the thread that entered the MonitoredScope has exited.
        """
        return self._exited

    @property
    def expired(self):
        """
            Returns true if the MonitoredScope instance has not been exited by the calling
            thread before it has expired.
        """
        is_expired = False
        now = time.time()
        if now > self._end_time:
            is_expired = True
        return is_expired

    @property
    def id(self):
        """
            The unique identifier for this MonitoredScope instance.
        """
        return self._id

    @property
    def label(self):
        """
            The human readable label has been assigned to identify this scope.
        """
        return self._label

    @property
    def message(self):
        """
            The message that will be logged if this MonitoredScope is not exited before
            the timemout has expired.
        """
        return self._message

    def set_diagnostic(self, diagnostic_function, *args, **kwargs):
        """
            Sets the diagnostic function and its associated args which will be run if
            the :class:`MonitoredScope` is not exited before it has expired.
        """
        self._diag_func = diagnostic_function
        self._diag_args = args
        self._diag_kwargs = kwargs
        return

    def trigger_notification(self):
        """
            On the first trigger of a notification.  Runs the diagnostic function, logs the label and
            message along with the information collected by the diagnostic function.
        """
        if not self._triggered:
            self._triggered = True
            if self.expired and self._diag_func:
                diagmsg = self._diag_func(*self._diag_args, **self._diag_kwargs)

                errlines = [
                    "MonitoredScope({}): Timeout waiting for thread to exit monitored scope.".format(self._label),
                    "MESSAGE: {}".format(self._message),
                    "DIAGNOSTIC:"
                ]
                errlines.extend(split_and_indent_lines(diagmsg, 1))

                errmsg = os.linesep.join(errlines)
                logger.error(errmsg)

        return