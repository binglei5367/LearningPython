#!/usr/bin/env python

def displayNumType(num):
	'''As the name says, it will display the type of a number'''
	
	print num, 'is',
	if isinstance(num, (int, long, float, complex)):
		print 'a number of type', type(num).__name__
	else:
		print 'not a number'
		
def testrun():
	displayNumType(520)
	displayNumType(-521)
	displayNumType(31.54)
	displayNumType(-3.1+5.4j)
	displayNumType('ooxx')
	
if __name__ == '__main__':
	testrun()