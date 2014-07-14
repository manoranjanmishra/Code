#Hackerrank - Maximising XOR
def dec2bin(a):
	s=""
	while(a>0):
		s="%d"%(a%2)+s
		a=a/2
	return s
def findxor(a,b):
	l_a=len(a)
	l_b=len(b)
	s_xor=""#stores xor of a & b
	if(l_a>l_b):
		b="0"*(l_a-l_b)+b
	else:
		a="0"*(l_b-l_a)+a
	#now l_a==l_b
	i=0#index
	while(i<l_a):
		if(a[i]!=b[i]):
			s_xor=s_xor+"1"
		else:
			s_xor=s_xor+"0"
		i=i+1
	return s_xor
def bin2dec(a):
	#a is a string, which is convenient to our program
	#function returns an integer however.
	l=len(a)
	d=0#stores the decimal equivalent
	i=0#index
	while(i<l):
		d=d+((int(a[-(i+1)]))*2**i)
		i=i+1
	return d
l=int(raw_input())
r=int(raw_input())
a=l
max=0
while(a<=r):
	b=l
	while(b<a):
		c=bin2dec(findxor(dec2bin(a),dec2bin(b)))
		if(c>max):
			max=c
		b=b+1
	a=a+1
print max