#!/usr/bin/env python

import os


def search(x):
	
	file_list = [f for f in os.dirlist('.') if os.path.isfile(f)]
	
	
	
def user_input():

	i = raw_input('Enter key words:\n')
	return i
	
	
def output():
	pass
	
def main():
	
	name = os.name
	abspath = os.path.abspath
	path = os.path.join(abspath, '')
	print 'OS: %s' % name 
	print 'PATH: %s' % path
	
	usrinput = user_input()
	
