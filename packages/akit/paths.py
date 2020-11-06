"""
.. module:: paths
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
from typing import List, Optional

from akit.environment.context import Context
from akit.exceptions import AKitRuntimeError

DIR_TESTRESULTS = None

TRANSLATE_TABLE_NORMALIZE_FOR_PATH = str.maketrans(",.:;", "    ")

def collect_python_modules(searchdir: str) -> List[str]:
    """
        Walks a directory tree of python modules and collects the names
        of all of the python module files or .py files.  This method allows
        for python namespaces by not forcing the root folder to contain a
        __init__.py file.
    """
    pyfiles = []

    for root, _, files in os.walk(searchdir, topdown=True):
        for fname in files:
            fbase, fext = os.path.splitext(fname)
            if fext == '.py' and fbase != "__init__":
                ffull = os.path.join(root, fname)
                pyfiles.append(ffull)

    return pyfiles

def ensure_directory_is_module(moduleDir, moduleTitle: Optional[str] = None):
    """
        Ensures that a directory is represented to python as a module by checking to see if the
        directory has an __init__.py file and if not it adds one.
    """
    serviceDirInit = os.path.join(moduleDir, "__init__.py")
    if not os.path.exists(serviceDirInit):
        with open(serviceDirInit, 'w') as initf:
            initf.write('"""\n')
            if moduleTitle is not None:
                initf.write('   %s\n' % moduleTitle)
            initf.write('"""\n')
    return

def get_directory_for_module(module):
    """
        Returns the directory for a module
    """
    if hasattr(module, '__path__'):
        module_dir = str(module.__path__._path[0]).rstrip(os.sep)
    elif hasattr(module, '__file__'):
        module_dir = os.path.dirname(module.__file__).rstrip(os.sep)
    else:
        raise AKitRuntimeError("Unable to get parent dir for module")

    return module_dir

def get_expanded_path(path: str) -> str:
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

        DIR_TESTRESULTS = get_expanded_path(testresult_path)

    return DIR_TESTRESULTS

def normalize_name_for_path(name):
    norm_name = name.translate(TRANSLATE_TABLE_NORMALIZE_FOR_PATH).replace(" ", "")
    return norm_name
