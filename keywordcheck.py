#!/usr/bin/env python

import keyword

def keywordCheck(string):
	return keyword.iskeyword(string)
	
def run():
	string = raw_input('Enter a strint: ')
	if keywordCheck(string):
		print "'%s' is a keyword" % string
	else:	
		print "'%s' is not a keyword" % string
		
if __name__ == '__main__':
	run()