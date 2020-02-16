"""
.. module:: akit.testing.testref
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the base :class:`TestRef` type used to reference to
               tests that will be included into an a test execution graph.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

class TestRef:
    """
    """

    def __init__(self, testcls, testmeth):
        self.testcls = testcls
        self.testmeth = testmeth
        return

    @property
    def test_name(self):
        tc = self.testcls
        test_name = "%s@%s#%s" % (tc.__module__, tc.__name__, self.testmeth.__name__)
        return test_name

    def create_instance(self, scope_type, recorder):
        testinst = self.testcls(self.testmeth, scope_type, recorder)
        return testinst

