#searching in strings. MIT Prob Set 3, Course Assignments
#from string import *	#or we can use the dot to use functions linked to a string.
def countSubStringMatch(target,key):
	i=0	#index of the string
	c=0	#count the number of occurrences
	a=[]#store the list of all occurrences of key in target.
	while (i<len(target)):
		i=target.find(key,i)
		if(i==-1):#there are no more occurrences, so stop searching
			break
		a.append(i)	#logically all of this belongs to an else block of the if statement above
		c=c+1		#but, since the if statement blocks control if it is true, all the statements below it automatically form the else block if the if statement is false.
		i=i+1
	if(c==0):
		s="Found no occurrences of %s in %s"%(key,target)
	else:
		#s="Found %d occurrences of %s in %s at:"%(c,key,target),a	#if you write this the return statement returns a set of values in parenthesis because, we are returning it a list and a string as s. But, if you write the statement below, we are inserting the list into the string s in the process of forming it, and as a result we are returning just a string.
		s="Found %d occurrences of %s in %s at:%r"%(c,key,target,a)
	return s
#print countSubStringMatch(raw_input(),raw_input())
def countSubStringMatchRecursive(target, key):
	a=[]	#store the list of indexes where the key was found.
	while True:
		i=target.find(key)
		if(i==-1):
			break
		a.append(i)
		target=target[i+1:]	#reduce the size of the target string.
	if(len(a)==0):
		s="Found no occurrences of %s in %s"%(key,target)
	else:
		s="Found %d occurrences of %s in %s at:%r"%(len(a),key,target,a)
	return s
#print countSubStringMatchRecursive(raw_input(),raw_input())

#Problem 2 of Problem Set 3, Course Assignment MIT 6_00
#tuples cannot be changed, but one can use concatenation with the a=a+b assignment to add elements to a tuple. Or, the tuple function can convert a list to a tuple, so one can first create a list & convert it to a tuple
def subStringMatchExact(target,key):
	a=()	#empty tuple to store the list of occurences
	#a=[]	#if you define a list, then activate the corresponding statements below. You must thus comment out all those statements that are for tuples.
	i=0
	while (i<len(target)):	#just for the record, this is an iterative loop. Because we are operating on the same thing over & over again. In my understanding a recursive loop operates on the results of the previous loop cycles.
		i=target.find(key,i)
		if(i==-1):	#the key doesn't exist in target, so dont check further & break this loop
			break
		a=a+(i,)	#concaenates the index to the tuple a
		#a.append(i)	#if you define a list & decide to convert it into a tuple
		i=i+1	#since we have a match, we want to continue checking after the indexwe found the match, so that the now-found-match isnt reported again
	#a=tuple(a)	#converts a which is a list, into a tuple.
	if(len(a)!=0):
		return a
	else:
		#return -1	#find returns a -1 incase the key isnt found inside the target.
		return a	#however returning an empty tuple will avoid any problems with tuple operations in later functions/problems.
#print subStringMatchExact(raw_input(),raw_input())

#Problem 3 of Problem Set 3 - MIT Course Assignment 6_00
#to find all matches even with one substitution.
#using the logic given in the problem sheet itself.
def constrainedMatchPair(firstMatch,secondMatch,length):
	#this function return a tuple of indexes in firstMatch for which the secondMatch forms a valid pair given the length of key1
	matches=() #empty tuple to store the valid matches
	a=0
	while(a<len(firstMatch)):
		b=0
		while(b<len(secondMatch)):
			if((secondMatch[b]-firstMatch[a]-length)==1):
				matches=matches+(firstMatch[a],)
			b=b+1
		a=a+1
	return matches

def matchButOne(target,key):
	target=target+" "	#this adds an empty character at the end of the string, so that if the first key matches at the end of the string, i.e the key matches with the end of the string with one substitution it can be reported
	#takes a target & a key & returns a tuple of all matches, or matches with exactly one substitution
	i=0
	match=()	#empty tuple to store the valid matches
	while(i<len(key)):
		#create two parts of the string that leave out the element whose substitution we allow.
		key1=key[:i]	#this would create a slice of the string with the i-th element not included in it.
		key2=key[i+1:]	#this would create a string with the i-th element ignored because it starts with the i+10th element in it
		#print "match for",key1,key2,"at",constrainedMatchPair(subStringMatchExact(target,key1),subStringMatchExact(target,key2),len(key1)) #shows matches are they are found & added to the matches tuple
		match=match+constrainedMatchPair(subStringMatchExact(target,key1),subStringMatchExact(target,key2),len(key1))
		i=i+1
	return match

def subStringMatchExactlyOneSub(target, key):
	target=target+" "	#this adds an empty character at the end of the string, so that if the first key matches at the end of the string, i.e the key matches with the end of the string with one substitution it can be reported
	all=matchButOne(target,key)
	exact=subStringMatchExact(target,key)
	#print all, exact	#you can use this to see what all matches, and the exact matches look like. Helps in checking if something is wrong.
	all=list(all)
	exact=list(exact)
	i=0
	while(i<len(exact)):	#these are two nested loops that browse through one and remove all the elements in the other that match this one.
		if(exact[i] in all):
			p=0
			while (p<len(all)):
				if(all[p]==exact[i]):
					del all[p]
				else:
					p=p+1
		i=i+1
	all.sort()
	all=tuple(all)
	return all
#print matchButOne(raw_input(),raw_input())
print subStringMatchExactlyOneSub(raw_input(),raw_input())
#Two modifications are made to the answers required by the problem sheet.. 
#1. The subStringMatchExact returns an empty tuple instead of -1
#2. The final function that prints the tuple of all indexes where the key is found adds an empty space at the end of the string-target