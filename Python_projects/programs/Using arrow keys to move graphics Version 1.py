from Tkinter import *
from math import *
from time import *
from random import *

root = Tk()
screen = Canvas(root, width=600, height=600, background="white")

#GETS CALLED ONCE AT THE BEGINNING OF THE PROGRAM.  IT SETS ALL THE GLOBAL VARIABLES
def setInitialValues():
    global xBall, yBall, ballRadius, xMouse, yMouse, xSpeed, ySpeed, maxSpeed, ball, Qpressed
    
    xBall = 300
    yBall = 300

    ballRadius = 20
    xMouse = 0
    yMouse = 0

    xSpeed = 0
    ySpeed = 0

    maxSpeed = 5

    ball = 0

    Qpressed = False


#GETS CALLED WHENEVER ANY KEY IS PRESSED DOWN
def keyDownHandler( event ):
    global xSpeed, ySpeed, Qpressed

    if event.keysym =="Left":   #LEFT ARROW WAS PRESSED
        xSpeed = -maxSpeed
        print("left")
    elif event.keysym == "Right":   #RIGHT ARROW WAS PRESSED
        xSpeed = maxSpeed
        print("right")
    elif event.keysym == "Up":   #UP ARROW WAS PRESSED
        ySpeed = -maxSpeed
        print("up")

    elif event.keysym == "Down":   #DOWN ARROW WAS PRESSED
        ySpeed = maxSpeed
        print("down")

    elif event.keysym == "q" or event.keysym == "Q":    #Q WAS PRESSED
        Qpressed = True



#GETS CALLED WHENEVER ANY KEY IS RELEASED
def keyUpHandler( event ):
    global xSpeed, ySpeed
    
    xSpeed = 0  #STOP THE BALL
    ySpeed = 0


#GETS CALLED IN EVERY FRAME. UPDATES THE POSITION OF THE BALL, USING THE CURRENT SPEEDS
def updateBallPosition():
    global xBall, yBall
    xBall = xBall + xSpeed
    yBall = yBall + ySpeed


#GETS CALLED IN EVERY FRAME.  DRAWS THE BALL AT ITS CURRENT LOCATION AND SIZE
def drawBall():
    global ball
    
    ball = screen.create_oval(xBall-ballRadius, yBall-ballRadius, xBall + ballRadius, yBall+ballRadius, fill= "blue")


#GETS CALLED IN EVERY FRAME TO CHECK IF THE GAME SHOULD CONTINUE OR NOT
def gameOver():
    if Qpressed == True:
        return True

    else:
        return False


#GETS CALLED ONCE AFTER THE MAIN GAME LOOP HAS STOPPED
def stopGame():
    screen.create_text( 300, 300, text="Thanks for playing...good bye", anchor=CENTER, font="Times 40")
    screen.update()
    sleep(2)
    root.destroy()


#GETS CALLED ONCE.  THIS IS THE MAIN PROCEDURE THAT RUNS THE GAME
def runGame():
    global xBall, yBall

    setInitialValues()

    while gameOver() == False:
        updateBallPosition()
        drawBall()
        screen.update()
        sleep(0.008)
        screen.delete(ball)

    stopGame()

   
#STARTS THE GAME BY PASSING CONTROL TO THE PROCEDURE runGame() 1000 MILLISECONDS AFTER PUSHING F5
root.after(1000, runGame)

#BINDS THE PROCEDURE keyDownHandler TO ALL KEY-DOWN EVENTS
screen.bind("<Key>", keyDownHandler)

#BINDS THE PROCEDURE keyUPHandler TO ALL KEY-UP EVENTS
screen.bind("<KeyRelease>", keyUpHandler)

screen.focus_set()

screen.pack()
root.mainloop()
