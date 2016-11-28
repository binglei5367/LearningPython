#!/usr/bin/env python
str = raw_input('enter something\n')
print (str)
try:
	int = int(raw_input('enter something else\n'))
	print (int)
except ValueError:
	print 'value error'
	