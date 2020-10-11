"""
.. module:: akit.environment.configuration
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the default runtime configration dictionary and the functions that
               are used to load the automation configuration file and overlay the settings on top of the
               default runtime configuration.

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
import os

RUNTIME_DEFAULTS = {
    "version": "1.0.0",
    "logging": {
        "levels": {
            "console": "INFO",
            "logfile": "DEBUG"
        },
        "logname": "%(jobtype)s.log"
    },
    "paths": {
        "landscape": os.sep.join(("~", "akit", "config", "landscape.json")),
        "results": os.sep.join(("~", "akit", "results")),
        "consoleresults": os.sep.join(("~", "akit", "console", "%(starttime)s")),
        "runresults": os.sep.join(("~", "akit", "results", "runresults", "%(starttime)s")),
        "testresults": os.sep.join(("~", "akit", "results", "testresults", "%(starttime)s"))
    }
}

RUNTIME_CONFIGURATION = collections.ChainMap(RUNTIME_DEFAULTS)
