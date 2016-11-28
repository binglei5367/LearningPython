#!/usr/bin/env python

codec = 'utf-8'
filename = 'unicode.txt'

hello_out = u'Hello World!\n'
bytes_out = hello_out.encode(codec)
file = open(filename, 'w')
file.write(bytes_out)
file.close()

file = open(filename, 'r')
bytes_in = file.read()
file.close()
hello_in = bytes_in.decode(codec)

print hello_in