#python example unit testing!

from mp3metadata import *
from mp3datastorage import *

def tester(test):
	if test is 0:
		return "pass"
	else:
		return "fail"


#tests for basic file ID3 Info
def ID3test():
	test = mp3data().trial()
	return tester(test)

#tests for adding ID3 into database
def AddDBtest():
	test = SQLmgr('test').add_test()
	return tester(test)

#tests for recursive directory searching
def mp3search(dirs):
	test = mp3data().mp3search(dirs)
	return tester(test)
