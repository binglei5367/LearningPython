#!/usr/bin/env python

def sortList(list):
	list.sort()
	return list
		
def run():
	list = []
	
	while True:
		input = raw_input('Enter an integer: ')
		if input:
			try:
				integer = int(input)
			except(ValueError):
				print 'invalid input'
				continue
			list.append(integer)
		else:
			break
	
	return sortList(list)
	
if __name__ == '__main__':
	run()