# a program to print scores when the input is between 0.0 to 1.0
print "This program will tell you your grade based on the score you input between 0.0 to 1.0"
try:
	score=float(raw_input("Enter your Score: "))
	if (score>1.0)or(score<0.0): #this checks if the score is in range.. if the score is within the range, further conditions are checked. IF not (which is what makes the condition of this if statement true, the print statement is executed
		print "Score is out of the range 0.0 to 1.0"
	elif score>=0.9:
		print "A"
	elif score>=0.8:
		print "B"
	elif score>=0.7:
		print "C"
	elif score>=0.6:
		print "D"
	elif score<0.6:
		print "F"
except:
	print "Bad Score"
#we used the try & except structure to catch a string input in the score. This is because inputting a string would give an error with the float operator. But, any other input would simply give a numeric value. thus we used a if-elif structure to write the program.
#The score>1.0 & score <0.0 allows execution only if the input score lies between the specified range.
#somehow if you try if score >1.0 and score<0.0 ::OR:: (score>1.0)and(score<0.0) ::OR:: (score>1.0)&(score<0.0) the code doesnot work.
#another way::
#this program is written using the ideas in bypass_ifelse.py
try:
	score=float(raw_input("Enter the score: "))
	print "Score out of range, Enter a score between 0.0 to 1.0 only"*((score<0.0)+(score>1.0))
	#that is the equivalent of:
	#if (score<0.0) or (score >1.0):
	#	print "Score out of range, Enter a score between 0.0 to 1.0 only"
	print "The grade is: "*(score<=1.0)*(score>=0.0)+"A"*(score>=0.9)*(score<=1.0)+"B"*(score<0.9)*(score>=0.8)+"C"*(score<0.8)*(score>=0.7)+"D"*(score<0.7)*(score>=0.6)+"F"*(score<=0.6)*(score>=0.0)#the part (score<=1.0) and the (score>=0.0) is to check out the part where the score is beyond range
	#that is the equivalent of code on lines 5 to 16 above
except:
	print "You must enter a number"
#one advantage is that it sandwiches all the if elif statements into one line.
