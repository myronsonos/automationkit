
import socket
import time

from akit.paths import get_expanded_path
from akit.xlogging import getAutomatonKitLogger

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

    def attach_to_devices(self, sshdevices, upnp_coord=None):

        ssh_config_errors = []

        for sshdev in sshdevices:
            devtype = sshdev["deviceType"]
            sshinfo = sshdev["ssh"]
            host = None

            if "host" in sshinfo:
                host = sshinfo["host"]
            elif devtype == "network/upnp":
                usn = sshdev["upnp"]["USN"]
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

                ip = socket.gethostbyname(host)
                self._ip_to_host_lookup[ip] = host

                agent = SshAgent(host, username, password=password, keyfile=keyfile, keypasswd=keypasswd)
                self._agent_table[host] = agent
            else:
                ssh_config_errors.append(sshinfo)

        return ssh_config_errors

    def load_from_config(self, lscape, upnp_coord=None):
        """
            Loads the :class:`SshPoolCoordinator` connection info from the config file.  The
            optional upnp_coord parameter is provided when the config file contains UPNP devices
            that support SSH.  The :class:`UpnpCoordinator` passed as the upnp_coord must be started
            up so it will have the opportunity to resolve the IP address of the upnp devices.
        """

        sshdevices = lscape.get_ssh_devices()

        self.attach_to_devices(sshdevices, upnp_coord=upnp_coord)

        return

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

