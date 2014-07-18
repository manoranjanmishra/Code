#Iteratively solving the gcd problem
def gcdi(a,b):
	(a,b)=(max(a,b),min(a,b))	#tuple assignment
	while True:
		c=a%b	#b divides a
		if(c==0):
			return b
		a=b
		b=c
#Recursively solving the problem - function calls itself.
def gcdr(a,b):
	(a,b)=(max(a,b),min(a,b))
	if(b==0):	#since b is the smaller of the two, if even one is zero, it is b.#we'll be here, when one number divides the other. In that case, the pair we have is the smaller number, and the remainder. So, it makes sense to return that number itself.
		return a
	r=a%b	#r is smaller than b
	return gcdr(r,b)	#why is the return part necessary? It is because the

#print gcdr(int(raw_input()),int(raw_input()))