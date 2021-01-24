# Program to cipher text inputted from the user via substitution - by Andy Blankley
from string import ascii_lowercase

# Input plaintext from UI
plaintext = input("Enter your plaintext: ")

# Set cipher text string
ciphertext = ""

# Set N = 25 i.e n will equal z in the ascii lowercase alphabet where a = 0
# Utilize this when it comes to the formula for substitution [n - index] = new character
n = 25

# Loop through each character. Make lower to avoid exceptions.
for c in plaintext.lower():
    # Verify if a space / not an alpha character added.  If so, add a space to the ciphertext
    if not c.isalpha():
        ciphertext += " "
        continue

    # Use formula of N - (index of c). i.e. when c is a,  index will be 0.  so n(25)-0 = 25. 
    # This means our character will be z
    ciphertext += ascii_lowercase[n-(ascii_lowercase.index(c))]

print("The cipher text is: ", ciphertext)
print("\nTo reverse, simply repeat: ")

plaintext = ""
for x in ciphertext:
    if not x.isalpha():
        plaintext += " "
        continue
    plaintext += ascii_lowercase[n-(ascii_lowercase.index(x))]

print("The deciphered text is: ", plaintext)
