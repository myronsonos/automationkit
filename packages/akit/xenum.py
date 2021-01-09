"""
.. module:: xenum
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module which contains functions for formatting text.

.. note:: The modules that are named `xsomething` like this module are prefixed with an `x` character to
          indicate they extend the functionality of a base python module and the `x` is pre-pended to
          prevent module name collisions with python modules.

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

from enum import Enum

class DocIntEnum(int, Enum):

    def __new__(cls, value, doc=None):
        self = Enum.__new__(cls, value)
        if doc is not None:
            self.__doc__ = doc
        return self