"""
.. module:: testcollector
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
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

from typing import Optional, Sequence, Union
from types import ModuleType

import fnmatch
import inspect
import os
import traceback

from akit.compat import import_file

from akit.mixins.integration import is_integration_mixin
from akit.mixins.scope import is_iteration_scope_mixin

from akit.paths import collect_python_modules

from akit.testing.testcontainer import TestContainer, inherits_from_testcontainer
from akit.testing.testpack import DefaultTestPack, inherits_from_testpack, testpack_compare
from akit.testing.testref import TestRef

from akit.xlogging.foundations import getAutomatonKitLogger

logger = getAutomatonKitLogger()

def find_included_test_modules_under_root(root: str, package: Union[str, None], module: str):
    """
        Walks through a directory tree starting at a root directory and finds all of the files that corresponded to
        the package, module expressions specified.

        :param root: The root directory to start from when performing the tree walk to look
                     for included tests.
        :param package: The package name component if there is one.  The package components are the directories
                        with __init__.py files up to the file where the module file itself is found. It could be
                        that there is only a module name.
        :param module: The module name component.  There must be a module because that is the file where the tests
                       are found.
    """


    included_files = []

    if package is None:
        # If package is None, then we had a single item expression, this means
        # we can look for a single file, or a directory with lots of files.
        filenames = os.listdir(root)
        for fname in filenames:
            if fnmatch.fnmatch(fname, module):
                ffull = os.path.join(root, fname)
                if os.path.isfile(ffull):
                    fbase, fext = os.path.splitext(fname)
                    if fext == ".py" and fbase != "__init__":
                        included_files.append(ffull)
                elif os.path.isdir(ffull):
                    included_files.extend(collect_python_modules(ffull))
    else:
        pkgpathpfx = package.replace(".", "/")
        fullpathpfx = pkgpathpfx + "/" + module
        for dirpath, _, filenames in os.walk(root):
            dirleaf = dirpath[len(root):].lstrip(os.sep)

            # If we are in the testroot, then dirleaf will be len 0
            if len(dirleaf) > 0:
                if dirleaf.startswith(fullpathpfx) or fnmatch.fnmatch(dirleaf, fullpathpfx):
                    included_files.extend(collect_python_modules(dirpath))
                elif dirleaf.startswith(pkgpathpfx) or fnmatch.fnmatch(dirleaf, pkgpathpfx):
                    for fname in filenames:
                        fbase, fext = os.path.splitext(fname)
                        if fext == ".py" and fbase != "__init__" and \
                            fbase.startswith(module) and fnmatch.fnmatch(fbase, module):
                            ffull = os.path.join(dirpath, fname)
                            included_files.append(ffull)

    return included_files

def parse_include_expression(expression: str, testmodule: Optional[ModuleType], method_prefix: str = "test"):
    """
        Parses the include expression in connection with the testmodule and method_prefix information provided
        and returns the components (package, module, testclass, testname) which can be used to perform a
        test tree search for included tests based on the expression.

        :param expression: A test include expression in the form of (package).(module)@(testclass)#(testcase).  The module,
                           testclass, and testcase are optional.  If these items are excluded every descendant test found
                           under the (package) will be included.
        :param testmodule: A test module that contains the tests to be run.  This is passed when a individual test file
                           debugging workflow is being used.
        :param method_prefix: The string prefix that identifies test methods on a :class:`TestContainer` derived class.
    """

    expr_package = None
    expr_module = None
    expr_testclass = None
    expr_testname = None

    # If test_module was passed then we are running a test module as a script or debugging a test module
    # so we handle the special case where we only collect the test references from the test module that
    # was set.
    if testmodule is not None:
        if expression.find(".") > -1 or expression.find("@") > -1 or expression.find(":") > -1:
            raise ValueError("parse_include_expression: The include expression for test module runs should only have a " \
                             "test class and test method.")

        testmodule_name = testmodule.__name__

        expr_package = "*"
        expr_module = "*"

        # If the full path to the module was set correctly by the generic entry point, then replace the package and module
        # expressions with exact expressions so we don't load coad that does not need to be loaded when we are scanning
        # for tests.
        if testmodule_name != "__main__":
            tm_name_parts = testmodule_name.split('.')
            if len(tm_name_parts) > 1:
                expr_package = '.'.join(tm_name_parts[:-1])
                expr_module = tm_name_parts[-1]

        if expression.find("#") > -1:
            expression, expr_testname = expression.split("#")
            if not expr_testname.startswith(method_prefix):
                raise ValueError("parse_include_expression: The testname component of the expression must start with the " \
                                "method_prefix=%r. expression%r" % (method_prefix, expression))

        expr_testclass = expression

    # If self._test_module was not set then we are performing a commmandline run where a test job or includes, excludes
    # collection was passed we need to use one of those to determine what to run.
    else:
        # Start from the end of the expression and work backwards to determine what components in the expression were passed

        # First look for the # to see if we have a test name specified.
        if expression.find("#") > -1:
            expression, expr_testname = expression.split("#")
            if not expr_testname.startswith(method_prefix):
                raise ValueError("parse_include_expression: The testname component of the expression must " \
                                "start with the method_prefix=%r. expression%r" % (method_prefix, expression))

        if expression.find("@") > -1:
            expression, expr_testclass = expression.split("@")

        comb_expr_comp = expression.split(".")
        if len(comb_expr_comp) > 1:
            expr_package = ".".join(comb_expr_comp[:-1])
            expr_module = comb_expr_comp[-1]
        else:
            expr_package = None
            expr_module = expression

    return expr_package, expr_module, expr_testclass, expr_testname

class TestCollector:
    """
        The :class:`TestCollector` object utilizes the include and exclude expressions along with any test_module
        provided to collect the information about the test references and the associated test packages that will
        be involved in test run.
    """

    def __init__(self, root: str, excludes: Sequence[str], method_prefix: str = "test", test_module: ModuleType = None):
        """
            Initializes a :class:`TestCollector` instance in order to process the test tree and
            collect references and test packages to be run.

            :param root: The root directory to scan for included tests
            :param excludes: A list or sequence of exclude expressions to apply during test collection operations.
            :param module_prefix: The prefix or word that test methods will start with.  The default is 'test'.
            :param test_module: A test module which is passed for the debug workflow where a test module is run directly
                                as a script using the generic_test_entrypoint or in the debugger by Right-Click

        """
        self._root = root
        self._root_directory_listing = None
        self._excludes = excludes
        self._method_prefix = method_prefix
        self._test_module = test_module
        self._references = {}
        self._test_packages = {}
        self._import_errors = {}
        return

    @property
    def import_errors(self):
        """
            A list of import errors that were encountered while collecting test references.
        """
        return self._import_errors.values()

    @property
    def references(self):
        """
            A list of :class:`TestReferences` that were collected.
        """
        return self._references

    def collect_integrations(self):
        """
            Iterates through all of the test references and and collects the IntegrationMixins that
            are found.
        """

        integrations = {}
        for _, ref in self._references.items():
            for bcls in ref.testcontainer.__bases__:
                if is_integration_mixin(bcls):
                    mikey = bcls.__module__ + "." + bcls.__name__
                    if mikey in integrations:
                        integrations[mikey][1].append(ref)
                    else:
                        integrations[mikey] = (bcls, [ref])

        integlist = [ i for i in integrations.values()]

        return integlist

    def collect_references(self, expression: str):
        """
            Collects and appends the test references based on the expression provided and the excludes
            for this class.  The `collect_references` method is intended to be called multiple times,
            once with each include expression provided by the users.  The :class:`TestCollector` will
            extend its collection of reference with each successive call.

            :param expression: An include expression to process and collect references for.
        """

        expr_package, expr_module, expr_testclass, expr_testname = parse_include_expression(expression, self._test_module, self._method_prefix)

        # Find all the files that are included based on the expr_package, expr_module expressions
        included_files = []

        if self._test_module is not None:
            test_module_basename, _ = os.path.splitext(self._test_module.__file__)
            included_files.append(test_module_basename + ".py")
        elif expr_package is not None:
            included_files = find_included_test_modules_under_root(self._root, expr_package, expr_module)

        import_errors = {}

        # Go through the files and import them, then go through the classes and find the TestPack and
        # TestContainer objects that match the specified include expression criteria
        rootlen = len(self._root)
        for ifile in included_files:
            modname = None
            try:
                ifilebase, _ = os.path.splitext(ifile)
                ifileleaf = ifilebase[rootlen:].strip("/")
                modname = ifileleaf.replace("/", ".")

                # Import the module for the file being processed
                mod = import_file(modname, ifile)

                # Go through all of the members of the
                test_class_coll = inspect.getmembers(mod, inspect.isclass)
                for testclass_name, testclass_obj in test_class_coll:
                    tcobj_module_name = testclass_obj.__module__
                    # We only want to include the classes that are from the target module
                    if tcobj_module_name != modname:
                        continue

                    test_class_name = testclass_obj.__module__ + "@" + testclass_obj.__name__
                    if expr_testclass is not None and not fnmatch.fnmatch(testclass_name, expr_testclass):
                        continue

                    if inherits_from_testcontainer(testclass_obj):
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
                            include_class = False
                            if expr_testclass is None:
                                include_class = True
                            else:
                                class_name = testclass_obj.__name__
                                if fnmatch.fnmatch(expr_testclass, class_name):
                                    include_class = True

                            if include_class:
                                # If we don't have a testname expression then add all the test test methods for the class
                                test_method_coll = inspect.getmembers(testclass_obj, inspect.isfunction)
                                for method_name, method_obj in test_method_coll:
                                    if method_name.startswith(self._method_prefix):
                                        tname = test_class_name + "#" + method_name
                                        tref = TestRef(testclass_obj, method_obj)
                                        self._references[tname] = tref

                    elif inherits_from_testpack(testclass_obj):
                        # If we find a TestPack object that matches the criteria, look to see if the
                        # expression had a testname.  If it didn't we should save the TestPack reference
                        # in order to load the tests from the test pack.
                        if expr_testname is None:
                            if expr_testclass is None:
                                self._test_packages[test_class_name] = testclass_obj
                            else:
                                class_name = testclass_obj.__name__
                                if fnmatch.fnmatch(expr_testclass, class_name):
                                    self._test_packages[test_class_name] = testclass_obj

            except ImportError:
                errmsg = traceback.format_exc()
                print(errmsg)
                import_errors[ifile] = (modname, ifile, errmsg)

        self._import_errors.update(import_errors)

        for modname, ifile, errmsg in import_errors.values():
            logger.error("TestCase: Import error filename=%r" % ifile)

        return

    def collect_testpacks(self):
        """
            Goes through all of the test references and collects a list of the :class:`TestPack` types that are
            included in the collection of test references.  The :class:`TestPack` collection can be used to
            determine analyze the integrations and scopes that are associated with the collected test references.
        """
        # The testpack_table is filled with the top-level testpack types which
        # also are the top level scopes associated with an object.
        testpack_table = {}

        default_testpack_refs = []

        # Walk through all the test references. For each test reference, find its immediate testpack
        # or if it doesn't have one assign it to the default testpack
        for _, ref in self._references.items():

            # Go through all the parent objects and add the current test ref to each of the scope
            # classes found in the main class
            ref_testpacks = []
            for bcls in ref.testcontainer.__bases__:
                if inherits_from_testpack(bcls):
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
        for _, nxt_tpack_val in testpack_table.items():

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

        self._test_packages = testpack_table

        # Sort the testpack table by weight
        testpacks = [ v for v in self._test_packages.values()]
        testpacks.sort(key=testpack_compare, reverse=True)

        return testpacks

    def expand_testpacks(self):
        """
            The includes and excludes passed to the :class:`TestCollector` can also be used to find :class:`TestPack`(s).
            When an include specification includes a :class:`TestPack`, all the tests that are associated with that
            :class:`TestPack` are included in the test run.  They `expand_testpacks` method goes through all of the
            :class:`TestPack`(s), collect test references for all of the tests and then adds the test references to
            the list of included tests.
        """

        excluded = []

        if self._excludes is not None:
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
        import_errors = {}

        for tpack_name, tpack_obj in self._test_packages.items():
            searchin = tpack_obj.searchin
            if searchin is None:
                # If searchin was None, then we scan utilize the descendant directories of root
                searchin = [ dir for dir in self._directories_in_root() if not dir.endswith("__pycache__") ]

            scanfiles = []
            for sdir in searchin:
                scanfiles = collect_python_modules(sdir, max_depth=0)

                rootlen = len(self._root)
                for ifile in scanfiles:
                    _, fext = os.path.splitext(ifile)
                    if fext == ".py":
                        ifile_full = os.path.join(sdir, ifile)
                        modname = None
                        try:
                            ifilebase, _ = os.path.splitext(ifile_full)
                            ifileleaf = ifilebase[rootlen:].strip("/")
                            modname = ifileleaf.replace("/", ".")
                            mod = import_file(modname, ifile_full)

                            test_class_coll = inspect.getmembers(mod, inherits_from_testcontainer)
                            for _, testclass_obj in test_class_coll:
                                test_class_name = testclass_obj.__module__ + "@" + testclass_obj.__name__
                                if issubclass(testclass_obj, TestContainer) and issubclass(testclass_obj, tpack_obj):
                                    # If we don't have a testname expression then add all the test test methods for the class
                                    test_method_coll = inspect.getmembers(testclass_obj, inspect.isfunction)
                                    for method_name, method_obj in test_method_coll:
                                        if method_name.startswith(self._method_prefix):
                                            tname = test_class_name + "#" + method_name
                                            tref = TestRef(testclass_obj, method_obj)
                                            self._references[tname] = tref

                        except ImportError:
                            errmsg = traceback.format_exc()
                            print(errmsg)
                            import_errors[ifile] = (modname, ifile, errmsg)

        self._import_errors.update(import_errors)

        for modname, ifile, errmsg in import_errors.values():
            logger.error("TestPack: Import error filename=%r" % ifile)

        return

    def _record_child_scopes_at_level(self, scope_cls, level): # pylint: disable=no-self-use
        """
            Records all the scopes found in the hierarchy of a class at the level specified.
        """

        scopes_found = []

        for nxt_cls in scope_cls.__bases__:
            if is_iteration_scope_mixin(nxt_cls):
                if not hasattr(nxt_cls, "refcount"):
                    setattr(nxt_cls, "refcount", 1)
                else:
                    nxt_cls.refcount += 1
                scopes_found.append(nxt_cls)

        return scopes_found

    def _directories_in_root(self):
        """
            Gets a list of all the directories in the root directory tree.
        """

        if self._root_directory_listing is None:
            self._root_directory_listing = []
            for root, _, _ in os.walk(self._root, topdown = False):
                self._root_directory_listing.append(root)

        return self._root_directory_listing
