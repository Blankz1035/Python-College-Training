# Program to determine corresponding grade from mark.

mark = int(input("Enter student mark: "))

if 70 <=  mark <= 100:
    print("1st Class Honours")
elif 60 <= mark < 70:
    print("2nd Class Honours, Grade 1")
elif 50 <= mark < 60:
    print("2nd Class Honours, Grade 2")
elif 40 <= mark < 50:
    print("Pass")
else:
    print("No Award.")