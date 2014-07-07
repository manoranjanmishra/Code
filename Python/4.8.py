#compute grade problem
#this program is written using the ideas in bypass_ifelse.py
def score_1(score):
	#this function is written using the ideas in bypass_ifelse.py
	print "Score out of range, Enter a score between 0.0 to 1.0 only"*((score<0.0)+(score>1.0))
	#that is the equivalent of:
	#if (score<0.0) or (score >1.0):
	#	print "Score out of range, Enter a score between 0.0 to 1.0 only"
	print "The grade is: "*(score<=1.0)*(score>=0.0)+"A"*(score>=0.9)*(score<=1.0)+"B"*(score<0.9)*(score>=0.8)+"C"*(score<0.8)*(score>=0.7)+"D"*(score<0.7)*(score>=0.6)+"F"*(score<=0.6)*(score>=0.0)#the part (score<=1.0) and the (score>=0.0) is to check out the part where the score is beyond range
def score_2(score):
	#this is the normal way to write this function
	if (score>1.0)or(score<0.0):
		print "The entered Score is out of the range 0.0 to 1.0"
	elif score>=0.9:
		print "Grade: A"
	elif score>=0.8:
		print "Grade: B"
	elif score>=0.7:
		print "Grade: C"
	elif score>=0.6:
		print "Grade: D"
	else:
		print "Grade: F"
try:
	score_input=float(raw_input("Enter the score: "))
	#score_1(score_input)
	score_2(score_input) #uncomment one of these lines and see the output
except:
	print "You must enter a number"