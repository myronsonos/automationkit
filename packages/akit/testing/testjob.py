"""
.. module:: akit.testing.testjob
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that is contains the :class:`TestJob` class which is utilized for each test
               run as the parent container for all test results.

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

import os
import uuid

from akit.recorders import JsonResultRecorder
from akit.results import ResultContainer, ResultType
from akit.testing.testsequencer import TestSequencer

class TestJob:
    """
        The :class:`TestJob` spans the execution of all :class:`TestPack` and organizes the
        flow of execution of test packs.  It allows for the sequencing of the execution of test
        packs so as to optimize the time test runs spend performing setup and tearnown tasks.  This
        allows for the optimization of infrastructure resources.
        
        * Single Instance
        * Setup Test Landscape
        * Jobs have an expected number of tests based
        * Collects and organizes results from all the :class:`TestPack` runs

        * Can be used to customize the sequencing of :class:`TestPack` runs.
    """

    name = "" # Friendly name for the test job
    description = "" # Description of the job

    includes = None # The test packs or tests that are included in this TestJob
    excludes = None # The tests that are to be excluded from this TestJob

    _instance = None

    def __new__(cls, *args, **kwargs):
        """
            Creates an instance of a TestJob and then returns that instance of the TestJob for all subsequent
            calls to create test Job instances.
        """
        if cls._instance is None:
            cls._instance = super(TestJob, cls).__new__(cls)
        return cls._instance

    def __init__(self, context, logger, testroot, includes=None, excludes=None, test_module=None, parser=None):
        """
            Constructor for a :class:`TestJob`.  It initializes the member variables based on the parameters passed
            from the entry point function and the class member data declared on :class:`TestJob` derived classes.
        """
        self._context = context
        self._logger = logger
        self._testroot = testroot

        if self.includes is None:
            self.includes = includes
            self.excludes = excludes

        self._test_module = test_module
        self._parser = parser
        self._starttime = None

        self._test_results_dir = None
        self._result_filename = None
        self._summary_filename = None
        self._import_errors_filename = None

        self._testpacks = None
        return

    def __enter__(self):
        self.begin()
        return self

    def __exit__(self, ex_type, ex_inst, ex_tb):
        self.finalize()
        return False

    def begin(self):
        """
            Called at the beginning of a test job in order to setup the recording of test results.
        """

        env = self._context.lookup("/environment")

        self._test_results_dir = env["output_directory"]
        self._starttime = env["starttime"]

        self._result_filename = os.path.join(self._test_results_dir, "testrun_results.jsos")
        self._summary_filename = os.path.join(self._test_results_dir, "testrun_summary.json")
        self._import_errors_filename = os.path.join(self._test_results_dir, "import_errors.jsos")

        return

    def execute(self):
        """
            Runs the tests that are included in the given :class:'TestPack'.
        """
        result_code = 0

        with TestSequencer(self._context, self._testroot, includes=self.includes, excludes=self.excludes) as tseq:

            # Discover the Tests, Integrations and Scopes
            count = tseq.discover(test_module=self._test_module)

            # Tell the sequencer to record any import errors that happened during discovery
            tseq.record_import_errors(self._import_errors_filename)

            if count > 0:
                if self._parser is not None:
                    # Parse any extended arguements now that we have discovered the integrations
                    tseq.parse_extended_args(self._parser)

                # Intitiate Resource Aquisition
                tseq.collect_resources()

                title = "Automation Test Run"
                runid = str(uuid.uuid4())
                start = str(self._starttime)

                with JsonResultRecorder(title, runid, start, self._summary_filename, self._result_filename) as recorder:
                    # Traverse the execution graph
                    self._testpacks = tseq.testpacks
                    result_code = tseq.execute_tests(runid, recorder, self.sequence)

            else:
                # We didn't find any tests so display a message, and set the return code to
                # indicate an error condition
                err_msg = "The include and exclude parameters specified resulted in an empty test set."
                if self.includes is not None:
                    err_msg += "INCLUDES:\n    %s\n" % "    \n".join(self.includes)
                else:
                    err_msg += "INCLUDES: None\n"
                if self.excludes is not None:
                    err_msg += "EXCLUDES:\n    %s\n" % "    \n".join(self.excludes)
                else:
                    err_msg += "EXCLUDES: None\n"
                self._logger.error(err_msg)
                result_code = -1

        return result_code


    def finalize(self):
        """
            Called at the end of a test job in order to flush the results of the test run, copy
            the report template to the output directory.
        """
        return

    def sequence(self):
        """
            Overridden by derived TestJob classes in order to customize the sequence of execution for the
            'TestPack'(s) associated with the TestJob.
        """
        for tp in self._testpacks:
            yield tp


class DefaultTestJob(TestJob):
    name = "Test Job"
    description = "Unspecified test job."

    def __init__(self, context, logger, testroot, includes=None, excludes=None, test_module=None):
        super(DefaultTestJob, self).__init__(context, logger, testroot, includes=includes, excludes=excludes, test_module=test_module)
        return
