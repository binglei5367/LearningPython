#!/usr/bin/env python

def hcf(int1, int2):
	'''calculate the highest common factor of two integers'''
	
	for i in range(1, min(int1, int2) + 1):
		if min(int1, int2) % i == 0:
			if max(int1, int2) % i == 0:
				hcf = i
			
	return hcf

def lcm(int1, int2):
	'''calculate the least common multiple of two intergers'''
	
	for i in range(1, min(int1, int2) + 1):
		if (max(int1, int2) * (min(int1, int2) + 1 - i)) % min(int1, int2) == 0:
			lcm = (max(int1, int2) * (min(int1, int2) + 1 - i))
	
	return lcm
	
def run():
	int1 = int(raw_input('Enter the first integer: '))
	int2 = int(raw_input('Enter the second integer: '))
	print 'the highest common factor of %d and %d is %d' % (int1, int2, hcf(int1, int2))
	print 'the least common multiple of %d and %d is %d' % (int1, int2, lcm(int1, int2))

if __name__ == '__main__':
	run()