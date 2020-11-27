"""
.. module:: musecoordinator
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Contains the MuseCoordinator which is used for managing connectivity with muse managed
        devices visible in the automation landscape.

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
import weakref

from http.server import HTTPServer, BaseHTTPRequestHandler

from akit.paths import get_expanded_path
from akit.xlogging.foundations import getAutomatonKitLogger

from akit.integration.agents.museagent import MuseAgent
from akit.integration.landscaping.landscapedevice import LandscapeDevice

class MuseCoordinator:
    """
    """

    instance = None
    initialized = False

    def __new__(cls, **kwargs):
        """
            Constructs new instances of the :class:`MuseCoordinator` object. The
            :class:`MuseCoordinator` object is a singleton so following instantiations
            of the object will reference the existing singleton
        """

        if cls.instance is None:
            cls.instance = super(MuseCoordinator, cls).__new__(cls)
        return cls.instance

    def __init__(self, control_point=False, workers=5, watch_all=False):
        thisType = type(self)
        if not thisType.initialized:
            thisType.initialized = True

            self._logger = getAutomatonKitLogger()

            self._envlabel = None
            self._authhost = None
            self._ctlhost = None
            self._version = None

            self._agent_table = {}
            self._usn_to_ip_lookup = {}
            self._ip_to_host_lookup = {}


        return

    @property
    def device_agents(self):
        dalist = [a for a in self._agent_table.values()]
        return dalist

    def attach_to_devices(self, lscape, envlabel, authhost, ctlhost, version, musedevices, upnp_coord=None):

        self._envlabel = envlabel
        self._authhost = authhost
        self._ctlhost = ctlhost
        self._version = version

        muse_config_errors = []

        for musedev_config in musedevices:
            devtype = musedev_config["deviceType"]
            museinfo = musedev_config["muse"]
            host = None

            if "host" in museinfo:
                host = museinfo["host"]
            elif devtype == "network/upnp":
                usn = musedev_config["upnp"]["USN"]
                if upnp_coord is not None:
                    dev = upnp_coord.lookup_device_by_usn(usn)
                    if dev is None:
                        dev = upnp_coord.lookup_device_by_usn(usn)
                    ipaddr = dev.IPAddress
                    host = ipaddr
                    self._usn_to_ip_lookup[usn] = ipaddr
                else:
                    muse_config_errors.append(museinfo)

            if host is not None:
                username = museinfo["username"]
                password = museinfo["password"]
                apikey = museinfo["apikey"]
                secret = museinfo["secret"]

                bearer = None
                if "bearer" in museinfo:
                    bearer = museinfo["bearer"]

                ip = socket.gethostbyname(host)
                self._ip_to_host_lookup[ip] = host

                agent = MuseAgent(envlabel, authhost, ctlhost, host, username, password, apikey, secret, bearer=bearer, version=self._version)
                self._agent_table[host] = agent

                coord_ref = weakref.ref(self)

                basedevice = None
                if usn is not None:
                    basedevice = lscape._internal_lookup_device_by_keyid(usn)
                    basedevice.attach_extension("muse", agent)
                else:
                    basedevice = LandscapeDevice(host, "network/muse", musedev_config)
                    basedevice.attach_extension("muse", agent)

                basedevice_ref = weakref.ref(basedevice)
                agent.initialize(coord_ref, basedevice_ref, host, ip, musedev_config)
            else:
                muse_config_errors.append(museinfo)

        return muse_config_errors

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

    def _callback_server_entry(self):

        class AuthenticationCallbackHandler(BaseHTTPRequestHandler):

            def do_GET(self):
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Hello, world!')

        self._callback_server = HTTPServer(('localhost', 5000), AuthenticationCallbackHandler)

        self._callback_server.server_forever()