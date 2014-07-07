#using the while statement on a few programs we wrote earlier.
#this one is the pay of the worker problem. #This code uses a function to compute the wage, it uses a while loop to accept inputs until the user wants to quit, and uses the try-except structure to ensure that the right type of input is given.
def wages(a,b): #whenever something has a block of statements under it, it ends with a : and the block of statements is all indented.
	#a is hours worked, and b is rate per hour
	wage=(a*b)+(((a-40)>0)*(a-40)*(0.5)*b)
	return wage
in_h=0# we must define the two variables before we can use them in the condition part of the while statement
in_r=0#take care (obviously) that the definition is outside the function definition
while (in_h!="x")*(in_r!="x")*(in_h!="X")*(in_r!="X"): #instead of that, you could also use while True.. (dont type TRUE) since the if statements already check for an x input, and break the loop execution.
	#First get the input for the two variables.
	in_h=raw_input("Enter the number of hours worked: ")
	if (in_h=="x")+(in_h=="X"):
		print"Wage Compute has Quit"
		break
	try:				#Check if the user has input a string of characters other than x or X
		hours=float(in_h)
	except:
		print "You must enter a number, or Enter X to quit."
		continue
	#in case you haven't entered x or X foe is here, and we are checking if you have entered a number. If you have it is stored in hours, if you havent you are warned to enter a number. Since num of hours worked is just as essential as the rate per hour, we want to start accepting a fresh set of values, which can only be done by starting a fresh iteration, hence the continue statement.
	in_r=raw_input("Enter the rate per hour: ")
	if (in_r=="x")+(in_r=="X"):
		print"Wage Compute has Quit."
		break
	try:				#Check if the user has input a string of characters other than x or X
		rate=float(in_r)
	except:
		print "You must enter a number, or Enter X to quit."
	#Now that we have the inputs for the two variables, lets convert them into numbers. If the two variables were x, meaning the user intends to quit, the foe wouldnot reach here.
	##The code on lines 31 to 38 is correct, except that if you input a string in hours, it will wait untill you input the rate to tell you that you input a string, which is not neat... (that is because the code on lines 11 to 14 and 21 to 24 will be executed before this block, which contains the checking statements, is executed. Instead, we rewrote it to include the check individually for each variable as it is input. So, the code on 15-20 checks if in_h is not x, but is a string, which is not acceptable. and the code on 25-28 checks if the in_r is not x, but is a string, which too is not acceptable. Since both values are required to do the computation, we start a fresh iteration by discarding the current one by using the continue statement.
	#try:
	#If the user didnt enter x or X, the foe will be here. If it is a number, we can use it to compute the wages. if it is not a number and is also not x or X, we must trip the execution.
	#	hours=float(in_h) #if in_h is not a number, this line will fail.
	#	rate=float(in_r)  #if in_r is not a number, this line will fail. 
	#	print "The calculated pay is:",wages(hours,rate)
	#except:
	#	print "You must enter a number, or Enter X to quit."
		#the try-except will ensure that a cycle of the loop ends gracefully, no matter what the input is.
	##	
#this ends the while statement. Note that each time the while statement executes, we check the input and after that compute the wages. Thus the try-except is inside the while.