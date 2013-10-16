#python example program!
from mp3metadata import *
from mp3datastorage import *

def tester(test):
	if test is 0:
		return "pass"
	else:
		return "fail"

def testsuite():
	#mp3 data tester
	test = mp3data().trial()
	print "MP3Metadata Test: " + tester(test)
	if tester(test) is 'pass':
		test = SQLmgr('test').add_test()
		print "MP3 Data Storage Test: " + tester(test)

