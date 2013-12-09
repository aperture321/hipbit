#!/usr/bin/env python
#tcp tester

import socket
import sys
import os
import time

TCP_IP = '74.5.183.40'
TCP_PORT = 1221
BUFFER_SIZE = 1024
try:
  limit = os.path.getsize("test.db") #4096 bytes
  currentamt = 0

  f = open("test.db", "rb")
  l = f.read(BUFFER_SIZE)
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((TCP_IP, TCP_PORT))
  s.send(str(limit) + "**") #first, send the limit with termination character
  while(1):
    s.send(l)
    if currentamt >= limit:
      break
    l = f.read(BUFFER_SIZE)
    currentamt += BUFFER_SIZE
    print "still sending.."

  s.close()

  print "Done."
  time.sleep(3)
except:
  print "Unexpected error:", sys.exc_info()[0]
  time.sleep(3)
