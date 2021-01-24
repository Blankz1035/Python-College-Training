# Program to calculate the difference from todays date and new years day.

import datetime

# get a date object representing today
this_date = datetime.date.today()

# Create a date object for new years day 2021
new_years_day = datetime.date(2021,1,1)
print("New Year's Day 2021 will be on a", this_date.strftime("%A"))

# Calculate the difference between two dates
delta = new_years_day - this_date
print("Number of days until New Year's Day: ", delta.days)

print(delta) # including time.

dicttt = {i:i*10 for i in range(1,11)}
print(datetime.datetime.fromisoformat("11/7/2020"))