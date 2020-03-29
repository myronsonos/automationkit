#!/usr/bin/env python

# Licensed under the MIT license
# http://opensource.org/licenses/mit-license.php

# Copyright 2006,2007 Frank Scholz <coherence@beebits.net>

import getopt
import sys
import string

from xmlrpc.client import Server

command = "status"
device = ''
volume = 50
uri = ''
id = 1000

arguments = {}

try:
    optlist, args = getopt.getopt(sys.argv[1:], "c:d:i:v:u:", ['command=', 'device=', 'id=', 'volume=', 'uri='])
except getopt.GetoptError:
    print("falsche parameter")
    sys.exit(1)

for option, param in optlist:
    if option in('-c', '--command'):
        command = param
    if option in('-d', '--device'):
        device = param
    if option in('-i', '--id'):
        id = param
    if option in('-v', '--volume'):
        volume = param
    if option in('-u', '--uri'):
        uri = param

skip = False
for p in sys.argv[1:]:
    if skip:
        skip = False
        continue
    if p.startswith('-'):
        skip = True
        continue
    k, v = p.split('=')
    arguments[k] = v
#print(('Arguments', arguments))

with Server("http://127.0.0.1:30020/RPC2") as sproxy:

    if command == "ping":
        r = sproxy.ping()

    if command == "list_devices":
        r = sproxy.list_devices()

    if command == "mute" and device != '':
        r = sproxy.mute_device(device)

    if command == "unmute" and device != '':
        r = sproxy.unmute_device(device)

    if command == "set_volume" and device != '':
        r = sproxy.set_volume(device, volume)

    if command == "play" and device != '':
        r = sproxy.play(device)

    if command == "pause" and device != '':
        r = sproxy.pause(device)

    if command == "stop" and device != '':
        r = sproxy.stop(device)

    if command == "next" and device != '':
        r = sproxy.next(device)

    if command == "previous" and device != '':
        r = sproxy.previous(device)

    if command == "set_av_transport_uri" and device != '' and uri != '':
        r = sproxy.set_av_transport_uri(device, uri)

    if command == "shutdown":
        r = sproxy.shutdown()

    if command == "create_object" and device != '':
        r = sproxy.create_object(device, id, arguments)

    if command == "import_resource" and device != '':
        r = sproxy.import_resource(device, arguments['source_uri'], arguments['destination_uri'])

    if command == "put_resource":
        r = sproxy.put_resource(arguments['url'], arguments['path'])

print(r)
