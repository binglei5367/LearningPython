#!/usr/bin/env python

def exchange(sentence):
	
	lens = len(sentence)
	
	up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	low = up.lower()
	sentence2 = ''
		
	for i in range(0, lens):
		word = sentence[i]
		if word in up:
			word = word.lower()
		elif word in low:
			word = word.upper()
		sentence2 += word
			
	return sentence2
	
def test():
	input = raw_input('Enter a sentence:\n')
	print 'Changed:\n', exchange(input)
	
if __name__ == '__main__':
	test()