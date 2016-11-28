#!/usr/bin/env python

def calculate(exp):
	'''calculate the result of a string expression'''
	
	operate = ['+', '-', '*', '/', '%', '**']
	for o in operate:
		trans = exp.split(o)
		if len(trans) == 2:
			N1 = float(trans[0])
			N2 = float(trans[1])
			oper = o
			if o == '+':
				return N1 + N2
			elif o == '-':
				return N1 - N2
			elif o == '*':
				return N1 * N2
			elif o == '/':
				return N1 / N2
			elif o == '%':
				return N1 % N2
			elif o == '**':
				return N1 ** N2
				
def run():
	exp = True
	while exp:
		exp = raw_input('enter expression to calculate:\n')
		print '=', calculate(exp)

if __name__ == '__main__':
	run()