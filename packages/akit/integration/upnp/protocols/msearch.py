"""
.. module:: msearch
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the :class:`MSearchProtocol` class and
               associated diagnostic.

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

class MSearchProtocol(ssdp.SimpleServiceDiscoveryProtocol):

    MULTICAST_ADDRESS = '239.255.255.250'
    PORT = 1900

    HEADERS = {
        "ST": MSearchTargets.ROOTDEVICE,
        "Man": "ssdp:discover",
        "MX": "1"
    }

    def __init__(self):
        return

    def datagram_received(self, data, addr):
        data = data.decode()

        if data.startswith('HTTP/'):
            self.response_received(ssdp.SSDPResponse.parse(data), addr)
        elif data.startswith('MSEARCH'):
            self.request_msearch(ssdp.SSDPRequest.parse(data), addr)
        elif data.startswith('NOTIFY'):
            self.request_notify(ssdp.SSDPRequest.parse(data), addr)
        else:
            self.request_other(ssdp.SSDPRequest.parse(data), addr)

    def response_received(self, response, addr):
        print(response, addr)
        print()
        return

    def request_msearch(self, request, addr):
        print(request, addr)
        print()
        return

    def request_notify(self, request, addr):
        print(request, addr)
        print()
        return

    def request_other(self, request, addr):
        print(request, addr)
        print()
        return