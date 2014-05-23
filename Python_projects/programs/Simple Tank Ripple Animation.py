from Tkinter import *
from time import *

root = Tk()
screen = Canvas(root, width=800, height=800, background = "black" )
screen.pack()

radius = int(input("please input the radius of the circle"))

xCenter = int(input("please input the x value of the center of the circle"))
yCenter = int(input("please input the y value of the center of the circle"))

xUL = xCenter - radius
xLR = xCenter + radius
yUL = yCenter - radius
yLR = yCenter + radius

while xUL > 0  and xLR <800 and yUL >0 and yLR <800:
    
    cirlce = screen.create_oval( xUL, yUL, xLR, yLR, fill = "blue", outline="red", width = 3)
    growth = 10
    radius = radius + growth

##    xCenter = 400
##    yCenter = 300

    xUL = xCenter - radius
    xLR = xCenter + radius
    yUL = yCenter - radius
    yLR = yCenter + radius

    
    sleep(0.01)
    screen.update()
    

