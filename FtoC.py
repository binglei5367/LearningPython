#!/usr/bin/env python

def divertFtoC(F):
	'''divert Fahrenheit to Celsius'''
	
	try:
		F = float(F)
		C = (F - 32) * (5.0 / 9.0)
		return C
	except ValueError,e:
		print 'Error:', e
	
def run():
	input = True
	while input:
		input = raw_input('Enter Fahrenheit: ')
		if input:
			print divertFtoC(input)
			
if __name__ == '__main__':
	run()