# Program to test year period for leap years
# A year is a leap year if it is divisible by 4, unless it is a century year (divisible by 100) that is not
# divisible by 400. e.g. 1800 and 1900 were not leap years; 1600 and 2000 were. 

startYear = int(input("Enter a starting year: "))
endYear = int(input("Enter a ending year: "))

while startYear <= endYear:

    if startYear % 400 == 0 or (startYear % 4 == 0 and not startYear % 100 == 0):
        print(f"Year {startYear} is a Leap Year")
    
    startYear +=1

