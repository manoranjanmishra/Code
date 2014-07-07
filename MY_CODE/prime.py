#computing a prime number findprime(). This function computes the n-th prime number, n is an argument of the function.
#And a function isprime() , which checks if a number is prime.

##Function:: isprime()
#returns 1 or True if it is prime.
#returns 0 or False if it is not Prime, or is a Fractional or Irrational number,or 0 or is a Negative number.
#returns 2 if the input is not a number.
#The flags we return are changeable, and if one doesn't need an output, one can comment the print statements out.
#This function uses only two variables, n & a. a is the argument to the function, n is an internal variable. There is no code outside the function.
#What if you enter X?? THe function will determine that it is a string, and will exit with the flag for strings.. i.e return 2
def isprime(a): #we want to test if a is prime or not. The argument you pass to the function is stored in the variable called a.
	#this function assumes that a is a integer.
	#add-in functionality.
	#we'd normally expect not to get strings as input, but just in case we do, we'll include the possibility here.one way is to include a condition in the try block, and the rest of the function in it. The except block then contains an error, and a return false or 0 statement. Or else, include the checking condition in the try part, and if it is true, do nothing. The except part has a return zero, or someother number so that an error can be flagged if required. Plus it can say "You entered a string"
	try:
		a=float(a) #maybe this is a little odd, but if a is a string this statement would not execute. If it's anything else, it'll do fine. And anyway, we check for fractionals in the next if statement itself.
	except:
		print "You entered a string!"
		return 2 #here 2 is our flag for string input.
	if(a!=int(a)):#if a is a integer, a will be equal to int(a). If not, then a is a fraction. In that case, there is no point going ahead. You could try chopping off the decimal part, or rounding it. But we're not doing that here.
		print "Fractional Numbers are neither prime nor composite."
		return 0
		#return False #the number is not prime so, we return False.
	if (a<0):
		print "Negative Numbers are neither prime nor composite."
		return 0
		#return False #the number is not prime so, we return False.
	if(a==0):
		print "0 is neither prime nor composite." #for the case that someone calls the function with zero as argument.
	n=1 #we start checking with 1, since we cannot divide by 0
	while (n<=a):#if you send a negative number, or zero to the function it will never be checked, because of the condition of the while loop.
		if (a%n==0): #i.e if a is divisible by n
			if (n==1)or(n==a): 	#if a is divisible by either 1 or a, then n can be either 1 or a
				if(n!=1):		#this prevents the function from returning a value for n=1
					print int(a),"is prime"
					#return True #whichever return statement you choose too include, note that only the first one gets executed. Any statement after that is simply ignored.
					return 1
			else:#a is divisible by n, but n is not 1 or a, a is not prime
				print int(a),"is not prime" #we don't need to check further. So on the first occurrence, print this statement and exit.
				#return False
				return 0
				#break the break statement is not needed here. Once a return statement is encountered, the value in it is returned, and the function stops executing. After the return 0 statement above, this break statement wont even be executed.. so no point including it at all.
		#the next few lines intend to reduce the number of computations, in order to make reaching the answer quicker.
		if (n>a/2)&(n!=a): #Even if n is equal to half of a, the first part of the if statement will be false, irrespective of whether a is odd or even. At that point when n is just more than half a, n!=a. So the if statement executes. n=a, the n=n+1 is skipped because of the continue statement. The next iteration is a%n being eval for n=a. When it reaches the if statement, n>a/2 is still true, so if not for the other n!=a, the n=n+1 would be skipped, and the loop would freeze endlessly evaluating at n=a. So, we include the n!=a condition, so as to tell that n has been set to a, dont do that again. Now n becomes a+1, which makes n<=a in the while loop false, and loop ends. This also takes care of the case when a=1 (where n=1 is greater than a/2=1/2, and n is assigned the value of a..1 again, making the loop freeze), so including a n!=1 is not necessary.
			n=a				#Execute only if n is not equal to a already. If it is, break the loop. (MORAL)
			continue #this is to prevent the n=n+1 statement from being executed on the next line..
		n=n+1	#if you put this statement before the previous if statement, you could save a loop-cycle. That is because, if n=n+1 comes after, the loop executes for a/2 + 1, and then n=a. If n=n+1 comes first, the loop executes for a/2, and since (a/2 + 1)>a/2, the next value in the loop is n=a
	#end of the checking loop. Since the loop has statements to return results, there are no more lines. Function ends.

##Function findprime() & findprime2()
#This function takes an argument n, and finds the nth prime number.
#The function findprime() is independent, and has all the code it needs to perform it's task. findprime2() however depends on the isprime() function above to work.
#Features common to both functions:
#if you send it a fractional number, it will print an error and quit/find the prime number corresponding to the integer part.
#if you send it a negative number, it will print an error, and quit/find the prime number corresponding to the number part, ignoring sign.
#if you send it zero, it will print an error, and quit. (optionally say that the first prime number is 2)

#findprime(n) uses three variables: a,b,c.. a is the test number, b is constantly increased to check if a is div, and based on that, if a is prime, c counts which prime number that is.
#findprime(n) is self sufficient, it doesn't depend on any external code.
def findprime(n):
	try: #we want to avoid strings, and negative or fractional numbers.
		n=float(n) #this statements checks if the argument is a number, if not, it will cause an error, and the except loop to execute.
		if (n!=int(n)):#then the number is a fractional number
			print "You entered a fraction!"
			n=int(n)#however we don't print/return an error, and instead we compute the prime number corresponding to the integer part.
		if (n<0):
			print "You entered a negative value!"
			n=0-n#instead of an error, we simply flip the sign, and find the corresponding prime.
		if (n==0):
			print "We count from 1. There is no prime that corresponds to 0.\nThe first prime number is 2"
			return 0#exit the function
	except:
		print "You entered a string!"
		return 0 #this is the return value we use for strings in this function.
	#this function finds the nth prime number.
	a=0 #we start counting from zero, and for each number we test if it is prime.
	c=0	#c stores the count of how many prime numbers we have found. Once c reaches n, we return the prime & stop.
	while (c<n):	#we didnt write c<=n because this condition would still hold even after the nth prime was found. Though c<=n is also fine, since we can always include a break in the if statement that checks if c==n.
		b=1	#b represents the number we divide a by, to test if a is prime. Since b has to start from 1 for every number b is outside the inner loop. b could have been after the loop too, but we have to initialise it first to use it.
		while (b<=a):	#we also need b to be equal to a, since a prime number is divisible by 1 or the number itself.
			if (a%b==0):
				if(b==1)or(b==a):	#then a is certainly prime.
					if (b!=1):		#we don't want to increase the count if it is only divisible by 1. And, if we are counting from zero, this saves us. Because in that case, it wont count 0 as a prime number, neither will it count 1, since in both cases the condition of the outer if statement is fulfilled.
						c=c+1			#since we found a prime number we need to count it.
						#print "The",c,"\bth Prime number is",a
				else:
					#the number a is divisible by a number other than 1 or itself. So, it is not prime, no point checking further. Break the loop.
					break
			b=b+1
			if (b>a/2)*(b!=(a+1)): #Quite simply we wait till b is equal to half of a, a%b s evaluated, and then b becomes a/2 + 1. We then immediately jump the value up to a. This value runs through the loop again, and again satisfies, b>a/2, but we don't want it getting assigned the value of a again, or else the loop will run infinitely (b is assigned a, runs, becomes a+1, a+1 is greater than a/2, b is assigned a again) to prevent it, we include the b!=(a+1) condition.. Since if b=a ran through the loop once, b is a+1 now, and we don't want a+1 passing the loop. [ If you're confused:: If the b=b+1 statement came after the if statement, and we set b=a, (we'd have to skip the b=b+1 statement), b=a would run through the loop and into the if statement, and we'd want to prevent b=a from passing the if statement, so we'd include a b!=a condition]
				b=a
			##point to learn is that, the if centers around choosing between b=b+1 and b=a basing on if b is more than half of a or not.
		if (c==n):
			print "The",int(n),"\bth prime number is",a
			return a #we return the nth prime number
			break #this statement is optional. If you remove it, and the condition of the outer while loop is c<n, then the loop wont execute another time. If the condition is c<=n, the loop will execute again and again until it finds the next prime number i.e the n+1th prime and will then quit.. though it will not print the n+1th prime.
		a=a+1 #this is to check for the next number.

def findprime2(n):
	#we use the isprime() function from above to find the nth prime number.
	try:
		n=float(n) #catches a string
		if (n!=int(n)):
			print "You entered a fraction!"
			n=int(n) #if n is a fraction, we assign it the integer part of the fraction.
		if (n<0):
			print "You entered a negative number"
			n=(0-n) #we flip the sign and assign it to n.
	except:
		print "You've entered a string!"
	#now that we have a numeric value of n, we proceed to find the nth prime number.
	a=1 #is prime doesn't like a zero. You could also start with a zero though.
	c=0 #to keep count of the number of primes we've calculated.
	while (c<n): #this means that the last value to go through will be the n-1, and when we find the nth prime, the loop prints the prime number and stops. If you put c<=n, the loop will still work, but it will keep going till it finds the n+1th number and stops.
		if (isprime(a)==1): #The print statements do not affect this. If you used return 0,1 or True,False , use the same here. But, if for a sequence of numbers you use isprime consider commenting out the print statements.
			c=c+1
		if(c==n):
			print "The",int(n),"th prime number is",a
			break #not essential here, but if you write c<=n it is required, or else the loop will only stop when it finds the n+1th prime number.
		a=a+1 #Don't forget this!
	#that's it.