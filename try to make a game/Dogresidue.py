Gold = 0
CENT = ['Dog residue']


def C1():
	print 'CENT: %r' % CENT
	C2()

def C2():
	input2 = raw_input('Dog residue > use, info, sell> ')
	if input2 == 'use':
		use()
	elif input2 == 'info':
		info()
	elif input2 == 'sell':
		sell()
	else:
		C2()
		
def use():
	if len(CENT) == 0:
		print "You used yourself, your soul was gone."
		exit(0)
	else:
		while len(CENT) < 8:
			CENT.append('Dog residue')
	
	C1()

def info():
	if len(CENT) == 0:
		print "You called for infomation, but only to get an 'idiot'."
		C1()
	else:
		print "It's dog residue."
		C2()

def sell():
	if len(CENT) == 0:
		print "You sold yourself."
		exit(0)
	else:
		CENT.pop()
		print "Your sold Dog residue. You got 5G."
		global Gold
		Gold = Gold + 5
		print "Gold: %dG" % Gold
		C1()

C1()