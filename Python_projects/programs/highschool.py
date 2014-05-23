cred = int(input("how many credits do you have?"))
neededcreds= 30 - cred
if cred >= 30:
    lit= input("have you passed the lit test?")
    if lit == "yes":
       hours = int(input("how many hours have you completed?"))
       needed= 40 - hours
       if hours >= 40:
            print ("you can pass!")
       else:      
            print ("you need " + str(needed) + " hours to pass") 
    else:
        print ("you cannot pass!")
    
else:
    print ("you need " + str(neededcreds) + " more credits")

