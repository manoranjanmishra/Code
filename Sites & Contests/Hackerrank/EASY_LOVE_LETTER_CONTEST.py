#Hackerrank: Love Letter Mystery
def char2int(a):
	b="abcdefghijklmnopqrstuvwxyz"
	return b.find(a)

def topalindrome(a):
	l=len(a)
	i=0
	o=0 #operations needed.
	while(i<l/2): #if you go up to l and then reduce o to half that is correct, but you only need to go halfway.
		n=((char2int(a[i]))-(char2int(a[-(i+1)])))
		if (n<0):
			n=0-n
		o=o+n
		i=i+1
	#reduce o to half, since we are spanning the entire string.
	return o

t=int(raw_input())
while (t>0):
	print topalindrome(raw_input())
	t=t-1