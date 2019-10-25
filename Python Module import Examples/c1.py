import calendar

t=calendar.TextCalendar(calendar.MONDAY)
c=t.formatmonth(2019,3)
print(c)

t=calendar.HTMLCalendar(calendar.MONDAY)
c=t.formatmonth(2019,3)
print(c)
