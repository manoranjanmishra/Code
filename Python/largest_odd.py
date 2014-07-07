print "Input three numbers, and this program will compute the largest odd & even number of the three numbers."
#we will catch if anybody tries inputting a string
try:
	x=float(raw_input("Enter x: "))
	y=float(raw_input("Enter y: "))
	z=float(raw_input("Enter z: "))
	#stacking these statements like these automatically stops execution the moment you eneter a string as input
	if(x>=0)&(y>=0)&(z>=0): #Even and odd numbers are positive numbers, so checking if somebody inputs a negative number.
	#technically even and odd numbers are integers too, so we should also put a check for that here.. the check being that, if a number doesnot have a fractional part int(number) will be equal to the number itself.
		if (x==0) or (y==0) or (z==0):
			print "0 is neither even nor odd"
		else:
			if(x==int(x))&(y==int(y))&(z==int(z)):
				max_odd=0
				max_even=0
				x=int(x)
				y=int(y)
				z=int(z)
				if ((x%2)!=0):
					max_odd=x
				else:			#since x can be either even or odd.
					max_even=x
				if (((y%2)!=0) & (y>max_odd)):
					max_odd=y
				else:			#if this block executes, y is obviously even.
					if (y>max_even):
						max_even=y
				if(((z%2)!=0) & (z>max_odd)):
					max_odd=z
				else:			#if this block executes, z is obviously even.
					if (z>max_even):
						max_even=z
				if(max_odd==0):
					print "There are no odd numbers"
				else:
					print "The largest odd number is:", max_odd
				if(max_even==0):
					print "There are no even numbers"
				else:
					print "The largest even number is", max_even
			else:
				print "Fractional numbers are neither even nor odd."
	else:
		print "Negative numbers are neither even nor odd"
except:
	print "You must enter a number"
#if you remove the code on lines 15 16 & 17 this code fails on the try block of line 3, and outputs the except statement "You must enter a number",, Why would that be?
#even putting an int before the (x%2)... doesn't work.
#another point.. WHen you use the &, and, or, operators with expressions like on lines 18, 20 & 22 you must enclose each expression in brackets. Try removing the brackets around y>max_odd or z>max_odd and test with an input of 11,13,15.. you get an output of 15 which is clearly wrong. So, you must use brackets.
#this code was first written to find out the largest odd number. It was then re edited to also find out the largest even number. For that purpose another variable max_even was created. The if statements on lines 19,23,28  check if x,y&z are odd.. thus if they fail the corresponding numbers are even. THis fact is used, along with a comparison to find out the largest even number.
#one could further try finding the least even and odd numbers, and so on. That simply involves adding a min_odd & a min_even variable, and inserting  if statements to check if a number is less than min (if yes, min = new number), else go ahead.