from math import *
def cylinderVolume (r,h):
    return (pi*r**2)*h

r=int(input("plesae input the radius of the cyllinder"))
h = int(input("pleas input the height of the cyllinder"))
print( "The area of the circle with radius 10 is " + str( cylinderVolume( r, h ) ))
