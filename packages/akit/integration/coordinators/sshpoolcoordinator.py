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

import socket
import time
import weakref

from akit.paths import get_expanded_path
from akit.xlogging.foundations import getAutomatonKitLogger

from akit.integration.landscaping.landscapedevice import LandscapeDevice

from akit.integration.agents.sshagent import SshAgent

class SshPoolCoordinator:
    """
        The :class:`SshPoolCoordinator` creates a pool of agents that can be used to
        coordinate the interop activities of the automation process and remote SSH
        nodes.
    """

    def __init__(self):
        self._logger = getAutomatonKitLogger()
        self._agent_table = {}
        self._usn_to_ip_lookup = {}
        self._ip_to_host_lookup = {}
        return

    @property
    def device_agents(self):
        dalist = [a for a in self._agent_table.values()]
        return dalist

    def attach_to_devices(self, lscape, sshdevices, upnp_coord=None):

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
                    self._usn_to_ip_lookup[usn] = ipaddr
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
                self._ip_to_host_lookup[ip] = host

                agent = SshAgent(host, username, password=password, keyfile=keyfile, keypasswd=keypasswd, allow_agent=allow_agent)

                self._agent_table[host] = agent

                coord_ref = weakref.ref(self)

                basedevice = None
                if usn is not None:
                    basedevice = lscape._internal_lookup_device_by_keyid(usn)
                    basedevice.attach_extension("ssh", agent)
                else:
                    basedevice = LandscapeDevice("network/ssh", sshdev_config)
                    basedevice.attach_extension("ssh", agent)

                basedevice_ref = weakref.ref(basedevice)
                agent.initialize(coord_ref, basedevice_ref, host, ip, sshdev_config)
            else:
                ssh_config_errors.append(sshinfo)

        return ssh_config_errors

    def lookup_agent_by_host(self, host):
        """
            Looks up the agent for a device by its hostname.  If the
            agent is not found then the API returns None.
        """
        agent = None

        if host in self._agent_table:
            agent = self._agent_table[host]

        return agent

    def lookup_agent_by_ip(self, ip):
        """
            Looks up the agent for a device by its ip address.  If the
            agent is not found then the API returns None.
        """
        agent = None

        if ip in self._ip_to_host_lookup:
            host = self._ip_to_host_lookup[ip]
            agent = self.lookup_agent_by_host(host)

        return agent

    def lookup_agent_by_usn(self, usn):
        """
            Looks up the agent for a UPNP device by its USN.  If the
            agent is not found then the API returns None.
        """
        agent = None

        if usn in self._usn_to_ip_lookup:
            ip = self._usn_to_ip_lookup[usn]
            agent = self.lookup_agent_by_ip(ip)

        return agent
    
    def verify_connectivity(self, cmd="echo 'It Works'", user=None, raiseerror=True):
        """
            Loops through the nodes in the SSH pool and utilizes the
            credentials for the specified user in order to verify
            connectivity with the remote node.

            :param cmd: A command to run on the remote machine in order
                        to verify that ssh connectivity can be establish.
            :type cmd: str
            :param user: The name of the user credentials to use for connectivity.
                         If the 'user' parameter is not provided, then the 
                         credentials of the default or priviledged user will be used.
            :type user: str
        """
        results = []

        for agent in self._agent_table.values():
            host = agent.host
            ipaddr = agent.ipaddr
            try:
                status, stdout, stderr = agent.run_cmd(cmd)
                results.append((host, ipaddr, status, stdout, stderr, None))
            except Exception as xcpt:
                if raiseerror:
                    raise
                results.append((host, ipaddr, None, None, None, xcpt))

        return results

