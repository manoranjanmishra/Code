#Problem 3: Largest Prime Factor: The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?
def problem3(n):
	#given a number n, this program tries to determine it's largest prime factor, using the fact that a number can at most be divisible by another that is half itself (or lesser). That is because the smallest factor of any number other than 1, is 2. If2 is not a factor, any other factor will be more than 2, and the corresponding factor will be less than half the number.
	while True:
		i=n/2
		while (i>0):
			if(n%i==0):
				break
			else:
				i=i-1
		if(i!=1):
			n=i
		else:
			i=n
			break
	return i
#while this does give the answer for 13195, it takes ~6000 evaluations to arrive at the answer: 29. And, for the test value: 6008514755143, it is too slow.
def problem3_v2(n):
	#the largest factor of a number other than itself can at best be half the number.
	while True:
		i=n/2
		while (i>0):
			if(n%i==0):
				break
			else:
				i=i-1
		if(i!=1):	#the additional while loop tries to check for factors starting from 1 upto n/2 and if found, the factor is divided & removed.
			n=i
			i=1
			while(i<=n/2):
				if(n%i==0):
					n=(n/i)
					break
				i=i+1
		else:
			i=n
			break
	return i	
#and modifying the function like this seems to have no benefit.
def problem3_v3(n):
	while True:
		i=n/2
		while (i>0):
			if(n%i==0)&(i!=1):
				n=i
				break
			if (n%((n/2)-i+1)==0)&(((n/2)-i+1)!=1):
				n=n/((n/2)-i+1)
				break
			i=i-1
		if(i==0):	#actually, n%i==0 for i=1 if n is prime, but then, i=i-1. So, the inner loop quits with a zero if n is prime. If it is not, then n is divisible by something. There are two tests, whichever yields the larger number is stored in n. n%i tests with larger numbers, so it should yield a larger i. But, n/2-i checks with smaller numbers, and hence the quotient yields the larger factor. Smaller the n/2-i, larger the factor.
			return n
def problem3_v4(n):
	while True:
		i=n/2
		while (i>0):
			if(n%i==0)&(i!=1):
				n=i
				break
			if (n%((n/2)-i+1)==0)&(((n/2)-i+1)!=1):
				n=n/((n/2)-i+1)
				break
			#the if statement below reduces computation in case we are checking for a prime number. It prevents double checking the same numbers. The reduction in time is noticeable for numbers with large prime factors.
			if(((n/2)-i+1)>i):#then there is no point double checking. As soon as the two streams( i.e (n/2)-i+1) & i) cross each other, we can stop (if we haven't already, and declare that our number is prime)
				i=0
				break
			i=i-1
		if(i==0):
			return n
print problem3_v4(int(raw_input()))
#The correct answer for 6008514755143 is 6857, and only v3 & v4 manages to find it. but even then, v3 takes >2.5hrs to find the prime factor for 60085147514345676 which is:10728049.
#armed with the extra if statement, v4 takes under 15 seconds to get the answer.
#587375025578562198297718910938239707254471237290013106178127520961352309631644955178500966891793997100526372324940868422271888065310848665509073304483846162673361601 is 13159 multiplied 40 times. v4 gets the answer in `5 secs. 13159 is a prime number.