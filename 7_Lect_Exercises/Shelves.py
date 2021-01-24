# Shelves as Persistent Dictionaries
# The purpose of the shelve module is to provide persistent data storage using a dictionary-like object.
# A shelve provides simple database functionality but stores the information in a file.
# To ue the shelve module in a Python program, you need to import it:
# import shelve
# Importing the entire module in this way gives access to all features, but they must be prefixed with the
# module name.
# To create a shelve object, use the open function:
# database = shelve.open(filename)

# The reason we do the import this way is to avoid a name conflict with the built-in function open.
# For example:
# The argument “english-spanish” corresponds to a file english-spanish.dat. If the file
# exists, the variable eng2sp provides access to it. If it doesn't already exist, a new empty file will be
# created.
# The shelve object functions as if it is a dictionary. Insert items into the shelve as you do for a
# dictionary:
# database[key] = value
# For example:
# Similarly you can access a value corresponding to a key using [] syntax
# You can display the shelve-dictionary keys:
# and iterate through the contents of the shelve:
# 
# # In other words, shelves are like Python dictionaries that are associated with an external file. A
# shelve can be thought of as a dictionary that persists after the program has terminates. Just as with a
# dictionary, a shelve's keys must be unique, and it must be an immutable type (e.g. a string, number or a
# tuple).
# To close the shelve file, use the shelve function close:
# shelve_variable.close()
# When you open the shelve again, you can access its data.



# Dictionary Comprehensions
# Dictionary comprehensions are just like list comprehensions, except that you group the expression
# using curly braces {} instead of square braces [].
# { key:value for var in sequence }
# Also, the left part before the for keyword expresses both a key and a value, separated by a colon. The
# notation is specifically designed to remind you of list comprehensions as applied to dictionaries.
# https://www.python.org/dev/peps/pep-0274/
# For example, you can create a dictionary containing as pairs each integer and its square:
# {i:i*i for i in range(1,10)}

# Count the frequencies of a letter in a string:
# freq = {letter: text.lower().count(letter) for letter in ascii_lowercase}

# YOu can then determine the max = max(freq,key=freq.get)

# The key keyword specifies how the maximum in the dictionary should be determined; in this case, by
# using the get() method, so that it returns the key corresponding to the largest value.

# In a similar way, you could create a dictionary containing as items each word in the text and the length
# of the word. 
# 
# First, I want to remove all punctuation marks from the text. This can be done using the
# string method translate(), which requires a “translation table” to specify the replacement
# characters.
# This can be done in a number of ways, but the following approach demonstrates another dictionary
# comprehension:
# The built-in function ord returns the Unicode value for a character. This translation table can then be
# used to replace each punctuation marker in the text with None (or alternatively an empty string could
# be used).

# EG:  translation = {ord(c): none for c in ".,:"}

# Find out longest word:   word_lengths = {word:len(word) for word in new_text.split()}



