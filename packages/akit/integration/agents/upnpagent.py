"""
.. module:: akit.integration.agents.upnpagent
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Module containing the :class:`UpnpAgent` class and associated diagnostic.

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
import os
import queue
import requests
import socket
import ssdp
import struct
import threading
import time
import typing
import traceback

from akit.integration.upnp.upnpprotocol import UpnpProtocol

class UpnpAgent:
    """
    """

    def __init__(self, coordinator, ifname, ifaddress, msearch_interval=60):

        self._coordinator = coordinator
        self._ifname = ifname
        self._ifaddress = ifaddress

        self._egate = None
        
        self._event_thread = None

        self._running = False

        return

    def start(self):
        """
        """

        self._egate = threading.Semaphore(1)

        try:
            sgate = threading.Event()

            self._running = True

            sgate.clear()
            self._events_thread = threading.Thread(name="UpnpAgent(%s) Events" % self._ifname, target=self._thread_entry_monitor, 
                                                   daemon=True, args=(sgate,))
            self._events_thread.start()
            sgate.wait()

        except:
            self._running = False
            self._egate.release()

            raise

        return

    def shutdown(self):
        self._running = False
        self._events_thread.join(timeout=5)
        return

    def wait_for_shutdown(self, timeout=None):
        # We need to be able to get 3 acquires to ensure all three threads
        # have exited
        acquires = 0
        try:
            self._egate.acquire(timeout=timeout)
            acquires += 1
        except TimeoutError:
            if acquires > 0:
                self._egate.release()
        return

    def _thread_entry_monitor(self, sgate):

        self._egate.acquire()

        multicast_address = UpnpProtocol.MULTICAST_ADDRESS
        multicast_port = UpnpProtocol.PORT

        try:
            sgate.set()

            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

            try:
                # Make sure other Automation processes can also bind to the UPNP address and port
                # so they can also get responses.
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)


                # Set us up to be a member of the group, this allows us to receive all the packets
                # that are sent to the group
                sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(multicast_address) + socket.inet_aton(self._ifaddress))

                sock.bind((multicast_address, multicast_port))

                while self._running:
                    request, addr = sock.recvfrom(1024)

                    print('IFNAME: %s ' % self._ifname)
                    print(request)
                    print()

            finally:
                sock.close()

        finally:
            self._egate.release()

        return

    

    

if __name__ == "__main__":
    agent = UpnpAgent("wlo1")
    agent.start()
    agent.begin_search()
    time.sleep(60 * 5)
    agent.begin_search()
    agent.wait_for_shutdown()
    pass

