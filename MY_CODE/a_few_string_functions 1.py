#A few string functions
def sepwords(a):
	l=len(a)
	i=0 #index of the string.
	#basic
	s=" "
	c=0#count of words.
	print "The words in the string are:"
	while (i<l):
		if(a[i]!=" "):
			s=s+a[i]
		if(a[i]==" ")or(i==(l-1)):
			if (s!=" "):
				c=c+1
				print s[1:]
			s=" "
		i=i+1
	print "The string has",c,"words"
def sepnums(a):#Extract numbers from a space separated list of numbers entered as a line
	l=len(a)
	i=0
	b=""
	c=0
	while (i<l):
		if(a[i]!=" "):
			b=b+a[i]
		if(a[i]==" ")or(i==(l-1)):#maybe we have a word, so check if b has changed. If yes, operate on it.
			if(b!=""):#then it has changed
				try:
					b=float(b)
					#b=int(b)#change b into a number. But to be safe, first b=float(b) & then b= int(b), that takes care of all the dots.
					print b
					c=c+1
				except: 	#<--To Learn from here: Try commenting out the pass statement below first, and run the code. Then, comment the except statement too. ... The error is because the try statement needs an except statement with it, even if te except statement does nothing.. like it does here.
					#print "Not a number"
					pass
			b=""#reset b
		i=i+1
	print "The number of numbers in the entered string is",c
def sniffnums(a):
	l=len(a)#if there are continuous digits in a string print them as a number. Else print out the digits. Count how many numbers are present
	i=0
	c=0#count numbers
	while (i<l):
		n=None
		try:
			n=int(a[i]) #this will check if a[i] is an integer or not.
			p=i+1#storing the index we found a number to start a search
			while True:
				try:#Once we find a number, we look ahead around it, if we find another number we continue looking ahead, untill we dont find a number. Then we quit, leaving the search at the position we left.
					n=n*10+(int(a[p]))#add next digit if present to end of existing n
					p=p+1
				except:
					i=p#since a[i] is not a number, we can resume searching from here again
					break#if the next digit is a letter, stop and exit loop.
			if (n!=None):#then we've found a number.
				print "The numbers in the entered string are: "*(c==0) #Since we included the statement here, it will only print when a number is found, and with the c==0 condition, it will print only the first time a number is found
				c=c+1
				print n
				n=None
		except:
			i=i+1
			continue
			#if it is not an integer, we're not interested. Go on looking further.
	print "The entered string had",c,"numbers."
def searchin(a,b):#searches for the shorter string in the longer one. We use string slices in this function
	l_a=len(a)
	l_b=len(b)
	i=0
	c=0
	if(a=="")or(b==""):
		print "Empty Search Phrase"
	elif(l_a>l_b):
		#then search for b in a
		while(i<l_a):#while(i<=(l_a-l_b)): If we are nearing the end of the string, then there are not many characters left to compare b, in that case we stop checking. Normally, this while loop would have read, while i<l_a, but we also want it to stop when there are less characters left than the length of b. Shouldn't there be a -1 too? Yes, but we count from 0, and we stop as and when it reaches l_a-l_b so, no minus 1  
			if (b==a[i:(i+l_b)]):
				if(c==0):
					print "Found the string\"",b,"\"at position",i+1,
				else:
					print i+1,
				c=c+1
			i=i+1
	elif(l_b>l_a):#while(i<=(l_b-l_a)):
		#then search for a in b
		while(i<l_b):
			if (a==b[i:(i+l_a)]):
				if(c==0):
					print "Found the string\"",b,"\"at position",i+1,
				else:
					print i+1,
				c=c+1
			i=i+1
	elif(l_a==l_b):
		if(a==b):
			print "String",a,"is same as String",b
			#return "same"
		else:
			print "String\"",a,"\"and String \"",b,"\" are different"
	if(a!="")&(b!="")&(l_a!=l_b):	
		print "\nFound",c,"instances in total"
def searchin2(a,b):#this is the same function as above except that we use a while loop to compare the strings
#first determine shorter string, then search shorter in longer string. If strings are of same length, use == instead of wasting time. If strings are empty, print that strings are empty
	l_a=len(a)
	l_b=len(b)
	c=0#counter
	if(a=="")or(b==""):#if any of the two strings to compare are empty, no point checking anything
		print "Empty Search Phrase"
	elif (l_a>l_b):
		#inside a look for b
		i=0
		#start at 0, but go till there are enough characters left for b
		while (i<l_a):#while(i<=(l_a-l_b)):
			i_b=0
			is_e=0
			while (i_b<l_b):#while(i<=(l_b-l_a)):
				if (b[i_b]==a[(i+i_b)]):
					is_e=1
				else:
					is_e=0
					break
				i_b=i_b+1
			if(is_e==1):#then strings are equal
				if(c==0):#print the following line only once for the string b
					print "Found an instance of the string\"",b,"\"at position:",
				print i+1,
				c=c+1
			i=i+1
	elif (l_b>l_a):
		#search for a in b
		i=0
		c=0#counter
		while(i<l_b):
			i_a=0
			is_e=0
			while(i_a<l_a):
				if(a[i_a]==b[(i+i_a)]):
					is_e=1
				else:
					is_e=0
					break
				i_a=i_a+1
			if(is_e!=1):
				if(c==0):
					#print the starting statement
					print "Found an instance of the string \"",a,"\" at position: ",
				print i+1,
				c=c+1
			i=i+1
	elif(l_a==l_b):#strings are of equal length, don't waste time comparing them.
		if (a==b):
			print "String \"",a,"\" is the same as string \"",b,"\""
		else:
			print "String \"",a,"\" is not the same as string \"",b,"\""
	if(l_a!=l_b)&(a!="")&(b!=""): #Don't print if length of a is same as b, or any of a & b are empty strings
		print "\nFound",c,"instances in total" #the \n is to shift to a new line, because our found instances statements end with a comma.
