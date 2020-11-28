
"""
.. module:: recorders
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module which contains the :class:`TaskBase` object which is used as the base.

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

from typing import Optional

import collections
import datetime
import json
import os
import shutil

from datetime import datetime

from akit.results import ResultCode, ResultType
from akit.templates import TEMPLATE_TESTSUMMARY
from akit.testing.utilities import catalog_tree


class JsonResultRecorder:
    """
        The :class:`JsonResultRecorder` object records test results in JSON format.
    """
    def __init__(self, title: str, runid: str, start: datetime, summary_filename: str,
                 result_filename: str, branch: Optional[str] = None, build: Optional[str] = None,
                flavor: Optional[str] = None):
        """
            Initializes the :class:`JsonResultRecorder` object for recording test results for
            a test run.
        """
        self._title = title
        self._runid = runid
        self._start = start
        self._output_dir = os.path.dirname(summary_filename)
        self._summary_filename = summary_filename
        self._result_filename = result_filename
        self._branch = branch
        self._build = build
        self._flavor = flavor

        self._rout = None

        self._error_count = 0
        self._failure_count = 0
        self._pass_count = 0
        self._skip_count = 0
        self._unknown_count = 0

        self._total_count = 0

        summaryreport_basename = os.path.basename(TEMPLATE_TESTSUMMARY)
        self._summary_report = os.path.join(self._output_dir, summaryreport_basename)

        self._summary = collections.OrderedDict((
            ("title", self._title),
            ("runid", self._runid),
            ("branch", branch),
            ("build", build),
            ("flavor", flavor),
            ("start", self._start),
            ("stop", None),
            ("result", "RUNNING"),
            ("landscape", None),
            ("detail", None)
        ))
        return

    def __enter__(self):
        """
            Starts up the recording process of test results.
        """
        self.update_summary()
        self._rout = open(self._result_filename, 'w')
        return self

    def __exit__(self, ex_type, ex_inst, ex_tb) -> bool:
        """
            Starts up the recording process of test results.

            :param ex_type: The type associated with the exception being raised.
            :type ex_type: type
            :param ex_inst: The exception instance of the exception being raised.
            :type ex_inst: Exception
            :param ex_tb: The traceback associated with the exception being raised.
            :type ex_tb: traceback

            :returns: Returns true if an exception was handled and should be suppressed.
            :rtype: bool
        """
        self.finalize()
        self.update_summary()
        return

    def record(self, result: ResultType):
        """
            Records an entry for the result object that is passed.

            :param result: A result object to be recorded.
            :type result: ResultType
        """
        if result.result_type == ResultType.TEST:
            self._total_count += 1

            result_code = result.result_code
            if result_code == ResultCode.PASSED:
                self._pass_count += 1
            elif result_code == ResultCode.ERRORED:
                self._error_count += 1
            elif result_code == ResultCode.FAILED:
                self._failure_count += 1
            elif result_code == ResultCode.SKIPPED:
                self._skip_count += 1
            else:
                self._unknown_count += 1

        json_str = result.to_json()

        self._rout.write("\30\n")
        self._rout.write(json_str)
        return

    def update_summary(self):
        """
            Writes out an update to the test run summary file.
        """
        with open(self._summary_filename, 'w') as sout:
            json.dump(self._summary, sout, indent=4)

        return

    def finalize(self):
        """
            Finalizes the test results counters and status of the test run.
        """
        stop = datetime.now()
        self._summary["stop"] = str(stop)

        self._summary["detail"] = {
            "errors": self._error_count,
            "failed": self._failure_count,
            "skipped": self._skip_count,
            "passed": self._pass_count,
            "total": self._total_count
        }

        if self._error_count > 0 or self._failure_count > 0:
            self._summary["result"] = "FAILED"
        else:
            self._summary["result"] = "PASSED"

        self._rout.close()

        catalog_tree(self._output_dir)
        shutil.copy(TEMPLATE_TESTSUMMARY, self._summary_report)

        return
