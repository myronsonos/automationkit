
"""
.. module:: akit.testing.testcontainer
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the base :class:`TestContainer` type and derived categorized test
               containers such as :class:`ArchitectureTestContainer`, :class:`BrickTestContainer`,
               :class:`LimitsTestContainer`, :class:`NegativeTestContainer`, :class:`BrickTestContainer`,
               :class:`SmokeTestContainer`, :class:`StressTestContainer`

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

import inspect
import sys
import traceback
import uuid

from akit.metadata import Category
from akit.mixins.scope import is_scope_mixin
from akit.exceptions import AKitOutOfScopeError, AKitRequestStopError, AKitSkipError
from akit.results import ResultCode, ResultType, ResultNode
from akit.xlogging import getAutomatonKitLogger

logger = getAutomatonKitLogger()

class TEST_CATEGORIES:
    ARCHITECTURE = "ARCHITECTURE"
    BRICK = "BRICK"
    LIMITS = "LIMITS"
    NEGATIVE = "NEGATIVE"
    POSITIVE = "POSITIVE"
    STRESS = "STRESS"
    SMOKE = "SMOKE"

class TestContainer:
    """
        The `TestContainer` object is the base container object that all other test containers
        should derive from.  The 'akit' framework unitizes the `TestContainer` as a code construct
        that is used to link testcases to external resources and also as a declaritive way to
        link test cases to the scopes of execution that they should execute in.  `TestContainer`s
        provide:
            * class and instance methods
            * class and instance data
            * integrated entities
            * a distrubuted context
            * a target scope that resides in a hierachy of scopes with a determined path
              and code to be able to enter and exit the target scope

        To integrate a testcase into the 'Automation Kit' test environment, a tester creates a
        test container class that derives from `TestContainer` itself or from a derived test.

        Users can define an entire hierarchy of `TestContainer` object that are used to pass on
        inherited or shared functionality to a derived container, however the primary means of passing
        on functionality should not necessarily be through the inheritance of a container.
        
        The passing on of functionality should take place through the appropriate parent or mixin
        type.  For example functionality that is used to interact with an external resource might
        come in through the inclusion of an :class:`akit.mixins.integration.IntegrationMixIn`
        parent type.  The passing on of functionality that is used to interact with a test containers
        target scope of execution should be included through the :class:`akit.mixins.scopes.ScopeMixIn`.

    """

    def __init__(self, testmethod, scope_type, recorder, *args, **kwargs):
        self._testmethod = testmethod
        self._scope_type = scope_type
        self._args = args
        self._kwargs = kwargs
        self._instance_id = str(uuid.uuid4())
        self._recorder = recorder
        self._cleanup_steps = []

        return

    @property
    def instance_id(self):
        return self._instance_id

    @property
    def scope_type(self):
        return self._scope_type

    @property
    def testname(self):
        tcls = self.__class__
        tname = "%s@%s#%s" % (tcls.__module__, tcls.__name__, self._testmethod.__name__)
        return tname

    def in_scope(self, expected):
        yes_in_scope = self._scope_type == expected
        return yes_in_scope

    def run(self, parent_inst):

        self._result = ResultNode(self._instance_id, self.testname, ResultType.TEST, parent_inst=parent_inst)

        testname = self.testname
        try:
            logger.info("RUNNING: TestCase %s" % testname)
            try:
                self.setUp()

                try:
                    self._testmethod(self)
                    self._mark_pass()
                except AssertionError as ass_err:
                    etype, einst, etb = sys.exc_info()
                    self._handle_failure(self._testmethod, etype, einst, etb)
                except Exception as tm_xcpt:
                    etype, einst, etb = sys.exc_info()
                    self._handle_error(self._testmethod, etype, einst, etb)

            except AKitSkipError as skp_err:
                self._mark_skip(skp_err.reason)
            except Exception as su_xcpt:
                self._raise_setup_error(su_xcpt)
            finally:
                cleanup_steps = list(self._cleanup_steps)
                while len(cleanup_steps) > 0:
                    cstep = cleanup_steps.pop()
                    try:
                        cstep()
                    except Exception as cu_xcpt:
                        etype, einst, etb = sys.exc_info()
                        self._handle_cleanup_error(etype, einst, etb)
            
        finally:
            self._result.finalize()
            logger.info("    %s: TestCase %s" % (self._result.result_code.name, testname))

        self._recorder.record(self._result)

        return

    def setUp(self):
        return

    def _handle_failure(self, tmethod, etype, einst, etb):
        fail_lines = traceback.format_exception(etype, einst, etb)
        self._result.add_failure(fail_lines)
        self._result.set_documentation(tmethod.__doc__)
        return

    def _handle_error(self, tmethod, etype, einst, etb):
        error_lines = traceback.format_exception(etype, einst, etb)
        self._result.add_error(error_lines)
        self._result.set_documentation(tmethod.__doc__)
        return

    def _handle_cleanup_error(self, etype, einst, etb):
        """
            Handle the cleanup step error by recording a warning.
        """
        warn_lines = traceback.format_exception(etype, einst, etb)
        self._result.add_warning(warn_lines)
        return

    def _handle_setup_error(self, etype, einst, etb):
        """
            Handle the cleanup step error by recording a warning.
        """
        error_lines = traceback.format_exception(etype, einst, etb)
        self._result.add_setup_error(error_lines)
        return

    def _mark_pass(self):
        """
            Mark this test as passed.
        """
        return self._result.mark_passed()

    def _mark_skip(self, reason):
        """
            Mark this test as skipped.
        """
        return self._result.mark_skip(reason)

    def _raise_setup_error(self, xcpt):
        return

@Category(TEST_CATEGORIES.ARCHITECTURE)
class ArchitectureTestContainer(TestContainer):
    """
        The `ArchitectureTestContainer` is a categorized `TestContainer` derivative that can be used
        as a base type for derivative test containers.  The `ArchitectureTestContainer` attaches the
        'ARCHITECTURE' category to the tests that reside in the container.
    """

@Category(TEST_CATEGORIES.BRICK)
class BrickTestContainer(TestContainer):
    """
        The `BrickTestContainer` is a categorized `TestContainer` derivative that can be used
        as a base type for derivative test containers.  The `BrickTestContainer` attaches the
        'BRICK' category to the tests that reside in the container.
    """

@Category(TEST_CATEGORIES.LIMITS)
class LimitsTestContainer(TestContainer):
    """
        The `LimitsTestContainer` is a categorized `TestContainer` derivative that can be used
        as a base type for derivative test containers.  The `LimitsTestContainer` attaches the
        'LIMITS' category to the tests that reside in the container.
    """

@Category(TEST_CATEGORIES.NEGATIVE)
class NegativeTestContainer(TestContainer):
    """
        The `NegativeTestContainer` is a categorized `TestContainer` derivative that can be used
        as a base type for derivative test containers.  The `NegativeTestContainer` attaches the
        'NEGATIVE' category to the tests that reside in the container.
    """

@Category(TEST_CATEGORIES.POSITIVE)
class PositiveTestContainer(TestContainer):
    """
        The `PositiveTestContainer` is a categorized `TestContainer` derivative that can be used
        as a base type for derivative test containers.  The `PositiveTestContainer` attaches the
        'POSITIVE' category to the tests that reside in the container.
    """

@Category(TEST_CATEGORIES.STRESS)
class StressTestContainer(TestContainer):
    """
        The `StressTestContainer` is a categorized `TestContainer` derivative that can be used
        as a base type for derivative test containers.  The `StressTestContainer` attaches the
        'STRESS' category to the tests that reside in the container.
    """

@Category(TEST_CATEGORIES.SMOKE)
class SmokeTestContainer(TestContainer):
    """
        The `SmokeTestContainer` is a categorized `TestContainer` derivative that can be used
        as a base type for derivative test containers.  The `SmokeTestContainer` attaches the
        'SMOKE' category to the tests that reside in the container.
    """

def inherits_from_testcontainer(cls):
    is_testcontainer = False
    if inspect.isclass(cls) and cls is not TestContainer and issubclass(cls, TestContainer):
        is_testcontainer = True
    return is_testcontainer
