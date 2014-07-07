#excercise 5.1
#this is an infinite loop, since we have to continue accepting values till the user enters done.
#we thus have to use the while statement.
#to find the average we also have to count the number of valid inputs so far, until the user enters "done" or "x"
sum=0 #harmless, since adding zero to anything doesn't change it
count=0 #harmless for the same reason as above
input=None #normally I would have set input equal to something, but since i can mark it empty, I set it equal to None
while (input!="Done")*(input!="done")*(input!="x"):#if any of these is false, the user wants to end the process, and this condition obviously evaluates to false and the while loop exits
	input=raw_input("Enter a Number: ") #this is for the user's input. It could be a number, or a string like Done or X, or neither.
	#first check if the user wants to stop/quit the process
	if(input=="done")+(input=="Done")+(input=="x")+(input=="X"):
		break #the loop to enter data quits, and we move to the execution of average, and the printing part
	try:
		input=float(input) #convert the input value to a num, so that you can add it
		count = count+1	#if the input value is actually a num, the foe is here, and we have to count this as valid input
	except:
		print "You must enter a Number.. or Done or X to exit"
		continue #i'm sure this statement is optional, aince the try-except structure will execute one or the other block of code as appropriate.. and since it is a while loop the foe shifts back to line 8.
	#if foe is here we have numeric input, and all we have to do is add it to sum
	sum=sum+input
average=sum/count
print "You entered",count,"numbers."
print "Their total is: ",sum,"and their average is: ",average
print sum,count,average

