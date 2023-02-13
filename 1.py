import datetime
today = datetime.date.today()
currentyear = today.year
print(currentyear)
endyear=int(input("enter the ending year:"))
print("here is the list of leapyears")
for year in range(currentyear,endyear):
    if (year % 4 == 0) and (year % 100 != 0):
        print(year)
    if (year % 400 == 0) and (year % 100 == 0):
        print(year)
    
