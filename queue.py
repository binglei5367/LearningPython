#!/usr/bin/env python

queue = []

def enQ():
	queue.append(raw_input('Enter new string: ').strip())
	
def deQ():
	if len(queue) == 0:
		print 'But the queue is empty'
	else:
		print "Remove '%s' from queue" % queue.pop(0)
	
def view():
	print 'queue: ', queue

cmd = {'e': enQ, 'd': deQ, 'v': view, 'q': quit}



def menu():
	menu = '''------
(e): enter item 
(d): delet item
(v): view queue
(q): quit 

choice: '''
	while True:
		while True:
			try:
				choice = raw_input(menu).strip()[0].lower()
			except (EOFError, KeyboardInterrupt, IndexError):
				choice == 'q'
			
			if choice in 'edvq':
				break
			else:
				print 'Invild option, please choose again'
				
		if choice == 'q':
			break
		else:
			cmd[choice]()

if __name__ == '__main__':
	menu()