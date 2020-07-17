"""
.. module:: akit.testing.testsequencer
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the base :class:`TestSequencer` type which is use to control
               the flow of the automation environment startup and test execution sequence.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>

"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@automationmojo.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import fnmatch
import inspect
import logging
import json
import os
import sys
import uuid

import akit.environment.activate
from akit.environment.context import ContextUser

from akit.mixins.scope import ScopeMixIn
from akit.mixins.scope import is_scope_mixin
from akit.results import ResultContainer, ResultType
from akit.testing.testcollector import TestCollector


logger = logging.getLogger("AKIT")

class TEST_SEQUENCER_PHASES:
    Initial = 0
    Discovery = 1
    Collection = 2
    Graph = 3
    Traversal = 4

class TestSequencer(ContextUser):

    def __init__(self, root, job=None, includes=[], excludes=[]):
        """
            Creates a 'TestSequencer' object which is used to discover the tests and control the flow of a test run.

            :param context: A reference to the global contenxt.
            :type context: akit.context.Context
            :param root: The path to the root folder that is the base of the tests.
            :type root: str
            :param includes: List of expressions used to determine which tests to include. 
                             (scope):(package).(package)@(module)#(testname)
            :type includes: list
            :param excludes: List of expressions used to determine which tests to exclued from the included tests. 
            :type excludes: list. 

        """
        self._root = root
        self._job = job
        self._includes = includes
        self._excludes = excludes
        self._integrations = []
        self._references = []
        self._scopes = []
        self._scope_roots = []
        self._import_errors = []
        self._testpacks = []
        return

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_inst, ex_tb):
        return False

    @property
    def import_errors(self):
        return self._import_errors

    @property
    def testpacks(self):
        return self._testpacks

    def collect_resources(self):
        
        return

    def discover(self, test_module=None):

        collector = TestCollector(self._root, excludes=self._excludes, test_module=test_module)

        # Discover the tests, integration points, and scopes.  If test modules is not None then
        # we are running tests from an individual module and we can limit discovery to the test module
        for inc_item in self._includes:
            collector.collect_references(inc_item)

        self._references = collector.references

        testcount = len(self._references)
        if testcount > 0:
            self._integrations = collector.collect_integrations()
            self._testpacks = collector.collect_testpacks()
            self._import_errors = collector.import_errors

        return testcount

    def execute_testpacks(self, runid: str, recorder, sequencer):

        exit_code = 0

        res_name = "(root)"

        root_container = ResultContainer(runid, res_name, ResultType.JOB)
        recorder.record(root_container)

        for tpack in sequencer():
            self._traverse_testpack(tpack, recorder, parent_inst=runid) 

        return exit_code

    def parse_extended_args(self, base_parser):
        
        return

    def record_import_errors(self, outputfilename: str):

        with open(outputfilename, 'w') as ief:
            for modname, filename, errmsg in self._import_errors:
                ieitem = {
                    "module": modname,
                    "filename": filename,
                    "trace": errmsg.splitlines(False)
                }
                json.dump(ieitem, ief, indent=4)

        return

    def _traverse_testpack(self, testpack, recorder, parent_inst=None):

        testpack_key = testpack.__module__ + "." + testpack.__name__
        logger.info("TESTPACK ENTER: %s" % testpack_key)

        try:
            res_inst = str(uuid.uuid4())

            result_container = ResultContainer(res_inst, testpack_key, ResultType.TEST_CONTAINER, parent_inst=parent_inst)
            recorder.record(result_container)

            self._enter_testpack(testpack)

            for tref in testpack.test_references:

                try:
                    # Create an instance of the test case using the test reference
                    testinst = tref.create_instance(recorder)

                    # Run the test, it shouldn't raise any exceptions unless a stop
                    # is raised or a framework exception occurs
                    testinst.run(result_container.result_inst)
                except Exception as xcpt:
                    pass

        finally:
            try:
                self._exit_testpack(testpack)
            except Exception as xcpt:
                #TODO: Handing exception logging here
                pass

            logger.info("TESTPACK EXIT: %s" % testpack_key)

        return

    def _enter_testpack(self, leaf_scope):
        rev_mro = list(leaf_scope.__mro__)
        rev_mro.reverse()

        for nxt_cls in rev_mro:
            if is_scope_mixin(nxt_cls):
                # We only want to call scope_enter when we find the type it is directly
                # implemented on
                if "scope_enter" in nxt_cls.__dict__:
                    nxt_cls.scope_enter()
                    if not hasattr(nxt_cls, "scope_enter_count"):
                        nxt_cls.scope_enter_count = 1
                    else:
                        nxt_cls.scope_enter_count += 1

        return

    def _exit_testpack(self, leaf_scope):
        norm_mro = list(leaf_scope.__mro__)

        for nxt_cls in norm_mro:
            if is_scope_mixin(nxt_cls):
                # We only want to call scope_enter when we find the type it is directly
                # implemented on
                if "scope_exit" in nxt_cls.__dict__:
                    nxt_cls.scope_exit()
                    if hasattr(nxt_cls, "refcount"):
                        nxt_cls.refcount -= 1
                    else:
                        logger.error("ERROR: Every scope should have a 'refcount' class variable.")
        return


