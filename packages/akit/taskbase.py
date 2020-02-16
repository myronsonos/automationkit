
"""
.. module:: akit.taskbase
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module which contains the :class:`TaskBase` object which is used as the base.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""
from akit.scope import requires_scope

class TaskBase:

    required_scopes = None

    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        return

    @classmethod
    def do(cls, scope, *args, **kwargs):
        return

    @classmethod
    def begin(cls, scope, *args, **kwargs):
        return

    def enter(self):
        self._scope.enter()
        return

    def exit(self):
        self._scope.exit()
        return

