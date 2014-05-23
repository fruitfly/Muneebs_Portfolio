from math import * 
def getArea (r):
    return pi*r**2
radius = int(input("Please input the radius of the circle in cm's"))
print ("The area of the circle with radius " + str(radius) + " is " + str( getArea( radius )) + "cm^3")
