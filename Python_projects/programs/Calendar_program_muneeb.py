months = [ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
Calendar = [ ["Jan",31] , ["Feb",28] , ["Mar",31], ["Apr",30], ["May",31], ["Jun",30], ["Jul",31], ["Aug",31], ["Sep",30], ["Oct",31], ["Nov",30], ["Dec",31]]

date1 = "Aug 07 , 2013"
date2 = "Sep 10 , 2013"
def getDayNum (date):
    daynumfordate = date.split()
    return (int(daynumfordate[1]))
print (getDayNum(date1))


    

def getMonthname (date):
    monthnamefordate = date.split()
    return (monthnamefordate[0])

print (getMonthname("Aug 07,2013"))
   
def daysLeftinCurrentmonth (date):
    month = (getMonthname(date))
    daynow = (getDayNum(date))
    daysinmonth = Calendar[months.index(month)][1]
    return(daysinmonth - daynow)

def monthsInBetween (date1,date2):
    startMonth = getMonthname(date1)
    endMonth = getMonthname(date2)
    print (startMonth)
    print (endMonth)
    smonth = months.index(startMonth)
    emonth = months.index(endMonth)
    return ((emonth-smonth)-1)

print (monthsInBetween("Mar 07,2013","Apr 8, 2013"))


def calendarcalculate (date1,date2):
    days = 0
    days = (daysLeftinCurrentmonth(date1)) + (getDayNum(date2))
    
    for i in range (0, monthsInBetween(date1,date2)):
        daysinmonth = Calendar[months.index(getMonthname(date1))+n][1]
        days = days + daysinmonth
        n = n +1
    return days


print (calendarcalculate(date1,date2))
    
    
    
