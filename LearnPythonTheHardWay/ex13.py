from sys import argv

script, first, second, third = argv
# Three arguments should be given before the script runs 
# The 'script' has been assigned, 
# it's the name of the script(the stuff you write with .py in the end)

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# These will ask User to enter something more after the script runs
forth = raw_input("Enter something more: ")
print "Your forth variable is:", forth
fifth = raw_input("Anything else? ")
print "Your fifth variable is:", fifth