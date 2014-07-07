#Hackerrank: Gem Stones
def isin(a,b):
	#we know b[i] returns the i+1 th character in a string.
	i=0#to count index of character in b
	c=len(b)
	while(i<c):
		if (a==b[i]):
			return True
			#return 1
		i=i+1
	return False
	#return 0
cs="abcdefghijklmnopqrstuvwxyz"
ss=" "#We use ss to store common characters b/w cs and input string, then after comparision we shift it to cs
N=int(raw_input())
while(N>0):
	b=raw_input()
	d=len(cs)
	a=0
	while (a<d):
		if isin(cs[a],b):
			ss=ss+cs[a]
		a=a+1
	cs=ss
	ss=" "
	N=N-1
print (len(cs)-1)