"""
.. module:: akit.testing.testsequencer
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the base :class:`TestSequencer` type which is use to control
               the flow of the automation environment startup and test execution sequence.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>

"""
import fnmatch
import inspect
import logging
import json
import os
import sys
import uuid

import akit.environment.activate

from akit.mixins.scope import DefaultScopeMixIn, ScopeMixIn
from akit.results import ResultContainer, ResultType
from akit.testing.testcollector import TestCollector
from akit.mixins.scope import is_scope_mixin


logger = logging.getLogger("AKIT")

class TEST_SEQUENCER_PHASES:
    Initial = 0
    Discovery = 1
    Collection = 2
    Graph = 3
    Traversal = 4

class TestSequencer:

    def __init__(self, context, root, job=None, includes=[], excludes=[]):
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
        self._context = context
        self._root = root
        self._job = job
        self._includes = includes
        self._excludes = excludes
        self._integrations = []
        self._references = []
        self._scopes = []
        self._scope_roots = []
        self._import_errors = []
        return

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_inst, ex_tb):
        return False

    @property
    def import_errors(self):
        return self._import_errors

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
            self._scope_table = collector.create_scope_table()
            self._import_errors = collector.import_errors

        return testcount

    def execute_tests(self, runid, recorder):

        scope_table = self._scope_table

        exit_code = 0

        res_name = "(root)"

        root_container = ResultContainer(runid, res_name, ResultType.ROOTCONTAINER)
        recorder.record(root_container)

        for leaf_scope in scope_table:
             self._traverse_scope(leaf_scope, recorder, parent_inst=runid)

        return exit_code

    def parse_extended_args(self, base_parser):
        
        return

    def record_import_errors(self, outputfilename):

        with open(outputfilename, 'w') as ief:
            for modname, filename, errmsg in self._import_errors:
                ieitem = {
                    "module": modname,
                    "filename": filename,
                    "trace": errmsg.splitlines(False)
                }
                json.dump(ieitem, ief, indent=4)

        return

    def _traverse_scope(self, leaf_scope, recorder, parent_inst=None):
        scope_key = leaf_scope.__module__ + "." + leaf_scope.__name__
        logger.info("SCOPE ENTER: %s" % scope_key)

        try:
            res_inst = str(uuid.uuid4())

            result_container = ResultContainer(res_inst, scope_key, ResultType.TESTCONTAINER, parent_inst=parent_inst)
            recorder.record(result_container)

            self._enter_leaf_scope(leaf_scope)

            if scope_key in ScopeMixIn.test_references:
                test_references = ScopeMixIn.test_references[scope_key]
                for tref in test_references:

                    try:
                        # Create an instance of the test case using the test reference
                        testinst = tref.create_instance(leaf_scope, recorder)

                        # Run the test, it shouldn't raise any exceptions unless a stop
                        # is raised or a framework exception occurs
                        testinst.run(result_container.result_inst)
                    except Exception as xcpt:
                        pass

        finally:
            try:
                self._exit_leaf_scope(leaf_scope)
            except Exception as xcpt:
                #TODO: Handing exception logging here
                pass

            logger.info("SCOPE EXIT: %s" % scope_key)

        return

    def _enter_leaf_scope(self, leaf_scope):
        rev_mro = list(leaf_scope.__mro__)
        rev_mro.reverse()

        for nxt_cls in rev_mro:
            if is_scope_mixin(nxt_cls):
                nxt_cls.scope_enter()
                if not hasattr(nxt_cls, "scope_enter_count"):
                    nxt_cls.scope_enter_count = 1
                else:
                    nxt_cls.scope_enter_count += 1

        return

    def _exit_leaf_scope(self, leaf_scope):
        norm_mro = list(leaf_scope.__mro__)

        for nxt_cls in norm_mro:
            if is_scope_mixin(nxt_cls):
                nxt_cls.scope_exit()
                if hasattr(nxt_cls, "refcount"):
                    nxt_cls.refcount -= 1
                else:
                    logger.error("ERROR: Every scope should have a 'refcount' class variable.")
        return


