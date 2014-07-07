#Hackerrank: Gen Stones (Resubmission)
def isin(a,b):
	i=0
	c=len(b)
	while(i<c):
		if (a==b[i]):
			return True
		i=i+1
	return False
cs=None
ss=" "
N=int(raw_input())
M=N
while(M>=0):
	if(M!=0):
		b=raw_input()
	if (M==N):
		cs=b
	if(M==0):
		b=cs
		cs="abcdefghijklmnopqrstuvwxyz"
	d=len(cs)
	a=0
	while (a<d):
		if isin(cs[a],b):
			ss=ss+cs[a]
		a=a+1
	cs=ss
	ss=" "
	M=M-1
print (len(cs)-1)
#code returns error with N=0 To fix you should enclose while loop on line 14 with a n!=0 guard condition