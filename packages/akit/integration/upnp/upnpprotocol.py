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
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import asyncio
import netifaces
import os
import re
import selectors
import socket
import threading
import time

import ssdp

from akit.exceptions import AKitTimeoutError

from asyncio import Protocol

REGEX_NOTIFY_HEADER = re.compile("NOTIFY[ ]+[*/]+[ ]+HTTP/1")

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

    IP = "IP"
    ROUTES = "ROUTES"

class MSearchRouteKeys:
    IFNAME = "LOCAL_IFNAME"
    IP = "LOCAL_IP"


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

class MSearchScanContent:
    """
        The :class:`MSearchScanContext` is an object that allows the sharing of scan results across threads
        that are scanning mulitple interfaces.  We utilize a shared scan context so we can find the devices
        faster.
    """

    def __init__(self, upnp_device_hints):
        self.upnp_device_hints = upnp_device_hints
        self.remaining_device_hints = [dh for dh in upnp_device_hints]

        self.have_hints = False
        if len(self.remaining_device_hints) > 0:
            self.have_hints = True

        self.continue_scan = True

        self.found_devices = {}
        self.matching_devices = {}

        self.lock = threading.Lock()
        return

    def register_device(self, ifname, usn, device_info, route_info):

        self.lock.acquire()
        try:
            if usn not in self.found_devices:

                device_info[MSearchKeys.ROUTES].append(route_info)

                self.found_devices[usn] = device_info

                if usn in self.remaining_device_hints:
                    self.remaining_device_hints.remove(usn)

                    self.matching_devices[usn] = device_info

                if self.have_hints and len(self.remaining_device_hints) == 0:
                    self.continue_scan = False
            else:
                existing_info = self.found_devices[usn]
                existing_info[MSearchKeys.ROUTES].append(route_info)

        finally:
            self.lock.release()

        return

def msearch_parse_request(content: bytes):
    """
        Takes in the content of the MSEARCH request and parses it into a
        python dictionary object.

        :param content: MSearch request content as a bytes.
        :type content: bytes

        :return: A python dictionary with key and values from the MSearch request
        :rtype: :class:`dict`
    """
    content = content.decode('utf-8')

    respinfo = None

    resplines = content.splitlines(False)
    if len(resplines) > 0:
        header = resplines.pop(0).strip()
        if header.startswith("M-SEARCH *"):
            respinfo = {}
            for nxtline in resplines:
                cidx = nxtline.find(":")
                if cidx > -1:
                    key = nxtline[:cidx].upper()
                    val = nxtline[cidx+1:].strip()
                    respinfo[key] = val

    return respinfo

def msearch_parse_response(content: bytes):
    """
        Takes in the content of the response of an MSEARCH request and parses it into a
        python dictionary object.

        :param content: MSearch response content as a bytes.
        :type content: bytes

        :return: A python dictionary with key and values from the MSearch response
        :rtype: :class:`dict`
    """
    content = content.decode('utf-8')

    respinfo = None

    resplines = content.splitlines(False)
    if len(resplines) > 0:
        header = resplines.pop(0).strip()
        if header.startswith("HTTP/"):
            respinfo = {}
            for nxtline in resplines:
                cidx = nxtline.find(":")
                if cidx > -1:
                    key = nxtline[:cidx].upper()
                    val = nxtline[cidx+1:].strip()
                    respinfo[key] = val

    return respinfo



def msearch_on_interface(scan_context, ifname, ifaddress, mx=1, st=MSearchTargets.ROOTDEVICE, response_timeout=45, interval=2):
    """
        The inline msearch function provides a mechanism to do a synchronous msearch
        in order to determine if a set of available devices are available and to
        determine the interfaces that each device is listening on.

        :param scan_context: A shared scan context that shares information between the scan threads and
                             speeds up the process of finding the expected UPNP devices across the
                             interfaces.
        :type scan_context: :class:`MSearchScanContent`
        :param timeout: The maximum time in seconds to wait for the expected devices to report.
        :type timeout: float

        :returns:  dict -- A dictionary of the devices that were found.
        :raises: TimeoutError, KeyboardInterrupt
    """

    route_info = {
        MSearchRouteKeys.IFNAME: ifname,
        MSearchRouteKeys.IP: ifaddress
    }

    multicast_address = UpnpProtocol.MULTICAST_ADDRESS
    multicast_port = UpnpProtocol.PORT

    msearch_msg = b"\r\n".join([
        b'M-SEARCH * HTTP/1.1',
        b'HOST: %s:%d' % (UpnpProtocol.MULTICAST_ADDRESS.encode("utf-8"), UpnpProtocol.PORT),
        b'MAN: "ssdp:discover"',
        b'ST: %s' % st.encode("utf-8"),
        b'MX: %d' % mx,
        b'',
        b''
    ])

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

    try:
        # Make sure other Automation processes can also bind to the UPNP address and port
        # so they can also get responses.
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Set the IP protocol level socket opition binding the socket to the interface
        # specified by the IP address provided
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.inet_aton(ifaddress))
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
        
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)

        sock.settimeout(interval)

        sock.sendto(msearch_msg, (multicast_address, multicast_port))

        current_time = time.time()
        end_time = current_time + response_timeout
        while current_time < end_time and scan_context.continue_scan:

            try:
                resp, addr = sock.recvfrom(1024)
                device_info = msearch_parse_response(resp)
                foundst = device_info.get(MSearchKeys.ST, None)
                if device_info is not None and foundst == st and MSearchKeys.USN in device_info:
                    devusn = device_info[MSearchKeys.USN]

                    device_info[MSearchKeys.ROUTES] = []
                    device_info[MSearchKeys.IP] = addr[0]

                    scan_context.register_device(ifname, devusn, device_info, route_info)

            except socket.timeout:
                pass

            current_time = time.time()

    except KeyboardInterrupt:
        raise
    finally:
        sock.close()

    return


def msearch_scan(expected_devices, interface_list=None, response_timeout=45, interval=2):

    if interface_list is None:
        interface_list = netifaces.interfaces()

    scan_context = MSearchScanContent(expected_devices)

    search_threads = []

    for ifname in interface_list:
        ifaddress = None

        address_info = netifaces.ifaddresses(ifname)
        if address_info is not None:
            # First look for IPv4 address information
            if netifaces.AF_INET in address_info:
                addr_info = address_info[netifaces.AF_INET][0]
                ifaddress = addr_info["addr"]

            # If we didn't find an ipv4 address, try using IPv6
            # if ifaddress is None and netifaces.AF_INET6 in addr_info:
            #    addr_info = address_info[netifaces.AF_INET6][0]
            #    ifaddress = addr_info["addr"]

            if ifaddress is not None:
                thname = "msearch-%s" % ifname
                thargs = (scan_context, ifname, ifaddress)
                thkwargs = { "response_timeout":response_timeout , "interval": interval}
                sthread = threading.Thread(name=thname, target=msearch_on_interface, args=thargs, kwargs=thkwargs)
                sthread.start()
                search_threads.append(sthread)

    # Wait for all the search threads to finish
    while len(search_threads) > 0:
        nxt_thread = search_threads.pop(0)
        nxt_thread.join()

    if len(scan_context.matching_devices) != len(expected_devices):
        err_msg = "Failed to find expected UPNP devices after a timeout of %s seconds.\n" % response_timeout

        missing = [dkey for dkey in expected_devices]
        for dkey in scan_context.found_devices:
            if dkey in missing:
                missing.remove(dkey)

        err_msg_lines = []
        err_msg_lines.append("EXPECTED: (%s)" % len(expected_devices))
        for dkey in expected_devices:
            err_msg_lines.append("    %r:" % dkey)
        err_msg_lines.append("")

        err_msg_lines.append("MATCHING: (%s)" % len(scan_context.matching_devices))
        for dkey in scan_context.matching_devices:
            err_msg_lines.append("    %r:" % dkey)
        err_msg_lines.append("")

        err_msg_lines.append("FOUND: (%s)" % len(scan_context.found_devices))
        for dkey in scan_context.found_devices:
            err_msg_lines.append("    %r:" % dkey)
        err_msg_lines.append("")

        err_msg_lines.append("MISSING: (%s)" % len(missing))
        for dkey in missing:
            err_msg_lines.append("    %r:" % dkey)
        err_msg_lines.append("")

        err_msg = os.linesep.join(err_msg_lines)
        raise AKitTimeoutError(err_msg)

    return scan_context.found_devices, scan_context.matching_devices

def notify_parse_request(content):
    """
        Takes in the content of the NOTIFY request and parses it into a
        python dictionary object.

        :param content: Notify request content as a string.
        :type content: str

        :return: A python dictionary with key and values from the Notify request
        :rtype: :class:`dict`
    """
    content = content.decode('utf-8')

    resp_headers = None
    resp_body = None

    mobj = REGEX_NOTIFY_HEADER.search(content)
    if mobj is not None:
        header_content = None
        body_content = None

        if content.find("\r\n\r\n") > -1:
            header_content, body_content = content.split("\r\n\r\n", 1)
        elif content.find("\n\n") > -1:
            header_content, body_content = content.split("\n\n", 1)
        else:
            header_content = content

        resplines = header_content.splitlines(False)
        
        # Pop the NOTIFY header
        resplines.pop(0).strip()

        resp_headers = {}
        for nxtline in resplines:
            cidx = nxtline.find(":")
            if cidx > -1:
                key = nxtline[:cidx].upper()
                val = nxtline[cidx+1:].strip()
                resp_headers[key] = val

        if body_content is not None:
            resp_body = body_content

    return resp_headers, resp_body

if __name__ == "__main__":
    from akit.integration.landscaping import Landscape

    landscape = Landscape()
    expected_upnp_devices = [usn for usn in landscape.get_upnp_device_lookup_table().keys()]

    found_devices, matching_devices = msearch_scan(expected_upnp_devices)

    print()
    print("FOUND DEVICES")
    for devkey, devinfo in found_devices.items():
        print("    USN: %s " % devkey)

    print()
    print("MATCHING DEVICES")
    for devkey, devinfo in matching_devices.items():
        print("    USN: %s " % devkey)

    print()
    print("Done")