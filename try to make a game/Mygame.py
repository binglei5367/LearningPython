from sys import exit


class Engine(object):
	
	def __init__(self,scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		
		while True:
			print "\n----------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)


class Scene(object):
	
	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)
	
	def act(self):
		global action
		action = raw_input("\n1.Explore\n2.Move\n>>>")
		
class Determination(Scene):
	
	def enter(self):
		print "Making this stupid game made you filled with determination.."
		exit(1)

class Ruins(Scene):
	
	def enter(self):
		raw_input()
		print "This is the ruins."
		raw_input()
		print "Full of rabbish."
		raw_input()
		self.act()
		
		if action == '1':
			print "\n..but nobody came.."
			return 'ruins'
		
		elif action == '2':
			print "Go on.."
			move = raw_input("1.next\n>>>")
			
			if move == '1':
				return 'snowdin'
			else:
				return 'ruins'
		
		else:
			return 'ruins'

class Snowdin(Scene):
	
	def enter(self):
		print "Welcome to Snowdin..!"
		print "Full of.. Snowballs!.."
		
		action = raw_input("\n1.Explore\n2.Move\n>>>")
		
		if action == '1':
			print "..but nobody came.."
			return 'snowdin'
		
		elif action == '2':
			move = raw_input("1.next\n2.last\n>>>")
			if move == '1':
				return 'waterfall'
			elif move == '2':
				return 'ruins'
			else:
				return 'snowdin'
		
		else:
			return 'snowdin'
		

class Waterfall(Scene):
	
	def enter(self):
		print "Fall into Waterfall"
		print "Dropping in water filled you with determination.."
		
		action = raw_input("\n1.Explore\n2.Move\n>>>")
		
		if action == '1':
			print "nobody came"
			return 'waterfall'
		
		elif action == '2':
			move = raw_input("1.next\n2.last\n3.hOI, there is a secret base!\n>>>")
			if move == '1':
				return 'hotland'
			elif move == '2':
				return 'snowdin'
			elif move == '3':
				return 'timmie'
		
		else:
			return 'waterfall'
		
		
class Timmie(Scene):
	
	def enter(self):
		print "Help Timmie go to the college"
		
		action = raw_input("1.Buy\n2.Sell\n3.Chat\n4.Quit\n>>>")
		
		if action == '1':
			print "hOI. Can't buy now."
			return 'timmie'
			
		elif action == '2':
			print "hOI. Can't sell, either."
			return 'timmie'
		
		elif action == '3':
			print "hOI"
			return 'timmie'
		
		elif action == '4':
			print "hOI. Good-bye"
			return 'waterfall'
		
		else:
			return 'timmie'


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
		'timmie': Timmie(),
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
		pass
	
	def USE(self):
		pass
	
	def DROP(self):
		pass


	
a_map = Map('ruins')
a_game = Engine(a_map)
a_game.play()