num= int(input("please input the amount you wish to withdraw"))

for bill in [100,50,20,10,2,1]:
    if bill== 100 and num/bill >=1:
        r = num/bill
        intpart,decimalpart = int(r),r-int(r)
        print (str(intpart) + " 100 dollar bills needed" )
        num = num-(intpart*100)
    elif bill==50 and num/bill >=1 :
        r = num/bill
        intpart,decimalpart = int(r),r-int(r)
        print (str(intpart) + " 50 dollar bills needed" )
        num = num-(intpart*50)
    elif bill==20 and num/bill >=1 :
        r = num/bill
        intpart,decimalpart = int(r),r-int(r)
        print (str(intpart) + " 20 dollar bills needed" )
        num = num-(intpart*20)
    elif bill==10 and num/bill >=1 :
        r = num/bill
        intpart,decimalpart = int(r),r-int(r)
        print (str(intpart) + " 10 dollar bills needed" )
        num = num-(intpart*10)
    elif bill==5 and num/bill >=1 :
        r = num/bill
        intpart,decimalpart = int(r),r-int(r)
        print (str(intpart) + " 5 dollar bills needed" )
        num = num-(intpart*5)
    elif bill==2 and num/bill >=1 :
        r = num/bill
        intpart,decimalpart = int(r),r-int(r)
        print (str(intpart) + " toonies needed" )
        num = num-(intpart*2)
    elif bill==1 and num/bill >=1:
        r = num/bill
        intpart,decimalpart = int(r),r-int(r)
        print (str(intpart) + " loonies needed" )
        num = num-(intpart*1)
       
    
        
