class Other(object):
	
	def override(self):
		print "Other override()"
	
	def implicit(self):
		print "Other implicit()"
	
	def altered(self):
		print "Other implicit()"

class Child(object):
	
	def __init__(self):
		self.other = Other()
	
	def implicit(self):
		self.other.implicit()
	
	def override(self):
		self.other.override()
	
	def altered(self):
		print "Child, before Other altered()"
		self.other.altered()
		print "Child, after Other altered()"

son = Child()

son.implicit()
son.override()
son.altered()