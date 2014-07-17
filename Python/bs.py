#to find square root of x by binary search needed in MIT Problem Set 4
def squareroot(a,n,q):
	l=0
	h=a
	s=a/2	#s is our starting guess, between 0 & a
	i=0		#counts the iterations.
	q=10**(0-q)
	while True:
		print "Iteration",i,"Guess:",s,"s^n",s**n
		if(s**n<(a+q))&(s**n>(a-q)):
			print "Answer: ",(int(s/q))*q
			break
		elif(s**n>(a+q)):
			h=s
			s=(l+s)/2
		elif(s**n<(a+q)):
			l=s
			s=(h+s)/2
		i=i+1
	return "Done!"
print squareroot(float(raw_input()),int(raw_input()),float(raw_input("Accuracy in Digits after decimal point: ")))