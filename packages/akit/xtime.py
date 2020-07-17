"""
.. module:: akit.xtime
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module which contains framework time related functions which extend the functionality to
               the python :module:`time` and  :module:`datetime` modules.

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

import time

FORMAT_DATETIME = "%Y-%m-%dT%H:%M:%S"

def format_time_with_fractional(tsecs) -> str:
    sec_comp = int(tsecs)
    frac_comp = (tsecs - sec_comp) * 1000
    dtstr = "%s.%03d" % (time.strftime(FORMAT_DATETIME, time.gmtime(sec_comp)), frac_comp)
    return dtstr