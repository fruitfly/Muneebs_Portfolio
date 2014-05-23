function = input("Please input the function in the form: y=mx+b")

indexofm = (function.index("="))+1

indexofx = function.index("x")

if indexofx == function.index("=")+1:
    slope = 1
elif function[indexofm]=="-":
    slope = -1
else:
    slope = function[indexofm:indexofx]

if  len(function)==indexofx+1:
    yint = 0
 
else:
    indexofb = indexofx+1
    yint  = int(function[indexofb:len(function)])
    

print("the slope of the function is " + str(slope))
print("the y-intercept of the function is " + str(yint))

    

