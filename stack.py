#!/usr/bin/env python

stack = []

def push():
	stack.append(raw_input('Enter new string: ').strip())

def pop():
	if len(stack) == 0:
		print 'But stack is empty'
	else:
		print "Remove string '%s' from stack" % stack.pop()

def view():
	print 'stack: ',stack


cmd = {'u': push, 'o':pop, 'v': view, 'q': quit}

def menu():
	menu = '''------
p(u)sh
p(o)p
(v)iew
(q)uit

choice:'''

	while True:
		while True:
			try:
				choice = raw_input(menu).strip()[0].lower()
			except (EOFError, KeyboardInterrupt, IndexError):
				choice = 'q'
				
			if choice in 'uovq':
				break
			else:
				print 'Invalid choice, please choose again'
			
		if choice == 'q':
			break
		
		cmd[choice]()

if __name__ == '__main__':
	menu()