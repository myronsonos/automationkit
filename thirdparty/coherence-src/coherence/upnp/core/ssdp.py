# Licensed under the MIT license
# http://opensource.org/licenses/mit-license.php

# Copyright 2005, Tim Potter <tpot@samba.org>
# Copyright 2006 John-Mark Gurney <gurney_j@resnet.uroegon.edu>
# Copyright (C) 2006 Fluendo, S.A. (www.fluendo.com).
# Copyright 2006,2007,2008,2009 Frank Scholz <coherence@beebits.net>
# Copyright 2014 Hartmut Goebel <h.goebel@crazy-compilers.com>
#
# Implementation of a SSDP server under Twisted Python.
#

import random
import string
import sys
import time
import socket

from typing import Tuple

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor, error
from twisted.internet import task
from twisted.web.http import datetimeToString

from coherence import log, SERVER_ID
from coherence.compat import bytes_cast, str_cast
from coherence.upnp.core import utils
import coherence.extern.louie as louie

SSDP_PORT = 1900
SSDP_ADDR = '239.255.255.250'


class SSDPServer(DatagramProtocol, log.Loggable):
    """
        A class implementing a SSDP server.  The notifyReceived and searchReceived methods
        are called when the appropriate type of datagram is received by the server.
    """
    logCategory = 'ssdp'

    def __init__(self, test: bool = False, interface: str = ''):
        # Create SSDP server
        log.Loggable.__init__(self)

        self.__test = test

        self._known = {}
        self._callbacks = {}
        self.active_calls = []
        self._resend_notify_loop = None
        self._expire_loop = None
        self._port = None
        if not self.__test:
            try:
                self._port = reactor.listenMulticast(SSDP_PORT, self, listenMultiple=True)
                #self.port.setLoopbackMode(1)
                self._port.joinGroup(SSDP_ADDR, interface=interface)
            except error.CannotListenError as err:
                self.error("Error starting the SSDP-server: %s", err)
                self.error("There seems to already be a SSDP server "
                           "running on this host, no need starting a "
                           "second one.")

            self._resend_notify_loop = task.LoopingCall(self._resendNotify)

            # notify every 777 seconds (~ 13 Minutes)
            self._resend_notify_loop.start(777.0, now=False)

            self._expire_loop = task.LoopingCall(self._expire)

            # expire every 333 seconds (~ 5.5 Minutes)
            self._expire_loop.start(333.0, now=False)

        return

    def stopNotifying(self):
        """
            Stops the notification loop and stops listening for events.
        """
        if self._resend_notify_loop and self._resend_notify_loop.running:
            self._resend_notify_loop.stop()
        if self._port:
            self._port.stopListening()
        return

    def shutdown(self):
        """
            Shuts down the services
        """
        for call in reactor.getDelayedCalls():
            if call.func == self.__send__discovery_request:
                call.cancel()
        if not self.__test:
            self.stopNotifying()
            if self._expire_loop.running:
                self._expire_loop.stop()
            # Make sure we send out the byebye notifications.
            for st in self._known:
                if self._known[st]['MANIFESTATION'] == 'local':
                    self.doByebye(st)

    def datagramReceived(self, data: bytes, endpoint: Tuple[str, int]):
        """
            Handle a received multicast datagram.
        """
        (host, port) = endpoint

        resp_info, headers, content = utils.parse_http_response(data)
        resp_proto, resp_code, resp_status = resp_info
        del content # we do not need the content

        self.info('SSDP command %s %s - from %s:%d', resp_proto, resp_code, host, port)
        self.debug('with headers: %s', headers)
        if resp_proto == 'M-SEARCH' and resp_code == b'*':
            # SSDP discovery
            self._discoveryRequest(headers, (host, port))
        elif resp_proto == b'NOTIFY' and resp_code == b'*':
            # SSDP presence
            self._notifyReceived(headers, (host, port))
        else:
            self.warning('Unknown SSDP command %s %s', esp_proto, resp_code)

        # make raw data available
        # send out the signal after we had a chance to register the device
        louie.send('UPnP.SSDP.datagram_received', None, data, host, port)

        return

    def register(self, manifestation: bytes, usn: bytes, st: bytes, location: bytes,
                       server: bytes = SERVER_ID, cache_control: bytes = b'max-age=1800',
                       silent: bool = False, host: bytes = None):
        """
            Register a service or device that this SSDP server will respond to."""

        self.info('Registering %s (%s)', st, location)

        self._known[usn] = {
            b'USN': bytes_cast(usn), # Unique Service Name
            b'LOCATION': bytes_cast(location),
            b'ST': bytes_cast(st), # Service Type
            b'EXT': b'',
            b'SERVER': bytes_cast(server),
            b'CACHE-CONTROL': bytes_cast(cache_control),
            b'MANIFESTATION': bytes_cast(manifestation),
            b'SILENT': silent,
            b'HOST': bytes_cast(host),
            b'last-seen': time.time(),
        }

        self.debug('%r', self._known[usn])

        if manifestation == 'local':
            self.doNotify(usn)

        if st == 'upnp:rootdevice':
            louie.send('Coherence.UPnP.SSDP.new_device', None, device_type=st, infos=self._known[usn])
            #self.callback("new_device", st, self._known[usn])

        return

    def unRegister(self, usn: bytes):
        if not self._isKnown(usn):
            return
        self.info("Un-registering %s", usn)
        st = self._known[usn][b'ST']
        if st == 'upnp:rootdevice':
            louie.send('Coherence.UPnP.SSDP.removed_device', None,
                       device_type=st, infos=self._known[usn])
            #self.callback("removed_device", st, self._known[usn])

        del self._known[usn]

        return

    def isKnown(self, usn: bytes) -> bool:
        """
            Checks to see if a service name is known.
        """
        return usn in self._known

    def service_seen(self, host: bytes, service_type: bytes, headers: dict) -> bool:
        """
        Mark a service as been seen. If the service is not yet known, automatically register it.

        Returns True, if the service was unknown.
        """
        dev_usn = headers[b'usn']
        dev_server = headers[b'server']
        dev_location = headers[b'location']
        dev_cachecont = headers[b'cache-control']

        known = False
        if dev_usn in self._known:
            self._known[dev_usn][b'last-seen'] = time.time()
            known = True
        else:
            self.register('remote', dev_usn, service_type,
                          dev_location, dev_server,
                          dev_cachecont, host=host)

        self.debug('updating last-seen for %r', dev_usn)

        return known

    def _notifyReceived(self, headers, endpoint):
        """
            Process a presence announcement.  We just remember the details of the SSDP
            service announced.
        """
        (host, port) = endpoint

        self.info('Notification from (%s,%d) for %s', host, port, headers[b'nt'])
        self.debug('Notification headers: %s', headers)

        if headers[b'nts'] == b'ssdp:alive':
            self.service_seen(host, headers[b'nt'], headers)
        elif headers[b'nts'] == b'ssdp:byebye':
            self.unRegister(headers[b'usn'])
        else:
            self.warning('Unknown subtype %s for notification type %s', headers[b'nts'], headers[b'nt'])
        louie.send('Coherence.UPnP.Log', None, 'SSDP', host,
                   'Notify %s for %s' % (headers[b'nts'], headers[b'usn']))
        return

    def __send__discovery_request(self, response, destination, delay, usn):
        self.info('send discovery response delayed by %ds for %s to %r',
                  delay, usn, destination)
        try:
            self.transport.write(response, destination)
        except (AttributeError, socket.error) as msg:
            self.info("failure sending out byebye notification: %r", msg)
        return

    def _discoveryRequest(self, headers, endpoint):
        """
            Process a discovery request.  The response must be sent to the address specified by endpoint.
        """
        (host, port) = endpoint

        self.info('Discovery request from (%s,%d) for %s', host, port, headers[b'st'])
        louie.send('Coherence.UPnP.Log', None, 'SSDP', host, 'M-Search for %s' % headers[b'st'])

        # Do we know about this service?
        for known in self._known.values():
            if known[b'MANIFESTATION'] == b'remote':
                continue
            elif known[b'SILENT'] and headers[b'st'] == b'ssdp:all':
                continue
            elif headers[b'st'] == known[b'ST'] or headers[b'st'] == b'ssdp:all':
                response = []
                response.append(b'HTTP/1.1 200 OK')
                for k, v in known.items():
                    if k not in (b'MANIFESTATION', b'SILENT', b'HOST'):
                        response.append('%s: %s' % (k, v))
                response.append(b'DATE: %s' % bytes_cast(datetimeToString()))
                response.extend((b'', b''))
                response = b'\r\n'.join(response)

                delay = random.randint(0, int(headers[b'mx']))
                reactor.callLater(delay, self.__send__discovery_request,
                                  response, (host, port), delay, known[b'USN'])
        return

    def __build_response(self, cmd, usn):
        resp = [b'NOTIFY * HTTP/1.1',
            b'HOST: %s:%d' % (bytes_cast(SSDP_ADDR), SSDP_PORT),
            b'NTS: %s' % cmd,
            ]
        stcpy = self._known[usn].copy()
        stcpy[b'NT'] = stcpy[b'ST']
        for k in (b'ST', b'MANIFESTATION', b'SILENT', b'HOST', b'last-seen'):
            try:
                # :fixme: this keys should always exist as we build the entry
                del stcpy[k]
            except:
                pass
        resp.extend(b': '.join(x) for x in stcpy.items())
        resp.extend((b'', b''))
        return b'\r\n'.join(resp)

    def doNotify(self, usn):
        """
            Do notification
        """
        if usn in self._known and not self._known[usn][b'SILENT']:
            self.info('Sending alive notification for %s', usn)
            resp = self.__build_response(b'ssdp:alive', usn)
            self.debug('doNotify content %s', str_cast(resp))
            try:
                # :fixme: why is this sent twice?
                self.transport.write(resp, (SSDP_ADDR, SSDP_PORT))
                self.transport.write(resp, (SSDP_ADDR, SSDP_PORT))
            except (AttributeError, socket.error) as msg:
                self.info("failure sending out alive notification: %r", msg)
        return

    def doByebye(self, usn):
        """
            Do byebye
        """
        # :todo: unite with doNotify(). Why are there differences at all?
        self.info('Sending byebye notification for %s', usn)
        resp = self.__build_response(b'ssdp:byebye', usn)
        self.debug('doByebye content %s', resp)
        if self.transport:
            try:
                self.transport.write(resp, (SSDP_ADDR, SSDP_PORT))
            except (AttributeError, socket.error) as msg:
                self.info("failure sending out byebye notification: %r", msg)
        return

    def _resendNotify(self):
        for usn, entry in self._known.items():
            if entry[b'MANIFESTATION'] == b'local':
                self.doNotify(usn)

    def _expire(self):
        """ check if the discovered devices are still ok, or
            if we haven't received a new discovery response
        """
        self.debug("Checking devices/services are still valid")
        removable = []
        for usn, entry in self._known.items():
            if entry[b'MANIFESTATION'] == b'local':
                continue
            expiry = int(entry[b'CACHE-CONTROL'].split(b'=')[1])
            now = time.time()
            last_seen = entry[b'last-seen']
            self.debug("Checking if %r is still valid - "
                       "last seen %d (+%d), now %d",
                       entry[b'USN'], last_seen, expiry, now)
            if last_seen + expiry + 30 < now:
                self.debug("Expiring: %r", entry)
                if entry[b'ST'] == b'upnp:rootdevice':
                    louie.send(b'Coherence.UPnP.SSDP.removed_device', None,
                               device_type=entry[b'ST'], infos=entry)
                removable.append(usn)
        for usn in removable:
            del self._known[usn]

    def subscribe(self, name, callback):
        self._callbacks.setdefault(name, []).append(callback)

    def unsubscribe(self, name, callback):
        callbacks = self._callbacks.get(name, [])
        if callback in callbacks:
            callbacks.remove(callback)
        self._callbacks[name] = callbacks

    def callback(self, name, *args):
        for callback in self._callbacks.get(name, []):
            callback(*args)
