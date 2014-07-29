def bisearchi(key,alist):
	h=len(alist)
	l=0
	while True:
		a=(l+h)/2
		if(alist[a]==key):
			return True
		elif((h-l)==1):	#then there is only one character between l & h, and if that is not the key we are looking for, it is not there in the list.
			return False
		elif(alist[a]>key):
			h=a
		elif(alist[a]<key):
			l=a
def bisearchr(key,alist):
	l=0
	h=len(alist)
	a=(l+h)/2
	if(h==0):	#it is important that this condition come first, since, we are slicing out parts of alist as we hand it down to other functions recursively, and eventually it ends up being an empty list.. and a=0 for that list. since it has no elements alist[0] causes an error & instead of going to the next if statement the program fails. So, check for empty list first.
		return False
	elif(alist[a]==key):
		return True
	elif(alist[a]>key):
		return bisearchr(key, alist[:a])
	elif(alist[a]<key):
		return bisearchr(key, alist[a+1:])