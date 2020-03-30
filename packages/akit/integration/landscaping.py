"""
.. module:: akit.integration.landscape
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the :class:`TestLandscape` class and associated diagnostic.

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

import inspect

from akit.compat import import_by_name
from akit.environment.variables import VARIABLES

class LandscapeDescription:
    """
        The base class for all derived :class:`LandscapeDescription` objects.  The
        :class:`LandscapeDescription` is used to load a description of the entities
        and resources in the tests landscape that will be used by the tests.
    """

    @classmethod
    def register_integration_points(cls, landscape):
        return

    def load(self, landscapefile):
        return
    

class Landscape:
    """
        The base class for all derived :class:`Landscape` objects.  The :class:`Landscape`
        object is a singleton object that provides access to the resources and test
        environment level methods.
    """
    landscape_description = LandscapeDescription

    _landscape_type = None
    _instance = None
    _initialized = False

    def __new__(cls):
        """
            Constructs new instances of the Landscape object from the :class:`Landscape`
            type or from a derived type that is found in the module specified in the
            :module:`akit.environment.variables` module or by setting the
            'AKIT_LANDSCAPE_MODULE' environment variable.
        """
        if cls._instance is None:
            if cls._landscape_type is None:
                cls._instance = super(Type, cls).__new__(cls)
            else:
                cls._instance = super(Landscape, cls._landscape_type).__new__(cls._landscape_type)
            # Put any initialization here.
        return cls._instance
        
    def __init__(self):
        """
            Initializes the Singleton initializer class
        """
        this_cls = type(self)
        if not this_cls._initialized:
            this_cls._initialized = True
            self.initialize()
        return

    def initialize(self):
        """
            Called by '__init__' once at the beginning of the lifetime of a Landscape derived
            type.  This allows the derived types to participate in a customized intialization
            process.
        """
        self._ordered_roles = []
        self._integrations = {}

        self.landscape_description.register_integration_points(self)
        return

    def diagnostic(self, diaglabel, diags):
        """
            Can be called in order to perform a diagnostic capture across the test landscape.
        """
        return
    
    def first_contact(self):
        """
            This method should be called as early as possible in order to ensure the entities in the
            automation landscape exist and the authentication credentials provided for these entities
            are valid and usable to interact with these entities.

            :returns list: list of failing entities
        """
        return
    
    def register_integation_point(self, role, imixin):
        """
            This method should be called from the attach_to_environment methods from individual mixins
            in order to register the base level integrations.  Integrations can be hierarchical so it
            is only necessary to register the root level integration mixins, the descendant mixins can
            be called from the root level mixins.
        """
        if role not in self._integrations:
            self._ordered_roles.append(role)
            self._integrations[role] = imixin
        else:
            raise AKitSemanticError("A mixin with the role %r was already registered." % role)

        return

def is_subclass_of_landscape(cand_type):
    """
        Returns a boolean value indicating if the candidate type is a subclass
        of :class:`Landscape`.
    """
    is_scol = False
    if inspect.isclass(cand_type) and issubclass(cand_type, Landscape):
        is_scol = True
    return is_scol

def load_and_set_landscape_type(lscape_module):
    """
        Scans the module provided for :class:`Landscape` derived classes and will
        take the first one and assign it as the current runtime landscape type.
    """
    class_items = inspect.getmembers(lscape_module, is_subclass_of_landscape)
    for cls_name, cls_type in class_items:
        type_module_name = cls_type.__module__
        if type_module_name == lscape_module.__name__:
            Landscape._landscape_type = cls_type
            break
    return

if VARIABLES.AKIT_LANDSCAPE_MODULE is not None:
    lscape_module = import_by_name(VARIABLES.AKIT_LANDSCAPE_MODULE)
    load_and_set_landscape_type(lscape_module)
    check_landscape = Landscape()
    pass