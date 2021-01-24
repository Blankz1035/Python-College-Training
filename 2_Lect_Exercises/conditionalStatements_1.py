# Program to demonstrate use of condition statements

username = input("Enter your username in lower case: ")

if username.islower():
    print("Thank you",username,"\nEntry Accepted!")
else:
    print("Oops! You have made a mistake! Try again.")


