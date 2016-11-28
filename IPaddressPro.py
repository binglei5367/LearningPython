#!/usr/bin/env python

def checkIP(str):
	'''check if it's a IP address string'''
	
	check = False
	address = str
	parts = address.split('.')
	if len(parts) == 4:
		for part in parts:
			try:
				num = int(part)
				if num not in range(0, 256):
					return False
			except(ValueError):
				return False
		check = True
	
	return check
			
def checkNum(str):
	'''check if it's an integer below 2^32 '''
	
	check = False
	try:
		number = int(str)
		str_bin = binary(str)
		if len(str_bin) in range(0, 33):
			check = True
	except(ValueError):
		return False
		
	return check
	
def binary(str_num):
	'''convert a number string to a binary number string'''
	
	int_num = int(str_num)
	str_bin = ''
	while True:
		if int_num == 0:
			break
		p = str(int_num % 2)
		str_bin = p + str_bin
		int_num = int_num / 2
		
	return str_bin
	
def IP(str_num):
	'''convert a number string to a  IP address string'''
	
	str_bin = binary(str_num)
	while len(str_bin) < 32:
		str_bin = '0' + str_bin
	
	parts = []
	part = ''
	for e in str_bin:
		part = part + e
		if len(part) == 8:
			parts.append(part)
			part = ''
	
	paras =[]
	for p in parts:
		para = int(p, 2)
		para = str(para)
		paras.append(para)
		
	str_ip = '.'.join(paras)
	
	return str_ip
	
def Number(str_ip):
	'''convert a IP address string to a number string'''
	
	parts = str_ip.split('.')
	paras = []
	for e in parts:
		p = binary(e)
		while len(p) < 8:
			p = '0' + p
		paras.append(p)
	
	str_bin = ''.join(paras)
	int_num = int(str_bin, 2)
	str_num = str(int_num)

	return str_num
	
def test():
	input = raw_input('Enter an integer or an IP Address:\n ')
	if checkIP(input):
		output = Number(input)
		print 'Number:\n ', output
	elif checkNum(input):
		output = IP(input)
		print 'IP address:\n ', output
	else:
		print 'Invalid input\n'
		
if __name__ == '__main__':
	test()