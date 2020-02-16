"""
.. module:: akit.context
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the :class:`Context` object and :class:`ContextCursor` that
               are used to maintain the shared automation context.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

import re
import os

from datetime import datetime

from akit.environment.variables import VARIABLES
from akit.environment.configuration import RUNTIME_CONFIGURATION


REGEX_PATH_VALIDATOR = re.compile("/{1}([a-zA-Z0-9]+)")

def validate_path_name(path):
    parts = None
    mobj = REGEX_PATH_VALIDATOR.findall(path)
    if mobj is not None:
        parts = list(mobj)
    return parts

class ContextCursor:

    def __init__(self, storeref):
        self._storeref = storeref
        return

    def fill_template(self, template):
        filled = template % self._storeref
        return filled

    def insert(self, path, obj):

        if isinstance(path, list) or isinstance(path, tuple):
            path_parts = path
            path = "/%s" %  "/".join(path_parts)
        else:
            path_parts = validate_path_name(path.rstrip("/"))
        
        self._insert(self._storeref, path, path_parts, obj)
    
        return

    def lookup(self, path):
        found_node = None

        if isinstance(path, list) or isinstance(path, tuple):
            path_parts = path
            path = "/%s" %  "/".join(path_parts)
        else:
            path_parts = validate_path_name(path.rstrip("/"))

        found_node = self._lookup(self._storeref, path, path_parts)

        return found_node

    def _insert(self, dref, path, path_parts, obj):

        if len(path_parts) > 0:
            leaf_name = path_parts[0]
            if len(path_parts) > 1:
                if leaf_name not in dref:
                    dref[leaf_name] = {}
                found_node = dref[leaf_name]
                self._insert(found_node, path, path_parts[1:], obj)
            else:
                dref[leaf_name] = obj
        else:
            raise ValueError("Invalid path=%s" % path)

        return

    def _lookup(self, dref, path, path_parts):

        found_node = None

        if len(path_parts) > 0:
            leaf_name = path_parts[0]
            if leaf_name in dref:
                found_node = dref[leaf_name]
                if len(path_parts) > 1:
                    if isinstance(found_node, dict):
                        found_node = self._lookup(found_node, path, path_parts[1:])
                    else:
                        LookupError("Context lookup failure for path=%s" % path)
                else:
                    if isinstance(found_node, dict):
                        found_node = ContextCursor(found_node)
            else:
                raise LookupError("Context lookup failure for path=%s" % path)
        else:
            raise ValueError("Invalid path=%s" % path)

        return found_node

    def __contains__(self, key):
        found = key in self._storeref
        return found

    def __getitem__(self, key):
        found_node = self._lookup(self._storeref, key, [key])
        return found_node

    def __setitem__(self, key, val):
        self._insert(self._storeref, key, [key], val)
        return

    def __repr__(self):
        return repr(self._storeref)
    
    def __str__(self):
        return str(self._storeref)

class Context:

    _instance = None
    _store = {}

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Context, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def insert(self, path, obj):

        if isinstance(path, list) or isinstance(path, tuple):
            path_parts = path
            path = "/%s" %  "/".join(path_parts)
        else:
            path_parts = validate_path_name(path.rstrip("/"))
        
        self._insert(self._store, path, path_parts, obj)
    
        return

    def lookup(self, path):
        found_node = None

        if isinstance(path, list) or isinstance(path, tuple):
            path_parts = path
            path = "/%s" %  "/".join(path_parts)
        else:
            path_parts = validate_path_name(path.rstrip("/"))

        found_node = self._lookup(self._store, path, path_parts)

        return found_node

    def _insert(self, dref, path, path_parts, obj):

        if len(path_parts) > 0:
            leaf_name = path_parts[0]
            if len(path_parts) > 1:
                if leaf_name not in dref:
                    dref[leaf_name] = {}
                found_node = dref[leaf_name]
                self._insert(found_node, path, path_parts[1:], obj)
            else:
                dref[leaf_name] = obj
        else:
            raise ValueError("Invalid path=%s" % path)

        return

    def _lookup(self, dref, path, path_parts):

        found_node = None

        if len(path_parts) > 0:
            leaf_name = path_parts[0]
            if leaf_name in dref:
                found_node = dref[leaf_name]
                if len(path_parts) > 1:
                    if isinstance(found_node, dict):
                        found_node = self._lookup(found_node, path, path_parts[1:])
                    else:
                        LookupError("Context lookup failure for path=%s" % path)
                else:
                    if isinstance(found_node, dict):
                        found_node = ContextCursor(found_node)
            else:
                raise LookupError("Context lookup failure for path=%s" % path)
        else:
            raise ValueError("Invalid path=%s" % path)

        return found_node

    def __contains__(self, key):
        found = key in self._storeref
        return found

    def __getitem__(self, key):
        found_node = self._lookup(self._store, [key])
        return found_node

    def __setitem__(self, key, val):
        self._insert(self._storeref, key, [key], val)
        return

default_environment = {
    "branch": VARIABLES.AKIT_BRANCH,
    "build": VARIABLES.AKIT_BUILD,
    "jobtype": VARIABLES.AKIT_JOBTYPE,
    "starttime": datetime.now(),
    "configuration": RUNTIME_CONFIGURATION,
    "output_directory": os.path.expanduser("~/aresults")
}

# Initialize the global context
context = Context()
context.insert("/environment", default_environment)

class ContextUser:
    context = Context()
