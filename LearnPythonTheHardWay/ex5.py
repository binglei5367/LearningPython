my_name = 'SaltSpeckle'
my_age = 19 # quite true
my_height = 177 # cm
my_weight = 64 # kg
my_eyes = 'Grey'
my_teeth = 'White'
my_hair = 'White'

print "Let's talk about %s." % my_name
print "He's %dcm tall." % my_height
print "He's %dkg heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height +my_weight)