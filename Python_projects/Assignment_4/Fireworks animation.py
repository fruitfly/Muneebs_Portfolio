from Tkinter import *
from time import *
from random import * 

root = Tk()
screen = Canvas(root, width=800, height=800, background = "black" )
screen.pack()
nummissiles =20
##int(input("How many balls do want to generate?"))
numfireworks= 15
x = []
y = []
speedx=[]
speedy=[]
missiles=[]
colors = ["blue","red","white"]
##ball = PhotoImage(file = "ball.gif")
radius = 6
gravity= -2
background = PhotoImage(file = "city skyline copy.gif")
screen.create_image(400,750,image =background )

for framecounter in range (0,10):
    welcome = screen.create_text(400,400,font="Arial 20 bold underline",text="Welcome to the Fireworks Show!",fill = "white")
    screen.update()
    sleep(0.1)
    screen.delete(welcome)
 

for i in range(0,nummissiles):
    newY = 400
    newX = 400
    newXspeed = randint(-10,20)
    newYspeed = randint(-10,20)

    
    x.append( newX )
    y.append( newY )
    speedx.append( newXspeed )
    speedy.append( newYspeed )
    missiles.append ( 0 )

n=0
for numfireworks in range (0,numfireworks):## animating 5 different fireworks
    
    for framecount in range(0,20):##animating the firework for 20 frames
        for i in range (0,len(missiles)):## animating each particle in the firwework
              ##this block of code makes the ball bounce 
##            if (y[i]+radius)>=800:
##                speedy[i]=speedy[i]*(-1)
##            if (x[i]+radius)>=800:
##                speedx[i]=speedx[i]*(-1)
##            if (x[i])<=0:
##                speedx[i]=speedx[i]*(-1)
##            if (y[i])<=0:
##                speedy[i]=speedy[i]*(-1)
            speedy[i] = speedy[i]-gravity
            y[i] = (y[i] + speedy[i])
            x[i] = (x[i] + speedx[i])
            colors1 = colors[i%len(colors)]
            missiles[i] = screen.create_oval( x[i], y[i],x[i]+radius, y[i]+radius, fill=colors1)
            screen.update()
            if (y[i]+radius)>=800:
                screen.delete(missiles[i])
                n=1
            if (x[i]+radius)>=800:
                screen.delete(missiles[i])
                n=1
            if (x[i])<=0:
                screen.delete(missiles[i])
                n=1
            if (y[i])<=0:
                screen.delete(missiles[i])
                n=1
        sleep(0.05)
        for i in range (0,len(missiles)):
            screen.delete(missiles[i])
    
    del x[:]
    del y [:]
    del missiles [:]
    del speedy[:]
    del speedx[:]
    ## the above code  deletes all previous vector values
    newY = randint(1,700)
    for i in range(0,nummissiles):##generating new vector values for the next firework animation.
                
        
        newXspeed = randint(-10,20)
        newYspeed = randint(-10,20)

        
        x.append(newY )
        y.append(newY )
        speedx.append(newXspeed )
        speedy.append(newYspeed )
        missiles.append (0)
        print (x,y)
        
 

##for FrameCount in range (0,10000)
for framecounter in range (0,10):
    theend = screen.create_text(400,400,font="Arial 20 bold underline",text="The End!",fill = "white")
    screen.update()
    sleep(0.1)
    screen.delete(theend)

        
    
