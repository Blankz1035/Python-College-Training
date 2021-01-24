# Program to demonstrate and discuss dictionaries and data structures

# Introduction to Dictionaries
# A dictionary is like a list, but more general. In a list, the index values (indices) have to be integers;
# in a dictionary they can be any immutable type (e.g a string, number or tuple).
# For example, this is a dictionary used to specify network proxy settings:
# proxy = { 'server' : 'proxy.ait.ie',
# 'port' = 3128,
# 'username' = 'b1234567'}
# You can think of a dictionary as a mapping between a set of indices (which are called keys) and a set of
# values. Each key maps to a value. 

# The association of a key and a value is called a key-value pair or sometimes an item.
# A dictionary can be used to represent various types of data:
# Key Value
# Student ID Exam Mark
# Name Phone Number
# Username Password
# Stock ID Quantity in stock
# Location Lattitude, Longitude
# ISBN Title, Author
# Attribute Value
# Lastname,Firstname Phone Number
# In each case, the key must be an immutable type, such as a string, number or a tuple. You cannot use a
# list as the key.


# Lets begin and create sample dictionaries:
# sample: English to Spanish words

eng2sp = {}  # define using curl braces
# Or you can use the dict() function

#length of function:  you can use the len() function to return how many key/value pairs in the dict.
#len(eng2sp)

eng2sp = {'one':'uno','two':'dos', 'three':'tres'}

# Inserting, Accessing and Changing items in a Dictionary
# To add items to the dictionary, you use square brackets: my_dictionary[key] = value

# This creates an item that maps from the key 'one' to the value 'uno' (the Spanish for 'one' is 'uno').
# You can use this [] syntax to access the value corresponding to a given key:
print(eng2sp["one"])

#IMPORTANT
# The same syntax is used to change the value corresponding to an existing key. In fact, the keys in a
# dictionary must be unique: if you tried to add a new item with the same key and a different value, you
# would just change the item's value.


# The dictionary method .get
# If you try to index a non-existent key in a dictionary, it will produce a KeyError:
# An alternative approach is to use the dictionary method .get(key), which returns the value
# associated with the specified key, or None if the key-value pair doesn't exist:

print()
print(eng2sp.get("two"))

# You can also specify a default value when trying to retrieve a value. This will stip the error.
# You can also specify a default value to use, in case the key does not exist in the dictionary:


# Printing a Dictionary
# If you print a non-empty dictionary, you see one or more key-value pairs with a colon between the key
# and value: 

# You can also create a dictionary using dict and a sequence of key-value pairs:
# dict = dict([('one':'uno'),('two':'dos')])

# When the keys are simple strings, it’s easier to specify pairs using keyword arguments:
# setting keys :  one="uno", two="dos"  etc
# However this will not work for identifier names that are not valid, such as numbers.


# Unpredictable Order
# But if you print eng2sp, you might be surprised by the order in which the items are presented:
# {'one': 'uno', 'three': 'tres', 'two': 'dos'}
# The order of the items is not the same as when the dictionary was created.
# In fact, if you type the same example on your computer, you might get a different result:
# In general, the order of items in a dictionary is not guaranteed. Python uses a technique (called
# Hashing) designed for very fast access, to determine where the key:value pairs are stored in a
# dictionary. You can think of the order of the dictionary items as unpredictable.
# But that’s not a problem because the elements of a dictionary are never accessed using integer indices.
# Instead, you use the keys to look up the corresponding values:
# The key 'two' always maps to the value 'dos' so the order of the items doesn’t matter. 



# Checking for keys and values
# The in operator also works on dictionaries; it tells you whether something appears as a key in the
# dictionary:
# To see whether something appears as a value in a dictionary, you can use
# "one" in eng2sp  -> locates a key value in the dictionary.
# values = eng2sp.values() ; "dos" in values.


# More commonly, you can apply the in operator directly to the result of the values() method: use in an if statement.


# Looping with Dictionaries
# Dictionaries can also be traversed using a for loop, but the loop will iterate only through the keys.
# If you want to access the corresponding value, then use the dict[key] syntax:
# or the .get() method:

# We can access the dictionary’s contents as a whole using the following dictionary methods:
# my_dictionary.keys() returns a dict_keys object containing a list of the keys
# my_dictionary.values() returns a dict_values object containing a list of the values
# my_dictionary.items() returns the a dict_values object containing a list of tuples
# where each tuple is a key-value pair
# The items() method allows you to loop through the key-value pairs together:
# If required, you can iterate through the key-value pairs in alphabetical order of the keys, by sorting the
# dictionary (which sorts the keys):
# Another way to achieve this is to sort the items:

# sorted(dict)

# DELETING AN ITEM IN THE DICT
# You can use the standard built in action del dict[key]
# If it does not exist an error is thrown. 

# If you want to empty the dictionary the method clear removes all items from the dictionary:
# my_dictionary.clear()
# Or setting the dictionary to a empty {}


########################
# Dictionaries and Tuples
# You can use a list of tuples to initialize a new dictionary:
# The built-in function dict() converts the list of tuples into a dictionary:
# The dictionary method update() also takes a list of tuples and adds them, as key-value pairs, to an
# existing dictionary:
# It is common to use tuples as keys in dictionaries (primarily because you can’t use lists).
# For example, a telephone directory might map from last-name, first-name pairs to telephone numbers.
# The expression in brackets is a tuple: directory["Bloggs","Joe"]
# You can use tuple assignment to traverse this dictionary.

# data_list = [('a',0), ('c',1)]
#data_dict = dict(data_list)
# data_dict.update([('d',3)])



