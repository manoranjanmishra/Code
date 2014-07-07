#Hackerrank: Manasa and Stones: https://www.hackerrank.com/challenges/manasa-and-stones
#Submission Passed. Be careful with the output. Learn to print on same line..  (to do!)
t=int(raw_input())
while (t>0):
	n=int(raw_input())
	l=n-1
	a=int(raw_input())
	b=int(raw_input())
	while (l>=0)&(a!=b):
		if (a<b)&(l!=0):
			print((a*l)+(b*((n-1)-l))),
		if (b<a)&(l!=0):
			print((b*l)+(a*((n-1)-l))),
		if(l==0):
			if(a<=b):
				print b*(n-1)
			if(a>=b):
				print a*(n-1)
		
		l=l-1
	if(a==b):
			print a*(n-1)
	t=t-1