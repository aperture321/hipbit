import os
import tcptest as tcpsend

def searchparams(filesfound):
    for root, dirs, files in os.walk("/home/aperture/hipbit"):
      for file in files:
        if file.endswith(".db") and file not in filesfound:
          filesfound.append(file)
          filepre = file[:file.find(".db")]
          filepre += ".html"
          os.system("sqlite3 -html %s 'select * from MusicData;' > %s" % (file, filepre))
          tcpsend.send(filepre)
    return 0

filesfound = []
while 1:
  searchparams(filesfound)
  
