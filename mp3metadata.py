#Mp3 metadata testing...

from ID3 import *

#TODO add further directory search methods

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
