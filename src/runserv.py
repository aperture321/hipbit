import os
import tcpsend


def searchparams(filesfound):
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".db") and file not in filesfound:
                filesfound.append(file)
                filepre = file[:file.find(".db")]
                filepre += ".html"
                os.system("sqlite3 -html %s 'select * from MusicData;' > %s" %
                          (file, filepre))  # will conver to .html
                tcpsend.send(filepre)  # send in the entire html
    return 0

filesfound = []
while 1:
    searchparams(filesfound)
