from sys import argv

script, filename = argv

print "We are going to erase %r." % filename
print "If you don't want that, hit CTRL-C on your keyboard." # CTRL-C will break the command immediately
print "If you do want, hit RETURN(Enter)." # RETURN(ENTER) will get the command going on

raw_input("ACT: ") # wait for User's act

print "Opening the file..." # This makes progress more visible
target = open(filename, 'w') # 'w' makes 'open' running for 'write'

print "Truncating the file. Completed!"
target.truncate() # As a matter of fact, this is unnecessary 
# because the file has been truncated if open the file with 'w'

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1 + '\n' + line2 + '\n' + line3)

# This will 'SAVE' the file
print "And finally, we close it."
target.close()

print "Don't you want to have a look at what you have writed?"
choose = raw_input("Y/N? >>>")

if choose == 'Y':
	print "Here is %r:" % filename
	targetplus = open(filename)
	print targetplus.read()
elif choose == 'N':
	print "That's alright."
else:
	print "unknown string"