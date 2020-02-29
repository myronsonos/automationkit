"""
"""

import traceback

import akit.environment.activate

from akit.exceptions import AKitOutOfScopeError
from akit.metadata import Keywords
from akit.mixins.integration import IntegrationMixIn
from akit.mixins.scope import ScopeMixIn

from akit.testing.testpack import TestPack
from akit.testing.testcontainer import TestContainer, PositiveTestContainer

from integrations.exampleintegrations import ExampleIntegrationMixIn
from scopes.examplescopes import ExampleScopeAMixIn, ExampleScopeAAMixIn, ExampleScopeABMixIn, ExampleScopeBMixIn


class TestPackageAA(TestPack, ExampleIntegrationMixIn, ExampleScopeAAMixIn):
    """
    """

class TestPackageAB(TestPack, ExampleIntegrationMixIn, ExampleScopeABMixIn):
    """
    """

class TestPackB(TestPack, ExampleIntegrationMixIn, ExampleScopeBMixIn):
    """
    """

class TestExampleAA(TestContainer, TestPackageAA):

    def test_hello_world_aa(self):
        print("Hello World, AA")
        return

class TestExampleAB(TestContainer, TestPackageAB):

    def test_hello_world_ab(self):
        print("Hello World, AB")
        return

class TestExampleB(TestContainer, TestPackB):

    def test_hello_world_b(self):
        print("Hello World, B")
        return

    def test_failure_b(self):
        """
            Test that raises an intentional failure.
        """
        raise AssertionError("Intentional failure")
        pass



if __name__ == "__main__":
    from akit.testing.entrypoints import generic_test_entrypoint
    generic_test_entrypoint()
