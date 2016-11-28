list = []
sum = 0
sum2 = 0
while len(list) < 5:
	e = int(raw_input('enter something to add to the list: '))
	list.append(e)
	sum += e
print list
print sum

for e in list:
	sum2 += e
print sum2