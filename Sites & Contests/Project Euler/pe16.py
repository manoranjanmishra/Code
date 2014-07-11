#Problem 16 - Project Euler
def problem16(n):
	a=2**n
	b="%d"%(a)
	l=len(b)
	i=0
	s=0
	while(i<l):
		s=s+int(b[i])
		i=i+1
	return s
print problem16(int(raw_input()))
#the answer for 2**1000 is 1366