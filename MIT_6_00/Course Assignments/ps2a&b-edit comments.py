#solving a diophantine equation
#we will try to solve the equation Ax+By+Cz=D, where the user inputs A,B,C.. and we list the values D can take, and the corresponding combinations of x,y,z.
#in addition we will maintain a record of the values D cannot take, and find the max such value mas max_notd. A,B,C are inputs from the user. The program will print out the value of D, and below it the sets of x,y & z corresponding to that D.
#how to find out the max not D? Notice that, all one has to do is find the minimum of A, B, C. Call this number p. If at anytime you can find p consecutive numbers, such that they are all values that D can take, then there is no value greater than the last max_notd value that D cannot take. That is because, further values can simply be obtained by adding p and it's multiples to the set of consecutive numbers you found.
#in our solution we print all combinations till we find a max_notd, and the consecutive p numbers after which no larger max_notd exists.
#as a failsafe we can we ask the user to input a maximum value of some sort after which we dont search anyfurther.
from math import * #this statement is to use the min function to find out the minimum of A,B&C at line 57. You could instead cooment out this line and that statement, and uncomment the if statements below it on lines which also do the same purpose.
print "Diophantine Equation Solver."
print "An equation of the type Ax+By+Cz=D is called a diophantine equation"
print "You have to enter values of A,B&C."
again=None
while (again!="X")*(again!="x"): #if the user inputs an x or X anytime, we stop.
	#accept inputs for A,B,C & check that they are either numbers or x, not any other string.
	#we are accepting negative input too. Though fractions are not welcome. If you're okay with fractions, comment out the code below.
	try:
		in_A=raw_input("Enter the Value of A: ")
		if(in_A=="X")or(in_A=="x"): #if the user enters an x at any step, the value of again is changed to x, and the loop is broken. Since we are not inside any other loop, this breaks the while loop at line 11, with again=x
			#again=in_A #this line is optional. Since we are breaking out of the while loop, the foe wont shift to line 11, so it is not essential to set again=x.
			break
		a=float(in_A) #if in_A is a number we assign it's value to a which represents A
		if(a!=int(a)):
			print "You entered a fraction!"
			a=int(a)
		#if(a<0)
		#	print "You entered a negative number!"
		#	a=0-a
		in_B=raw_input("Enter the Value of B: ")
		if(in_B=="X")or(in_B=="x"):
			#again=in_B
			break
		b=float(in_B) #if in_B is a number we assign it's value to b which represents B
		if(b!=int(b)):
			print "You entered a fraction!"
			b=int(b)
		#if(b<0)
		#	print "You entered a negative number!"
		#	b=0-b
		in_C=raw_input("Enter the Value of C :")
		if(in_C=="X")or(in_C=="x"):
			#again=in_C
			break
		c=float(in_C) #if in_C is a number we assign it's value to c which represents C
		if(c!=int(c)):
			print "You entered a fraction!"
			c=int(c)
		#if(c<0)
		#	print "You entered a negative number!"
		#	c=0-c
	except:
		print "You must enter a number, or x to quit."
		continue
	#now we have integer inputs for a,b,c (they can be positive or negative)
	#we proceed to check the diophantine equation. We have to generate x,y & z as well as D. First generate D, then generate x,y,z and check if the equation solves to D.
	#since we are checking for a condition, we can either have while True, with an if statement with a break statement in it.. or include this condition in the while statement itself.
	#initialise the variables first, one for each of x,y & z. one for D, one to store the last D so that we can check id the Ds we evaluate are continuous, and a counter to count the number of Ds that are continuous
	#calculate the minimum of A,B&C.
	minval=min(a,b,c)
	#minval=None #keep this statement commented out if the statements on 59-64 are commented out too.
	#if(a>minval)or(minval==None)
	#	minval=a
	#if(b>minval)
	#	minval=b
	#if(c>minval)
	#	minval=c
	
	D=0 #D is the number that we'll take and find x,y,z for. We initialize D here.
	max_notD=0#we'll have positive D values.. so starting with a 0 is not bad. if you start with a None, you must include a max==None condition, in the comparision statement.
	cntd=0#this is to calculate the number of digits that are continuous.
	#now we go into the equation solving part, we choose a D, and then we sequentially evaluate x,y & z for each D. If we find a x,y, z we print it. Then we check to see if this D is consecutive to the last D, if it is , we increment contd, or else, we reset contd to 0. We repeat this process.. untill contd is equal to the min of a,b,c.
	while True:
		D=D+1
		thisd=0
		x=0
		while(x<=D):
			y=0
			while(y<=D):
				z=0
				while(z<=D):
					if(((a*x)+(b*y)+(c*z))==D):
						#if foe is here we have found a solution.
						if (thisd==0):
							print "For D=",D,"the values of x,y,z are: " #thisd ensures that this line only prints once for a particular D, and we can also count how many solutions a particular d has.
						print x,y,z #this prints the values of x,y,z that satisfy the diophantine equation.
						thisd=thisd+1#count this valid solution.
					z=z+1
				y=y+1
			x=x+1
		if(thisd!=0):
			print thisd,"solutions for",D
		if(thisd==0):
			max_notD=D #this statement should not be in the else to the if statement on line 79 because, that condition doesn't hold for all x,y,z.. the first time it doesn't hold, max_notD will be assigned the value of D, even though there are other x,y,z for which it is a solution. So the right place to check & assign values, is when a value of D has been checked for solutions and no solution has been found.
			cntd=0 #if continuity breaks no point counting continuous Ds
		else:
			cntd=cntd+1#if the continuity in Ds that have valid solutions is lost no point in counting how many continuous Ds satisfy the equation
		if(cntd==minval):#then there is no point checking beyond this limit for a D for which no solution of the equation exists.
			print "The largest number for which no solution of the equation exists is: ",max_notD
			#print "Given",a,",",b,"&",c,"the largest value of D for which no solution exists is",max_notD
			print "The smallest set of consecutive numbers that are a solution of the equation are:"
			while(cntd>0):
				print (D-cntd)+1 #find a way to print this on one line separated by spaces.
				cntd=cntd-1
			print "Phew!" #this will be printed only if a solution is found.
			break
	#Now we have quit the while loop on line 73, and we are in the loop of line 12.. This will start the Diophantine Equation Solver unless someone enters x.
	again=raw_input("If you want to quit press x or X. To restart, just press Enter: ")
if(in_A=="x")or(in_A=="X")or(in_B=="x")or(in_B=="X")or(in_C=="x")or(in_C=="X"):
	print "Diophantine Equation Solver has quit. :)"
if(again=="x")or(again=="X"):
 print "Diophantine Equation Solver has finished & quit."
 #after so much trial and eroor and what took me an entire afternoon and evening, i finished this in over 7 hours.
 #speaking of state variables the only two state variables we use are, the number of solutions a specific value of D has, i.e thisd, and the number of consecutive D's that have solutions, cntd.