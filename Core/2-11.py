stick = True

while stick:
	choose = raw_input('1: get the summary of five numbers\n2: get the average of five numbers\nX: quit the script\n')
	if choose == '1':
		sum = 0
		print 'Enter five integers:'
		for i in range(5):
			sum += int(raw_input())
		print 'summary =', sum
		print
	elif choose == '2':
		sum = 0
		print 'Enter five integers:'
		for i in range(5):
			sum += int(raw_input())
		print 'average =', float(sum) / 5
		print
	elif choose == 'x' or choose == 'X':
		print 'goodbye'
		print
		stick = False