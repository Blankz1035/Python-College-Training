# Functions 
def printScreen (string): 
    print(string)


print("Hello World")

a = input("Enter a user name") 
printScreen(a)

miles = float(input('Enter number of miles: '))
printScreen(miles)

num_users = int(input('How many new users? '))
printScreen(num_users)

longstring = '''This is a long string with extra line spaces
and here is some more '''
printScreen(longstring)



# Output
# Use the built-in function print print(“Hello World”)
# Separate multiple output with a comma:
# print(“Temperature is”, fahrenheit)
# The comma automatically inserts a space between the items in the output
# Another example: print(“Hello”, name)

# To output a blank line print()
# To round off to the nearest integer print(“Temperature is”, round(fahrenheit))
# To round off to 2 decimal places
# print(“Fahrenheit temperature is”, round(fahrenheit,2))

# Strings
# Strings are used to represent text data: a single character, a word, sentence or longer text.
# You can assign a string to a variable using matching quotes:
# username = 'jbloggs'
# message = "hello world"
# paragraph = '''In a hole in the ground there lived a hobbit. Not
# a nasty, dirty, wet hole, filled with the ends of worms and an
# oozy smell, nor yet a dry, bare, sandy hole with nothing in it to
# sit down on or to eat: it was a hobbit-hole, and that means
# comfort.'''
# Triple-quotes are used for multiline strings. Alternatively you can use the back-slash \ as a line
# continuation character