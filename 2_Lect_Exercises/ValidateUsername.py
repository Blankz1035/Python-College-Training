# Program to validate a username input based on certain criteria. - Andy Blankley

#Inputs
username = input("\nEnter a username: ")
print("Username entered:", username)

# Processing / Validations
# 1. Validate username length is between(and including) 4 and 8 characters long
# 2. Validate is only alpha numeric and no special characters
# 3. Validate first letter is lower case.

# Outputs
if username.isalnum() == False or not 4 <= len(username) <= 8 or not username[0].islower():
    print("\nOops! Username entered is not valid: ", username)
else:
    print("\nUsername validated successfully")

# End of program.
