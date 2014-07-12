#Problem 4 - Project Euler
#The largest number which is a product of three digit numbers & is a palindrome:
def problem4(n):
	#input a value of n, the program tries to find the largest palindrome which is a product of numbers lesser than n.
	i=n-1
	max=0	#we dont expect negative numbers here, so max can be 0
	#max_i=0
	#max_j=0
	while(i>0):
		j=i
		while(j>0):
			p=i*j
			s_p="%d"%(p)
			l=len(s_p)
			k=0 #index of the string s_p
			while(k<l/2):
				if(s_p[k]!=s_p[l-k-1]):
					k=0		#we've used k as the signal itself. If a number is a palindrome, k will be l/2-1 & not zero. So, by setting k=0 in case a match fails, we ensure that after the check either k is 0 or l/2-1
					break	#check no further.
				k=k+1
			if(k!=0)&(p>max):
				max=p
				#max_i=i
				#max_j=j
			j=j-1
		i=i-1
	#return "%d is a product of %d & %d"%(max,max_i,max_j)
print problem4(int(raw_input()))
#906609 is the answer. It is a product of 993 & 913. If you uncomment the lines you can also see the factors of the numbers.