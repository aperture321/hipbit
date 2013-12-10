#store file attributes component

import sqlite3 as sql
import os
import mp3metadata

#TODO add directory of the database
#Allow database recognition and resetting the database

class SQLmgr:

	def __init__(self, username): #note everytime function is called MusicData table is dropped!
		self.serv = False
		self.errors = open("error.txt", "w")
		self.servcount=1
		db = username + ".db"
		self.db = db
		if self.db in os.listdir("."): #database already exists
			pass
		else:
			try:
				serv = sql.connect(db)
				with serv:
					self.serv = serv.cursor()
					self.serv.execute("DROP TABLE IF EXISTS MusicData")
					self.serv.execute("CREATE TABLE MusicData(Id INT, ALBUM TEXT, ARTIST TEXT, TITLE TEXT, PATH 	TEXT)")
					self.serv.close()
			except sql.Error, e:
				print "Error executing SQL table. ", e.args[0]
				return 1

	def wipe_database(self, username):
		self.db = username + ".db"
		try:
			os.remove(self.db)
		except sql.Error, e:
			print "Error wiping database."
			return 1				


	def add_db(self, case):
		try:	
			with sql.connect(self.db) as serv:
				self.serv = serv.cursor()
				self.serv.execute("INSERT INTO MusicData VALUES (?, ?, ?, ?, ?);", case)
				self.servcount += 1
				self.serv.close()
		except sql.Error, e:
			self.errors.write(str(case[-1]) + "\n")

	def addmp3todb(self, filetup):
		try:
			case = []
			case.append(self.servcount)
			for h,j in filetup[1].items():
				if h in ["ALBUM", "ARTIST", "TITLE"]:
					case.append(j)
			stringtype = filetup[0]
			specialcase = stringtype[stringtype.find("aperture/")+9:]
			specialcase = specialcase.replace(" ","%20")
			specialcase = "ftp://74.5.183.40/" + specialcase
			case.append(specialcase) #should've been the filetup[0], but time constraints changed this.
			
			self.add_db(tuple(case))
		except:
			self.errors.write("Error writing: " + filetup[1] + "\n")
			

	def add_test(self, filedir):
		try:
			tester = mp3metadata.mp3data().returnobj()
			case = []
			case.append(self.servcount)
			#tuple pairings will proceed in this order.
			for k,v in tester.items():
				if k in ["ALBUM", "ARTIST", "TITLE"]:
					case.append(v)		
			case.append(filedir) #this is how it should be.
			self.add_db(tuple(case))
			return 0
		except sql.Error, e:
			print e.args[0]
			return 1

