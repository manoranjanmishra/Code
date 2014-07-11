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
#while True:
#	print ishashad(int(raw_input()))#for testing purpose uncomment these lines