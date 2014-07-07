#problems from MIT problem set 1
#this is a program to compute the n-th prime number
#for a given number we try dividing it by all numbers upto itself, starting with one.In case it is divisible by a number other than one and itself, we stop.
while True:
	try:
		n=float(raw_input("Which prime number do you want? "))
		if(n!=int(n)):
			print "You entered a fraction!"
			n=int(n)
		if(n<=0):
			print "You entered a negative number!"
			n=int(0-n)
		break
	except:
		print "You must input a number."
#now we have an input for n.
#we have to set about finding the nth prime number.
test=1#we increment this number gradually and test to see if it is prime
count=0#if we find that test is prime we increment count by 1. If count equals n, we have found our prime number.
cycles=0
#we need two while loops, one to increment test, and the other to check if test is prime or not.
#n=int(n) #why is this line here? It is not required, since we have already taken care of it at line 9
while (count<n):
	test=test+1
	div=1
	a=0 #no of factors.
	while (div<=test): #if you put while True, foe runs through it the first time fine.. but since the while itself doesnt have a condition that will become false at some point in time, it keeps getting executed. Each time it runs, div increases by 1. Now, when div is increasing, no where in the loop, we have any check to trip it if it increases beyond test. If div>test, the if loop will never hold, and with no check on div, it will simply keep increasing, with the loop never ending. So, with while true, you either put a check like if(div>=test): break.. or put this in the condition itself. 
		cycles=cycles+1 #to find out how many times this loop is executed
		if (test%div)==0: #instead of counting the number of factors each number has, here we simply break the loop, the first time we find a factor other than one and the number itself.. this way we are discarding any numbers that have a factor other than one, BEFORE reaching the number itself.
			if (div==1)or(div==test):
				a=a+1
			else:
				break
		div=div+1
		if (div>(test/2))*(div!=(test+1)): #if you just wrote if (div>=(test/2)): div=test, the program doesn't print any result, neither does it stop. This is because, the first time this line is executed, div is set equal to test. The loop then executes because the condition to check at line 27 is div<=test (you can't say div<test, because a prime number is div by itself.. and by doing this div will never reach test, so no number will have two divisors.. the program will go on and on, and never stop.. since a will never be 2, and count will never increase and reach n, and thus the outer while loop will never break), then as the loop executes, div becomes test+1 and then this condition is again satisfied, since test plus one is obviously more than test/2.. div is again RESET to test, and the loop repeats endlessly, because on the next iteration div is again test+1.. and the if condition executes again, on and on. To halt it, we have to stop the "if" on executing as and when div is test+1 (because in the endless case it never rises beyond test+1, after which it is reset).. so add the (div!=(test+1)).. since on the next iteration, as div is test+1, the loop is broken, as break executes.. and then a new number is tried.. since foe shifts to line 23
			div=test						#this code is intended to reduce the number of times this loop is run, and hence save some time.
	if (a==2):
		count=count+1 #a prime number has exactly two factors.
		#print "Prime #",count,"is: ",test #you can use this statement to find the list of all prime numbers upto the one you are searching for.
		#print cycles,"cycles so far" #and the number of computation cycles upto that point.
	if (count==n):
		print "The",n,"th prime number is",test,"!"
		print "Found it in",cycles,"cycles" #this statement tells us the number of computations, the number of times the while loop on line 23& 27 was executed to find the result.
		break
print "Done!"
#this program works.
#but, I want to reduce the number of cycles.  Because of how we check for prime numbers, line 30 weeds out not only odd numbers, but any number that returns a zero remainder before div==test. 
#in the numbers that are prime, i think it would greatly reduce the number of cycles, if we included code that set div=test, once div is more than test/2.. this shouldnot affect anything, because if div>test/2, test/div can never be zero. This idea is tried on lines 41 & 42. But this doesn't seem to improve anything. That is because the correct place for it is lines 35-36 at the end of the inner while loop. Out side, the div value simply get's reset to 1 each time the loop is re run.
#one thing i want to do, is to make this a function.. one that generates the nth prime number.
#another thing I want to do, is to make this an interactive program, where you enter n.. wait for it to compute. Or enter x to quit. If you enter something other than x it prints an error, if you enter a number, it will try computing the prime number corresponding to that.
#some statistics, they are measured by looking at a stopwatch, so they have a ~2 sec error:
# n			time		cycles			prime
# 100		
# 1000		00:02		1874557			7907
# 10000		04:52						104729
# 100000	
# 1000000

