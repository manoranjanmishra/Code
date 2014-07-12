#A Program inspired by Project Euler Problem 3
#This program finds out the prime factors of a number, and lists them in descending order as they are found.
#Idea: A number is divisible at best by a factor that is equal to or lesser than half itself.
def primefactor(a):
	while(a!=1):
		n=a	#storing a in a temp variable, which will get reduced to the largest prime factor. We then divide a by this factor & continue until a=1, when we stop.
		#find the largest prime factor of a.
		while True:
			i=n/2
			while(i>0):
				if(n%i==0):
					if(i!=1):
						n=i
					break
				if((n%((n/2)-i+1))==0):
					if(((n/2)-i+1)!=1):
						n=n/((n/2)-i+1)
						break
				if(i<((n/2)-i+1)):
					i=1	#if you're manually breaking the loop because you think it is a prime number, set i to 1.. because that is our flag for a prime number. Without that i simply stays at 2i=n/2+1 and keeps repeating.
					break
				i=i-1
			#if i is equal to 1, then n is a prime number
			if(i==1):
				a=a/n
				print n
				break
	#if control reaches here, a=1 and there are no factors left.
	return 1
def primefactor_v2(n):
	#the above program discards factors already evaluated and factored out, and re-evaluates them. This takes more time. To save time, we print factors as they are factored out, since i believer that these numbers are prime numbers. In fact, i think: "The smaller a factor is, the more the chance it is prime"
	while True:
		i=n/2
		while (i>0):
			if(n%i==0):
				if(i!=1):
					print n/i
					n=i
				break
			if((n%(((n/2)-i)+1))==0):
				if ((((n/2)-i)+1)!=1):
					print (((n/2)-i)+1)
					n=n/(((n/2)-i)+1)
					break
			if(i<(((n/2)-i)+1)):
				i=1
				break
			i=i-1
		if(i==1):#then we have a prime number
			return n	#since we have factored out every possible factor, this should be a prime number
#A major difference between primefactor & primefactor_v2 is that, in primefactor the largest prime factor is evaluated by factoring out all smaller factors, and then this information is discarded: The number is then divided by the largest prime factor just found, and then process repeated on the remaining number. v2 however realises that all the numbers being factored out are also factors, and should be listed. Moreover, I've said that such factors are all prime. I need a proof of that.
#print primefactor_v2(int(raw_input()))