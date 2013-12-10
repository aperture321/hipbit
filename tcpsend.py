#!/usr/bin/env python
#tcp tester

import socket
import sys
import os
import time

def send(filetosend):
  TCP_IP = '74.5.183.40'
  TCP_PORT = 1221
  BUFFER_SIZE = 1024
  try:
    limit = os.path.getsize(filetosend) #will get bytesize
    currentamt = 0
    f = open(filetosend, "rb")
    l = f.read(BUFFER_SIZE)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(str(limit) + "**" + filetosend + "&&") #first, send the limit with termination character, then filename and another termination character.
    while(1):
      s.send(l)
      if currentamt > limit:
        print currentamt
        break
      l = f.read(BUFFER_SIZE)
      currentamt += BUFFER_SIZE
      print "still sending.."
    print "Done."
    time.sleep(3)
    s.close()
  except:
    print "Unexpected error:", sys.exc_info()[0]
    time.sleep(3)
    s.close()
