#!/usr/bin/env python

def leapyear(year):
	'''Judge wether it is a leap year or not'''
	
	if (year % 4 == 0) and (year % 100 != 0):
		return True
	elif (year % 4 == 0) and (year % 400 == 0):
		return True

		
def run():
	year = int(raw_input('Enter the year:\n'))
	if leapyear(year):
		print 'It is a leap year'
	else:
		print 'It is not a leap year'
		
if __name__ == '__main__':
	run()