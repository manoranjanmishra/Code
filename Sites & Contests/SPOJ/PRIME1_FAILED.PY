#SPOJ-Prime1
#Submitted - Failed. Exec.Time>6s
def isprime(a):
	t=1
	while(t<=a):
		if(a%t==0):
			if(t==1)or(t==a):
				if(t!=1):
					print a
			else:
				break
		t=t+1
		if(t>a/2)&(t!=(a+1)):
			t=a
T = int(raw_input())
i=1
while (i<=T):
	m,n = [int(x) for x in raw_input().split(' ')]
	c=m
	while(c<=n):
		isprime(c)
		c=c+1
	print "\r"
	i=i+1