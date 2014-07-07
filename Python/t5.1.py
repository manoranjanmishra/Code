#problems from Chapter 5 of think like a cs
#but i have not written a function here

print "This program will check if the Fermat theorem is right for three integers a,b &c for a given n"
try:
	a=float(raw_input("Enter the value of a: "))
	b=float(raw_input("Enter the value of b: "))
	c=float(raw_input("Enter the value of c: "))
	n=float(raw_input("Enter the value of n: "))
	if ((a**n)+(b**n))==(c**n):
		print "Holy Smokes, Fermat was wrong!"
	else:
		print "No, that doesn't work"
except:
	print "You must enter a number"
#if you enter large value of a,b,c,n the program returns "You must enter a number" which means the try block returns a error. Why would that be?

print "And, this one will check if three numbers can form the sides of a triangle"
#our try-except blocks are mostly used for catching string input.
try:
	a=float(raw_input("Enter the length of a side: "))
	b=float(raw_input("Enter the length of another side: "))
	c=float(raw_input("Enter the length of the last side: "))
	if (((a+b)>=c)&((a+c)>=b)&((b+c)>=a)):
		print "They cannot form a triangle"
	else:
		print "They form a triangle"
except:
	print "You must enter a number"
#(((a+b)>=c) and ((a+c)>=b) and ((b+c)>=a))	will also work on line 24 above
#(((a+b)<=c) or ((a+c)<=b) or ((b+c)>=a)) will also work. This si because we are checking for conditions that all have to be false.. or de moivre's law. When an expression is negated, the and becomes an or, and the or becomes an and.
#Three lengths can form a triangle iff the sum of two of them is GREATER than the third side.
#i DONT UNDERSTAND THE CONDITION OF THREE SIDES FORMING A TRIANGLE