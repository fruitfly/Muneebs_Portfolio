num1= int(input("Please input the first number"))
if  num1<=0:
    print ("there is no GCD for 0")
if num1 > 0:
    num2 = int(input("Please input the second number"))
    if num2<=0:
        print ("there is no GCD for 0")
    if num2 > 0:
        
        if num1 > num2:
            max1 = num1
            min1 = num2
        if num1 < num2:
            max1 = num2
            min1 = num1

        r = max1%min1
        while r != 0:
            max1 = min1
            min1 = r
            r = max1%min1
        print (min1)

    
    
    
    
