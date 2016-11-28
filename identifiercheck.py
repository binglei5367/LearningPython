#!/usr/bin/env python

import string

def check(input):

	"""check if suitable as an identifier"""
	
	alphas = string.letters + '_'
	nums = string.digits
	
	if input[0] in alphas:
		for e in input[1:]:
			if e in string.letters + nums:
				return True
	else:
		return False
		

def result(check):
	
	"""return the result as a string"""
	
	if check:
		return 'okay as an indentifier'
	else:
		return 'cannot be an identifier'
		

def show(input):
	
	"""show the result"""
	
	print '-result:'
	print result(check(input))
	print '-done'
	
def run():
	
	"""keep running"""
	
	print '-check begin'
	while True:
		input = raw_input('-enter the identifier you wanna check: ')
		if not input:
			break
		show(input)
		
		
if __name__ == '__main__':
	run()