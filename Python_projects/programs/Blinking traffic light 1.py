from Tkinter import *
from random import *
from time import *


root = Tk()
screen = Canvas( root, width=800, height=800, background = "black" )
screen.pack()

#TRAFFIC LIGHT BOX
lamp = screen.create_rectangle(400, 200, 600, 650, fill = "orange")
post = screen.create_rectangle(475, 650, 525, 800, fill = "orange")


#BLINKING LIGHTS ANIMATION
diameter = 100

lightColors = ["green", "yellow", "red"]
lightHeights = [500, 375, 250]

for i in range(0, 200):

    #PAINT 3 BLACK DISKS
    for k in range(0,3):
        screen.create_oval(450, lightHeights[k], 550, lightHeights[k]+diameter, fill ="black")
        screen.update()


    #PAINT THE COLORED LIGHT ON TOP OF ONE OF THOSE BLACK DISKS
    #BOTH THE HEIGHT AND THE COLOR MUST CHANGE WITH EVERY ITERATION OF THE OUTER LOOP
    screen.create_oval(450, lightHeights[i%3], 550, lightHeights[i%3]+diameter, fill = lightColors[i%3])


    screen.update()
    sleep(1)
    
    
