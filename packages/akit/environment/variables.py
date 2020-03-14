"""
.. module:: akit.environment.variables
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module which contains the :class:`VARIABLES` object which is used store the environment variables.

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
import sys

environ = os.environ

class VARIABLES:
    AKIT_BRANCH = "unknown"
    if "AKIT_BRANCH" in environ:
        AKIT_BRANCH = environ["AKIT_BRANCH"]

    AKIT_BUILD = "unknown"
    if "AKIT_BUILD" in environ:
        AKIT_BUILD = environ["AKIT_BUILD"]

    AKIT_JOBTYPE = "unknown"
    if "AKIT_JOBTYPE" in environ:
        AKIT_JOBTYPE = environ["AKIT_JOBTYPE"]
    
    AKIT_LANDSCAPE_MODULE = "somens.integration.somelandscape"
    if "AKIT_LANDSCAPE_MODULE" in environ:
        AKIT_LANDSCAPE_MODULE = environ["AKIT_LANDSCAPE_MODULE"]

def extend_path(dir_to_add):

    found = False

    for nxt_item in sys.path:
        nxt_item = nxt_item.rstrip(os.sep)
        dir_to_add = dir_to_add.rstrip(os.sep)
        if nxt_item == dir_to_add:
            found = True
            break

    if not found:
        sys.path.insert(0, dir_to_add)
        os.environ["PYTHONPATH"] = dir_to_add + os.pathsep + os.environ["PYTHONPATH"]

    return