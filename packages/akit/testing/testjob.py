"""
.. module:: akit.testing.testjob
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that is contains the :class:`TestJob` class which is utilized for each test
               run as the parent container for all test results.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

import uuid

from akit.recorders import JsonResultRecorder
from akit.results import ResultContainer, ResultType
from akit.testing.testsequencer import TestSequencer

class TestJob:
    """
        The `TestJob` spans the execution of all `TestPacks` and organizes the flow of execution
        of test packs in order to allow for the sequencing of the execution of test packages so as
        to optimize the time test runs spend performing setup and tearnown tasks.  This allows for
        the optimizations of infrastructure resources.
        
        * Single Instance
        * Setup Test Landscape
        * Jobs have an expected number of tests based
        * Collects and organizes results from all the TestPack runs

        * Can be used to customize the squencing of TestPack runs.
    """

    name = "" # Friendly name for the test job
    description = "" # Description of the job

    includes = None # The test packs or tests that are included in this TestJob
    excludes = None # The tests that are to be excluded from this TestJob

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(TestJob, cls).__new__(cls)
        else:
            raise RuntimeError("You can only have one 'TestJob' instance for a given test run.")
        return cls._instance

    def __init__(self, context, logger, testroot, includes=None, excludes=None, test_module=None):
        self.context = context
        self.logger = logger
        self.testroot = testroot

        self.includes = self.includes
        if includes is not None:
            self.includes = includes
        
        self.excludes = self.excludes
        if excludes is not None:
            self.excludes = excludes

        self.test_module = test_module
        return

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_inst, ex_tb):
        self.finalize()
        return False

    def begin(self):
        """
            Called at the beginning of a test job in order to setup the recording of test results.
        """
        env = self.context.lookup("/environment")

        self.test_results_dir = env["output_directory"]

        self.result_filename = os.path.join(test_results_dir, "testrun_results.jsos")
        self.summary_filename = os.path.join(test_results_dir, "testrun_summary.json")
        self.import_errors_filename = os.path.join(test_results_dir, "import_errors.jsos")
        return

    def execute(self, title, runid, starttime):
        """
            Runs the tests that are included in the given :class:'TestPack'.
        """
        result_code = 0

        with JsonResultRecorder(title, runid, start, self.summary_filename, self.testresult_filename) as recorder:
            # Traverse the execution graph
            result_code = tseq.execute_tests(runid, recorder)

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

        result_code = 0

        with TestSequencer(self.context, self.testroot, includes=self.includes, excludes=self.excludes) as tseq:

            # Discover the Tests, Integrations and Scopes
            count = tseq.discover(test_module=self.test_module)

            # Tell the sequencer to record any import errors that happened during discovery
            tseq.record_import_errors(import_errors_filename)

            if count > 0:
                # Parse any extended arguements now that we have discovered the integrations
                tseq.parse_extended_args(parser)

                # Intitiate Resource Aquisition
                tseq.collect_resources()

                title = "Automation Test Run"
                runid = str(uuid.uuid4())
                start = str(env["starttime"])

                result_code = self.execute(title, runid, start)

            else:
                # We didn't find any tests so display a message, and set the return code to
                # indicate an error condition
                err_msg = "The include and exclude parameters specified resulted in an empty test set."
                err_msg += "INCLUDES:\n    %s\n" % "    \n".join(includes)
                err_msg += "EXLUDES:\n    %s\n" % "    \n".join(excludes)
                self.logger.error(err_msg)
                result_code = -1

        return result_code


class DefaultTestJob(TestJob):
    name = "Test Job"
    description = "Unspecified test job."

    def __init__(self, context, logger, testroot, includes=None, excludes=None, test_module=None):
        super(TestJob, self).__init__(context, logger, testroot, includes=includes, excludes=excludes, test_module=test_module)
        return
