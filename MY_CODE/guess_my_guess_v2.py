#Guess my Guess v2.0
#rewritten with functions, and ability to replay without having to change rpg, and oat (renamed to nog here)
from random import * #this is for the random function required for the computer's guess.
#function getnum(a,t)
#returns the number if the response is as expected
#returns x if user wants to quit.
#returns xx if the user didn't give the accepted response in the allowed number of tries.
def getnum(a,t):
	#a is the string we want to print when we use get num.
	#t is the number of tries we want to give the user to let him enter what we want him to enter.
	c=1 #if the user enters something we don't want, we keep a count of that.
	while (t==0)or(c<=t): #either there are no limits set to try again, which is represented by 0 here, or if a limit is set and the user hasnt hit the limit
		try:
			b=raw_input(a) #we use a to print our message to the user, and get the input
			if(b=="x")or(b=="X"):#this represents the exit codes, you can add in more here. If a user enters any of these, our function returns a specific value, meaning the user wants to quit. You can add another if statement below to represent different quit codes
				return "x" #x is the I-WANT-TO-QUIT code.
			b=float(b) #if user doesn't want to quit, the foe will be here. We want a number, so we are checking if the user has entered a number instead.
			return b	#if it;s a number, return the entered number.
		except:
			print "You entered a string! Enter a number, or enter x to quit."
			c=c+1 #count the wrong response
	return "xx" #xx is our user didn't give the correct response in the required number of tries code. In case the allowed tries is 0, i.e t=0, this statement will never be executed since the loop will never end.
#end of function

def playgame(a,b):
	#a is the number of times a user is allowed to guess one of the computer's guesses.
	#b is the number of computer guesses the user is allowed to play
	r=0		#retries per guess, this
	c=0.0	#we start counting at 0 for the number of correct answers.
	t=0.0	#total number of tries the user has made.
	while (b>0):
		cg=int(10*random()) #this generates an integer between 0 & 10
		r=a#a decays to zero with each time the computer guesses, so with a new guess it has to be reset. This statement resets it.
		while (r>0):
			ug=getnum("Your Guess: ",0)
			if (ug=="x"):
				if(t!=0):#print only if user has played atleast one attempt
					print "Great game!"*((c/t)>=0.8),"Well played!"*((c/t)<0.8)*((c/t)>=0.6),"You'll do better"*((c/t)<0.6)
					print "No of Correct Attempts:",int(c),"\t No of Attempts",int(t) #print this info before game exits.
				return "x"
			t=t+1
			if (ug==cg):
				print "Correct!"
				c=c+1
				break
			print "Wrong! Try again."*(a!=1)#for the last chance, we print nothing, since we want to say wrong, and include the right answer too.
			r=r-1
		if(r==0):
			print "Wrong! The answer is",cg,"!"
		b=b-1
	if(t!=0): #for the case if someone elters 0 for rpg & nog (see below), the c/t statements create a divide-by-zero error since both c & t are zero. To avoid that, we put a t!=0 as a if statement. In that case the while loop never executes.
		print "Great game!"*((c/t)>=0.8),"Well played!"*((c/t)<0.8)*((c/t)>=0.6),"You'll do better"*((c/t)<0.6)
	return "o" #we use o as the signal for game over because the user ran out of attempts.

def game(): #we've placed the code to play the game inside a function too.
	again=None
	print "Guess my Guess v2.0\n"
	while(again!="x"):
		rpg=getnum("How many chances do you want to guess my guess: ",0)
		if (rpg=="x"):
			again="x"
			continue
		nog=getnum("How many numbers do you want to guess at, before it is Game Over?: ",0)
		if (nog=="x"):
			again="x"
			continue
		again=None#if you chose to play with different settings, again is r at this point, so the while loop will be skipped. So, we reset "again"
		while(again!="x")&(again!="r"): #again=r means replay with different rpg & nog
			print "You have",int(rpg),"chances per guess and",int(nog),"guesses to play"
			again=playgame(rpg,nog) #we store the value of the playgame() function in again, which is the flag for deciding how the game progresses.
			if (again=="x"): #the user quit the game session, ask if user wants to replay or quit the game
				again=raw_input("To quit the game, just press Enter.\n To replay with the same settings, enter Y.\n To replay with different settings, enter R: ")
				if (again=="y")or(again=="Y"):
					continue #this skips everything else in the loop, and starts the game again by calling the playgame function
				elif (again=="r")or(again=="R"):
					break #this breaks the loop, and shifts control to the outer loop which requests user to enter rpg & nog again
				else:
					again="x"
					break			
			if (again=="o"):
				again=raw_input("To quit the game, enter x.\n To play again with the same settings, just press Enter. To change settings and play, enter R: ")
				if (again=="x")or(again=="X"):
					again="x"
					continue
				elif (again=="r")or(again=="R"):
					again="r"
				else:
					continue
	print "Guess my guess 2.0 has quit. :)"
	return "Guess my Guess v2.0 has quit"
#to play the game call the function game()
game()