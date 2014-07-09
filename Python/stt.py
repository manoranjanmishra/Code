#write the code for the game of rotation
n=int(raw_input())
a=raw_input()
c=1
l=len(a)
max=None
min=None
while(c<=n):
	print "in while 0"
	m=c
	sum=0
	b=""
	i=0
	while (i<l):
		print "in while 1"
		while(i<l):
			print "in while 2"
			if(a[i]!=" "):
				b=b+a[i]
				i=i+1
				continue
			if(a[i]==" "):
				i=i+1
				break
		#now b contains a number,i points just after a blank space.
		b=float(b)
		sum=sum+b*m
		m=m+1
		if(m>n):
			m=1
		b=""
	if(sum>max)or(max==None):
		max=sum
	if(sum<min)or(min==None):
		min=sum
	c=c+1
print "Max: ",max
print "Min: ",min	