"""
.. module:: landscapedevice
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the :class:`TestLandscape` class and associated diagnostic.

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

import weakref

class LandscapeDeviceExtension:

    def __init__(self):
        self._coord_ref = None
        self._basedevice_ref = None
        self._configinfo = None
        self._extid = None
        self._location = None
        return

    @property
    def coordinator(self):
        coord = None
        if self._coord_ref is not None:
            coord = self._coord_ref()
        return coord

    @property
    def configuration(self):
        return self._configinfo

    @property
    def basedevice(self):
        dev = None
        if self._basedevice_ref is not None:
            dev = self._basedevice_ref()
        return dev

    @property
    def extid(self):
        return self._extid

    @property
    def location(self):
        return self._location

    def initialize(self, coord_ref: weakref.ReferenceType, basedevice_ref: weakref.ReferenceType, extid: str, location: str, configinfo: dict):
        """
            Initializes the landscape device extension.
        """
        self._coord_ref = coord_ref
        self._basedevice_ref = basedevice_ref
        self._extid = extid
        self._location = location
        self._configinfo = configinfo
        return