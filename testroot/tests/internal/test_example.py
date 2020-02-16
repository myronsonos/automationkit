"""
"""

import traceback

import akit.testing.activate

from akit.exceptions import AKitOutOfScopeError
from akit.metadata import Keywords
from akit.mixins.integration import IntegrationMixIn
from akit.mixins.scope import ScopeMixIn

from akit.testing.testcontainer import TestContainer, PositiveTestContainer

from integrations.exampleintegrations import ExampleIntegrationMixIn
from scopes.examplescopes import ExampleScopeAMixIn, ExampleScopeAAMixIn, ExampleScopeABMixIn, ExampleScopeBMixIn


class TestExampleAA(TestContainer, ExampleIntegrationMixIn, ExampleScopeAAMixIn):

    def test_hello_world_aa(self):
        print("Hello World, AA")
        return

class TestExampleAB(TestContainer, ExampleIntegrationMixIn, ExampleScopeABMixIn):

    def test_hello_world_ab(self):
        print("Hello World, AB")
        return

class TestExampleB(TestContainer, ExampleIntegrationMixIn, ExampleScopeBMixIn):

    def test_hello_world_b(self):
        print("Hello World, B")
        return

    def test_failure_b(self):
        """
            Test that raises an intentional failure.
        """
        raise AssertionError("Intentional failure")
        pass

class TestMultiScope(PositiveTestContainer, ExampleScopeABMixIn, ExampleScopeBMixIn):
    def __init__(self, *args, **kwargs):
        PositiveTestContainer.__init__(self, *args, **kwargs)
        return

    def test_multi_scope(self):
        if self.in_scope(ExampleScopeABMixIn):
            print("Multi-Scope in ExampleScopeABMixIn Yaaaah!!!")
        elif self.in_scope(ExampleScopeBMixIn):
            print("Multi-Scope in ExampleScopeBMixIn Yaaaah!!!")

        self.shout_out()

        try:
            self.only_in_B()
        except AKitOutOfScopeError:
            err_msg = traceback.format_exc()
            print(err_msg)
            pass
        except:
            err_msg = traceback.format_exc()
            print(err_msg)
            pass

        return

class TestMultipleScope(PositiveTestContainer, ExampleScopeAMixIn, ExampleScopeBMixIn):
    pass


if __name__ == "__main__":
    from akit.testing.entrypoints import generic_test_entrypoint
    generic_test_entrypoint()
