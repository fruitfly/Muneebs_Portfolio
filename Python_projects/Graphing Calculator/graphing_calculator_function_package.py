####################################################################
# Title: graphing_calculator_package
# Programmers:  Muneeb A. , Sanan A. , Faraz F. , Islam E.
# Last modified:  Dec 10th, 2013
# Purpose: This program draws a linear or a quadratic function and 
#          returns important information about the function
#####################################################################
import math
from Tkinter import *










#finds the a,b,c values of the function and returns these values in an array
def seperateFunctionstring (function):
    rightside = function[2:len(function)]
    ## finding the 'a' value
    myIndexa = rightside.find("x*2")
    
    if myIndexa==-1:
        a = 0
    
        
    else:
        astring = rightside[0:myIndexa]
        n=0
        d=0
        
        a = astring
        if a =="":
            a = 1

        if a == "-":
            a = -1
        
            
        for i in range (0, len(astring)): ## checking for fractions
            if astring[i]=='/':     
                n = float(astring[0:i])
                d = float(astring[i+1:len(astring)])
                a = float(n/d)
    a = float(a)
    
    ##finding the 'b' value
    if a==0: ## if the equation is linear
        myIndexb = rightside.find("x")
        
    else:
        rightside = rightside[myIndexa+3:len(rightside)]
        myIndexb = rightside.find("x")
        
        
    if myIndexb==-1:
        bstring ="0"
    else:
        bstring = rightside[0:myIndexb]
    n=0
    d=0
    b = bstring
    if b =="+":
        b = 1

    if b == "-":
        b = -1
    if b=="":
         b =1
    
       
    for i in range (0, len(bstring)): ## checking for fractions
        if bstring[i]=='/':
            n = float(bstring[0:i])
            d = float(bstring[i+1:len(bstring)])
            b = float(n/d)

    b = float(b)
    
    ## finding the 'c' value
    if myIndexb == -1:
        cstring = rightside[(myIndexa):len(rightside)]
        
        
    else:
        cstring = rightside[myIndexb+1:len(rightside)]
        
    n=0
    d=0
    
    if cstring=="" or cstring=="0":
        c=0
    else:
        c = (cstring)
    
    for i in range (0, len(cstring)): ## checking for fractions
        if cstring[i]=='/':
            n = float(cstring[0:i])
            
            d = float(cstring[i+1:len(cstring)])
            
            c = (n/d)
            
    
    c= float(c)
    
    abcvals = [a,b,c]
    
    return (abcvals)
















#checks if the function is Quadratic or Linear
def isQuadorLinear(function):
    abcvals = seperateFunctionstring(function)
    if abcvals[0]==0:
        return False
    else:
        return True




















#Calculates the Y value of a certain inputted x value    
def calculateYvalue(x, function):
    abcvals = seperateFunctionstring(function)
    a = abcvals[0]
    b = abcvals[1]
    c = abcvals[2]
    y = (a)*x**2+(b)*x+c
    return y
















#scaling the x-axis
def getRatioforxaxis(xMax,xMin):
    if xMax == xMin:
        print("your max and minimum values are the same. Please input different numbers")
    else:
        xratio = (800/(xMax-xMin))
    return xratio
















#scaling the y-axis
def getRatioforyaxis(xMax,xMin,function):
    if xMax == xMin:
        print("your max and minimum values are the same. Please input different numbers")
    #calculate the yMax and yMin values using the calculateYvalue function and the xMin and xMax values
    else:    
        yMax = calculateYvalue(xMax,function)
        yMin = calculateYvalue(xMin,function)
        if yMax==yMin:
            yMin = yMin*(-1)
    if yMax>yMin:
        yratio = (800/(yMax-yMin))
    else:
        yratio = (800/(yMin-yMax))
    return yratio















#creating orderedpairs of the function based on the a,b,and c values
def generateOrderedpairs(xMin, xMax,function):
    abcvals = seperateFunctionstring(function)
    array = []
    x = xMin
    spacing = 0.1
    #numpoints represents how many points would have to be made in order to cover the distance between max and min, using the specified spacing 
    numpoints = int((xMax-xMin)/spacing)
    xratio = getRatioforxaxis(xMax,xMin)
    yratio = getRatioforyaxis(xMax,xMin,function)
    for i in range (0, numpoints):
        y = (calculateYvalue(x,function))
        y = ((y *(-1)*yratio)+400)# the extra calculations are there to scale the y and x values
        
        
        array.append(((x*xratio)+400,y))
        x = x + spacing
    

    return array
















#this function simply returns the roots (x-intercepts) of the function
def getRoots (function):
    abcvals = seperateFunctionstring(function)
    if abcvals[0] == 0:
        b= abcvals[1]
        c= abcvals[2]
        
        x= -(c)/b
        return ("The root of this linear function is " + str(x))
    else:
        a= abcvals[0]
        b= abcvals[1]
        c= abcvals[2]
        if ((b**2)-4*(a)*(c))<0:
            return ("There are no real roots (complex roots)")
        else:
            x1 = ((-(b))+ (math.sqrt((b**2)-4*(a)*(c))))/(2*(a))
            if x1==-0.0:
                x1=0
            x2 = ((-(b))- (math.sqrt((b**2)-4*(a)*(c))))/(2*(a))
            if x2==-0.0:
                  x2=0
            return ("The roots are " + str(x1) +  " and " + str(x2))


     

















#returns the y-intercepts of the function
def getYintercepts (function):
    abcvals = seperateFunctionstring(function)
    c = abcvals[2]
    return ("The y-intercept of this function is " + str(c))

















#gets the slope of a linear function
def getSlope(function):
    abcvals = seperateFunctionstring(function)
    if isQuadorLinear(function)==False:
        slope = abcvals[1]
        return ("The slope of this function is " + str(slope))
    else:
        return ("No slope because the function is quadratic")




















#Returns the coordinates for the vertex and the direction of opening
def getVertexandopening (function):
    abcvals = seperateFunctionstring(function)
    if (isQuadorLinear(function))==False:
        b = abcvals[1]
        if b>0:
            return ("The function's direction is upwards and has no vertex because it is a linear function")
        else:
            return ("The function's direction is downwards and has no vertex because it is a linear function")
        
    else:
        a = abcvals[0]
        b = abcvals[1]
        x = (-(b)/(2*(a)))
        if x == -0.0:
            x =0.0
        y = calculateYvalue(x,function)
        if a>0:
            return ("The function's direction is upwards and has a vertex at (" + str(x) + "," + str(y) + ")")
        else:
            return ("The function's direction is downwards and has a vertex at (" + str(x) + "," + str(y) + ")")



























#this procedure plots all the points of the function and draws the scale appropriately        
def drawFunction(function, xMax, xMin):
    
    myInterface = Tk()
    myScreen = Canvas(myInterface, width=800, height=800, background="white")
    myScreen.pack()
    #x axis
    myScreen.create_line( 0, 400, 800, 400, fill = "black")
    #y-axis
    myScreen.create_line( 400, 0, 400, 800, fill = "black")
    #for scaling
    xratio = getRatioforxaxis(xMax,xMin)
    yratio = getRatioforyaxis(xMax,xMin,function)

    #numbering and labelling both the y and x-axis
    maxval = max(xMax,calculateYvalue(xMax,function))
    x = 0
    n=0
    while (x < maxval):
        xcoord  = x * xratio + 400
        ycoord  = x * yratio + 400
        nxcoord  = (-1*x * xratio + 400)
        nycoord  = (-1*x * yratio + 400)


        
        myScreen.create_oval(nxcoord , 400 , nxcoord + 3 , 400 + 3 , fill="black")
        myScreen.create_text(nxcoord , 400 + 10 , text = x * -1)
        
        myScreen.create_oval(xcoord      , 400 , xcoord      + 3 , 400 + 3 , fill="black")
        myScreen.create_text(xcoord      , 400 + 10 , text = x )
        
        myScreen.create_oval(400 , nycoord , 400 + 3 , nycoord + 3 , fill="black")
        #skips numbering
        if n%2==1:
            myScreen.create_text(400 +10 , nycoord , text = x * -1)

        myScreen.create_oval(400 , ycoord , 400 + 3 , ycoord + 3 , fill="black")
        #skips numbering
        if n%2==1:
            myScreen.create_text(400 +10, ycoord , text = x )
        n=n+1
        x = x + 2

        
        
        
  
    
        
        
        
        
    #plotting the points of the function
    array = generateOrderedpairs(xMin, xMax,function)
    for i in range (0,len(array)-1):
        x = array[i][0]
        x2 = array[i+1][0]
        y= array[i][1]
        y2 = array[i+1][1]
        myScreen.create_oval(x,y,x+1, y+1, fill="black")
        myScreen.create_line(x,y,x2,y2,fill="black", width= 5)
        myScreen.update()

        
    #printing the key info.
    print("############################################")
    print("Here are the Key features of this function:")
    print(getRoots(function))
    print(getYintercepts(function))
    print(getSlope(function))
    print(getVertexandopening(function))


