#!/usr/bin/env python
#Filename: decorator.py

	
def log(func):
	def wrapper(*args, **kw):
		print 'call %s()' % func.__name__
		return func(*args, **kw)
	return wrapper
	
@log
def now():
	print 'Jun-13-2016'