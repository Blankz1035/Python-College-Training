# Program to discuss the date time module.

# The dates can come in different formats, and with or without a time, and can also refer to different
# timezones. Python provides a number of modules to assist with manipulating dates and times,
# including time and datetime.

# Unix Time: How Python (and Computers in General) Count Time
# Unix Time is a system for describing a point in time. It is the number of seconds that have elapsed
# since the Unix Epoch (minus leap seconds) which was arbitrarily defined as 00:00:00 UTC on the 1st of
# January 1970. The name comes from the fact that it was originally implemented on UNIX operating
# systems https://en.wikipedia.org/wiki/Unix_time. UTC stands for Coordinated Universal Time and
# refers to the time at a longitude of 0° https://en.wikipedia.org/wiki/Coordinated_Universal_Time.
# Python, and nearly all programming languages, incorporate the concept of Unix time. Python provides
# a module called time which contains a function time() that returns the number of seconds since the
# Unix Epoch https://realpython.com/python-datetime/:

# Sample program:
import time
print("Number of seconds since the unix epoch: ", time.time())



# The time module also provides a function gmtime() which takes a parameter representing the
# number of seconds since the Epoch and returns the current UTC time as a time structure, e.g.

# This contains 9 values, representing date and time as follows
# Variable          Meaning                                         Example
# tm_year           The year 2020
# tm_mon            The month as a number (1-12)                    11 is November
# tm_mday           The day of the month (1-31)                     3 is the 3rd of November
# tm_hour           The hour using a 24-hour clock                  15 is 3pm
# tm_min            The minutes past the hour (0-59)                59 (so 15:59 or 3.59pm)
# tm_sec            The seconds past the minute (0-59)              19 (so 15:59:19)
# tm_wday           The day of the week (0-6, 0 is Monday)          1 is Tuesday
# tm_yday           The day of the year, 1-366                      308 is the 3rd of November for 2020 (a leap year)
# tm_isdst          Daylight Savings Time in effect?                0 or 1 0 means Daylight Savings Time is not in effect

# https://docs.python.org/3/library/time.html#time.struct_time


# By default gmtime() returns the current time. 
# You can also use it to check your system’s definition of the “Epoch”, by passing in zero as the
# parameter:
# This shows that this system is using the UNIX Epoch, 00:00:00 UTC on the 1st of January 1970.
# https://docs.python.org/3/library/time.html#time.gmtime
# Another function localtime() is similar, but it returns the local time:
# In this case, Daylight Savings Time is in effect.

# Current utc time
print(time.gmtime())
# 0 Seconds since epoch time.
print(time.gmtime(0))

## Local time 
print(time.localtime())



# Standard Date Format
# Different countries/regions represent dates in different ways. In Ireland, we usually use the format dd/
# mm/yy, e.g. 03/11/2020 is the 3rd of November 2020. However, in the US, this would be represented as
# 11-03-2020. 
# 
# To avoid confusion, the International Organization for Standardization (ISO) specifies the
# following format for representing dates and times: https://en.wikipedia.org/wiki/ISO_8601
# YYYY-MM-DD HH:MM:SS
# for example 2020-11-03 17:20:15
# https://realpython.com/python-datetime/#how-standard-dates-can-be-reported



# The datetime Module
# Python’s datetime module provides a number of classes for working with dates and times, including:

# date: To represent a date. It contains the attributes: year, month, and day.

# time: To represent an idealized time, independent of any particular day, assuming that every day has
# exactly 24*60*60 seconds. (There is no notion of “leap seconds” here.) Attributes: hour, minute,
# second, microsecond, and tzinfo (timezone information).

# datetime: A combination of a date and a time. Attributes: year, month, day, hour, minute,
# second, microsecond, and tzinfo.

# timedelta: A duration expressing the difference between two date, time, or datetime
# instances (objects) to microsecond resolution.

# https://docs.python.org/3/library/datetime.html
# 
# The module provides a combination of class methods and instance methods. A class method is called
# in reference to the class itself, e.g. datetime.date.fromisoformat(date_string). An
# instance method is called on an instance (object), e.g. the datetime.date instance method
# fires_date.replace(), which returns a date object with specified values replaced.
#
#  Working with date Objects
# A date object represents a date, containing a year, month and day. You can create a date object using
# the syntax: date(year, month, day)
# where year, month and day are numbers that produce a valid date.
# 
# For example, new_years_eve is a date object associated with 2020-12-31 (31st December 2020):
# You can access values of the individual attributes:

# If you provide invalid numbers, you’ll get a ValueError:
# There’s no such date as the 30th of February

# import datetime

# The date class provides a class method today() to generate an object representing today’s date:
# this_date = datetime.date.today()

# The class method fromisoformat(date_string) returns a date object from a
# date_string in the format YYYY-MM-DD:

# The instance method isoformat() returns a string representing the date in YYYY-MM-DD
# format:
# day = datetime.date(2020,10,1)
# day.isoformat()

# The instance method replace() returns a date with the same values, except those specified by
# keyword arguments year, month and day.
# For example, to change the month:
# day.replace(month=3) etc


##################


# The instance method strftime(format) returns a string representing the date, specified by a
# format string.

# For example, if you want to display the date in the format dd/mm/yyyy:
# day.strftime("%d/%m/%y")

# Alternatively, you may want to display the date in a more readable format for humans:
# Details of the format string specifiers are available in the Python Documentation online:
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes


#Example for storing dates in a dictionary:
# months_dict = dict((name, number) for name, number in zip(calendar.month_name[1:], range(1,13)))

# Maximum and Minimum Dates
# A list of date objects can be processed using the min function, to identify the earliest and latest dates
# in the list.

# If you are splitting a date and its not in ISO format, you need to split the string and reformat it when passing into a date object.
# eg. dd, mm, yy = date_string.split("/")
# Alternatively, you could use the datetime class method strptime(date_string,format)
# returns a datetime object corresponding to a date_string, parsed according to the specified
# format



# Date and Time Calculations with the timedelta Class
# A timedelta object represents a duration, the difference between two dates or times.
#  https://docs.python.org/3.8/library/datetime.html#timedelta-objects

# This is useful when you want to determine the time difference between two dates/times, or to calculate
# a date or time based on an adjustment to another date or time. It’s important to ensure that you’re
# working with dates/times in the same timezone, or the results will be incorrect.


# A timedelta object represents a time difference in days, seconds and microseconds. If it
# represents the difference between two dates, then the seconds and microseconds will be zero.



# The datetime.datetime class
# A datetime object is a combination of a date and a time. It contains all the information from a date
# object and a time object and has the following attributes: year, month, day, hour, minute,
# second, microsecond, and tzinfo.
# https://docs.python.org/3.8/library/datetime.html#datetime-objects

# The class method now() returns the local date and time, whereas utcnow() returns the UTC time.
# They are the same at this time of year in Ireland:

# You can create a datetime object by specifying the values for year, month, day, hour, minute,
# second, microsecond. Omitted time values default to zero. For example:

# The class method fromisoformat(date_string) returns a datetime object using a string in
# ISO format: YYYY-MM-DD HH:MM:SS

# The above example also shows the instance method strftime() which returns a formatted date and
# time string.
# The class method strptime(date_string,format) returns a datetime object
# corresponding to a date_string, parsed according to the specified format. For example:

# If you are only interested in the date, leave out the time arguments:
# 
# Working with Date and Time in Python: datetime
# You can access each attribute of a datetime object:

# There are also the following instance methods:
# date() Return date object with same year, month and day.
# time() Return time object with same hour, minute, second, microsecond
# replace() Return a datetime with the same attributes, except for those attributes given new
# values by whichever keyword arguments are specified. This is similar to the replace() method
# provided by the date class.
# isoformat() Return a string representing the date and time in ISO format:

# The date and time are separated by the character T. You can change this by specifying a different
# separating character, such as a space, e.g.
# strftime(format)

# Return a string representing the datetime object, specified by a format string.
# Details of the format string specifiers are available in the Python Documentation online:
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
