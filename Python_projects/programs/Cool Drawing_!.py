from Tkinter import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=800, height=800, background = "white" )
screen.pack()


radius = 30
xBall1 =[100,200,300,400,500]
yball1 = 200
yball2= 400

for i in range (0,5):
    
    screen.create_oval(xBall1[i]-radius, yball1-radius,xBall1[i]+radius, yball1+radius, fill="blue")

    
    for a in range (0,5):
        screen.create_line(xBall1[i], yball1, xBall1[a],yball2,fill="black")





for i in range (0,5):
    screen.create_oval(xBall1[i]-radius, yball2-radius,xBall1[i]+radius, yball2+radius, fill="blue")

    for a in range (0,5):
        screen.create_line(xBall1[i], yball2, xBall1[a],yball1,fill="black")














