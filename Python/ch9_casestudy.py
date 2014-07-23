#case study: all code is hardwired to use the words.txt file and may not be optimal
def avoids(a,b):
	#b: is the string of forbidden letters
	#a: is the word
	for i in b:
		if(a.find(i)!=-1):
			return False
	return True
#print avoids(raw_input(),raw_input())

def findletters(c):
	count=0
	tf=open("words.txt")
	for a in tf:
		a=a.strip()	#not essential because it doesn't affect the avoids function
		if avoids(a,c):
			count=count+1
	return count
#print findletters(raw_input())

def charstats():	#tells us how many words use a character.
	#we can run avoids on each letter of the alphabet and then compile a list of how many words dont have the alphabet, or based on that a percentage. Next, we sort the list from lowest to highest, and then add up the percentages of avoided words.
	abc="abcdefghijklmnopqrstuvwxyz"
	total=113809
	listl=[]
	for i in abc:
		avoid_i=findletters(i)
		contains_i=total-avoid_i
		ci_per=contains_i/total
		tuple_i=(contains_i,avoid_i,i)
		listl=listl+[tuple_i]
	#now we have the statistics of each letter.
	listl.sort()	#with this we have the character with the least number of words containing it.
	return listl

def excludesleast(n):	#n specifies how many characters to exclude.. like find how many words can be made at the most even when we avoid n characters
	stats=charstats()
	#print "Contains-Avoids-Character"
	#print stats	#at this point it should return q as the first element
	i=0
	chars=""
	total=113809
	number=0
	while(i<n):	#if one enters 5, qjxzw. And for 26, qjxzwvkfybhmpgucdlotnraise
		chars=chars+stats[i][2]	#this accesses the requisite tuple, and from it extracts the stored character and adds it to the list of stored characters
		i=i+1
	return chars
#s=int(raw_input())
#p=excludesleast(s)
#print "Atmost",findletters(p),"words dont contain %d characters: %s"%(s,p)

def uses_only(a,b):
	#a is the word, and b is the list of allowed letters
	for i in a:
		if(b.find(i)==-1):
			return False
	return True
#print uses_only(raw_input(),raw_input())

def uses_all(a,b):
	for i in b:
		if(a.find(i)==-1):
			return False
	return True
#print uses_all(raw_input(),raw_input())

def is_abecedarian(a):
	b=list(a)	#splits the word into a list of letters
	b.sort()
	i=0
	c=""
	d=""
	while(i<len(a)):	#forms a word from the now-sorted string of letters
		c=c+b[i]
		d=d+b[-(i+1)]
		i=i+1
	if(c==a)or(d==a):
		return True
	else:
		return False
#print is_abecedarian(raw_input())

def is_abecedarian2(a):	#without the use of lists
	ch="abcdefghijklmnopqrstuvwxyz"
	l=len(a)
	i=0
	while (i<(len(a)-1)):
		if(ch.find(a[i])<ch.find(a[i+1])):	#alphabetic order
			while(i<(len(a)-1)):
				if(ch.find(a[i])<=ch.find(a[i+1])):
					i=i+1
				else:
					return False
			return True
		if(ch.find(a[i])>ch.find(a[i+1])):	#reverse alphabetic order
			while(i<(len(a)-1)):
				if(ch.find(a[i])>=ch.find(a[i+1])):
					i=i+1
				else:
					return False
			return True
		if(ch.find(a[i])==ch.find(a[i+1])):
			i=i+1
	return True
#print is_abecedarian2(raw_input())

def cartalk1():
	tf=open("words.txt")
	wlist=[]
	for word in tf:
		word=word.strip()
		l=len(word)
		i=0
		while(i<(l-6)):
			if((word[i]==word[i+1])&(word[i+2]==word[i+3])&(word[i+4]==word[i+5])):
				wlist=wlist+[word]
			i=i+1
	return wlist
#print cartalk1()

def cartalk2():
	numl=range(100000,1000000)	#all six digit numbers
	rnum=[]
	for i in numl:
		n=i		#storing i in another number, so as to not affect i, maybe this is not necessary because i is not a index for the for loop
		a=str(n)
		b=a[-4:]	#last four digits
		if(b==b[::-1]):		#using string slicing to reverse a number
			#if we are here the last four digits are palindromic
			n=n+1
			a=str(n)
			b=a[-5:]
			if(b==b[::-1]):
				#then last five digits are palindromic
				n=n+1
				a=str(n)
				b=a[-5:-1]
				if(b==b[::-1]):
					#middle four are palindromic
					n=n+1
					a=str(n)
					if(a==a[::-1]):
						rnum=rnum+[(i,n)]
	return rnum
#print cartalk2()

def cartalk3():
	#what is the age difference between son & mom?