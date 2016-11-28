#!/usr/bin/env python

def check(a, b):
	'''check if a is part of b'''
	
	a = a.lower()
	b = b.lower()
	
	return (a in b)
	
def test():
	a = raw_input('Enter a strint: ')
	b = raw_input('Enter another string: ')
	if check(a, b):
		print "'%s' is part of '%s'" % (a, b)
	else:
		print "'%s' is not part of '%s'"
		
if __name__ == '__main__':
	test()