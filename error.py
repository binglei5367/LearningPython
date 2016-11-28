#!/urs/bin/env python

def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		input = raw_input('Enter anything to raise an error:\n')
		bar(input)
	except ValueError, e:
		raise ValueError('Input error')
		#print 'ValueError:', e
	except ZeroDivisionError, e:
		print 'ZeroDivisionError:', e
	finally:
		print 'End'
		
if __name__ == '__main__':
	main()