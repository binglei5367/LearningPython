#!/usr/bin/env python

# transfort an integer to an IP adress

def check(address):
	'''check if it is a IP Adress format'''
	
	parts = address.split('.')
	if len(parts) == 4:
		for part in parts:
			try:
				num = int(part)
				if num not in range(0, 256):
					return False
			except(ValueError):
				return False
		return True
	else:
		return False
	

def bin(int):
	'''convert integer to a binary string'''
	
	bin = ''
	while True:
		if int == 0:
			break
		p = str(int % 2)
		bin = bin + p
		int = int / 2
	return bin

def IP(str_num):
	'''format a binary string number to a IP Adress form'''
	
	if len(str_num) > 32:
		return 'Integer out of range'
	
	while len(str_num) < 32:
		str_num = '0' + str_num
		
	ip = []
	part = ''
	for e in str_num:
		part = part + e
		if len(part) == 8:
			dec = int(part, 2)
			ip.append(str(dec))
			part = ''
	
	return '.'.join(ip)
	
def Num(str_IP):
	'''covert an IP to an integer'''
	
	parts = str_IP.split('.')
	bin_num = ''
	for part in parts:
		p = bin(int(part))
		while len(p) < 8:
			p = '0' + p
		bin_num = bin_num + p
	if len(bin_num) == 32:
		num = int(bin_num, 2)
	else:
		return '???'
	
	return num
	
def test():
	input = raw_input('enter an integer or an IP address: ')
	if check(input):
		print('Number:\n'), Num(input)
	else:
		try:
			num = int(input)
			binary = bin(num)
			print('IP Adress:\n'), IP(binary)
		except(ValueError):
			print('Invalid input')
		
if __name__ == '__main__':
	test()