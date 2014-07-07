#conditional statements
print "This program will print the wage of an employee based on the number of hours worked."
try:
	hours=float(raw_input("Number of hours worked:"))
	rate=float(raw_input("Enter rate per hour: $"))
	if hours>40:
		pay=(40*rate)+((hours-40)*rate*1.5)
	else:
		pay=hours*rate
	print "The Pay for", hours, "hours, is $", pay
except:
	print "Please Enter a number"
#pay=(hours*rate)+(hours>=40)*(0.5*rate)
#print "The Pay for ",hours,"hours, is $",pay
#this also works. and eliminates the use of a conditional statement.
#does this mean that we can replace the use of and by the * sign? and the or by the + sign?
