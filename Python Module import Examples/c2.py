import calendar
#c=calendar.calendar(2019,2,2,2)
#print(c)
c=calendar.month(2019,5)
print(c)
print(calendar.isleap(2012))
print(calendar.leapdays(2012,2021))

for month in calendar.month_name:
   print(month)
for day in calendar.day_name:
   print(day)

print(calendar.month_name)

