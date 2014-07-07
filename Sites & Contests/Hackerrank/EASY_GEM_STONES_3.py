#Hackerrank: Gem Stones (Resubmission) v3.
#removed the isin function, replaced with the in command.
cs=None
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
		if (cs[a] in b)&(cs[a] not in ss):#if a character is already in the common characters string, don't add it.
			ss=ss+cs[a]
		a=a+1
	cs=ss
	ss=""
	M=M-1
print (len(cs))
#code returns error with N=0 To fix you should enclose while loop on line 14 with a n!=0 guard condition