#This code is a tiny(really??) computer game called Guess my Guess. The computer guesses a number between 1 to 10.
#The user then tries to guess the number in the number of attempts that is input in the beginning of the game.
#There are a fixed number of total attempts the user is allowed, which is also input at the beginning of a game.
#Thus, it's like, I'll like to be given three attempts at each number, and seven attempts overall. If i guess wrong seven times, the game is over.
#Should the user guess correct, the computer guesses again, and the game repeats. If the user inputs x or X the game asks for confirmation and then exits.
#This version of the Game does not use any functions.
import random #this is for the random.random() function at line 33, which the computer uses to guess an integer. ##if instead you wrote 'from random import *' you would have been able to call random.random() simply as random() on line 33.
print "Guess my Guess v1.0\n"
again="y" #We need to define again before the while loop on the next statement starts using it. Any value other than X or x is fine. We chose y.
while (again!="x")*(again!="X"):
	#the following part of the code is to get input for the number of tries per guess, and the number of tries overall.
	try:		#Since the input statements follow one another, the input breaks incase the user enters something that is not a number.
		retries=float(raw_input("How many retries do you want to guess my guess?: "))
		retries=int(retries) #incase the user enters a fraction, we dont want to print an error, we just take the decimal part
		lives=float(raw_input("How many numbers do you want to guess at, before it's Game Over?: "))#lives=float(raw_input("How many chances do you want to have overall, before it's Game Over?: ")) was a previous game idea, but asking how many times to try is a better idea apparently
		lives=int(lives)
		#what if somebody enters a negative number? We'll not print an error in that case too, and simply take the positive part.
		if (retries<0):			##Code to ignore the minus sign
			retries=0-retries	##and to simply take the positive part
		if (lives<0):			##and assign it to the variable it was intended for.
			lives=0-lives		##No errors, and we pretend nothing ever happened. :)
		print "You have",retries,"chances to guess one of my guesses and",lives,"guesses to try"#print "You have",retries,"chances to guess one of my guesses and",((lives>retries)*lives),"retries in all"*(lives>retries),"\b\b\b\b one guess to try"*(lives<=retries) #in case lives is lesser than retries the user must be told that he can play only one guess, or else he must be told that he has such many lives.
		#if (lives<retries):
		#	lives=retries #in case the user enters a lesser number of lives than retries, we let the user complete guessing one number atleast before the game gets over.
	except:
		print "You must enter a number. Guess my Guess v1.0 will quit.";oat=-2;break #this statement prevents a variable not defined error at line 29-30 since the retries & lives variables are defined inside the try block itself.
	#once we have the number of tries per guess, and the number of tries over all, the game can begin.
	#incase the user wants to keep playing after game over without changing the retries per guess (rpg) and overall retries (oat) we have to assign them to two variables separately, so that the previously input variables are not changed.
	rpg=retries		#RETRIES PER GUESS
	oat=lives		#OVER ALL TRIES.
	#one thing I'm confused about here is to put what while loop where? oat outside rpg or rpg outside oat?
	while (oat>0):
		cg=int(10*random.random())#computer makes a guess. The random.random() guesses a fractional number with no integer part, so we first multiply it by ten, to give it an integer part, and then use int on it.
		#cg=7 #this is the temporary guess statement we are using for testing purposes.
		rpg=retries #Retries per guess must be reset to it's original value each time the user completes guessing.
		#print "The number of retries was reset"*(rpg==retries)
		while (rpg>0): #if you try rpg>=0 it also allows negative values of rpg... Why? Actually, No. It doesn't allow negative values of rpg. The debug statement on line 60 prints rpg after rpg=rpg-1 executes. There rpg was zero because the while loop allows rpg>=0, and then rpg=0 becomes rpg=-1, the while loop trips. And we go out to the oat while loop. There the rpg is reset again. You can see that this happens because the debug statement on line 34 is executed. Now the loop continues. rpg gets the reset value, and by the time it is printed, the value has already reduced by one. Mean while, the value of oat is reducing by one with each wrong try. if the code on line 57-58 removed, the oat value will stay negative.. untill rpg also becomes negative.. then the inner loop exits, and goes to the outer loop, which also exits since oat>0 for the outer loop to work. How to fix this? First ensure (rpg>0) this will ensure that 3 retries give 3 chances and not 4. And, to preventing oat becoming negative and allowing additional chances, enable the code on lines 57-58. The break statement terminates execution as and when oat becomes zero. That way as foe shifts to outer loop, the outer loop with oat>0 also quits.
			##trial=3 #in-case the user doesn't input a number, we give him 3 retries.
			#user tries a guess. If the input is a string, we warn the user that a number has to be input, and let him try again.. however rpg is not changed.
			while True: #an infinite loop. If the user enters a number, the try block executes and breaks the loop. If the input is a string the except block executes and continues the loop.
				try:
					user_input=raw_input("Your guess: ")
					if (user_input=="X")or(user_input=="x"): #Either X or x means quit.
						oat=-1	#if oat is 0 the statement on line 69 would be triggered. -1 is our "exit flag".
						break	#The break statement means that the user doesn't want to guess anymore, and wants to quit the game. This loop is exit. oat=-1 is an exit flag.
					guess=float(user_input)
					break
				except:
					print "You must enter a number, or Enter X to quit."
					#trial=trial-1
					continue
			##if (trial==0):
			##	print "You entered a non numeric value",trial,"times. You must enter a number"
			##	continue #since the input is not a number, guess has no value, and hence there is no point processing the rest of the loop, we let the user try again
			#if foe is here, that means we have a numeric guess.
			if (oat==-1):#then the user wants to exit the game and line 44 was never executed.
				break #this break statement breaks this loop, and shifts foe to the outer oat>0 loop. since oat=-1, the outer loop will fail.
			guess=int(guess) #we convert it into an integer, since the computer is guessing an integer anyway.
			if (guess<0):
				guess=0-guess #this is to convert negative input to positive numbers.. i.e dropping the minus sign.
			#then we check the guess.
			if (guess!=cg): #if guess is wrong..
				rpg=rpg-1	#the retry count is reduced by one, the overall try count is also reduced by one.
				#oat=oat-1	#oat is anyway equal to or greater than rpg. ##because of a change in the gaming strategy, we have commented out this line. To restore code to play the initial game, replace lines 15,22 with their commented parts & uncomment this line.
				if (oat==0):#if you remove this, and oat somehow reduces to zero during this loop i.e until rpg becomes zero, oat will become negative.. and more importantly it will lose it's purpose.
					break	#if the oat reduces to zero during the execution of this loop, this statement will break execution and cause foe to shift to outer loop, which will immedieately evaluate to false, and terminate the game.
				print "Wrong guess, Try again!"
				#print "RPG",rpg,"OAT",oat #debugging statement used to fix the nested while structure
			else:
				print "Correct!"
				break #if the users guess is correct, this loop must end and the computer must guess again. So this loop is broken, and foe shifts to outer loop.
		oat=oat-1 #this is part of the changed game strategy. To revert to the initial game, refer to line 64, and comment out this line.
		#the code below this line is outside the inner while loop "while(rpg>=0)" (above).
		if (rpg==0)or(oat==0): #the user exceeded the maximum number of tries, so the foe is executing this statement, either the rpg is zero, or the oat is zero or neither is zero, or one of them is zero. If neither is zero, the print statement is not executed. If either or both is zero, the print statement prints the correct guess.
			print "The Correct Guess is",cg
	print "Oops! You have no retries left. Game Over"*(oat==0)
	#print "Guess my Guess v1.0 has quit."*(oat==-1)#this statement is executed only if the user inputs an x at line 40.
	if (oat==-2): #this is because of line 72. to revert to initial strategy, comment out this line too.
		print "Guess my Guess v1.0 has quit."
		again="x"#this will ensure that the game quits when you enter an x as a guess.
	#but it might happen that you've exhausted oat and you want to be given a choice to stop playing, or to start over again.
	if (oat!=-2):#if the user manually quit, by entering a x, this block will not be executed. The -2 is because of line 72.
		again=raw_input("If you want to quit playing, Enter a x. To continue, just press Enter: ")
		#notice line 80 above.
print "Guess my Guess 1.0 has quit"*((again=="X")or(again=="x"))*(oat!=-2)
#This game is basically ready. It has a few issues.
#Some one can enter a character, i.e anything other than a number at the prompt that asks for guesses and tries, and that will basically break the program. For a fix, one could define oat at line 26, before the break statement. Note that if the break is executed the while loop on line 10 is exit and that shifts foe directly to line 85.. and we don't want line 85 to print, since line 26 already gives the message. Since line 85 holds if again is X or x, and because the break statement is executed, again has the value we gave it at line9. So, it doesn't matter what value we give oat as long as we define it.
#This is a bland game, there ae not features.. as in if you enter something wrong there is no way to go back and change it. If you do not want to re-enter retries & chances and just stick with the old ones that you entered, this code doesnot do that.
#And, I will not modify this game-code any further. Any new code I wrote for this game is at g2.py
#I do want to write out the algorithmic (diagrammatic) version of this code.