#!/usr/bin/env python

def reverse(str):
	lens = len(str)
	str2 = ''
	for i in range(1, lens + 1):
		str2 += str[0 - i]
	return str2

def palindrome(string):
	'''Check a string if it is a palindrome'''
	
	if string == reverse(string):
		return True
		
def makepalindrome(string):
	'''Create a palindrome'''
	
	return string + reverse(string)

def test():
	input = raw_input('Enter a string: ')
	
	if palindrome(input):
		print 'It is a palindrome'
	else:
		print 'It is not'
	
	print 'And make a palindrome: %s' % makepalindrome(input)
		
if __name__ == '__main__':
	test()