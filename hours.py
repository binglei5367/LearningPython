#!/usr/bin/env python

def hours(minutes):
	'''return a tuple of hours and minutes'''
	
	hour = minutes / 60
	minute = minutes % 60
	
	return (hour, minute)

def showout(tuple):
	return '%dh%dmins' % tuple
	
def input():
	inputstuff = raw_input('Enter minutes: ')
	try:
		minutes = int(inputstuff)
	except(ValueError):
		return 0
		
	return minutes
	
def run():
	minute = input()
	hour = hours(minute)
	print showout(hour)
	
if __name__ == '__main__':
	run()