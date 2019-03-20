# Finds the number of Sundays that fell on the first of the month in the 21st
# century
# This one is hacked together and can definitely be improved

import time

def increment_day(current_date):
    # Increment day of week
    current_date[0] = (current_date[0] + 1)%7

    # Get days in the current month
    days_this_month = days_in_month[current_date[2]]
    # Add an extra day if it's February and a leap year
    if current_date[2] == 1 and is_leap_year(current_date[3]):
        days_this_month += 1

    # Increment day of month
    current_date[1] = (current_date[1] + 1)%days_this_month
    # If we moved to a new month increment the month
    if current_date[1] == 0:
        current_date[2] = (current_date[2] + 1)%12
        # If we moved to new year increment the year
        if current_date[2] == 0:
            current_date[3] += 1

def is_leap_year(year):
    if year%4 == 0:
        if year%100 != 0:
            return True
        elif year%400 == 0:
            return True
        else:
            return False
    else:
        return False

start = time.clock()

# Number of days in each month (not counting leap years)
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# Current date in format [weekday,day,month,year]
# All entries are zero-indexed apart from year
current_date = [0,0,0,1900]

sunday_firsts = 0

while current_date[1:] != [30,11,2000]:
    increment_day(current_date)
    if current_date[3]>1900 and current_date[:2] == [6,0]:
        sunday_firsts += 1

end = time.clock()

print sunday_firsts
print "Time taken: ", end-start, " s"
