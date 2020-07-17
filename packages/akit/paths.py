"""
.. module:: akit.paths
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

import os

from akit.environment.context import Context

DIR_TESTRESULTS = None

def get_expand_path(path: str) -> str:
    """
        Returns a path expanded using expanduser, expandvars and abspath for
        the provided path.
    """
    exp_path = os.path.abspath(os.path.expandvars(os.path.expanduser(path)))
    return exp_path

def get_path_for_artifacts(label) -> str:
    """
        Returns a path in the form (testresultdir)/artifacts/(label)
    """
    trdir = get_path_for_testresults()
    afdir = os.path.join(trdir, "artifacts", label)
    return afdir

def get_path_for_testresults() -> str:
    """
        Returns a the timestamped path where test results and artifacts are deposited to
    """
    global DIR_TESTRESULTS
    if DIR_TESTRESULTS is None:
        ctx = Context()
        env = ctx.lookup("/environment")
        conf = ctx.lookup("/environment/configuration")

        testresult_path = conf["paths"]["testresults"]

        fill_dict = {
            "starttime": str(env["starttime"]).replace(" ", "T")
        }
        testresult_path = testresult_path % fill_dict

        DIR_TESTRESULTS = get_expand_path(testresult_path)

    return DIR_TESTRESULTS

