#problem-1
def ishashad(n):
	#an integer div by the sum of it's digits is a hashad number
	a="%d"%(n)
	l=len(a)
	i=0
	s=0
	while (i<l):
		s=s+int(a[i])
		i=i+1
	if((n%s)==0):
		return True
	else:
		return False
def findhashad(n):
	#given an upper limit n, the function determines all hashad numbers upto n, and also counts them.
	c=0
	i=1
	while(i<=n):
		if ishashad(i)==True:
			print i,"\t",
			c=c+1
		i=i+1
	print "\nThere are",c,"Hashad numbers upto",n,"starting from 1"
#while True:
#	print ishashad(int(raw_input()))#for testing purpose uncomment these lines
#findhashad(int(raw_input()))