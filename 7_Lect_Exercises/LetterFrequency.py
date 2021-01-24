# Program to demonstrate dictionaries : letter frequency
from string import ascii_lowercase

text = input("Enter a phrase: ").lower()
# frequencies = {letter: text.lower().count(letter) for letter in ascii_lowercase}

# print("Letters  Frequencies")

# for l in sorted(frequencies.keys()):
#     print(f"{l} {frequencies[l]}")


# Part 2 : Using the zip function with a dictionary of letters.
# Create a tumple list and convert to a dictionary.

print()
print("Part two of the exercise using tuples and dictionaries:")
letter_freq = dict(zip(ascii_lowercase, [0]*26))

for l in text.lower():

    if l.isalpha():
        if l in letter_freq:
            letter_freq[l] = text.count(l)

for l in sorted(letter_freq.keys()):
    print(f"{l} {letter_freq[l]}")

print(f"Most popular letter: {max(letter_freq, key=letter_freq.get)} with {max(letter_freq.values())}")
