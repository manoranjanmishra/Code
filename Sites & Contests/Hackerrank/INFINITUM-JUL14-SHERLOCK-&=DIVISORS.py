#Hackerrank: Sherlock & Divisors
#number of divisors divisible by2. Submission Failed. Timeout.
def check(n):
	i=1
	c=0
	while((2*i)<=(n/2)):
		if(n%(2*i)==0):
			c=c+1
		if(((n/2)-i)%2==0):
			if ((n%((n/2)-i))==0):
				c=c+1
		if((i)>((n/2)-i)):
			break
		i=i+1
	return c
def check_v2(n):
	if(n%2!=0):	#if a number is not divisible by 2 at the start, then 2 is not a factor, so there are no divisors of the number that are divisible by 2. No point checking further.
		return 0
	#prime factorise a number. A number with n different prime-factors has 2**n divisors. Since, in a divisor, each factor may either occur or not occur and thus for each occurrence of a unique prime factor the number of divisors becomes double. If a factor occurs twice, there are 3 possibilities: the factor doesnt occur, it occurs once, it occurs twice.. For n occurences the number of divisors becomes n+1 times.
	c_2=1	#Counts how many factors are 2, and since it starts with 1, c_2 is one more than the number of 2s present.
	l_f=1	#Stores the last found prime factor.
	l_fc=1	#Counts how many times a specific factor has occured + 1.
	n_d=1	#number of divisors other than 2.
	while(n!=1):
		i=n/2
		while(i>0):
			if(n%i==0):
				if(i!=1):
					if(n/i==2):
						c_2=c_2+1
					else:
						if(n/i==l_f):
							l_fc=l_fc+1
						else:
							l_f=n/i
							n_d=n_d*l_fc
							l_fc=2
					n=i
				break
			if(n%((n/2)-i+1)==0):
				if(((n/2)-i+1)!=1):
					if(((n/2)-i+1)==2):
						c_2=c_2+1
					else:
						if(((n/2)-i+1)==l_f):
							l_fc=l_fc+1
						else:
							l_f=((n/2)-i+1)
							n_d=n_d*l_fc
							l_fc=2
					n=n/((n/2)-i+1)
					break
			if(i<((n/2)-i+1)):
				i=1
				break
			i=i-1
		if(i==1):
			#print n,c_2,n_d
			if(n==2):
				c_2=c_2+1
			else:
				if(n==l_f):
					l_fc=l_fc+1
				else:
					n_d=n_d*l_fc
					l_fc=2
			break
	n_d=n_d*l_fc
	return(n_d*c_2-n_d)
t=int(raw_input())
while(t>0):
	print check_v2(int(raw_input()))
	t=t-1