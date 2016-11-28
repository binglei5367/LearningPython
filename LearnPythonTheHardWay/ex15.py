# To get your command line arguments
from sys import argv

# command line arguments will be assigned to these two arguments
script, filename = argv

# return a file object
txt = open(filename)

# print the filename
print "Here is your file %r:" % filename
# use the 'read' method to read the content of your file
print txt.read()

# print each line of the file one by one
#print txt.readline(),
#print txt.readline(),
#print txt.readline()

# print each line as a list
#print txt.readlines()

# close the file
txt.close()