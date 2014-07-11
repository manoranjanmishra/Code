#Problem 20 - Project Euler
def problem20(n):
	f_n=1
	while (n>0):
		f_n=f_n*n
		n=n-1
	s_f_n="%d"%(f_n)
	l=len(s_f_n)
	s=0
	i=0
	while(i<l):
		s=s+int(s_f_n[i])
		i=i+1
	return s
print problem20(int(raw_input()))
#The correct answer is 648 for 100!