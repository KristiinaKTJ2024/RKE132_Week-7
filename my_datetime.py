import datetime

now = datetime.datetime.now()

print(now.year) #kuvab preaguse aasta
print(now.month) #kuvab praeguse kuu
print(now.day)  #kuvab preaguse kuupäeva numbri (1-31)
print(now.hour) #kuvab tunni (0-23)

weekday = now.strftime("%A")
print(weekday)
