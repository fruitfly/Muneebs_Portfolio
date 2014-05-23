from Tkinter import *
from time import *
from random import * 

root = Tk()
screen = Canvas(root, width=800, height=800, background = "black" )
screen.pack()

xStar = 0
yStar = 0
starSize = 0
d = 0

for i in range (0,500):
    xStar = randint (50,750)
    yStar = randint (50,750)
    starSize = randint(1,5)
    screen.create_oval(xStar-starSize,yStar-starSize,xStar+starSize,yStar+starSize, fill = "white")
    d =d +1


print (d)
