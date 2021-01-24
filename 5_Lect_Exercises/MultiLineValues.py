# Program to demonstrate mult line processing to access values
# We will utilize the split() function to process the data.

# Often data within file will be on multiple lines. We need to be able to process this accordingly. Additionally for data analysis too.
# Example would be a first and lastname. "John Doe". We can split this to be first and last name.

# To separate the line into two values, use the string .split() method:
#  firstname, lastname = hero.split()
# By default the .split() method splits the string into components using spaces within the string.

print()
print("This program will generate a user name from input line")

with open("6_Lect_Exercises/users.txt") as file_users:
    
    for user in file_users:
        user.strip()

        if user.count(" ") == 1:
            first, last = user.split()

            # User is valid so process.
            username = (first[0] + last).lower()
            print(f"Username is: {username}")
        else:
            print("User not valid")


# However, it is very important to note that the split() function will generate a runtime error if there are multiple spaces between words!
# This will be an exception. The same will occur for a blank line! Or if there are multiple spaces.
# Split() will only really work for 2 words.

# A way to deal with this is to check the spacing between the words i.e check for white space. 
# However best approach is to use exception handling.

###############  COMMA SEPARATED VALUES: ############
# CSV files are often sep by , or by colons. We can handle this factor by using the split function still, but passing an arg.
# Spreadsheets can be converted to csv for data science usage for programs. 
# You must specify the delimitter when it comes to spliting the values.
# Additionally, remember that for certain data you may need to specify a parameter for encoding! exampel: ISO-8859-1  latin-1

# TIP: You can also specify a maxSplit arg for the split(). This will split only the specified number of times and the final will
# push all into after. This can be go to split a string and if you need to further process the remaining string.
print()
print("CSV file input!")
print()
with open("6_Lect_Exercises/testcsv.csv") as csv_in:

    for line in csv_in:        
        id, name, email, age = line.split(",")
        print(f"Line details: ID {id}, Name {name}, Email {email}, Age {age}")
        