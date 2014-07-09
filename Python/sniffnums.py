def sniffnums_skeleton(a):
#This is the skeleton code to sniff integer numbers out of the string. It is here to show us the algorithm to sniff numbers out of a string.
	l=len(a)	#find the length of the string, so that when processing the string we know when to stop.
	i=0		#i is the index of the string, using which we access characters from the string.
	c=0		#c counts how many numbers we have found till now.
	while (i<l):
		try:								#check if the character at index i is a number or not. We cant write if a[i] is a number: , so
			int(a[i])						#we've used try & except. int(a[i]) converts the character at i into a number, provided it is a number. Which is a good way to check if a[i] is a number.
			p=i+1							#if it is a number, we want to find out if there are any more numbers in continuation- that is because digits in continuation form a number. If there are letters inbetween then they are separate numbers.
			while True:						#plus we can't change i, so we shift to another index, and also start checking from the next character.
				try:
					int (a[p])
					p=p+1					#if it is a number, go ahead.
				except:						#if it's not, stop there. We'll pick up later from here to continue our search for the next number.
					break
			print int(a[i:p]),				#the characters between i & p contain a string of only numbers. The int() converts them from a string to a number.
			c=c+1							#we found a number, so lets count it. You could instead/also do anything with the number we've extracted.
			i=p								#Now that we're done, let's go to the next number... picking up from where we left off. So, i=p
		except:
			i=i+1
	print "\nThe entered string had",c,"numbers in it."
#call the function defined above.
sniffnums_skeleton(raw_input())