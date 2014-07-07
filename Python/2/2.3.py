#a program to prompt for hours worked, and then print the wages.
print "This program will help you compute gross pay"
print "Enter the hours of work & rate per hour, to compute gross pay"
hours=raw_input("Enter no of hours worked:")
rate=raw_input("Enter rate per hour")
#print "Gross pay=",int(hours)*int(rate)
print "Gross Pay=", float(hours)*float(rate)
#The flaot converts the string type to float type. If incase one enters dots in the string the int type conversion will fail.
