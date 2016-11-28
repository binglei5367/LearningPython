#!/usr/bin/env python

'readTextFile.py -- read and display text file'

from os import path

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