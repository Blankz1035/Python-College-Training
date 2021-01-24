# Program to generate a star wars name by Andy Blankley

# Add in some programming details / pseudo code for the program
# Input firstname
firstname = input("Enter your first name: ")
# Input lastname
lastname = input("Enter your last name: ")
# Input mothers_maiden_name
mothers_maiden_name = input("Enter your Mothers Maiden name: ")
# Input birthplace
birthplace = input("Enter your Birth Place: ")

# generate star_wars_name
#1. firstname - get first 3 characters of fname and 2 charcters of lname for first input
#2. lastname - take MmN and birthplace 2 and 3rd characters respectively.
#3. combind these results and make first letter of each word uppercase using title() function
sw_firstname = firstname[:3] + lastname[:2]
sw_lastname = mothers_maiden_name[:2] + birthplace[:3]
sw_name = (sw_firstname + " " + sw_lastname).title()

# print start_wars_name
# Fixing uppercase in middle of name -> use on title() or lowercase etc.
print("Your star wars name is: ", sw_name)

