"""
.. module:: akit.testing.testref
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the base :class:`TestRef` type used to reference to
               tests that will be included into an a test execution graph.

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
class TestRef:
    """
    """

    def __init__(self, testcls, testmeth):
        self.testcls = testcls
        self.testmeth = testmeth
        return

    @property
    def test_name(self) -> str:
        tc = self.testcls
        test_name = "%s@%s#%s" % (tc.__module__, tc.__name__, self.testmeth.__name__)
        return test_name

    def create_instance(self, recorder):
        testinst = self.testcls(self.testmeth, recorder)
        return testinst

