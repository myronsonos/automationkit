
"""
.. module:: akit.recorders
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module which contains the :class:`TaskBase` object which is used as the base.

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

import collections
import datetime
import json
import os
import shutil
import typing

from datetime import datetime

from akit.results import ResultCode, ResultType
from akit.templates import TEMPLATE_TESTSUMMARY
from akit.testing.utilities import catalog_tree



class TextRecorder:
    pass

class JsonResultRecorder:
    """
        {
            "title": "Automation Test Run",
            "id": "b606a644-bd62-49f5-afda-9f48e865dd49",
            "start": "",
            "stop": "",
            "result": "PASSED",
            "detail": {
                "passed": 0,
                "errors": 0,
                "failed": 0,
                "skipped": 0,
                "total": 0
            }
        }
    """
    def __init__(self, title: str, runid: str, start: datetime.datetime, summary_filename: str,
                 result_filename: str, branch: typing.Optional[str]=None, build: typing.Optional[str]=None,
                flavor: typing.Optional[str]=None):
        self._title = title
        self._runid = runid
        self._start = start
        self._output_dir = os.path.dirname(summary_filename)
        self._summary_filename = summary_filename
        self._result_filename = result_filename
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
        self.update_summary()
        self._rout = open(self._result_filename, 'w')
        return self
    
    def __exit__(self, ex_type, ex_inst, ex_tb):
        self.finalize()
        self.update_summary()
        return

    def record(self, result):
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

        with open(self._summary_filename, 'w') as sout:
            json.dump(self._summary, sout, indent=4)

        return

    def finalize(self):
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