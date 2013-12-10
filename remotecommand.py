import os

os.system("sqlite3 -html rec.db 'select * from MusicData;' > rec2.html")
print "success"
