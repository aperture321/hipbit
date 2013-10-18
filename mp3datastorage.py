#store file attributes component

import sqlite3 as sql

import mp3metadata

#TODO don't drop tables all the time
#Allow database recognition and resetting the database

class SQLmgr:

	def __init__(self, username): #note everytime function is called MusicData table is dropped!
		self.serv = False
		self.servcount=1
		db = username + ".db"
		self.db = db
		try:
			serv = sql.connect(db)
			with serv:
				self.serv = serv.cursor()
				self.serv.execute("DROP TABLE IF EXISTS MusicData")
				self.serv.execute("CREATE TABLE MusicData(Id INT, ALBUM TEXT, ARTIST TEXT, TITLE TEXT)")
				self.serv.close()
		except sql.Error, e:
			print "Error executing SQL table. ", e.args[0]

	def add_db(self, case):
		try:	
			with sql.connect(self.db) as serv:
				self.serv = serv.cursor()
				self.serv.execute("INSERT INTO MusicData VALUES (?, ?, ?, ?);", case)
				self.servcount += 1
				self.serv.close()
		except sql.Error, e:
			print "An error occurred inserting data."
			print e.args[0]

	def add_test(self):
		try:
			tester = mp3metadata.mp3data().returnobj()
			case = []
			case.append(self.servcount)
			#tuple pairings will proceed in this order.
			for k,v in tester.items():
				if k in ["ALBUM", "ARTIST", "TITLE"]:
					case.append(v)		
			self.add_db(tuple(case))
			return 0
		except sql.Error, e:
			print e.args[0]
			return 1

