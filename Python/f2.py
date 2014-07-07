#solving equations of the type Ax+By+Cz=D to find the values of D that have valid integer solutions in terms of x,y & z and to find those solutions.
#to find the max value of D that doesn't have a solution, and to then find the sequence of consecutive numbers that follow it.
#returns the maximum number that doesn't have any corresponding valid solutions. Optionally, it prints the first set of consecutive numbers that have valid solutions in the equation
#we assume A,B,C are all positive, non-fractional numbers. If they are not, the function has a try except that will return False. If you enter x or X, it exits too and also returns x or X
def dioeqn(a,b,c):
	if(a=="x")or(a=="X"): #if a input is x or X, we stop executing further, and return x.
		return x
	if(b=="x")or(b=="X"):
		return x
	if(c=="x")or(c=="X"):
		return x
	try:
		a=float(a)
		b=float(b)
		c=float(c) #catches strings.
	except:
		print "You entered a string!"
		return False
	#now a,b,c are float numbers.
	#minval=min(a,b,c) #Doing this needs 'from math import *'
	#to find the minimum of a,b,c
	minval=None
	if (a<minval)or(minval==None):
		minval=a
	if(b<minval):
		minval=b
	if(c<minval):
		minval=c
	d=0 #let's start by testing for d=0.
	cntd=0	#this is to keep track of how many continuous numbers have at least 1 valid solution. So each time s!=0, cntd=cntd+1. If s==0, we rest cntd to zero, because the continuity is lost.
	maxnotd=0
	cycles=0#cumulatively count how many cycles are executed
	#we now have to initialise variables x,y & z. Initialise them with zero.
	while True: #this loop keeps incrementing D by 1.
		s=0	#this counts the number of solutions for each D value. THe solutions are printed as they are found.
		x=0
		while (x<=d):
		#while(x<=(d/a)): #to reduce the number of computation cycles. It reduces the number of cycles by a*b*c times!
			y=0
			while (y<=d):
			#while (y<=(d/b)):
				z=0
				while(z<=d):
				#while (z<=(d/c)):
					cycles=cycles+1
					if (((a*x)+(b*y)+(c*z))==d):
						#then we have found a solution for this d.
						s=s+1
						#you can comment out the following 3 lines if you do not need to see the solutions as they are calculated
						if(s==1):
							print "The solutions for",d,"are: " #that is so that this line is printed only once for each D.. and including it inside the outer if statement means that, if a D value has no solutions this line wont be printed.
						print x,y,z
					z=z+1
				y=y+1
			x=x+1
		#now all possible x,y,z for a particular D have been counted.
		if (s!=0): #means that the current D has at least one solution
			cntd=cntd+1 #we count this D hoping that the next D be a solution, in this way once we reach minval, we stop.
		else:
			maxnotd=d #Since s==0, this value of D has not solution. This statement should be executed at-most once for each D value, so it should be outside the x,y,z loops
			cntd=0 #if any one  D has no valid solution, cntd is reset to 0, forgetting the consecutive numbers with valid solutions before it, since continuity was broken
		if(cntd==minval): #then all further numbers will be consecutively ones with valid solutions
			#time to print results and stop checking further.
			print "The largest number for which no solution of the equation exists is: ",maxnotd
			print "The first sequence of consecutive numbers after which every number has a valid solution is:"
			while (cntd>0):
				print (d-cntd+1)
				cntd=cntd-1
			print "This took",cycles,"cycles"
			return maxnotd #once this statement is executed no statement below it will be executed, so it is at the very end. And, it makes the break statement optional
			#break #Optional:: this breaks the outer while loop, and stops execution
		d=d+1 #don't forget this. We didn't put this right after x=x+1 because we needed the value of D all along, till here.
	#this is outside the while loop.
#function ends
#the code with the commented out while loops activated to reduce computing cycles got to the solution of dioeqn(101,102,103) in 172491826 cycles, while the non optimised code was still struggling to reach 1000
#the sequence is 5050 to 5150, with maxnotd being 5049
#while the non optimised code doesnt print results as fast it is still working. It is all right, but takes way more time.						