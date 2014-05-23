a = int(input("Please input the a term"))
b = int(input("Please input the b term"))
c = int(input("Please input the c term"))

if a == 0:
    quadterm = ''
elif a == -1:
    quadterm = '-x^2'
elif a  == 1:
    quadterm = 'x^2'
else:
    quadterm = str(a) + 'x^2'

if b == 0:
    linterm = ''
elif b == 1:
    linterm = '+ x'
elif b == -1:
    linterm = '- x'
elif b < 0:
    linterm = '-' + str(-b) + 'x'
else:
    if a == 0:
        linterm = str(b) + 'x'
    if a > 0:
        linterm = '+' + str(b) + 'x'
    

if c == 0:
    conterm= ''
elif c < 0:
    conterm = '-' + str(-c)
elif c > 0:
    conterm = '+' +str(c)
    if b == 0:
        conterm = str(c)

print (quadterm+linterm+conterm)
