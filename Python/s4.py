#Hackerrank: Sherlock & The Beast
#Submission
t=int(raw_input())
while(t>0):
	n=int(raw_input())
	l=n
	a=0
	if(l!=0):
		while(l>=0):
			if(l%3==0)&((n-l)%5==0):
				print "5"*l+"3"*(n-l)
				a=a+1
				break
			l=l-1
	if(a==0):
		print "-1"
	t=t-1
