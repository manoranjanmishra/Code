#46 Simple Python Excercises:
#Started on Fri, July 11 2014.

#Q-1
def num_max(a,b):
	#a, b are arguments of the function
	if(a>b):
		return a
	else:
		return b
#print num_max((float(raw_input())),(float(raw_input())))

#Q-2
def max_of_three(a,b,c):
	#a,b,c are the three arguments to this function
	max=a
	if(b>max):
		max=b
	if(c>max):
		max=c
	return max
def max_of_three_2(a,b,c):
	if(a>b)&(a>c):
		return a
	if(b>a)&(b>c):
		return b
	if(c>a)&(c>b):
		return c
def max_of_three_3(a,b,c):
	max=None
	if(a>b):
		max=a
	else:
		max=b
	if(c>max):
		max=c
	return max
#print max_of_three((float(raw_input())),(float(raw_input())),(float(raw_input())))

#Q-3
def length(a):
	#a is a string, this function finds it's length
	i=0	#i is our index variable
	try:
		while True:
			a[i]	#try accessing the string at index i. If there is no character, then this will trigger an error and the except block will be executed.
			i=i+1	#if there is a character, count it.
	except:
		return i
def length_2(a):
	i=0
	for char in a:	#though i've written it here, I don't understand the for statement.
		i=i+1
	return i
#print length_2(raw_input())

#Q-4
def is_vowel(a):
	#the length of a is specified to be 1. So, if it's longer, or lesser we'll print an appropriate error.
	if(a==""):
		print "The entered string was empty"
	elif(len(a)>1):
		print "You can only input a character"
	elif(a!=" "):	#the !=" " is a fix for using the function in the next question
		if(a=="a")or(a=="e")or(a=="i")or(a=="o")or(a=="u"):
			#return "Vowel"
			#return "\n%s is a Vowel"%(a)	#we've used a format character to insert the input character itself. You may use whichever return statement suits you.
			return True
		else:
			#return "Consonant"
			#return "\n%s is a Consonant"%(a)
			return False
#print is_vowel(raw_input())

#Q-5
def translate(a):
	#Robber's Language translator. Double each consonant, and put an o in between
	l=len(a)
	i=0
	ts=""	#ts stores our translated string
	while(i<l):
		if (is_vowel(a[i])==False):
			ts=ts+a[i]+"o"+a[i]
		else:
			ts=ts+a[i]
		i=i+1
	return "%s in Robber's Language is %s"%(a,ts)
#print translate(raw_input())

#Q-6
#! haven't studied lists yet.

#Q-7
def reverse(a):
	l=len(a)
	i=1
	rl=""	#this is the reverse string we'll be generating
	while (i<=l):
		rl=rl+a[-i]
		i=i+1
	return rl
def reverse_2(a):
	l=len(a)
	i=0
	rl=""
	while(i<l):
		rl=a[i]+rl
		i=i+1
	return rl
def reverse_3(a):
	l=len(a)
	i=0
	rl=""
	while(i<l):
		rl=rl+a[l-(i+1)]
		i=i+1
	return rl
#print reverse(raw_input())

#Q-8
def is_palindrome(a):
	if(a==reverse(a)):
		return "%s is a Palindrome"%(a)
		#return False
	else:
		return "%s is not a Palindrome"%(a)
def is_palindrome2(a):
	l=len(a)
	i=0
	while (i<l/2):
		if(a[i]==a[l-(i+1)]):
			i=i+1
		else:
			return "%s is not a Palindrome"%(a)	#since return returns a result and stops evaluation immediately, we don't need to use a break statement.
	return "%s is a Palindrome"%(a)
#print is_palindrome(raw_input())
