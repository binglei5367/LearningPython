from sys import exit
from random import randint

GOLD = 0
CENT = ['Dogresidue']
hp = 10


class Engine(object):
	
	# initial the object
	def __init__(self,scene_map):
		self.scene_map = scene_map
	
	# current_scene will get the scenes name pointing to a scene object	
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		# method will keep going. Every enter() will provide the key to the next
		while True:
			print "----------"
			
			if current_scene.enter() == '':
				print "You fell into Ruins by accident."
				next_scene_name = 'ruins'
			else:
				next_scene_name = current_scene.enter()
			# call the enter method to start the content of the scene
			# method enter() will return the name of the next scene
			
			current_scene = self.scene_map.next_scene(next_scene_name) 
			# now current scene will be the next
			


		

class Scene(object):
	
	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)
	
	def act(self):
		global action
		action = raw_input("\n1.Explore\n2.Move\n>>>")
		
class Determination(Scene):
	
	def enter(self):
		print "Making this stupid game made you filled with determination..",
		raw_input()
		exit(1)

class Ruins(Scene):
	
	def enter(self):
		raw_input()
		print "This is the ruins.",
		raw_input()
		print "Full of rabbish.",
		raw_input()
		self.act()
		
		if action == '1' or action == '':
			print "\n..but nobody came..",
			raw_input()
			return 'ruins'
		
		elif action == '2':
			print "Go on.."
			move = raw_input("1.next\n>>>")
			
			if move == '1' or move == '':
				return 'snowdin'
			else:
				return 'ruins'
		
		else:
			return 'ruins'

class Snowdin(Scene):
	
	def enter(self):
		raw_input()
		print "Welcome to Snowdin..!",
		raw_input()
		print "Full of.. Snowballs!..",
		raw_input()
		self.act()
		
		if action == '1' or action == '':
			print "..but nobody came..",
			raw_input()
			return 'snowdin'
		
		elif action == '2':
			move = raw_input("1.next\n2.last\n>>>")
			if move == '1' or move == '':
				return 'waterfall'
			elif move == '2':
				return 'ruins'
			else:
				return 'snowdin'
		
		else:
			return 'snowdin'
		

class Waterfall(Scene):
	
	def enter(self):
		raw_input()
		print "Fall into Waterfall",
		raw_input()
		print "Dropping in water filled you with determination..",
		raw_input()
		self.act()
		
		if action == '1' or action == '':
			print "nobody came"
			return 'waterfall'
		
		elif action == '2':
			move = raw_input("1.next\n2.last\n3.hOI, there is a secret base!\n>>>")
			if move == '1' or move == '':
				return 'hotland'
			elif move == '2':
				return 'snowdin'
			elif move == '3':
				return 'temmie'
		
		else:
			return 'waterfall'
		
		
class Temmie(Scene):
	
	def enter(self):
		print "Help Temmie go to the college",
		raw_input()
		
		action = raw_input("1.Buy\n2.Sell\n3.Chat\n4.Quit\n5.I wanna check up my wallet first\n>>>")
		
		if action == '1':
			print "hOI. Can't buy now."
			return 'temmie'
			
		elif action == '2':
			sell()
			return 'temmie'
		
		elif action == '3':
			print "hOI"
			return 'temmie'
		
		elif action == '4':
			print "Good-bye, hOI"
			return 'waterfall'
		
		elif action == '5':
			act_CENT()
			return 'temmie'
			
		else:
			return 'temmie'


class Hotland(Scene):
	
	def enter(self):
		print "..I don't know why..But this is the end anyhow.."
		
		action = raw_input("Hitting ENTER will fill you with determination..")
		return 'determination'


class Map(object):
	
	scenes = {
		'determination': Determination(),
		'ruins': Ruins(),
		'snowdin': Snowdin(),
		'waterfall': Waterfall(),
		'temmie': Temmie(),
		'hotland': Hotland()
	}
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)




class Monster(object):
	
	def FIGHT(self):
		pass
	
	def ACT(self):
		pass
	
	def CONT(self):
		pass
	
	def MERCY(self):
		pass



class Stuff(object):
	
	def INFO(self):
		print "There is no infomation for this."
	
	def USE(self):
		print "Useless."
	
	def DROP(self):
		print "You don't know what to drop."
		
	def whattodo(self):
		what = raw_input("1.INFO\t2.USE\t3.DROP\t>>>")
		
		if what == '1':
			self.INFO()
			
		elif what == '2':
			self.USE()
			
		elif what == '3':
			self.DROP()
			
		else :
			print '???'
			self.whattodo()

class Dogresidue(Stuff):
	
	def INFO(self):
		print "It's dog residue",
		raw_input()
	
	def USE(self):
		while len(CENT) < 8:
			CENT.append('Dogresidue')
		print "Your bag is full of dog residue.",
		raw_input()
	
	def DROP(self):
		print "You dropped it like rubbish.",
		raw_input()
		CENT.pop(choose - 1)


def act_CENT():
	print GOLD
	print CENT
	
	stuffs = {'Dogresidue': Dogresidue()}
	
	print "Choose a stuff(1-8) to operate: ",
	raw_choose = raw_input()
	if raw_choose == '':
		return
	else:
		choose = int(raw_choose)
	
	if 0 < choose < 9:
		stuff_name = CENT[choose - 1]
		stuff_get = stuffs.get(stuff_name)
		stuff_get.whattodo()
	else:
		print "So you want to do something with your own body"
		

def sell():
	
	if len(CENT) == 0:
		print "But you have nothing"
	
	else:
		print CENT
		raw_choose = raw_input("choose 1-8 to sell\t>>>")
		if raw_choose == '':
			return
		else:
			choose = int(raw_choose)
		
		print '"oH you have %s!! Temmie want that!"' % CENT[choose - 1]
		raw_input(">>>sell it")
		
		print '"Shut up and take my money!"'
		get_money = randint(3,8)
		CENT.pop(choose - 1)
		
		print "You got %dG" % get_money
		global GOLD
		GOLD += get_money
		


a_map = Map('ruins')
a_game = Engine(a_map)
a_game.play()