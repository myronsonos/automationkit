"""
.. module:: extensible
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing classes that enable the discovery of extensions

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

from typing import List

import inspect
import os

from akit.compat import import_by_name
from akit.paths import get_directory_for_code_container

class LoadableExtension: # pylint: disable=too-few-public-methods
    """
        Marks a class as an extension for collection purposes so we can distinguish
        extension classes from base classes
    """

def collect_extensions_under_code_container(container, ext_base_type) -> List[type]:
    """
        Scans the code `container` provide and all descendant containers for classes
        that inherit from the type passed as `ext_base_type`

        :param container: A python package or module to scan for extension types.
        :type container: ModuleType
        :param ext_base_type: A python class type that serves as a base class to identify other
                              types that are a type of extension.
        :type ext_base_type: Type

        :returns: A list of types found that inherit from `ext_base_type`
        :rtype: List[Type]
    """
    ext_collection = []

    # This is declare here so it can be used as a closure
    nxtmod = None

    def is_extension_class(obj):
        result = False

        if inspect.isclass(obj):
            obj_container = obj.__module__
            if obj_container == nxtmod.__name__ and LoadableExtension in obj.__bases__:
                result = issubclass(obj, ext_base_type) and obj is not ext_base_type
        return result

    container_name = container.__name__
    container_dir = get_directory_for_code_container(container)
    container_parts = container_name.split(".")
    container_root = os.sep.join(container_dir.split(os.sep)[:-len(container_parts)])
    rootlen = len(container_root)

    for dirpath, _, filenames in os.walk(container_dir):
        leafdir = dirpath[rootlen:].lstrip(os.sep)
        leafcontainer = leafdir.replace(os.sep, ".")
        for nxtfile in filenames:
            nfbase, nfext = os.path.splitext(nxtfile)
            if nfext != ".py":
                continue

            nxtmodname = "%s.%s" % (leafcontainer, nfbase)
            nxtmod = import_by_name(nxtmodname)
            if nxtmod is None:
                continue

            ext_collection.extend(inspect.getmembers(nxtmod, predicate=is_extension_class))

    return ext_collection

def generate_extension_key(*parts) -> str:
    """
        Generates a unique key that identifies an extension type based on where
        it was found in a hiearchy of code containers.

        :params parts: List of names of the path to the extension type
        :type parts: List[str]

        :returns: A unique path based identifier for a type.
        :rtype: str
    """
    extkey = "/".join(parts)
    return extkey
