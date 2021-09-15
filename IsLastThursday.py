import datetime
from datetime import date  #to find day corresponding to date
import calendar

def isLastThursday(input_date): #to check whether input date is last Thursday or not.
    day,month,year=(int(i) for i in input_date.split(' '))
    born = datetime.date(year,month,day)
    dayname = born.strftime("%A") #return day from date

    if (dayname== 'Thursday'):  #if day is Thursday
        if(month==2 and day>=22 and day<=29): #if it is last Thursday in Feburary or not
            return True
        elif (day <= 31 and day>=24 ):  #if it is last Thursday in other month or not
            return True
        else:               #if not last thursday
            return False
    else:                       #if day other than Thursday
        return False  
date= input("Enter date in format- 'dd mm yyyy'   =   " )
func=isLastThursday(date)
print(func)