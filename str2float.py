from functools import reduce
	
def str2float(s):
	def char2num(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
	def fn(x, y):
		return x * 10 + y
	
	if s.find('.') == -1:
		return reduce(fn,(map(char2num, s)))
	else:
		L = list(s)
		i = 0
		while L[i] !='.':
			i = i + 1
		num1 = reduce(fn, map(char2num,s[:i]))
		num2 = reduce(fn, map(char2num,s[i + 1:])) / (10 ** (len(s) - i - 1))
		return num1 + num2