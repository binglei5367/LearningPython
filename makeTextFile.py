#!/usr/bin/env python

'makeTextFile.py -- create text file'

from os import linesep, path

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
print '-Done-'