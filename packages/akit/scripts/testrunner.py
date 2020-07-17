#!/usr/bin/env python3
"""
.. script:: akit.timeouts
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Script used to run 'TestJobs', 'TestPacks' and 'Tests'.

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

import argparse
import logging
import os
import uuid

# We need to load the context first because it will load configuration
from akit.compat import import_by_name
from akit.environment.context import Context
from akit.environment.variables import extend_path
from akit.paths import get_path_for_testresults
from akit.xlogging import LEVEL_NAMES, logging_initialize, getAutomatonKitLogger

import akit.integration.landscaping

from akit.testing.testjob import DefaultTestJob
from akit.testing.testsequencer import TestSequencer
from akit.recorders import JsonResultRecorder

def testrunner_main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-r", "--root", dest="root", action="store", default=".", help="The root directory to scan for tests.")
    parser.add_argument("-j", "--job", dest="job", action="store", default=None, help="The identifier of the job to run.")
    parser.add_argument("-i", "--include", dest="includes", action="append", default=[], help="Add an include search statement.")
    parser.add_argument("-x", "--exclude", dest="excludes", action="append", default=[], help="Add an exclude filter statement.")
    parser.add_argument("-o", "--output", dest="output", action="store", default=None, help="The output directory where results and artifacts are collected.")
    parser.add_argument("--console-level", dest="consolelevel", action="store", default="INFO", choices=LEVEL_NAMES, help="The logging level for console output.")
    parser.add_argument("--logfile-level", dest="logfilelevel", action="store", default="DEBUG", choices=LEVEL_NAMES, help="The logging level for logfile output.")

    args = parser.parse_args()

    try:
        ctx = Context()
        env = ctx.lookup("/environment")
        conf = ctx.lookup("/environment/configuration")

        # Set the jobtype
        env["jobtype"] = "testrun"

        test_root = os.path.abspath(os.path.expandvars(os.path.expanduser(args.root)))
        if not os.path.isdir(test_root):
            errmsg = "The specified root folder does not exist. root=%s" % args.root
            if test_root != args.root:
                errmsg += " expanded=%s" % test_root
            raise argparse.ArgumentError("--root", errmsg)

        # Make sure we extend PATH to include the test root
        extend_path(test_root)

        # Setup the output directory
        output_path = args.output
        if output_path is not None:
            conf["paths"]["testresults"] = output_path

        test_results_dir = get_path_for_testresults()
        if not os.path.exists(test_results_dir):
            os.makedirs(test_results_dir)
        env["output_directory"] = test_results_dir

        # Setup the logging levels
        log_levels = {
            "console": args.consolelevel,
            "logfile": args.logfilelevel 
        }
        conf["logging"]["levels"] = log_levels

        # Initialize logging
        logging_initialize()
        logger = getAutomatonKitLogger()

        job = args.job
        includes = args.includes
        excludes = args.excludes

        if job is None and includes is None:
            errmsg = "You must specify either --job or --includes in order to include at least one test to run."
            raise argparse.ArgumentError("--job", errmsg)

        if job is not None and (len(includes) > 0 or len(excludes) > 0):
            errmsg = "The --job arguement cannot be used with the --includes or --excludes flags."
            raise argparse.ArgumentError("--job", errmsg)

        # At this point in the code, we either lookup an existing test job or we create a test job
        # from the includes, excludes or test_module
        TestJobType = DefaultTestJob
        if job is not None:
            job_parts = job.split("@")
            if len(job_parts) != 2:
                errmsg = "A --job parameter must be of the form 'package.module@JobClass'"
                raise argparse.ArgumentError("--job", errmsg)

            job_package, job_class = job_parts
            
            try:
                job_mod = import_by_name(job_package)
            except ImportError as ierr:
                errmsg = "Failure while importing job package %r"  % job_package
                raise argparse.ArgumentError("--job", errmsg)

            if not hasattr(job_mod, job_class):
                errmsg = "The job package %r does not have a job type %r." % (job_package, job_class)
                raise argparse.ArgumentError("--job", errmsg)

            TestJobType = getattr(job_mod, job_class)

        result_code = 0
        with TestJobType(logger, test_root, includes=includes, excludes=excludes) as tjob:
            result_code = tjob.execute()

        exit(result_code)

    finally:
        pass

    return

if __name__ == "__main__":
    testrunner_main()
