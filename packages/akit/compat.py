"""
.. module:: akit.compat
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains functions that are utilized to provide compatibility across different
               operating system platforms and python version.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@automationmojo.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = ""

import sys
import importlib

is_python3 = sys.version_info[0] == 3
is_python_pre_3_5 = (is_python3 and sys.version_info[1] < 5)

def import_by_name(modulename):
    """
        Imports a module by name.
    """

    mod = importlib.import_module(modulename)
    
    return mod

def import_file(name, loc):
    """
        Import module from a file. Used to load models from a directory. 
        
        :param unicode name: Name of module to load.
        :param (unicode / Path) loc: Path to the file.

        returns: The loaded module.
    """
    mod = None
    if name not in sys.modules:
        if is_python_pre_3_5:
            import imp

            mod = imp.load_source(name, loc)
        else:
            import importlib.util

            spec = importlib.util.spec_from_file_location(name, str(loc))
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
    else:
        mod = sys.modules[name]

    return mod

def bytes_cast(val):
    if isinstance(str):
        val = val.encode('utf-8')
    return val

def str_cast(val):
    if isinstance(str):
        val = val.decode('utf-8')
    return val