#!/usr/bin/env python

# transfort an integer to an IP adress

def trans(int):
	
	octs = oct(int)[1:]
	while len(octs) % 3 != 0:
		octs = '0' + octs
		
	part = ''
	ip = []
	for e in octs:
		part = part + e
		if len(part) == 3:
			ip.append(part)
			part = ''
	
	IP = '.'.join(ip)
		return IP
		
def test():
	input = raw_input('enter an integer: ')
	try:
		num = int(input)
		print('IP Adress:\n'), trans(num)
	except(ValueError):
		print('Invalid input, please try again')
		test()
		
if __name__ == '__main__':
	test()