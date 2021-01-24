# Program to demonstrate checking if a password is in a list.
# Cracker the password hacker.

password = input("Enter a password to check: ")
lineNum = 1

#1. open a file with texts on a new line.
with open("6_Lect_Exercises/test.txt") as file_in:

    #2. loop through each line.
    for word in file_in:

        #3. check for same and output.
        if password == word.strip():
            print(f"Oops. Password '{password}' has been found at line {lineNum}.") 
            break

        # Add count
        lineNum += 1

    else:
        print("Password not found in list.")