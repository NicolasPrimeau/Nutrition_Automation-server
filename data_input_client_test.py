#!/usr/bin/env python

import socket
import sys
import json

PORT = 50001

if len(sys.argv) == 3:
  PORT = sys.argv.pop()

if len(sys.argv) == 2:
  HOST = sys.argv.pop()
else:
  sys.stdout.write("Need to specify a host IP\n")
  sys.exit()

ADDR = (HOST,PORT)

BUFFER_SIZE = 1024

f = {}
f['bin'] = 1
f['quantity'] = 20

message = json.dumps(f)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)
s.send(message)
s.close()


