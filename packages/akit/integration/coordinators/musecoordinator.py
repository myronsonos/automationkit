"""
.. module:: musecoordinator
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Contains the MuseCoordinator which is used for managing connectivity with muse managed
        devices visible in the automation landscape.

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


class MuseCoordinator:
    """
    """

    instance = None
    initialized = False

    def __new__(cls, **kwargs):
        """
            Constructs new instances of the :class:`MuseCoordinator` object. The 
            :class:`MuseCoordinator` object is a singleton so following instantiations
            of the object will reference the existing singleton
        """

        if cls.instance is None:
            cls.instance = super(MuseCoordinator, cls).__new__(cls)
        return cls.instance

    def __init__(self, control_point=False, workers=5, watch_all=False):
        if not self.initialized:
            self.initialized = True

            
            self._agents = []
            self._children = {}

            self._running = False

        return
