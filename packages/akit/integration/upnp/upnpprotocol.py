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
__license__ = "MIT"

import asyncio
import selectors
import socket
import time

import ssdp

from akit.exceptions import AKitTimeoutError

from asyncio import Protocol

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


class UpnpProtocol(ssdp.SimpleServiceDiscoveryProtocol):

    MULTICAST_ADDRESS = '239.255.255.250'
    PORT = 1900

    HEADERS = {
        "ST": MSearchTargets.ROOTDEVICE,
        "Man": "ssdp:discover",
        "MX": "1"
    }

    def __init__(self, notifyQueue, responseQueue):
        if responseQueue is None:
            print("oops")
        self._notifyQueue = notifyQueue
        self._responseQueue = responseQueue
        return

    def datagram_received(self, data, addr):
        data = data.decode()

        if data.startswith('HTTP/'):
            self.response_received(ssdp.SSDPResponse.parse(data), addr)
        elif data.startswith('M-SEARCH'):
            self.request_msearch(ssdp.SSDPRequest.parse(data), addr)
        elif data.startswith('NOTIFY'):
            self.request_notify(ssdp.SSDPRequest.parse(data), addr)
        else:
            self.request_other(ssdp.SSDPRequest.parse(data), addr)

    def response_received(self, response, addr):
        if self._responseQueue is None:
            print("oops")
        self._responseQueue.put_nowait((response, addr))
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


def inline_msearch(expected_devices, response_timeout=30, retry_count=5):
    """
        The inline msearch function provides a mechanism to do a synchronous msearch
        in order to determine if a set of available devices are available and to
        determine the interfaces that each device is listening on.

        :param expected_devices: The devices that are expected to be found by the msearch
        :type expected_devices: dict
        :param timeout: The maximum time in seconds to wait for the expected devices to report.
        :type timeout: float

        :returns:  dict -- A dictionary of the devices that were found.
        :raises: TimeoutError, KeyboardInterrupt
    """

    found_devices = {}
    matching_devices = {}

    class InlineMSearchProtocol(ssdp.SimpleServiceDiscoveryProtocol):

        def connection_lost(self, exc):
            loop = asyncio.get_event_loop()
            loop.stop()
            return

        def datagram_received(self, data, addr):
            data = data.decode()
            if data.startswith('HTTP/'):
                response = ssdp.SSDPResponse.parse(data)

                status_code = response.status_code
                if status_code == 200:
                    headers = dict([ (k.upper(), v) for k, v in response.headers])

                    usn = headers[MSearchKeys.USN]
                    if usn not in found_devices:
                        found_devices[usn] = headers

                    if usn in expected_devices and usn not in matching_devices:
                        matching_devices[usn] = headers

                    if len(matching_devices) == len(expected_devices):
                        run_loop = asyncio.get_event_loop()
                        run_loop.stop()

                print(response)

            return

    transport = None
    connect = None

    try:
        search_loop = asyncio.new_event_loop()

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

        multicast_address = UpnpProtocol.MULTICAST_ADDRESS
        multicast_port = UpnpProtocol.PORT

        # Bind to all addresses so we can find out which addresses each
        # expected device is actually listening on
        multicast_group = ('0.0.0.0', UpnpProtocol.PORT) 

        # Set us up to be a member of the group, this allows us to receive all the packets
        # that are sent to the group
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.INADDR_ANY)

        # Make sure other Automation processes can also bind to the UPNP address and port
        # so they can also get responses.
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

        sock.bind(multicast_group)

        protocol = InlineMSearchProtocol()

        def protocol_factory():
            return protocol

        connect = search_loop.create_datagram_endpoint(protocol_factory, sock=sock)
        transport, protocol = search_loop.run_until_complete(connect)

        attempt_counter = 0
        while attempt_counter < retry_count:
            notify = ssdp.SSDPRequest('M-SEARCH', headers=UpnpProtocol.HEADERS)
            notify.sendto(transport, (UpnpProtocol.MULTICAST_ADDRESS, UpnpProtocol.PORT))

            # Setup our Timeout
            now_time = search_loop.time()
            end_time = now_time + response_timeout
            def timeout_stop():
                search_loop.stop()
            search_loop.call_at(end_time, timeout_stop)

            search_loop.run_forever()

            if len(matching_devices) == len(expected_devices):
                break

            attempt_counter += 1

        if len(matching_devices) != len(expected_devices):
            err_msg = "Failed to find expected UPNP devices after %d retries with a timeout of %s seconds.\n" % (retry_count, response_timeout)

            err_msg += "EXPECTED: (%s)\n" % len(expected_devices)
            for dkey, dval in expected_devices.items():
                err_msg += "    %r:\n" % dval
            err_msg += "\n\n"

            err_msg += "MATCHING: (%s)\n" % len(matching_devices)
            for dkey, dval in matching_devices.items():
                err_msg += "    %r:\n" % dval
            err_msg += "\n\n"

            err_msg += "FOUND: (%s)\n" % len(found_devices)
            for dkey, dval in found_devices.items():
                err_msg += "    %r:\n" % dval
            err_msg += "\n"

            raise AKitTimeoutError(err_msg)

    except KeyboardInterrupt as kerr:
        raise
    finally:
        if transport is not None:
            transport.close()
        if connect is not None:
            connect.close()

    return found_devices, matching_devices


if __name__ == "__main__":
    from akit.integration.landscaping import Landscape

    landscape = Landscape()
    expected_upnp_devices = landscape.get_upnp_device_lookup_table()

    inline_msearch(expected_upnp_devices)

    print("Done")