red = int(input("how many drops of red dye did you put?"))
while red > 10:
    print("Too high!  Try again.")
    red = int(input("how many drops of red dye did you put?"))
if red >= 0 and red <= 10:
    blue = int(input("how many drops of blue dye did you put?"))
    while blue > 10:
        print ("Too High! Try again.")
        blue = int(input("how many drops of blue dye did you put?"))
    if blue >= 0 and blue <= 10:
        if red == 0 and blue > 0:
            print ("the mixture is blue")
        if blue == 0 and red > 0:
            print ("the mixture is red")
        if blue > 0 and red > 0:
            print ("the mixture is purple")
        if blue == 0 and red == 0:
            print ("the mixture is clear")
       
            
     
        
