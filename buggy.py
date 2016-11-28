#!/usr/bin/env python

# get the input from user
num_str = raw_input('Enter a number: ')

# change the input into integer type
num_num = int(num_str)

# create a list of the numbers from 1 to the number you enter
fac_list = range(1, num_num+1)
print 'BEFORE:', fac_list

# initiate i
i = 0

# delet the factors of the number
while i < len(fac_list):
	
	# check if it's a factor
	if num_num % fac_list[i] == 0:
		# if so, delet it and don't change i for the list have been shorter
		del fac_list[i]
		continue
	
	# change i
	i = i + 1

# print out the outcome	
print 'AFTER:', fac_list