#!/usr/bin/env python

English = {
1: 'one',
2: 'two',
3: 'three',
4: 'four',
5: 'five',
6: 'six',
7: 'seven',
8: 'eight',
9: 'nine',
0: 'zero'
}
English2 = {
10: 'ten',
11: 'eleven',
12: 'twelve',
13: 'thriteen',
14: 'forteen',
15: 'fifteen',
16: 'sixteen',
17: 'seventeen',
18: 'eighteen',
19: 'ninteen',
}
English3 = {
2: 'twenty',
3: 'thirty',
4: 'forty',
5: 'fifty',
6: 'sixty',
7: 'seventy',
8: 'eighty',
9: 'ninty'
}

def reEnglish(num):
	
	if num == 1000:
		return 'one-thousand'
	if num == 0:
		return 'zero'
	
	n3 = num / 100
	n2 = num % 100 / 10
	n1 = num % 10
	
	e1, e2, e3 = '', '', ''
	
	if n3:
		e3 = English[n3] + '-hundred-'
	if n2:
		if n2 < 2:
			e2 = English2[num % 100]
		else:
			e2 = English3[n2] + '-'
			if n1:
				e1 = English[n1]
	else:
		if n1:
			e1 = 'and-' + English[n1]
		
	return e3 + e2 + e1
	
def run():
	input = raw_input('Enter a number(0 - 1000): ')
	try:
		num = int(input)
		if num in range(0, 1001):
			print 'That is:', reEnglish(num)
		else:
			print 'Invild number, please try again'
	except (ValueError):
		print 'Invild input, please try again'
		run()
		
if __name__ == '__main__':
	run()