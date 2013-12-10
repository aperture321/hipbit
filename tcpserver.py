#!/usr/bin/env python

import socket
import sys
import os

TCP_IP = ''
TCP_PORT = 1221
BUFFER_SIZE = 1024
currentamt = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  s.bind((TCP_IP, TCP_PORT))
  s.listen(1)

  while True:
    conn, addr = s.accept()
    print "Connection address: ", addr
    while 1:
      limit = conn.recv(30) #this will get your limit size
      other = limit[limit.find("&&")+2:] #save extra packet stuff
      fname = limit[limit.find("**")+2:limit.find("&&")]
      limit = limit[:limit.find("**")] #get byte amount
      limit = int(limit)
      filepath = "htmlfiles/" + fname
      f = open(filepath, 'wb')
      f.write(other)
      print limit
      l = conn.recv(BUFFER_SIZE) #get byte bufferred back
      while (1):
        if currentamt > limit:
          f.write(l)
          break
        f.write(l)
        l = conn.recv(BUFFER_SIZE)
        currentamt += BUFFER_SIZE
      currentamt = 1024 #reassign values
      limit = ''
      break
    f.close() #close your file after you're done
    conn.close()

  s.close()
except:
  print "ending"
  s.close()
  sys.exit()
