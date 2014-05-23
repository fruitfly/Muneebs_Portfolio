from Tkinter import *
from time import *
from random import *

tk = Tk()
screen = Canvas(tk, width=800,height=600, background="white")
screen.pack()

numPenguins = 8

length = 700    #THE LENGTH OF THE LOG
radius = 20     #THE WIDTH OF THE BOXES 
xMin = 50       #THE X-VALUE OF THE LEFT END OF THE LOG
yLog = 200
speed = 3       #HOW FAST THE BOXES MOVE
fallingSpeed = 40
averageGap = int(length/numPenguins) #HOW MUCH SPACE IS BETWEEN EACH BOX AT THE BEGINNING

penguins = []
xSpeeds = []
ySpeeds = []
xPos = []
yPos = []
stillOnTheLog = []
penguinleft = PhotoImage(file = "penguinLeft.gif")
penguinright = PhotoImage(file = "penguinRight.gif")



#RETURNS THE (POSITIVE) DISTANCE BETWEEN THE TWO VALUES x1 AND x2.  
def distance(x1, x2):
    #implement this function.
    if x1>x2:
        return (x1-x2)
    else:
        return (x2-x1)
    


#RETURNS TRUE IF THE TWO NEIGHBOURING BOXES WITH INDICES index1 AND index2 HAVE JUST COLLIDED
def collision(index1, index2):
    
    if distance((xPos[index1]),(xPos[index2 ])) <= (radius*2) and yPos[index1]==yPos[index2]:
        return True
    else:
        return False


#RETURNS TRUE IF THE BOX WITH INDEX i IS ABOUT TO FALL OFF THE LOG 
def readyToFallOff( i ):
    
    if (xPos[i])<=(xMin-radius) or  ((xPos[i])>=((xMin+length)+radius)):
        return True
    
    else:
        return False

#DRAWS THE LOG
def drawLog():    
    screen.create_line(xMin, yLog+radius, xMin+length, yLog+radius, fill="black", width=4) 
             

#DRAWS THE BOX AT INDEX i AT ITS CURRENT POSITION
def drawPenguin(i):
    xCentre = xPos[i]
    yCentre = yPos[i]
    
    x1 = xCentre - radius
    y1 = yCentre - 3*radius
    x2 = xCentre + radius
    y2 = yCentre + radius



    penguins[i] = screen.create_image(x1,y1+20,image=penguinleft)


#IF TWO BOXES HAVE JUST COLLIDED, THIS FUNCTION GETS CALLED AND REVERSES THE DIRECTION OF EACH
#BOX BY MULTIPLYING THEIR SPEEDS BY -1
def reversePenguinSpeeds(i):
    xSpeeds[i] = -xSpeeds[i]
    xSpeeds[i+1] = -xSpeeds[i+1]

    
#CREATES THE INITIAL ARRAYS
def createArrays():   
    for i in range(0,numPenguins):
        
        penguins.append( 0 )
        
        stillOnTheLog.append( True )
        
        newSpeed = choice([speed, -speed])
        xSpeeds.append( newSpeed )

        yPos.append( yLog )
        ySpeeds.append( 0 ) 

        xRangeMin = xMin + i*averageGap + radius
        xRangeMax = xMin + (i+1)*averageGap - radius
        newX = randint(xRangeMin, xRangeMax)
        xPos.append( newX )



#RUNS THE MAIN ANIMATION LOOP
def runAnimation():
    
    numPenguinsStillOnLog = numPenguins

    createArrays()

    drawLog()
    
    while numPenguinsStillOnLog > 0: #RUN THE ANIMATION FOREVER

        for i in range(0, numPenguins): #FOR EACH BOX, DRAW IT IN ITS CURRENT POSITION, CHECK FOR COLLISIONS, AND UPDATE ITS POSITION
            
            drawPenguin( i )

            if stillOnTheLog[i] == True: 

                if i < numPenguins - 1: #THE LAST PENGUIN ON THE RIGHT DOESN'T HAVE TO WORRY ABOUT COLLISIONS
                    
                    if stillOnTheLog[i+1] == True: #ONLY CHECKS FOR COLLISIONS IF THE BIRD TO YOUR RIGHT IS STILL ON THE LOG
                        
                        if collision(i, i+1): #IF THE TWO PENGUINS AT INDICES i AND i+1 HAVE JUST COLLIDED, THEN REVERSE THEIR SPEEDS
                           reversePenguinSpeeds(i)

                if readyToFallOff( i ):
                    ySpeeds[i]= 20
                    xSpeeds[i]=0
                    yPos[i] = yPos[i] +ySpeeds[i]


            xPos[i] = xPos[i] + xSpeeds[i]
##            yPos[i] = yPos[i] + ySpeeds[i]
            #UPDATE THE Y POSITIONS, TOO
            

        screen.update()
        sleep(0.05)

        
        for i in range(0, numPenguins): 
            screen.delete( penguins[i] )


#THIS LINE CALLS THE PROCEDURE runAnimation.
runAnimation()



