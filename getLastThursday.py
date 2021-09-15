
import datetime
from datetime import date, timedelta    #to find day corresponding to date
import calendar                         #to find last day

def getLastThursday(input_month):                       #to get date of last Thursday
    month=int(input_month)
    year=2021
    lastday=calendar.monthrange(year, month)[1]         #return lastdate of month
    born = datetime.date(year,month,lastday)         
    last = born.strftime("%A")                          #return day corresponding to lastdate
    day_delta = datetime.timedelta(days=-1)             
    start_date = born                                   #lastdate of every month
    end_date = start_date + 7*day_delta                 #date 7 days before lastdate

    for i in range((start_date - end_date ).days):      #return date of last Thursday 
    
        dateforThursday=start_date + i*day_delta        #give every date of last week
        day1=dateforThursday.strftime("%A")             #day corresponding to date
        if (day1 == 'Thursday'):                        #if it is thursday then return date of thursday
            return dateforThursday

input_date=input("Enter month numer in format- 'mm' = ")    #object
print(getLastThursday(input_date))
