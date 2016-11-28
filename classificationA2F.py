#!/usr/bin/env python

def classificate(grade):
	'''classification according to grade'''
	
	if 90 <= grade <= 100:
		return 'A'
	elif 80 <= grade <= 89:
		return 'B'
	elif 70 <= grade <= 79:
		return 'C'
	elif 60 <= grade <= 69:
		return 'D'
	elif 0 <= grade <= 60:
		return 'F'
	else:
		return 'error'
		
def run():
	grade = int(raw_input('enter the grade:\n'))
	print 'that is', classificate(grade)
	
if __name__ == '__main__':
	run()