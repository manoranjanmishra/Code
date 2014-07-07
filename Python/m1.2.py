#this is MIT problem set 1 problem #2
#according to the question, the product of primes lesser than a number n, becomes very close to e**n as n becomes large. And, it becomes closer as n grows further.
#this means that if you take the log of both sides, the sum of the logarithms of all primes less than the number n, should be approximately equal to the number n itself.
#to test this, we need to find primes till we reach the number n, for each prime find the logarithm of that prime, and add the logarithm of each prime up. Continue this till we reach n. To check, one can then print the ratio of n to the sum of logarithms, and see how close the ratio is to 1.
from math import *
while True:
	try:
		n=float(raw_input("Compute Primes till: "))
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
#we have to set about finding all prime numbers till n.
test=1#we increment this number gradually and test to see if it is prime
count=0#We just want to see how many primes exist till the number n
cycles=0
sum_log=0.0 #we want the sum_log to be a float quantity, though 0.0 is not necessary
#we need two while loops, one to increment test, and the other to check if test is prime or not.
while (test<n): #to check if the test number is prime, only till test reaches n. SInce the next line increases test by 1, test<n ensures that the last number tested is n-1, and thus in all n numbers are tested.
	test=test+1
	div=1
	a=0 #no of factors.
	while (div<=test): 
		cycles=cycles+1
		if (test%div)==0:
			if (div==1)or(div==test):
				a=a+1
			else:
				break
		div=div+1
		if (div>=(test/2))*(div!=(test+1)): 
			div=test				
	if (a==2):
		count=count+1 #That's for us, we're counting how many primes exist till n
		sum_log=sum_log+log(test)#if the test number is prime we need to add it's logarithm to the sum of log of the previous primes.
	#now continue testing with the next number.
#once all primes are found.. we have sum_log and also n
ratio=sum_log/n #this is expected to be lesser than 1
print "There are",count,"primes lesser than",n
print "The sum of logarithms is",sum_log#you could use, (float(int(sum_log*100)))/100 to limit the number of decimal places to 2.
print "The ratio of the sum of the Logarithms of all primes less than N, to N is: ",ratio
print "That is different from 1 by approximately",int(100-ratio*100),"\b%"