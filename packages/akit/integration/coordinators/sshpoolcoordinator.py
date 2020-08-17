
import time

from akit.xlogging import getAutomatonKitLogger

from akit.integration.landscaping import Landscape
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
        return

    def load_from_config(self, upnp_coord=None):
        """
            Loads the :class:`SshPoolCoordinator` connection info from the config file.  The
            optional upnp_coord parameter is provided when the config file contains UPNP devices
            that support SSH.  The :class:`UpnpCoordinator` passed as the upnp_coord must be started
            up so it will have the opportunity to resolve the IP address of the upnp devices.
        """
        lscape = Landscape()

        sshdevices = lscape.get_ssh_devices()

        ssh_config_errors = []

        for sshdev in sshdevices:
            devtype = sshdev["deviceType"]
            sshinfo = sshdev["ssh"]
            ipaddr = None
            if "IP" in sshinfo:
                ipaddr = sshinfo["IP"]
            elif devtype == "network/upnp":
                usn = sshdev["USN"]
                if upnp_coord is not None:
                    dev = upnp_coord.lookup_device_by_usn(usn)
                    ipaddr = dev.IPAddress
                    self._usn_to_ip_lookup[usn] = ipaddr
                else:
                    ssh_config_errors.append(sshinfo)

            if ipaddr is not None:
                username = sshinfo["username"]
                password = sshinfo["password"]
                agent = SshAgent(ipaddr, username, password)
                self._agent_table[ipaddr] = agent
            else:
                ssh_config_errors.append(sshinfo)

        return

    def lookup_agent_by_ip(self, ip):
        """
            Looks up the agent for a device by its IP address.  If the
            agent is not found then the API returns None.
        """
        agent = None

        if ip in self._agent_table:
            agent = self._agent_table[ip]

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


if __name__ == "__main__":
    from akit.integration.coordinators.upnpcoordinator import UpnpCoordinator

    lscape = Landscape()
    upnp_hint_list = lscape.get_upnp_device_lookup_table()
    
    upnp_coord = UpnpCoordinator()
    upnp_coord.startup_scan(upnp_hint_list, exclude_interfaces=['lo'])

    sshpool = SshPoolCoordinator()
    sshpool.load_from_config(upnp_coord=upnp_coord)
    results = sshpool.verify_connectivity()

    for host, ip, status, stdout, stderr, xcpt in results:
        print ("Host: %s IP: %s" % (host, ip))
        print ("STDOUT:\n%s" % stdout)
        print ("STDERR:\n%s" % stderr)
        print ()

    agent = sshpool.lookup_agent_by_usn("uuid:RINCON_7828CAF55FF001400::upnp:rootdevice")
    agent.directory_tree("/")

    time.sleep(600)