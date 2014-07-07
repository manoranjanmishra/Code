#excercise 5.2
#this will print out the maximum  and the minimum of all the entered numbers.
#we will need two variables max_num & min_num to store these values. Besides a try-except will be used to see if the user inputs strings that arent valid or wants to quit.
max_num=None
min_num=None #this initialises the containers for the maximum and minimum variables
input=None
pos_count=0
neg_count=0
count=0
while (input!="done")*(input!="Done")*(input!="x")*(input!="X"):
	input=raw_input("Enter your number: ")
	if (input!="done")*(input!="Done")*(input!="x")*(input!="X"):
		#lets try it in a different way.. lets leave the break statement to the else block
		try:
			input=float(input)
			count=count+1
			#if the foe is here we have a number as input.
			if (max_num<input)or(max_num==None):#dont get it wrong here.. if you write (max_num>input) that is wrong. Look at it for a sec, what does it mean??... What we should be writing is that, fi the input we have is larger than max, we should store it as the new max number.
				max_num=input
			if (min_num>input)or(min_num==None):
				min_num=input
			if (input>=0):
				pos_count=pos_count+1
			else:
				neg_count=neg_count+1
		except:
			print "You must enter a number. Or, enter Done or X to quit"
			#continue is optional since it will be last statement to be executed, and there is nothing to skip.
	else:
		#print "The Input section has ended"
		break
if (count!=0):
	print "You entered",count,"numbers","of which",pos_count,"are positive and",neg_count,"are negative"
	print "The maximum number is",max_num,"and the minimum is",min_num
else:
	print "You didn't enter any numbers"

