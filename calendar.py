import calendar

a,b,c=map(int,input().split())
x=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
print(x[calendar.weekday(c,a,b)])
