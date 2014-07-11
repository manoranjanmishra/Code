#Problem 6 - Project Euler
def problem6(n):
	i=1
	s_sq=0
	s=0
	while(i<=n):
		s=s+i
		s_sq=s_sq+i*i
		i=i+1
	sq_s=s*s
	return (sq_s-s_sq)
def problem6_v2(n):
	s_sq=(n*(n+1)*((2*n)+1))/6
	sq_s=((n*(n+1))/2)**2
	return (sq_s-s_sq)
#print problem6(int(raw_input()))