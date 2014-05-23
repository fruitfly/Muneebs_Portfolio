from math import * 

def getDistance (x1,y1,x2,y2):
    a = abs(x1-x2)
    b= abs(y1-y2)

    c = sqrt((a**2)+(b**2))
    return c

print(getDistance(0,10,5,6))
    
