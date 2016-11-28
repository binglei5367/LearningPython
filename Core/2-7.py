string = raw_input('enter something: ')

x = 1
while x <= len(string):
	print string[x - 1]
	x += 1
	
string = raw_input('enter something else: ')
for word in string:
	print word