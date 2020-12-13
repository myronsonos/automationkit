"""
.. module:: sshpoolcoordinator
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Contains the SshPoolCoordinator which is used for managing connectivity with pools of ssh capable devices

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

from typing import List, Optional, Union

import socket
import weakref

from akit.paths import get_expanded_path

from akit.integration.coordinators.coordinatorbase import CoordinatorBase
from akit.integration.coordinators.upnpcoordinator import UpnpCoordinator

from akit.integration.landscaping.landscapedevice import LandscapeDevice

from akit.integration.agents.sshagent import SshAgent

class SshPoolCoordinator(CoordinatorBase):
    """
        The :class:`SshPoolCoordinator` creates a pool of agents that can be used to
        coordinate the interop activities of the automation process and remote SSH
        nodes.
    """
    # pylint: disable=attribute-defined-outside-init

    def __init__(self, lscape, *args, **kwargs):
        super(SshPoolCoordinator, self).__init__(lscape, *args, **kwargs)
        return

    def _initialize(self, *_args, **_kwargs):
        """
            Called by the CoordinatorBase constructor to perform the one time initialization of the coordinator Singleton
            of a given type.
        """
        # pylint: disable=arguments-differ
        self._cl_usn_to_ip_lookup = {}
        self._cl_ip_to_host_lookup = {}
        return

    def attach_to_devices(self, sshdevices: List[dict], upnp_coord: Optional[UpnpCoordinator]=None):
        """
            Processes a list of device configs and creates and registers devices and SSH device extensions
            attached with the landscape for the devices not already registered.  If a device has already
            been registered by the UPNP coordinator then a device extension is created and attached to the
            existing device.

            :param sshdevices: A list of ssh device configuration dictionaries.
            :param upnp_coord: The UpnpCoordinator singleton instance.
        """

        lscape = self._lscape_ref()

        ssh_config_errors = []

        for sshdev_config in sshdevices:
            devtype = sshdev_config["deviceType"]
            sshinfo = sshdev_config["ssh"]
            host = None
            usn = None

            if "host" in sshinfo:
                host = sshinfo["host"]
            elif devtype == "network/upnp":
                usn = sshdev_config["upnp"]["USN"]
                if upnp_coord is not None:
                    dev = upnp_coord.lookup_device_by_usn(usn)
                    if dev is None:
                        dev = upnp_coord.lookup_device_by_usn(usn)
                    ipaddr = dev.IPAddress
                    host = ipaddr
                    self._cl_usn_to_ip_lookup[usn] = ipaddr
                else:
                    ssh_config_errors.append(sshinfo)

            if host is not None:
                username = sshinfo["username"]
                password = sshinfo["password"]

                keyfile = None
                if "keyfile" in sshinfo:
                    keyfile = get_expanded_path(sshinfo["keyfile"])

                keypasswd = None
                if "keypasswd" in sshinfo:
                    keypasswd = sshinfo["keypasswd"]

                allow_agent = False
                if "allow_agent" in sshinfo:
                    allow_agent = sshinfo["allow_agent"]

                ip = socket.gethostbyname(host)
                self._cl_ip_to_host_lookup[ip] = host

                agent = SshAgent(host, username, password=password, keyfile=keyfile, keypasswd=keypasswd, allow_agent=allow_agent)

                self._cl_children[host] = agent

                coord_ref = weakref.ref(self)

                basedevice = None
                if usn is not None:
                    basedevice = lscape._internal_lookup_device_by_keyid(usn) # pylint: disable=protected-access
                    basedevice.attach_extension("ssh", agent)
                else:
                    basedevice = LandscapeDevice(host, "network/ssh", sshdev_config)
                    basedevice.attach_extension("ssh", agent)

                basedevice_ref = weakref.ref(basedevice)
                agent.initialize(coord_ref, basedevice_ref, host, ip, sshdev_config)
            else:
                ssh_config_errors.append(sshinfo)

        return ssh_config_errors

    def lookup_device_by_host(self, host: str) -> Union[LandscapeDevice, None]:
        """
            Looks up the agent for a device by its hostname.  If the
            agent is not found then the API returns None.

            :param host: The host name of the LandscapeDevice to search for.

            :returns: The found LandscapeDevice or None
        """
        device = None

        self._coord_lock.acquire()
        try:
            if host in self._cl_children:
                device = self._cl_children[host].basedevice
        finally:
            self._coord_lock.release()

        return device

    def lookup_device_by_ip(self, ip) -> Union[LandscapeDevice, None]:
        """
            Looks up the agent for a device by its ip address.  If the
            agent is not found then the API returns None.

            :param ip: The ip address of the LandscapeDevice to search for.

            :returns: The found LandscapeDevice or None
        """
        device = None

        self._coord_lock.acquire()
        try:
            if ip in self._cl_ip_to_host_lookup:
                if ip in self._cl_ip_to_host_lookup:
                    host = self._cl_ip_to_host_lookup[ip]
                    if host in self._cl_children:
                        device = self._cl_children[host].basedevice
        finally:
            self._coord_lock.release()

        return device

    def lookup_device_by_usn(self, usn: str) -> Union[LandscapeDevice, None]:
        """
            Looks up the agent for a UPNP device by its USN.  If the
            agent is not found then the API returns None.

            :param usn: The USN of the LandscapeDevice to search for.

            :returns: The found LandscapeDevice or None
        """
        device = None

        self._coord_lock.acquire()
        try:
            if usn in self._cl_usn_to_ip_lookup:
                ip = self._cl_usn_to_ip_lookup[usn]
                if ip in self._cl_ip_to_host_lookup:
                    host = self._cl_ip_to_host_lookup[ip]
                    if host in self._cl_children:
                        device = self._cl_children[host].basedevice
        finally:
            self._coord_lock.release()

        return device

    def verify_connectivity(self, cmd: str = "echo 'It Works'", user: Optional[str] = None, raiseerror: bool = True) -> List[tuple]:
        """
            Loops through the nodes in the SSH pool and utilizes the
            credentials for the specified user in order to verify
            connectivity with the remote node.

            :param cmd: A command to run on the remote machine in order
                        to verify that ssh connectivity can be establish.
            :param user: The name of the user credentials to use for connectivity.
                         If the 'user' parameter is not provided, then the
                         credentials of the default or priviledged user will be used.
            :param raiseerror: A boolean value indicating if this API should raise an Exception on failure.

            :returns: A list of errors encountered when verifying connectivity with the devices managed or watched by the coordinator.
        """
        results = []

        for agent in self.children_as_extension:
            host = agent.host
            ipaddr = agent.ipaddr
            try:
                status, stdout, stderr = agent.run_cmd(cmd)
                results.append((host, ipaddr, status, stdout, stderr, None))
            except Exception as xcpt: # pylint: disable=broad-except
                if raiseerror:
                    raise
                results.append((host, ipaddr, None, None, None, xcpt))

        return results
