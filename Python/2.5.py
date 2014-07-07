#this prigram will covert an input temperature to Fahrenheit from Celcius
print "This program converts from Celcius to fahrenheit"
#When the user inputs a value it has to be converted to float
cel=float(raw_input("Enter your temperature in Celcius")) #We convert it to float so that we dont get a rounded off fahrenheit value.
fah=(9/5)*(cel+32) #F=9/5(C+32) & C=(5/9F)-32
print "The temp. in Fahrenheit is ",fah
# a nice thing i just noticed is that you can also enter negative values, and the int or float converters dont complain about it.
print "Now lets try it the oher way round"
fah=float(raw_input("Enter the temperature in Fahrenheit"))
cel=((5/9)*fah)-32
print "THe temperature in degrees Celcius is", cel
#the formulae for the conversions is wrong. Rewrite the code.
