print "You'll be asked to enter your name, the program will then print your name after that"
#one might try to prevent people from entering numbers here, and so we can play with the try-except structure
first_name=raw_input("Please enter your first name: ")
try:
	a=float(first_name)
	print "You cannot enter a number as your name!"
except:
	last_name=raw_input("Please enter your last name: ")
	try:
		b=float(last_name)
		print "You cannot enter a number as your name!"
	except:
		print "Hi!", first_name,last_name
#The code on lines 15-22 are wrong
#try:
#	first_name=raw_input("Please enter your first name: ")
#	a=float(first_name)
#	last_name=raw_input("Please enter your last name: ")
#	b=float(last_name)
#	print "You cannot enter a number as your name!"
#except:
#	print "Hi!", first_name,last_name
#The code on lines 24 to 31 is absolutely all right except it allows you to enter numbers on both names before printing an error
#first_name=raw_input("Please enter your first name: ")
#last_name=raw_input("Please enter your last name: ")
#try:
#	a=float(first_name)
#	b=float(last_name)
#	print "You cannot enter a number as your name!"
#except:
#	print "Hi!", first_name,last_name
#We went a step beyond what was asked and tried enabling a basic check on the values entered as the first and last names. If it is a number the program quits with an error message saying that you entered a number
#This program uses the fact that try-except statements can be nested. the basic thing to be learnt is that try and except act as labels for blocks of code. if the try block has an error somewhere then the except block executes, the except block in turn can have further try and except blocks inside it.
#What if there is an error in the except block? If the statement where the error occurs is inside a try block, the corresponding except block will be executed , otherwise the program will quit with an error. You can very easilt check this by, inserting b=float(last_name) after line 8 above.