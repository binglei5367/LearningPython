#!/usr/bin/env python

while True:
	num = int(raw_input('Enter a number: '))

	if num > 0:
		print num, '> 0'
	elif num == 0:
		print num, '= 0'
	else:
		print num, '< 0'