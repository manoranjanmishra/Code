#program for Excercise 2.4 from Think Python
#to calculate the volume of a sphere
#let's ask the radius from the user, and we'll store it as a float.
print "This program helps to calculate the surface area and volume of a sphere"
radius=float(raw_input("Enter the Radius of the sphere"))
#now that we have the radius of the sphere we can caluclate the area and volume of the sphere
volume=(4/3)*(3.141592653)*(radius**3)
area=4*(3.141592653)*(radius**2)
print "The area of the sphere of radius",radius,"is",area,"and it's volume is",volume
# we have used the actual value of pi, one could use the 22/7 value. In that case for a radius of 5, the area is 300 and the volume is 375
