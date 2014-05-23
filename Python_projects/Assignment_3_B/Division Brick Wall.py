from Tkinter import *

root = Tk()
screen = Canvas(root, width=1200, height=1200, background = "white" )
screen.pack()



denominator = int(input("please input a number"))

spacing =800 / denominator
for rowNumber in range(1,denominator+1):

    widthofboxes= 800/float(rowNumber)
    heightofboxes= 800/denominator

    for boxnumber in range (0,rowNumber):
        xUL = boxnumber*widthofboxes+50
        yUL = (heightofboxes*rowNumber)-(heightofboxes-30)
        xLR = xUL + widthofboxes
        yLR = yUL+heightofboxes
        screen.create_rectangle( xUL, yUL, xLR, yLR, fill="red", outline="black")
        xtext = xUL+(widthofboxes/2)
        ytext = yUL+(heightofboxes/2)
        if rowNumber >=10:
            fontSize=int(spacing/3)
            myFavouriteFont = "Times " + str( fontSize ) + " bold"
            numberstring = ("1/" + str(rowNumber))
            screen.create_text( xtext,ytext, text = numberstring , font = myFavouriteFont, fill = "blue")
        else:
            
            numberstring = ("1/" + str(rowNumber))
            fontSize = int( spacing/2 ) 
            myFavouriteFont = "Times " + str( fontSize ) + " bold"
            screen.create_text( xtext,ytext, text = numberstring , font = myFavouriteFont, fill = "blue")


screen.update()

    
