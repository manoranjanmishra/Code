#using while statements on a few of the programs we wrote earlier.
#this one is the score grading system
print "This program will translate the score you enter into a grade"
def scorer(a):
	#THIS FUNCTION IS WRITTEN USING THE IDEAS CONTAINED IN BYPASS_IFELSE
	#print "Score is out of range"*((a>1.0)+(a<0.0)) #this is the equivalent of if(a>1.0)or(a<0.0): print "Score..."
	a=(a/100)*(a>1.0)#this line was added later, to simply divide the score by 100 without returning an error. You can comment this line, and uncomment the following one, to revert this functionality
	print "The Grade is: "*(a<=1.0)*(a>=0.0)+"A"*(a<=1.0)*(a>=0.9)+"B"*(a<0.9)*(a>=0.8)+"C"*(a<0.8)*(a>=0.7)+"D"*(a<0.7)*(a>=0.6)+"F"*(a<0.6)*(a>=0.0) #since each part has very specific ranges specified, values out of the range will print nothing.

input=0 #this is just to initialise the variable that will store the input score
while (input!="x")*(input!="X"): #Keep going until the user enters x or X. In that case, the if statement doesn't execute, and as soon as the flow-of-execution (foe) shifts back to the while statement, the loop terminates. In case the user hasn't entered a x or a X, the if statement executes, and the foe goes back to the while statement, which consequently evaluates to true, and the execution continues till an x or X is entered.
	input=raw_input("Enter the Score, or Enter x to quit: ")
	if (input!="x")*(input!="X"): #if the input is an x the user intends to quit, so there is no sense trying to evaluate the float part and print an error, which is why it is contained inside here. if it is not x, then an error message must telll the user to either type x or the score.. which is part of the except. Either case is thus handled, and the if statement executes. the if is basically checking if you entered x. If you didnt, you want the score evaluated. "if" you did, you want to quit.
		try:
			score=float(input)
			scorer(score)
		except:
			print "You must enter a number, or Enter x to quit."
print "Score Grader has finished & Quit." #if you don't enter an x or X foe will never come to this statement. Only if you do that, with the intention to close the grader, foe comes to this statement and executes it, showing that the grader has successfully quit.