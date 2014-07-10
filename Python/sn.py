#An alternate way to sniff numbers using slice
#The sniff nums function fails if you pass it a number with a decimal part.
#These functions try to fix that in different ways. The easiest way is sniffnums*
#Each function has a statement that prints the number sniffed from the string. If you want the numbers on the same line, then put a comma at the end. Else remove it.
def sniffnums2(a): #Rewriting the same function as sniffnums, but using slice & int to convert from string to number.
	l=len(a)
	i=0
	c=0
	while (i<l):
		try:
			int(a[i])#check if a[i] is a number
			p=i+1 #Next, starting from the next index, start a search till you reach a character that is not a number. If you set p=i that is allright. In sniffnums, we assigned a[i] to n, and wanted to add subsequent numbers, so we shifted the search index to the next num. We could've instead not done that: i.e check if a[i] is an integer, if it is, assign 0 to the variable n then start a search at i itself, and as we go forward, n=n*10 + int(a[i]) adds digits after n. 'n' is the number we're creating by reading consequent digits out of the string. Once we count & print it (or do other operations on it) we then discard it- (anyway once a non-digit is found, control shifts out of the inner loop to the outer one, and when again a digit is found n is initialised to 0. Though in sniffnums.. since we've initialised n outside the first while loop itself, we re-set it to none.)
			while True:
				try:
					int(a[p])
					p=p+1 #if it's a number, go to the next character.
				except:
					#if the next character is not a number, break the loop. Now p points to the index of the character after the number (which is not a number).
					break
			#the value of i still points to where we found our first digit. Using i & p, take a slice of the string. Since we are here, a[p] is not a number, and so we can put the digits we've found, together & call it a number.
			n=int(a[i:p])
			if (c==0):
				print "The numbers in the entered string are: "
			print n
			c=c+1
			i=p#Start off again from where the inner loop left it.
		except:
			i=i+1#increment i, so that as the loop starts again, it looks at the next character. If you don't do this, and the next number is a character, the loop cycles endlessly.. since there is nothing to advance i. When you do it, and the next number is a character, the value of i simply skips forward, and then the next character is tried.
	if (c!=0):
		print "\nThe entered string had",c,"numbers"
	if (c==0):
		print "The entered string had no numbers in it"
def sniffnums3(a): #fixing the problem we had with decimal points.
	#One dot is not a cause of worry. Two are. So, we initiate a counter when we find our first dot, and then count till we find the next one. Then we stop & from there start looking again
	l=len(a)
	i=0
	c=0
	while (i<l):
		d=0 #Each time a number is found, the count of dots has no meaning, if we terminated the search on a second dot, we're starting it with that same dot & counting it.
		try:
			if (a[i]!="."):
				int(a[i])	#Skipped if a[i] is a dot. So, now we have both numbers and dots.
			else:
				d=d+1	#d is our counter for dots. We increase it when we find a dot.
			p=i+1
			while True:
				try:
					if(a[p]!="."):
						int(a[p])
					else:
						d=d+1
					if(d==2):
						break
					p=p+1
				except:
						break
			#now p points to either a character or a dot, and between p & i there are integers and at-most one dot.
			if(p!=(i+1))or(d==0):#if(p==(i+1)), then probably there were two consecutive dots.. or there is a single digit number. If its a single digit number, then d=0
				n=float(a[i:p])
				if (c==0):
					print "The numbers in the entered string are: "
				c=c+1
				print n #if you want integers to look like integers, the you could use d to see if a[i:p] is an integer or floating point. d==0:integer, d==1:Fraction
			i=p #if a[i:p] is just a dot, ignore it. And, keep looking.
		except:
			i=i+1
	if (c!=0):
		print "\nThe entered string had",c,"numbers"
	if (c==0):
		print "The entered string had no numbers in it"
def sniffnums4(a):#We've only fixed a little bit in the program above, by letting in + & - signs initially too.
	l=len(a)
	i=0
	c=0
	while (i<l):
		d=0#our counter for .
		try:
			if(a[i]!=".")&(a[i]!="+")&(a[i]!="-"):#Allow a plus or minus sign at the start. After that in the subsequent search, don't allow any sign, except for dots. Actually this code was written with a lot of extra if statements. Turns out, if you let a sign in at a later stage, it creates a mess, which no number of if-statement-filtrations can fix.
				int(a[i])
			else:
				if(a[i]=="."):
					d=d+1
			p=i+1	#right now, we either have a dot, plus, minus or a number at the i position. If the counter for *any* of those symbols becomes 2, we stop searching further.
			while True:
				try:
					if(a[p]!="."):
						int(a[p])
					else:
						if(a[p]=="."):
							d=d+1
					if(d==2):
						break
					p=p+1
				except:
					break
			#now between p & i there is a string consisting of at most 1 dot & one sign. Moreover, the sign comes before the dot.
			n=float(a[i:p])
			if(c==0):
				print "The numbers in the entered string are: "
			c=c+1
			print n
			i=p
		except:
			i=i+1
	if (c!=0):
		print "\nThe entered string had",c,"numbers"
	if (c==0):
		print "The entered string had no numbers in it"
def sniffnums5(a):#this is intended to be a basic function that respects decimal points. We won't be using slicing here.However, this program doesn't understand signs.
	l=len(a)
	i=0
	c=0
	while(i<l):
		c_d=0
		exd=0	#after we've crossed a decimal point , exd tells us how many digits we have crossed after the decimal point.
		n=None
		try:
			if(a[i]!="."):
				n=int(a[i])
			else:
				if(a[i]=="."):
					c_d=c_d+1
			p=i+1
			while True:
				try:
					if(a[p]!="."):
						int(a[p])
						if(c_d==1):
							if(p==(i+1)):
								n=0	#if we encounter a dot at the beginning of a number then set n to zero to avoid errors with the next statement. Or else, since n is initialised to None, we get a adding None with Integer error. However the initialisation is done only if the character after the dot is a number. If we encounter a dot within a number, the n=0 wont be executed since p!=i+1 in that case.
							exd=exd+1
							n=n+((int(a[p]))*(10**(0-exd)))
						else:
							n=n*10+int(a[p])
					else:
						c_d=c_d+1
					if(c_d==2):
						break
					p=p+1
				except:
					break
			#we now have a number stored in n and p points to a character.
			if(n!=None):
				if(c==0):
					print "The numbers in the entered string are: "
				print n
				c=c+1
			i=p
		except:
			i=i+1
	if (c!=0):
		print "\nThe entered string had",c,"numbers"
	if (c==0):
		print "The entered string had no numbers in it"