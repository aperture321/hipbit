#store file attributes component

import sqlite3 as sql

import mp3metadata

class SQLmgr:

	def __init__(self, username):
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
				self.serv.close()
		except sql.Error, e:
			print "An error occurred inserting data."
			print e.args[0]

	def add_test(self):
		try:
			tester = mp3metadata.mp3data().returnobj()
			case = []
			case.append(1) #testing purpose counter
			for k,v in tester.items():
				if k in ["ALBUM", "ARTIST", "TITLE"]:
					case.append(v)		
			self.add_db(tuple(case))
			return 0
		except sql.Error, e:
			print e.args[0]
			return 1

