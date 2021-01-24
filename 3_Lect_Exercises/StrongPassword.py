# Program to generate a strong password

from string import digits, punctuation
from random import choice

line = input("Input a line of text: ")

# Set password to empty text
password = ""

# for each word in line
for line in line.split():
    # get first letter in word and add letter to password
    password += line[0]

# Capitalise the password
password = password.capitalize()

# Randomly select a special character and add to the password
password += choice(punctuation)

# Randomly select a digit and add to the password
password += choice(digits)

print("Password is: ", password)