"""
.. module:: akit.integration.upnp.protocols.msearch
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the :class:`MSearchRootDeviceProtocol` class and
               associated diagnostic.

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>

"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@automationmojo.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = ""

import ssdp
import weakref

class MSearchTargets:
    ROOTDEVICE = "upnp:rootdevice"
    ALL="ssdp:all"

class MSearchKeys:
    CACHE_CONTROL = "CACHE-CONTROL"
    EXT = "EXT"
    LOCATION = "LOCATION"
    SERVER = "SERVER"
    ST = "ST"
    USN = "USN"


class MSearchRootDeviceProtocol(ssdp.SimpleServiceDiscoveryProtocol):
    PORT = 1900
    HEADERS = {
        "ST": MSearchTargets.ROOTDEVICE,
        "Man": "ssdp:discover",
        "MX": "1"
    }

    def __init__(self, agent):
        self._agent_ref = weakref.ref(agent)
        return

    def response_received(self, response, addr):
        print(response, addr)
        print()

        reason = response.reason
        status_code = response.status_code
        version = response.version
        headers = dict([ (k.upper(), v) for k, v in response.headers])

        # Process the packet
        location = headers[MSearchKeys.LOCATION]

        # promote our reference to the agent and push and update
        agent = self._agent_ref()
        if agent is not None:
            agent._update_root_device(location, headers)

        return

    def request_received(self, request, addr):
        print(request, addr)
        print()
        return