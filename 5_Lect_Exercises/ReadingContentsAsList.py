# Program to demonstrate reading a text file as a list of lines.
# The readlines() method returns a list representing the contents of the file; each line is a separate
# item in the list. 

# Example: Read in a text file and pick a random word from the list.

from random import choice, randint
from string import punctuation

print()
wordlist = []

with open("6_Lect_Exercises/test.txt") as file_in:

    # Put all into the alllines as a list.
    alllines = file_in.readlines()

    # Randomly pick two words from list
    for word in alllines:
        wordlist.append(word.split(" "))

    word1 = choice(choice(wordlist)).strip().capitalize()
    word2 = choice(choice(wordlist)).strip().capitalize()

    # Pick a random digit.
    digit =  randint(0,9)

    # Randomly select a special character
    character = choice(punctuation)

    # password generation
    password = word1 + str(digit) + word2 + character

    print(f"New password suggestion: {password}")


################################################
# You can also read an entire file as a complete string using the read() method.
# This will read the entire contents as a string for further processing.
# Now i can use splitlines() method to split the sequnce into its lines.
# You can also use the count() to count how many occurrences of a string is in a passage. 
# Length of the passage can also be done by using the len() function to count how many lines.

# count all words  ->  len(contents.split())
# count all lines  ->  len(contents.splitlines())
# occurrences of word - > len(contents.count("string"))



