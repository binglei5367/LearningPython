#!/usr/bin/env python


def compare(a, b, c):
	'''Get three numbers and return a list from smaller to bigger of them'''
	
	while not (a < b < c):
		if a > b:
			a, b = b, a
			# a = a + b
			# b = a - b
			# a = a - b
		if b > c:
			b, c = c, b
			# b = b + c
			# c = b - c
			# b = b - c
	
	return [a, b, c]

def run():
	'''Run this script'''
	
	print 'Enter three integers: '

	a = int(raw_input())
	b = int(raw_input())
	c = int(raw_input())
	
	print '-' * 6
	print 'From lower to higher:'
	for e in compare(a, b, c):
		print e,
	print
		
	print 'From highter to lower:'
	for e in range(3):
		print compare(a, b, c)[2 - e],
		
if __name__ == '__main__':
	run()