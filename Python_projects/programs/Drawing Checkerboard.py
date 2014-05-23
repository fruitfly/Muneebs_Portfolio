from Tkinter import *

root = Tk()
screen = Canvas(root, width=800, height=800, background = "blue" )
screen.pack()

boxSize = 800/8


for rowNumber in range(0,8):

    yUL = rowNumber * boxSize
    yLR = yUL + boxSize

    

    for columnNumber in range (0,8):

        xUL = boxSize * columnNumber
        xLR = xUL + boxSize
        z = columnNumber+rowNumber
        if z%2==0:
            screen.create_rectangle( xUL, yUL, xLR, yLR, fill="white", outline="red")
        else:
            screen.create_rectangle( xUL, yUL, xLR, yLR, fill="black", outline="red")
        if z%2==0 and rowNumber<=2:
            screen.create_oval(xUL,yUL,xLR,yLR,fill="red",outline="white")
        if z%2==0 and rowNumber>=5:
            screen.create_oval(xUL,yUL,xLR,yLR,fill="green",outline="white")
       
        screen.update()

    
