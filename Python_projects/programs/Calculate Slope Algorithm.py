def getSlope(x1,x2,y1,y2):
    if (x2-x1)==0:
        return "undefined"
    else:
        return (y2-y1)/(x2-x1)

a = int(input("Enter the first x value"))
b = int(input("Enter the second y value"))
c = int(input("Enter the first x value"))
d = int(input("Enter the second y value"))


    
    

print("The slope of the line between the points is " + str( getSlope(a,c,b,d) ))

    
