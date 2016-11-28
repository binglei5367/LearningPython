#!/usr/bin/env python

from os import path, linesep

def make():
	while True:
		filename = raw_input('Enter filename: \n')
		if path.exists(filename):
			print 'Error: "%s" already exists' % filename
		else:
			break
		
	content = []
	print 'Enter lines (".end." to quit).\n'

	while True:
		enter = raw_input('-')
		if enter == '.end.':
			break
		else:
			content.append(enter)
		
	file = open(filename, 'w')
	file.writelines(['%s%s' % (x, linesep) for x in content])
	file.close()
	print '--Done--'

def read():
	while True:
		filename = raw_input('Enter the filename: ')
		if path.exists(filename):
			break
		else:
			print '"%s" dose not exist' % filename
			
	try:
		file = open(filename, 'r')
	except IOError, e:
		print "** file open error:", e
	else:
		lines = file.readlines()
		print '-' * 6
		for line in lines:
			print line.strip('\n')
		print '-' * 6
		file.close()
		
		
def run():
	print 'To make or to read a text file?'
	choose = raw_input('1.make	2.read\nelse: end\n>')
	if choose == '1':
		make()
	elif choose == '2':
		read()
		
if __name__ == '__main__':
	run()