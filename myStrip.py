#!/usr/bin/env python

def myStrip(str):
	'''
	Return a copy of the string with leading and trailing whitespace removed
	'''
	
	i, j = 0, -1
	while str[i] == ' ':
		i += 1		
	while str[j] == ' ':
		j -= 1
		
	return str[i: j+1]
	
def test():
	input = raw_input('Enter something: ')
	print myStrip(input)
	
if __name__ == '__main__':
	test()