'''
Milestone Project 3
'''

### Imports
import calendar

### Learning 'calendar' import

# Creation of text calendar
# 'calendar.SUNDAY' states start of the month will be MONDAY
c = calendar.TextCalendar(calendar.MONDAY)

# Text formats a chosen month (2022, 6) and displays it
str = c.formatmonth(2022, 6)
print(str)


# Can access each month this way
""" for name in calendar.month_name:
    print(name)
 """

for day in calendar.day_name:
    print(day)