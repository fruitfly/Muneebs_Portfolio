from Tkinter import *
myInterface = Tk()
myScreen = Canvas(myInterface, width=800, height=800, background="black")
myScreen.pack()

xorigin = 100
              
yorigin = 600
numlines = int(input("please input the number of lines"))
linelength = 500

xmax = xorigin + linelength
ymax = yorigin - linelength
space = linelength/numlines
x1 = xorigin + space
y1 = yorigin
x2 = xorigin
y2 = ymax + space

xaxis = myScreen.create_line(xorigin,yorigin,xmax,yorigin,fill="blue",width = 2)
yaxis = myScreen.create_line(xorigin,yorigin,xorigin,ymax,fill="blue",width = 2)

for linecounter in range (1,numlines):

    x1 = x1 +space
    y1 = yorigin
    x2 = xorigin
    y2 = y2 + space
    myScreen.create_line(x1,y1,x2,y2, fill ="blue", width = 4)

    

    

