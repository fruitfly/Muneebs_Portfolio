num = str(input("input any number between 1 and 100"))

while int(num) > 100:
     print ("must be between 1-100")
     num = str(input("input any number between 1 and 100"))



digits = len(num)

onesdigit = num[digits-1]

    
if onesdigit >= "4" or num >="11" and num <="20" and num != "2":
    print (num + 'th')
else:
    if onesdigit == '0':
         print (num + 'th')
    if onesdigit == '1':
        print (num + 'st')
    if onesdigit == '2':
        print (num + 'nd')
    if onesdigit == '3':
        print (num + 'rd')

    
# made in python 2.6.5
