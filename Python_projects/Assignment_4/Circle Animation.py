#Purpose:  This program creates beautiful string-art patterns inside a circle
#Prerequisites: Arrays, modular indexing, and Grade 11 trigonometry
#Programmer:  Muneeb Ahmed
#Last modified:  Sept. 30, 2013


#IMPORTS
from Tkinter import *
from math import *
from time import *
from random import choice 

#SETS UP THE DRAWING CANVAS
screenHeight = 700
screenWidth = 700
root = Tk()
screen = Canvas( root, width=screenWidth, height=screenHeight, background = "black" )
screen.pack()


#SETS PARAMETERS
xCenter = screenWidth / 2
yCenter = screenHeight / 2
radius = 0.4 * screenWidth
nailRadius = 5
numNails = 60
skip = 30


stringColors = [ "blue", "red", "green","purple","white","violet" ] #ADD MORE COLORS TO THE LIST FOR DIFFERENT EFFECTS
numColors = len( stringColors )


#CREATES AN ARRAY OF EVENLY SPACED NAILS ALONG THE OUTER CIRCLE
#THESE POINTS WILL BE THE NAILS BETWEEN WHICH THE STRINGS ARE STRUNG
deltaTheta = 360.0 / numNails

nails = []

for pointCounter in range( 0, numNails ):
    
    thetaDegrees = pointCounter * deltaTheta
    theta = radians( thetaDegrees )
    
    x1 = xCenter + radius * cos( theta )
    y1 = yCenter - radius * sin( theta )
    
    newNail = [ x1, y1 ]
    nails.append( newNail )
    
    #DRAW THE POINTS
    screen.create_oval( x1-nailRadius, y1-nailRadius, x1+nailRadius, y1+nailRadius, fill="white" )



#THIS LOOP WILL DRAW THE STRINGS BETWEEN THE NAILS, GIVEN THE SIZE OF THE SKIP.
#YOU FILL IN THIS PART
for nailCounter in range(0,len(nails)):

    #formulas for the starting index and the ending index go here
    xStart = nails[nailCounter][0]
    yStart = nails[nailCounter][1]
    xEnd = nails[(nailCounter+skip)%len(nails)][0]
    yEnd = nails[(nailCounter+skip)%len(nails)][1]
    colors = stringColors[nailCounter%numColors]
    
    

    
    #formulas for xStart, yStart, xEnd and yEnd go here
     

    #draw the current line    
    screen.create_line(xStart,yStart,xEnd,yEnd, fill=colors )
    screen.update()
    
    #delay to create the animation effect
    sleep(0.01)

