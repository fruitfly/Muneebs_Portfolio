from Tkinter import *
from time import *
from math import * 

root = Tk()
screen = Canvas(root, width=1200, height=1200, background = "white" )
screen.pack()

radius = 400
radiusofmh = 5
radiusofsh = 100
radiusofhh = 300

xCenter = 500
yCenter = 500

xUL = xCenter - radius
xLR = xCenter + radius
yUL = yCenter - radius
yLR = yCenter + radius
screen.create_oval( xUL, yUL, xLR, yLR, fill = "", outline="black", width = 3)
##screen.create_line(xCenter,yCenter,xCenter,yCenter-radiusofmh) #this is the minute hand
##screen.create_line(xCenter,yCenter,xCenter,yCenter-radiusofsh) #this is the second hand
##screen.create_line(xCenter,yCenter,xCenter,yCenter-radiusofhh) #this is the hour hand
x=0

theta = 90
##
##x1 = xCenter
##y1 = yCenter
##x2 = degrees((sin(theta)))+500
##y2 = (degrees((cos(theta))))+500
##
##
##print (x2)
##minutehand =screen.create_line(x1,y1,x2,y2, fill = "black")


while x==0:
    x1 = xCenter
    y1 = yCenter
    x2 = (radiusofmh*degrees(sin(theta)))+500
    print (x2)
    y2 = (radiusofmh*degrees(cos(theta)))+500
    minutehand =screen.create_line(x1,y1,x2,y2, fill = "black")
    theta = theta +6 
    screen.update()
    sleep (1)
    screen.delete(minutehand)

##for x in range (0,3): # this is repeated four times for each quadrant of rotation on the second hand
##    theta = 86
##
##    while theta >0:
##        x1s = xCenter
##        y1s = yCenter
##        x2s = radiusofsh * (math.sin(theta))
##        y2s = radiusofsh * (math.cos(theta))
##        screen.create_line(x1s,y1s,x2s,y2s, fill = "black")
##        theta = theta - 6
##        screen.sleep(1.0) # sleep for a second
##
##for x in range (0,3): # this is repeated four times for each quadrant of rotation on the hour hand
##    theta = 86
##
##    while theta >0:
##        x1h = xCenter
##        y1h = yCenter
##        x2h = radiusofhh * (math.sin(theta))
##        y2h = radiusofhh * (math.cos(theta))
##        screen.create_line(x1h,y1h,x2h,y2h, fill = "black")
##        theta = theta - 6
##        screen.sleep(3600.0) # sleep for an hour
##
##
##    
##    
##    
