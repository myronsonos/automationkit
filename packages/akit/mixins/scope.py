"""
    .. module:: akit.mixins.scope

    A scope represents a predefined state that is reached by the execution of code.  The state represents a
    requirement that is needed to be met in order for a task to be able to run.

    Scopes have a name that is like a file system path /environment/configuration

    Scopes can contain state and they are deposited into the context in a leaf just like other nodes.


"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@automationmojo.com"
__status__ = "Development" # Prototype, Development or Production
#__license__ = ""

import inspect
import weakref

from akit.environment.context import ContextUser

class ScopeMixIn(ContextUser):   
    """
        The :class:`ScopeMixIn` object is the base object class that is used for scope declaration. :class:`ScopeMixIn`
        derived objects are used to create a hierarchy of scopes that are representative of the scopes of execution
        that are represented by the runtime environment.  These scopes of execution are used to establish the runtime
        contexts that task and test instantiations can be run inside of.  The scopes of a runtime environment are
        typically hierarchical in nature starting with the root object of a tree and build more complexed 
        environments as they the hierarchy is ascended.

        The code of the :class:`ScopeMixIn` is divided into class level code and instance level code.  The hierarchy
        of the :class:`ScopeMixIn` derived objects are used by the :class:`akit.testing.testsequencer.Sequencer`
        object to determine the grouping and order of the tests or tasks to be run.  The class level code of the
        :class:`ScopeMixIn` is run by the :class:`akit.sequencer.Sequencer` object based on the class hierarchy to
        establish the order that scopes are entered and exited as the automation sequence is executed by the
        :class:`akit.testing.testsequencer.Sequencer` object.  The :class:`ScopeMixIn` class level code, is executed
        before any object that inherits from a :class:`ScopeMixIn` derived object is instantiated, so the state for the
        scope has been establish.

        The :class:`ScopeMixIn` instance level code is utilized to inter-operate with the state of the scope and also
        provides scope specific functionality.

    """

    TEMPLATE_SCOPES_PREFIX = "/scopes/%s"

    pathname = None

    descendants = {}
    test_references = {}

    def __init__(self):
        """
            The default contructor for an :class:`ScopeMixIn`.
        """
        if self.pathname is None:
            scope_type = type(self)
            scope_leaf = (scope_type.__module__ + "." + scope_type.__name__).replace(".", "/")
            self.pathname = self.TEMPLATE_SCOPES_PREFIX % scope_leaf

        # Create a weak reference to this scope in the global context and create a finalizer that
        # will remove the weak reference when the scope object is destroyed
        wref = weakref.ref(self)
        weakref.finalize(self, scope_finalize, self.context, self.pathname)

        self.context.insert(self.pathname, wref)
        return

    @classmethod
    def scope_enter(cls):
        """
            This API is called by the sequencer when a scope of state is being entered by an automation
            run.  The derived `ScopeMixIn` implementation should initialize the scope they are designed
            to manage and if initialization fails, they should raise a :class:`akit.exceptions.AKitScopeEntryError`
            error.

            :raises :class:`akit.exceptions.AKitScopeEntryError`:
        """
        return

    @classmethod
    def scope_exit(cls):
        """
            This API is called by the sequencer when an automation run is exiting a scope.  The derived
            ScopeMixIn implementation should use this opportunity to tear down the scope that it is
            managing.
        """
        return

def is_scope_mixin(cls): -> bool
    is_scopemi = False
    if inspect.isclass(cls) and cls is not ScopeMixIn and issubclass(cls, ScopeMixIn):
        is_scopemi = True
    return is_scopemi

def scope_finalize(context, pathname):
    context.
    return