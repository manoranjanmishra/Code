l=0
h=100
print "Please think of a number between 0 and 100!"
while True:
	g=(l+h)/2	#since l & h are integers g is always a rounded down integer
	print "Is your secret number %d?"%(g)
	u=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
	while not(u in "lhc"):
		print "Sorry, I did not understand your input."
		print "Is your secret number %d?"%(g)
		u=raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
	if(u=="c"):
		print "Game over. Your secret number was: ",g
		break
	if(u=="l"):
		l=g
	if(u=="h"):
		h=g