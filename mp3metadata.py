#Mp3 metadata testing...

from ID3 import *

#TODO add further directory search methods
import os

class mp3data:
	def trial(self):
		try:
			filename = 'testfolder/furelise.mp3'
			id3info = ID3(filename)  
			for i in id3info.items():
				continue#print i
			return 0 #indicates a pass!
		except:
			return 1
	def returnobj(self):
		filename = 'testfolder/furelise.mp3'
		id3info = ID3(filename)
		return id3info

	def mp3search(self, dir_path):
		try:
			for root, dirs, files in os.walk(dir_path):
				for file in files:
					if file.endswith(".mp3"):
						print os.path.join(root, file)
			return 0
		except:
			return 1
