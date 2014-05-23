players = ["Muneeb","Dumb person","Rich Guy","smart person","gary","john","bob"]
em3 = ["you","are","not","it"]
i = 0
print ("the ryhme is: you are not it!")
print ("the starting players are " + str(players))
for roundnum in range (0 ,len(players)-1):

    if len(players) == 2:
        i=0

    for wordnum in range (0,len(em3)):
       
        
        if wordnum != 0:
            i = (i+1)% (len(players))
            print(em3[wordnum] + "=" + players[i])

            if wordnum==3:
                print ("")
                print (players[i] + " is out!")
                players.remove(players[i])
                
                

        else:
            i=i%len(players)
            print ("")
            print(em3[wordnum] + "=" + players[i])
    

    if len(players) == 1:
        print ("")
        print ("the winner is " + str(players[0]))

    else:
        print ("")
        print ("the remaining player(s):  " + str(players))
        
