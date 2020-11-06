"""
.. module:: userconfig
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that is utilized to provide a mechanism for the user to override configuration defaults by
               specifying them in a file.

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

import json
import os

from akit.environment.variables import VARIABLES
from akit.paths import get_expanded_path

FILE_USER_CONFIGURATION = get_expanded_path(VARIABLES.AKIT_USER_CONFIGURATION)

USER_CONFIGURATION = None

def load_user_configuration():
    """
        Function that is used to load the user configuration file and overlay the user configuration
        onto default automation kit configuration.
    """
    global USER_CONFIGURATION

    if USER_CONFIGURATION is None:
        if os.path.exists(FILE_USER_CONFIGURATION):
            with open(FILE_USER_CONFIGURATION, 'r') as cf:
                USER_CONFIGURATION = json.load(cf)
        else:
            USER_CONFIGURATION = {}

    return USER_CONFIGURATION
