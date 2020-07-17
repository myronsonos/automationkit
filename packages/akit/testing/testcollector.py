"""
.. module:: akit.testing.testcollector
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module that contains the `TestCollector` object which is utilized to collection the
               information about the tests, scopes and integration that will be included in an
               automation run.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@automationmojo.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import fnmatch
import inspect
import os
import sys
import traceback

from akit.compat import import_file

from akit.mixins.integration import IntegrationMixIn, is_integration_mixin
from akit.mixins.scope import ScopeMixIn, is_scope_mixin

from akit.testing.testcontainer import TestContainer, inherits_from_testcontainer
from akit.testing.testpack import TestPack, DefaultTestPack, is_testpack, testpack_compare
from akit.testing.testref import TestRef
from akit.testing.utilities import find_testmodule_root, find_testmodule_fullname

from akit.xlogging import getAutomatonKitLogger

logger = getAutomatonKitLogger()

class TestCollector:
    """
    """

    def __init__(self, root, excludes, method_prefix="test", test_module=None):
        self._root = root
        self._root_directory_listing = None
        self._excludes = excludes
        self._method_prefix = method_prefix
        self._test_module = test_module
        self._references = {}
        self._testpacks = []
        self._import_errors = []
        return

    @property
    def import_errors(self):
        return self._import_errors

    @property
    def references(self):
        return self._references

    def collect_integrations(self):

        integrations = {}
        for _, ref in self._references.items():
            for bcls in ref.testcls.__bases__:
                if is_integration_mixin(bcls):
                    mikey = bcls.__module__ + "." + bcls.__name__
                    if mikey in integrations:
                        integrations[mikey][1].append(ref)
                    else:
                        integrations[mikey] = (bcls, [ref])

        return integrations

    def collect_references(self, expression):
        """
            Collects and appends the test references based on the expression provided and the excludes for this class.
        """
        expr_package = None
        expr_module = None
        expr_testclass = None
        expr_testname = None

        # If self._test_module was set then we are running a test module as a script or debugging a test module
        # so we handle the special case where we only collect the test references from the test module that
        # was set.
        if self._test_module is not None:
            if expression.find(".") > -1 or expression.find("@") > -1 or expression.find(":") > -1:
                raise ValueError("TestCollector:collect_reference: The include expression for test module runs should " \
                                 "only have a test class and test method.")

            expr_package = "*"
            expr_module = "*"

            if expression.find("#") > -1:
                expression, expr_testname = expression.split("#")
                if not expr_testname.startswith(self._method_prefix):
                    raise ValueError("TestCollector:collect_references: The testname component of the expression must " \
                                    "start with the method_prefix=%r. expression%r" % (self._method_prefix, expression))

            expr_testclass = expression

        # If self._test_module was not set then we are performing a commmandline run where a test job or includes, excludes
        # collection was passed we need to use one of those to determine what to run.
        else:
            if expression.find("#") > -1:
                expression, expr_testname = expression.split("#")
                if not expr_testname.startswith(self._method_prefix):
                    raise ValueError("TestCollector:collect_references: The testname component of the expression must " \
                                    "start with the method_prefix=%r. expression%r" % (self._method_prefix, expression))

            if expression.find("@") > -1:
                expression, expr_testclass = expression.split("@")

            comb_expr_comp = expression.split(".")
            if len(comb_expr_comp) > 1:
                expr_package = ".".join(comb_expr_comp[:-1])
                expr_module = comb_expr_comp[-1]
            else:
                expr_package = expression
                expr_module = None

        # Find all the files that are included based on the expression
        included_files = []

        if self._test_module is not None:
            test_module_basename, test_module_ext = os.path.splitext(self._test_module.__file__)
            included_files.append(test_module_basename + ".py")
        else:
            if expr_package is None:
                filenames = os.listdir(self._root)
                for fname in filenames:
                    ffull = os.path.join(self._root, fname)
                    if os.path.isfile(ffull):
                        if fnmatch.fnmatch(fname, expr_module):
                            fbase, fext = os.splitext(fname)
                            if fext == ".py" and fbase != "__init__":
                                included_files.append(ffull)
            else:
                for dirpath, dirnames, filenames in os.walk(self._root):
                    dirleaf = dirpath[len(self._root):].lstrip(os.sep)
                    if len(dirleaf) == 0 and expr_package.find(".") == -1:
                        for fname in filenames:
                            fbase, fext = os.path.splitext(fname)
                            if fext == ".py" and fbase.startswith(expr_package):
                                ffull = os.path.join(dirpath, fname)
                                included_files.append(ffull)
                    elif os.path.exists(os.path.join(dirpath, "__init__.py")):
                        pkgname = dirleaf.replace("/", ".")
                        if fnmatch.fnmatch(pkgname, expr_package):
                            if expr_module is not None:
                                for fname in filenames:
                                    if fname.startswith(expr_module) or fnmatch.fnmatch(fname, expr_module):
                                        fbase, fext = os.path.splitext(fname)
                                        if fext == ".py" and fbase != "__init__":
                                            ffull = os.path.join(dirpath, fname)
                                            included_files.append(ffull)
                            else:
                                for fname in filenames:
                                    fbase, fext = os.path.splitext(fname)
                                    if fext == ".py" and fbase != "__init__":
                                        ffull = os.path.join(dirpath, fname)
                                        included_files.append(ffull)

        import_errors = []

        # Go through the files and import them, then go through the classes and find the TestPack and
        # TestContainer objects that match the specified 
        rootlen = len(self._root)
        for ifile in included_files:
            try:
                ifilebase, ifileext = os.path.splitext(ifile)
                ifileleaf = ifilebase[rootlen:].strip("/")
                modname = ifileleaf.replace("/", ".")
                mod = import_file(modname, ifile)
                test_class_coll = inspect.getmembers(mod, inherits_from_testcontainer)
                for testclass_name, testclass_obj in test_class_coll:
                    tcobj_module_name = testclass_obj.__module__
                    # We only want to include the classes that are from the target module
                    if tcobj_module_name == modname:
                        test_class_name = testclass_obj.__module__ + "@" + testclass_obj.__name__
                        if expr_testclass is not None:
                            if fnmatch.fnmatch(testclass_name, expr_testclass):
                                if issubclass(testclass_obj, TestContainer):
                                    if expr_testname is not None:
                                        # We have a testname expression so go through all the test methods and and check
                                        # the test method names
                                        test_method_coll = inspect.getmembers(testclass_obj, inspect.isfunction)
                                        for method_name, method_obj in test_method_coll:
                                            if method_name.startswith(self._method_prefix):
                                                if fnmatch.fnmatch(method_name, expr_testname):
                                                    tname = test_class_name + "#" + method_name
                                                    tref = TestRef(testclass_obj, method_obj)
                                                    self._references[tname] = tref
                                    else:
                                        # If we don't have a testname expression then add all the test test methods for the class
                                        test_method_coll = inspect.getmembers(testclass_obj, inspect.isfunction)
                                        for method_name, method_obj in test_method_coll:
                                            if method_name.startswith(self._method_prefix):
                                                tname = test_class_name + "#" + method_name
                                                tref = TestRef(testclass_obj, method_obj)
                                                self._references[tname] = tref
                                elif issubclass(testclass_obj, TestPack):
                                    # If we find a TestPack object that matches the criteria, look to see if the
                                    # expression had a testname.  If it didn't we should save the TestPack reference
                                    # in order to load the tests from the test pack.
                                    if expr_testname is None:
                                        self._testpacks[test_class_name] = testclass_obj

                        else:
                            # If we don't have a testclass expression then add all the test classes and test methods
                            test_method_coll = inspect.getmembers(testclass_obj, inspect.isfunction)
                            for method_name, method_obj in test_method_coll:
                                if method_name.startswith(self._method_prefix):
                                    tname = test_class_name + "#" + method_name
                                    tref = TestRef(testclass_obj, method_obj)
                                    self._references[tname] = tref

            except Exception as xcpt:
                errmsg = traceback.format_exc()
                print(errmsg)
                import_errors.append((modname, ifile, errmsg))

        self._import_errors.extend(import_errors)

        for modname, ifile, errmsg in import_errors:
            logger.error("TestCase: Import error filename=%r" % ifile)

        return

    def collect_testpacks(self):

        # The testpack_table is filled with the top-level testpack types which
        # also are the top level scopes associated with an object.
        testpack_table = {}

        default_testpack_refs = []

        # Walk through all the test references. For each test reference, find its immediate testpack
        # or if it doesn't have one assign it to the default testpack
        for ref_name, ref in self._references.items():

            # Go through all the parent objects and add the current test ref to each of the scope
            # classes found in the main class
            ref_testpacks = []
            for bcls in ref.testcls.__bases__:
                if is_testpack(bcls):
                    ref_testpacks.append(bcls)

            # If we didn't find a TestPackMixIn derived object, then
            # add this test reference to the DefaultTestPackMixIn
            ref_leaf_testpack_count = len(ref_testpacks)
            if ref_leaf_testpack_count == 0:
                default_testpack_refs.append(ref)

            elif ref_leaf_testpack_count == 1:
                leaf_testpack_cls = ref_testpacks[0]

                if leaf_testpack_cls.test_references is None:
                    leaf_testpack_cls.test_references = []

                test_references = leaf_testpack_cls.test_references
                test_references.append(ref)

                mtpkey = leaf_testpack_cls.__module__ + "." + leaf_testpack_cls.__name__
                if mtpkey not in testpack_table:
                    testpack_table[mtpkey] = leaf_testpack_cls

            else:
                raise Exception("Assigning a TestCollection to more than one TestPack is not currently supported.")

        # We need to go through all of the testpacks and walk the class hierarchy of each
        # and as we find a scope derived type, we need to add that type into a table based
        # on its level in the class hierarcy.  The testpack type ensures we have one reference
        # into the type hierarchy at level 0. We will be executing the scopes starting with
        # level 0 and moving up based on usage.

        # As we walk the tree we increment each scopes usage counter. When a scope exits, we can
        # decrement its reference count.  We will walk the full scope hierarchy as we run
        # the tests associated with each testpack, however, we only execute the enter code
        # when the scope is entered for the first time and we only execute the exit code when
        # the last reference count is removed.
        for nxt_tpack_key, nxt_tpack_val in testpack_table.items():

            # The tope TestPack will always have a reference count of 1
            nxt_tpack_val.refcount = 1

            # Preset the level to 0 and weight to 1
            level = 0
            weight = 1
            
            found_at_level = [nxt_tpack_val]
            while True:
                search_scopes = found_at_level
                level += 1
                found_at_level = []
                for nxt_scope in search_scopes:
                    found_scopes = self._record_child_scopes_at_level(nxt_scope, level)
                    found_at_level.extend(found_scopes)
                    for fscope in found_scopes:
                        weight += ((fscope.refcount) * (level + 1))

                if len(found_at_level) == 0:
                    break

            # The weight of the TestPack is a combination of how deep the levels of scopes are under
            # the TestPack and the number of scopes.  We try to optimize the ordering of running
            # the TestPack(s) by weight
            nxt_tpack_val.weight = weight



        if len(default_testpack_refs) > 0:
            DefaultTestPack.test_references = default_testpack_refs

        self._testpacks = list(testpack_table.values())

        # Sort the testpack table by weight
        self._testpacks.sort(key=testpack_compare, reverse=True)

        return self._testpacks

    def expand_testpacks():

        excluded = []
        # Go through all of the exclude expressions and utilize them to mark the TestPack objects that
        # should be excluded from the test run
        for ex_expr in self._excludes:
            for tpack_name, tpack_obj in self._test_packages.items():
                if tpack_name.startswith(ex_expr):
                    excluded.append(tpack_name)

        # Go through all the excluded test packs and then remove them from the test packs catalog
        # by name
        for tpack_name in excluded:
            del self._test_packages[tpack_name]

        # Go through all of the test package references and load the tests that are associated with the
        # test package
        for tpack_name, tpack_obj in self._test_packages.items():
            searchin = tpack_obj.searchin
            if searchin is None:
                # If searchin was None, then we scan utilize the descendant directories of root
                searchin = self._root_directories()

            for sdir in searchin:
                scanfiles = [f for f in os.listdir(sdir) if os.path.isfile(f)]
                for nxtfile in scanfiles:
                    fbase, fext = os.path.splitext(nxtfile)
                    if fext == ".py":
                        nxtfile_full = os.path.join(sdir, nxtfile)
                        try:
                            ifilebase, ifileext = os.path.splitext(ifile)
                            ifileleaf = ifilebase[rootlen:].strip("/")
                            modname = ifileleaf.replace("/", ".")
                            mod = import_file(modname, ifile)

                            test_class_coll = inspect.getmembers(mod, inherits_from_testcontainer)
                            for testclass_name, testclass_obj in test_class_coll:
                                test_class_name = testclass_obj.__module__ + "@" + testclass_obj.__name__
                                if issubclass(testclass_obj, TestContainer) and issubclass(testclass_obj, tpack_obj):
                                    # If we don't have a testname expression then add all the test test methods for the class
                                    test_method_coll = inspect.getmembers(testclass_obj, inspect.isfunction)
                                    for method_name, method_obj in test_method_coll:
                                        if method_name.startswith(self._method_prefix):
                                            tname = test_class_name + "#" + method_name
                                            tref = TestRef(testclass_obj, method_obj)
                                            self._references[tname] = tref

                        except Exception as xcpt:
                            errmsg = traceback.format_exc()
                            print(errmsg)
                            import_errors.append((modname, ifile, errmsg))
        
        self._import_errors.extend(import_errors)

        for modname, ifile, errmsg in import_errors:
            logger.error("TestPack: Import error filename=%r" % ifile)

        return

    def _record_child_scopes_at_level(self, scope_cls, level):
        scopes_found = []

        for nxt_cls in scope_cls.__bases__:
            if is_scope_mixin(nxt_cls):
                if not hasattr(nxt_cls, "refcount"):
                    setattr(nxt_cls, "refcount", 1)
                else:
                    nxt_cls.refcount += 1
                scopes_found.append(nxt_cls)

        return scopes_found

    def _root_directories(self):
        if self._root_directory_listing is None:
            self._root_directory_listing = []
            for root, dirs, files in os.walk(self._root, topdown = False):
                self._root_directory_listing.append(root)

        return self._root_directory_listing
