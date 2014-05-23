############################################################################################

#TITLE:  BUBBLE TROUBLE

#PURPOSE:  A video game whos objective is to destroy all the bubbles on screen before your lives run out

#DATE LAST MODIFIED: 1/23/2014

#PROGRAMMER:  Muneeb Ahmed

############################################################################################



from Tkinter import *
from math import *
from random import *
from time import *

## creating the screen
root = Tk()
screen = Canvas( root, width = 800, height = 800, background = "white")










def generateVars():
    global numbubbles, xbubbles, ybubbles, xspeed, yspeed, radius, bubbles, xspeedcharacter, currentx, n, character_straight, character_right_walk, character_right_walk_1
    global  character_left_walk, character_left_walk_1, quitGame, score, livesleft, xMouse, yMouse,start,button,text,gravity,fire,gametimer,currenty,approxradius,missiley,missilex,missilespeed,missile, livesdisplay, scoredisplay
    global colour,bubblecolours


    #Geernating ball characteristics
    
    numbubbles = 10
    xbubbles = []
    ybubbles = []
    xspeed=[]
    yspeed=[]
    radius=[]
    colour=["blue", "red", "green","white","purple", "magenta"]
    bubblecolours = []
    
    bubbles = []
    for i in range(0,numbubbles):
        xbubbles.append(randint(100,700))
        ybubbles.append(randint(100,500))
        xspeed.append(randint(-6,6))
        yspeed.append(randint(3,6))
        radius.append(randint(10,40))
        bubbles.append(i)
        bubblecolours.append(colour[i%6])
        

    #Characteristics of the character
    xspeedcharacter = 0
    currentx = 400
    currenty = 785
    approxradius = 22.36
    character_straight = PhotoImage(file = "character_straight.gif")
    character_right_walk = PhotoImage(file = "character_right_walk.gif")
    character_right_walk_1=PhotoImage(file = "character_right_walk_1.gif")
    character_left_walk =PhotoImage(file = "character_left_walk.gif")
    character_left_walk_1=PhotoImage(file = "character_left_walk_1.gif")

    ##General Vars
    quitGame=False
    score = 0
    livesleft = 3
    xMouse = 0
    yMouse = 0
    start=False
    fire =False
    gametimer = 0
    livesdisplay = 0
    scoredisplay = 0
    
    #missile characteristics
    missile = screen.create_line(0,0,1,1,fill="white")
    missiley = 800
    missilex = 0
    missilespeed = 10


    ## drawing tbe background image
    Background = PhotoImage(file="background.gif")
    background = screen.create_image(0 ,0,image=Background)

    
##    button = screen.create_rectangle(100, 350, 700, 450, fill="")
##    text = screen.create_text(400,400, text = "Press Enter to Play Game")
    












## Calculates the distance between any two bubbles and returns true if they are colliding
def isCollision (x1,y1,radius1, x2,y2,radius2):
    
    a =abs(x1-x2)
    
    b= abs(y1-y2)
    
    c = radius1 + radius2
    if ((a)**2)+((b)**2)<=((c)**2):
        return True
    else:
        return False
    
#Test   
print(isCollision(-6,10,3,-2,7,2)) #should print True











## Calculates the distance between  a bubble and the character and returns true if they are colliding
def collisioncharacterandbubbles (i):
    global currentx,currenty,xbubbles,ybubbles,approxradius,radius
    a = abs(ybubbles[i]-currenty)
    b = abs(xbubbles[i]-currentx)
    
    if ((radius[i]+approxradius)**2)>=(a**2)+(b**2):
        return True
        
    else:
        return False










## Calculates whether or not the harpoon collides with a bubble. Returns true if there is a collision
def collisionharpoonandbubbles(i):
    global missilex, xbubbles,fire, bubbles, radius
    diameter1 = xbubbles[i]-radius[i]
    diameter2 = xbubbles[i]+radius[i]
    if fire==True:
        if missilex >=diameter1 and missilex<=diameter2:
            if ybubbles[i]+radius[i]>=missiley:
                return True
            else:
                return False
    
    else:
        return False
    











## draws and animates the character
def drawCharacter():
    global character_left_walk_1, character_left_walk, character_right_walk, character_right_walk_1, xspeedcharacter, currentx,n, character,gametimer,currenty

    ## moving the character
    currentx = currentx+xspeedcharacter

    ## if the character is standing still: draw a certain image
    if xspeedcharacter==0:
        character = screen.create_image(currentx-10, currenty-20, image = character_straight)
    ## if the character is moving left: draw the left animation
    if xspeedcharacter<0:
        ## the gametimer simply enables the program to alternate between animations so that it looks like the character is walking
        gametimer = gametimer+1
        if gametimer%2.5==1:
            character =screen.create_image(currentx-10, currenty-20, image = character_left_walk)
        else:
            character =screen.create_image(currentx-10, currenty-20, image = character_left_walk_1)
    ## if the character is moving right: draw the right animation
    if xspeedcharacter>0:
        gametimer = gametimer+1
        if gametimer%2.5==1:
            character =screen.create_image(currentx-10, currenty-20, image = character_right_walk)
        else:
            character =screen.create_image(currentx-10, currenty-20, image = character_right_walk_1)
    
    














## called when the player hits the spacebar. Draws a straight, black line that travels upwards
def fireharpoon ():
    global missilex,missiley,missilespeed, fire,missile

    missiley = missiley - missilespeed

    missile = screen.create_line(missilex,missiley,missilex,800, fill = "black", width=5)
    #once the missile reaches the top of the screen, delete it
    if missiley == 0:
        fire = False
        missiley = 800
        screen.delete(missile)
    
    
    




















## draws and updates all the bubbles. Checks for collisions as well
def drawBubbles():
    global xbubbles, ybubbles, xspeed, yspeed,livesleft,colour,score,bubblecolours
    for i in range (0,len(bubbles)-1):
        ## reverse the directions of the bubble and take away a life when the player collides with a bubble
        if collisioncharacterandbubbles (i)==True:
            xspeed[i]=xspeed[i]*-1
            yspeed[i]=yspeed[i]*-1
            livesleft = livesleft-1
            print("collision bw character and bubble")
        
        ## reverse the direction if the bubbles any wall    
        if xbubbles[i]-radius[i]<=0 :

            xspeed[i]=xspeed[i]*-1
        if xbubbles[i]+radius[i]>=800:

            xspeed[i]=xspeed[i]*-1
        if ybubbles[i]-radius[i]<=0  :

            yspeed[i]=yspeed[i]*-1
        if ybubbles[i]+radius[i]>=800:

            yspeed[i]=yspeed[i]*-1


        xbubbles[i]=xbubbles[i]+xspeed[i]
        ybubbles[i]=ybubbles[i]+yspeed[i]
        bubbles[i] = screen.create_oval(xbubbles[i]-radius[i],ybubbles[i]-radius[i], xbubbles[i]+radius[i],ybubbles[i]+radius[i],fill=bubblecolours[i])
        if collisionharpoonandbubbles(i)==True:
            screen.delete(bubbles[i])
            del bubbles[i]
            print(bubbles)
            del radius[i]
            del xbubbles[i]
            del ybubbles[i]
            del xspeed[i]
            del yspeed[i]
            score = score +10
            
            print(len(bubbles))
            
            



























## draws the score and lives left on the screen
def drawStats():
    global livesleft, score,livesdisplay,scoredisplay
    
    livesdisplay=screen.create_text(65,10,text="lives left = " + str(livesleft),font = "Times 15")
    scoredisplay = screen.create_text(700,10,text = "Score = " +str(score),font = "Times 15")




























## detects keystrokes
def getKeyStroke( event ):
    global quitGame, xspeedcharacter, start, fire

    if event.keysym == "q" or event.keysym == "Q": #TESTS WHETHER THE USER PUSHED Q OR q
        quitGame = True
        
    elif event.keysym == "Right":
        xspeedcharacter = 4
        #how could you make the hiker fire a bullet?
    elif event.keysym == "Left":
        xspeedcharacter = -4

    
    
























## detects when a key is lifted
def keyUpHandler (event):
    global xspeedcharacter,currentx,missilex,fire,button,text,start
    if event.keysym == "Right" or event.keysym=="Left":
        xspeedcharacter = 0
    if event.keysym == "space":
        fire =True
        missilex = currentx
    if event.keysym == "Return":
        start =True
        screen.delete(button,text)























## returns the position of the mouse
def getMousePosition( event ):
    global xMouse, yMouse
    
    xMouse = event.x
    yMouse = event.y
    





















## detects a mouse click
def mouseClickDetector(event):
    global xclick, yclick

    xclick = event.x
    yclick = event.y
    










## gets called when the player presses the quit game button
def quitgame():
    global quitGame
    quitGame = True






## main game procedure
def runGame():
    global quitGame,missile,livesdisplay, scoredisplay
    ## generate the initial variables
    generateVars()
    
    ## run the game until quitGame is true 
    while quitGame==False:
        drawCharacter()
        drawBubbles()
        if fire==True:
            fireharpoon()
        drawStats()
        screen.update()
        sleep(0.01)
        for i in range (0,len(bubbles)):
            screen.delete(bubbles[i])
        screen.delete(character,missile,livesdisplay, scoredisplay)
        ## if all bubbles have been destroyed off the screen- end the game
        if len(bubbles)==1:
            screen.create_text(400,400,text="YOU WON!", font = "Times 30")
            screen.update()
            sleep(2)
            screen.delete(character)
            quitGame=True
        ## if the player loses all his/her lives- end the game
        if livesleft==0:
            screen.create_text(400,400,text="You Lost!",font = "Times 30")
            screen.update()
            sleep(2)
            screen.delete(character)
            quitGame=True
    
    root.destroy()      

















##
###CALLS THE MAIN PROCEUDRE runGame 1000 MILLISECONDS AFTER THE WINDOW IS CREATED
root.after( 2000, runGame )


#BINDS THE USER'S MOUSE-MOVEMENTS TO THE PROCEDURE getMousePosition(), DEFINED ABOVE.
#THAT IS, WHENEVER THE USER MOVES THE MOUSE, getMousePosition() GETS CALLED
screen.bind("<Motion>", getMousePosition )
screen.bind("<Button-1>", mouseClickDetector)

#BINDS THE USER'S KEY-STROKES TO THE PROCEDURE getKeyStroke(), DEFINED ABOVE.
screen.bind("<Key>", getKeyStroke)

screen.bind("<KeyRelease>", keyUpHandler)


## drawing the quit game button
drawRectangleButton = Button( root, text = "Click to quit", command = quitgame, anchor = CENTER)
drawRectangleButton.pack()
drawRectangleButton.place(x=400, y=0,width=100)

#CREATES THE SCREEN AND SETS THE EVENT LISTENER
screen.pack()
screen.focus_set()


#STARTS THE PROGRAM
root.mainloop()

    
    
