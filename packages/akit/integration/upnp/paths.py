"""
.. module:: paths
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing constants for different paths utilize by the code generator that are relative to the test framework.

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


import os

DIR_UPNP = os.path.dirname(__file__)


DIR_UPNP_EXTENSIONS = os.path.join(DIR_UPNP, "extensions")

DIR_UPNP_EXTENSIONS_DYNAMIC = os.path.join(DIR_UPNP_EXTENSIONS, "dynamic")
DIR_UPNP_EXTENSIONS_DYNAMIC_EMBEDDEDDEVICES = os.path.join(DIR_UPNP_EXTENSIONS, "dynamic", "embeddeddevices")
DIR_UPNP_EXTENSIONS_DYNAMIC_ROOTDEVICES = os.path.join(DIR_UPNP_EXTENSIONS, "dynamic", "rootdevices")
DIR_UPNP_EXTENSIONS_DYNAMIC_SERVICES = os.path.join(DIR_UPNP_EXTENSIONS, "dynamic", "services")
DIR_UPNP_EXTENSIONS_STANDARD = os.path.join(DIR_UPNP_EXTENSIONS, "standard")
DIR_UPNP_EXTENSIONS_STANDARD_EMBEDDEDDEVICES = os.path.join(DIR_UPNP_EXTENSIONS, "standard", "embeddeddevices")
DIR_UPNP_EXTENSIONS_STANDARD_ROOTDEVICES = os.path.join(DIR_UPNP_EXTENSIONS, "standard", "rootdevices")
DIR_UPNP_EXTENSIONS_STANDARD_SERVICES = os.path.join(DIR_UPNP_EXTENSIONS, "standard", "services")

DIR_UPNP_GENERATOR = os.path.join(DIR_UPNP, "generator")

DIR_UPNP_GENERATOR_DYNAMIC = os.path.join(DIR_UPNP_GENERATOR, "dynamic")
DIR_UPNP_GENERATOR_DYNAMIC_EMBEDDEDDEVICES = os.path.join(DIR_UPNP_GENERATOR, "dynamic", "embeddeddevices")
DIR_UPNP_GENERATOR_DYNAMIC_ROOTDEVICES = os.path.join(DIR_UPNP_GENERATOR, "dynamic", "rootdevices")
DIR_UPNP_GENERATOR_DYNAMIC_SERVICES = os.path.join(DIR_UPNP_GENERATOR, "dynamic", "services")

DIR_UPNP_GENERATOR_STANDARD = os.path.join(DIR_UPNP_GENERATOR, "standard")
DIR_UPNP_GENERATOR_STANDARD_EMBEDDEDDEVICES = os.path.join(DIR_UPNP_GENERATOR, "standard", "embeddeddevices")
DIR_UPNP_GENERATOR_STANDARD_ROOTDEVICES = os.path.join(DIR_UPNP_GENERATOR, "standard", "rootdevices")
DIR_UPNP_GENERATOR_STANDARD_SERVICES = os.path.join(DIR_UPNP_GENERATOR, "standard", "services")
