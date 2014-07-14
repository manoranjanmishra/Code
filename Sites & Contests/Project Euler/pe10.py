#Problem 10 - Project Euler
def problem10(n):
	c=0	#count the generated prime numbers
	i=1	#Start generating prime numbers from i
	sum=0
	while (i<n):
		i=i+1
		j=1
		while True:
			if(i%j==0)&(j!=1):
				break
			if(j>(i/j)):	#if no factors have been found yet, none will be found beyond now. This makes the function check for even lesser numbers.
				break
			j=j+1
		if(j>(i/j)):
			sum=sum+i
			c=c+1
	return sum
#print problem10(int(raw_input()))
#the correct answer is 142913828922. This program does it in 1:20s.