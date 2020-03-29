# Licensed under the MIT license
# http://opensource.org/licenses/mit-license.php
#
# Copyright (C) 2006 Fluendo, S.A. (www.fluendo.com).
# Copyright 2006, Frank Scholz <coherence@beebits.net>

import socket
import time

from typing import Tuple

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor
from twisted.internet import task

from coherence.upnp.core import utils
import coherence.extern.louie as louie
from coherence import log
from coherence.compat import bytes_cast, str_cast
from coherence.upnp.core.ssdp import SSDP_PORT, SSDP_ADDR


class MSearch(DatagramProtocol, log.Loggable):
    logCategory = 'msearch'

    def __init__(self, ssdp_server, test=False):
        log.Loggable.__init__(self)
        self.ssdp_server = ssdp_server
        self._double_discover_loop = None
        self._port = None
        if not test:
            self._port = reactor.listenUDP(0, self)

            self._double_discover_loop = task.LoopingCall(self.double_discover)
            self._double_discover_loop.start(120.0)

    def stopDiscovery(self):
        if self._double_discover_loop:
            self._double_discover_loop.stop()
        if self._port:
            self._port.stopListening()

    def datagramReceived(self, data: bytes, endpoint: Tuple[str, int]):
        (host, port) = endpoint

        resp_info, headers, content = utils.parse_http_response(data)
        resp_proto, resp_code, resp_status = resp_info
        del content # we do not need the content
        
        self.info('datagramReceived from %s:%d, protocol %s code %s', host, port, resp_proto, resp_code)

        if resp_proto.startswith(b'HTTP/1.') and resp_code == b'200':
            dev_svctype = headers[b'st']
            dev_usn = headers[b'usn']
            self.msg('for %r', dev_usn)
            if self.ssdp_server.service_seen(host, dev_svctype, headers):
                self.info('register as remote %(usn)s, %(st)s, %(location)s', headers)

        return

        # make raw data available
        # send out the signal after we had a chance to register the device
        louie.send('UPnP.SSDP.datagram_received', None, data, host, port)

    def double_discover(self):
        " Because it's worth it (with UDP's reliability) "
        self.info('send out discovery for ssdp:all')
        self.discover()
        self.discover()

    def discover(self):
        req = [b'M-SEARCH * HTTP/1.1',
                b'HOST: %s:%d' % (bytes_cast(SSDP_ADDR), SSDP_PORT),
                b'MAN: "ssdp:discover"',
                b'MX: 5',
                b'ST: ssdp:all',
                b'', b'']
        req = b'\r\n'.join(req)

        try:
            self.transport.write(req, (SSDP_ADDR, SSDP_PORT))
        except socket.error as msg:
            self.info("failure sending out the discovery message: %r", msg)
