#Problem 1 : Project Euler.
def problem1(n):
	#this program prints the sum of all numbers divisible by either 3, or 5 from 1 till n. You input n.
	sum=0
	i=1
	while(i<n):
		if((i%3==0)or(i%5==0)):
			sum=sum+i
		i=i+1
	return sum
print problem1(int(raw_input()))
#Correct Answer: 233168