
"""
.. module:: results
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

import collections
import enum
import json
import os
import time
import traceback
import uuid

from akit.xtime import format_time_with_fractional

class ResultCode(enum.IntEnum):
    UNSET = 0
    PASSED = 1
    SKIPPED = 2
    ERRORED = 3
    FAILED = 4
    UNKOWN = 5

class ResultType(enum.IntEnum):
    JOB = 0
    PACKAGE = 1
    SCOPE = 2
    TASK_CONTAINER = 3
    TASK = 4
    TEST_CONTAINER = 5
    TEST = 6
    STEP_CONATINER = 7
    STEP = 8

class ResultNode:

    def __init__(self, result_inst, result_name, result_type, result_code=ResultCode.UNSET, parent_inst=None):
        self._result_inst = result_inst
        self._result_name = result_name
        self._parent_inst = parent_inst
        self._result_code = result_code
        self._result_type = result_type
        self._start = time.time()
        self._stop = None
        self._errors = []
        self._failures = []
        self._warnings = []
        self._reason = None
        self._docstr = None
        return

    @property
    def parent_inst(self):
        return self._parent_inst

    @property
    def result_code(self):
        return self._result_code

    @property
    def result_inst(self):
        return self._result_inst

    @property
    def result_name(self):
        return self._result_name

    @property
    def result_type(self):
        return self._result_type

    def add_error(self, err_lines):
        trim_lines = []
        for nline in err_lines:
            nline = nline.rstrip()
            nlindex = nline.find(os.linesep)
            if nlindex > -1:
                trim_lines.append(nline[:nlindex])
                trim_lines.append(nline[nlindex + 1:])
            else:
                trim_lines.append(nline)
        self._errors.append(trim_lines)
        return

    def add_failure(self, fail_lines):
        trim_lines = []
        for nline in fail_lines:
            nline = nline.rstrip()
            nlindex = nline.find(os.linesep)
            if nlindex > -1:
                trim_lines.append(nline[:nlindex])
                trim_lines.append(nline[nlindex + 1:])
            else:
                trim_lines.append(nline)
        self._failures.append(trim_lines)
        return

    def add_warning(self, warn_lines):
        trim_lines = []
        for nline in warn_lines:
            nline = nline.rstrip()
            nlindex = nline.find(os.linesep)
            if nlindex > -1:
                trim_lines.append(nline[:nlindex])
                trim_lines.append(nline[nlindex + 1:])
            else:
                trim_lines.append(nline)
        self._warnings.append(trim_lines)
        return

    def set_documentation(self, docstr):
        self._docstr = docstr
        return

    def finalize(self):
        self._stop = time.time()

        if len(self._failures) > 0:
            self._result_code = ResultCode.FAILED
        elif len(self._errors) > 0:
            self._result_code = ResultCode.ERRORED
        elif self._result_code == ResultCode.UNSET:
            self._result_code = ResultCode.UNKOWN

        return

    def mark_passed(self):
        self._result_code = ResultCode.PASSED
        return

    def mark_skip(self, reason):
        self._result_code = ResultCode.SKIPPED
        return

    def to_json(self):


        detail = collections.OrderedDict([
            ("reason", self._reason),
            ("errors", self._errors),
            ("failures", self._failures),
            ("warnings", self._warnings)
        ])

        if self._docstr is not None:
            detail["documentation"] =  self._docstr

        start_datetime = format_time_with_fractional(self._start)
        stop_datetime = format_time_with_fractional(self._stop)

        jobj = collections.OrderedDict([
            ("name", self._result_name),
            ("instance", self._result_inst),
            ("parent", self._parent_inst),
            ("rtype", self._result_type.name),
            ("result", self._result_code.name),
            ("start", start_datetime),
            ("stop", stop_datetime),
            ("detail", detail)
        ])

        jstr = json.dumps(jobj, indent=4)

        return jstr

class ResultContainer:

    def __init__(self, result_inst, result_name, result_type, parent_inst=None):
        self._result_inst = result_inst
        self._result_name = result_name
        self._parent_inst = parent_inst
        self._result_type = result_type
        return

    @property
    def parent_inst(self):
        return self._parent_inst

    @property
    def result_inst(self):
        return self._result_inst

    @property
    def result_name(self):
        return self._result_name

    @property
    def result_type(self):
        return self._result_type

    def to_json(self):

        jobj = collections.OrderedDict([
            ("name", self._result_name),
            ("instance", self._result_inst),
            ("parent", self._parent_inst),
            ("rtype", self._result_type.name)
        ])

        jstr = json.dumps(jobj, indent=4)

        return jstr
