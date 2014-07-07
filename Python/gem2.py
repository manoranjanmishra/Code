#Hackerrank: Gem Stones (Resubmission) v4.
def isin(a,b):
	i=0
	c=len(b)
	while(i<c):
		if (a==b[i]):
			return True
		i=i+1
	return False
cs=""
ss=""
N=int(raw_input())
M=N
while(M>0):
	if(M!=0):
		b=raw_input()
	if (M==N):
		cs=b
	d=len(cs)
	a=0
	while (a<d):
		if isin(cs[a],b)& (not isin(cs[a],ss)):#You need to put brackets around the not isin
			ss=ss+cs[a]
		a=a+1
	cs=ss
	ss=""
	M=M-1
print (len(cs))#since ss is am empty string, the length of cs is the same as ss, see cs=ss above.
#code returns error with N=0 To fix you should initialise cs="" not cs=None