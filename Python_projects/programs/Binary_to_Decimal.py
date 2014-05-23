binary = input("please input the binary number")

def binaryToDecimal(binary):
    decimal = 0 
    a = binary[len(binary)-1]
    n = 1 
    for i in range (0,len(binary)):
        decimal = int(decimal) + int(a)*(2**i)
        a = binary[(len(binary)-1)-n]
        n = n+1

    

print(binaryToDecimal(binary))

