stick = True
while stick:
	num = int(raw_input('Enter an integer: '))
	if 0 < num < 100:
		print 'Yes, it is.'
		stick = False
	else:
		print 'Not really'