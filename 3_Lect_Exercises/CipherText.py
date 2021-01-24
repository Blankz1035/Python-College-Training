# Program to demonstrate the use of encryption of text
# We replace each letter with its position in the alphabet . the orginal message is known as plaintext and the cipher is known
# as cipher text

from string import ascii_lowercase, ascii_uppercase #abcdef... wxyz

# input a message 
plaintext  = input("Enter a message: ")

ciphertext = ""

# for each character, covert to lower case
for character in plaintext.lower():
    # if the character is not a letter, skip this
    if not character.isalpha():
        continue # skips this character 
    else: 
        # get position of the letter in the alphabet
        index = ascii_lowercase.index(character)

        # add to cipher text
        ciphertext += str(index) + " "

print("The cipher text is: ", ciphertext)

# You can also use the pass statement which will allow a piece of logic to skip. example if you have a loop, you can have a pass statement 
# in here to skip the logic. this allows you to keep this code in the project without removing.

# Cipher exercise: 
# Julius Caesar is credited with a basic substitution cipher in which he shifted each
# letter of the alphabet along by 3 places. The original message is referred to as the
# plaintext, represented in lowercase characters, and the enciphered message is
# referred to as the ciphertext, represented in uppercase characters.
# So a is enciphered as D, b is enciphered as E, … The letters at the end of the alphabet (x, y and z)
# wrap-around to be substituted by the first three

newplaintext = input("Enter a new plain text to be encrypted: ")

newciphertext = ""

for c in newplaintext.lower():
    # For each character in the message
	# if it's a letter
	if c.islower():
		# convert it to a number
		number = ascii_lowercase.index(c)
		# add 3 to the number        
		new_number = (number + 3) % 26
		# find the UPPERCASE letter for the new number
		new_letter = ascii_uppercase[new_number]
		# add the letter to the ciphertext
		newciphertext += new_letter
	# otherwise just add it on
	else:
		newciphertext += c 


#print("find ", ascii_lowercase.find('y'))

# Each lower case letter is in the range 97-122 (26 characters.)
print(newciphertext)