#ex4.6
print "This program will compute the wages of a person, based on the number of hours worked & rate per hour"
#to check for string input we will be using the try-except structure
def wage(a,b):
	#if hours are beyond 40 the rate becomes 1.5 times. You could also assign these to variables and accept them as input, in which case the wage function will take four inputs.
	#indentation is essential, as everywhere in Python where a block of code is encased within another block/line of code.
	if (a>40):
		wage=(40*b)+((a-40)*1.5*b)
	else:
		wage=a*b
	#wage=(a*b)+(a>40)*0.5*(a-40)*b This will also work. This is possibly because the value of a condition check expression like (a>40) here is either 1 or 0 and multiplying that allows us to include a condition part in the formula itself.
	return wage
try:
	hours=float(raw_input("Enter the number of hours worked: "))
	rate=float(raw_input("Enter the base rate per hour: "))
	print "The wage for the person is",wage(hours,rate)
except:
	print "You must enter a number"