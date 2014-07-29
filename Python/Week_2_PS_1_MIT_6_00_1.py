#Problem Set 1: https://courses.edx.org/courses/mitx/6.00.1_3x/2t2014/courseware/week_2/basic_problem_set_1/
#This is because I couldn't make a submission as the deadlines had passed

#Question 1:
"""Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
For problems such as these, do not include raw_input statements or define the variable s in any way. Our automated testing will provide a value of s for you - so the code you submit in the following box should assume s is already defined. If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem set."""
s=raw_input()
count=0
for char in s:
	if (char in "aeiou"):
		count=count+1
print "Number of vowels: ",count

#Question 2:
"""Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
For problems such as these, do not include raw_input statements or define the variable s in any way. Our automated testing will provide a value of s for you - so the code you submit in the following box should assume s is already defined. If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem set."""
s=raw_input()
#k=raw_input()
k="bob"
if(s=="")or(k==""):
	exit()
count=0
indexes=[]
i=0
while True:
	i=s.find(k,i)
	if(i==-1):
		break
	count=count+1
	indexes=indexes+[i]	#store the indexes where k is found
	i=i+1
if(count==0):
	print "String %s does not occur in %s"%(k,s)
else:
	print "String %s occurs %d times in %s"%(k,count,s)
	
#Question 3:
"""ALPHABETICAL SUBSTRINGS  (15 points possible)
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
For problems such as these, do not include raw_input statements or define the variable s in any way. Our automated testing will provide a value of s for you - so the code you submit in the following box should assume s is already defined. If you are confused by this instruction, please review L4 Problems 10 and 11 before you begin this problem set.

Note: This problem is fairly challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head."""
s=raw_input()
i=0
subs=""
max_subs_len=0
max_subs=None
while (i<(len(s)-1)):
	subs=subs+s[i]
	if(s[i]>s[i+1]):	#the subsequent letter is not alphabetic & we must stop & reset subs. If we check first and then add, we'll be leaving out the last letter in aplhabetic order each time, unless one adds it to the else statement also. Instead, we **factor** out the statement and place it outside if statement.. and by checking for the converse condition, we eliminate the if statement altogether (and make the else statement the new if statement).
		a=len(subs)
		if(a>max_subs_len):
			max_subs_len=a
			max_subs=subs
		subs=""
	i=i+1
print "Longest substring in alphabetical order is: ",max_subs