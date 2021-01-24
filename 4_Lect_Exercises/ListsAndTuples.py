# Program to example the use of lists within Python.

# Eg.1 - How to define a list.
users = ['andy', 'majella', 'sebastian', 'sean', 1, 2, 3]
print("Print out of list: ", users)

# Eg. 2 -> An empty list 
empty_list = []
empty_list2 = list()  # creates an empty list using list class.

# Eg. 3. create a list with a specified number of items.
scores = [0] * 10  # This will create a list with 10 elements with value 0

values = list(range(10))  # [0,1,2,3,4...]

# Inbuilt functions useful for lists:
# Python provides a number of useful built-in functions for processing lists.
# len returns the number of items in the list
# sum returns the total of the numbers in the list
# sorted returns a sorted copy of the list
# min returns the smallest number, or the string that's first in alphabetical order
# max returns the largest number, or the string that's last in alphabetical order
# All of these functions will act on a list. be careful that the type is correct when using this.


# eg. 4. -> Adding an item to the list can be done using the append() function. 
# Append is add at end.
# Tip: use the append function to add and store values in a list during a while/for loop.
###### Lists provide a number of other methods that are called using dot notation, such as
# list_variable.append(item)
# They are:
# list_variable.extend(other_list)
# Extend the list by appending all the items from the other_list
# list_variable.insert(i, x)
# Insert an item x at a specified position i.
# list_variable.remove(x)
# Remove the first item from the list whose value is equal to x.
# list_variable.pop([i])
# Remove the item at the given position i in the list, and return it.
# If no index is specified, pop() removes and returns the last item in the list.
# (The square brackets around the i in the method signature denote that the parameter is optional, not that
# you should type square brackets at that position.)
# list_variable.clear()
# Remove all items from the list.
# list_variable.index(x[, start[, end]])
# Return the index in the list of the first item whose value is equal to x.
# list_variable.count(x)
# eturn the number of times x appears in the list.
# list_variable.sort()
# Sorts the list items in order
# list_variable.reverse()
# reverses the order of the list items

# sorting by default does lowest to highest. You can add additional parameters to aid this, or use the reverse function. Eg. marks.sort(reverse=True)
# Sort and Sorted can be seen as the same. However sorted returns a copy of the list and keeps the original list in tact. Sort will sort the list changing the original.


# eg. 5 -> Processing: You can process loops using for loops. We are looping over a sequence of elements from a list.
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

for day in weekdays:
    print(day)


if 'Monday' in weekdays:  # Case sensitive.
    print("found in list using if statement")
else:
    print("didnt find in list.")


# eg. 6 Using the split() function will split a string by default with spaces between. Such as Hello World becomes ['Hello', 'World']
# You can specify a split delimitter by saying .split("<split>")
# You can Limiting Splits With Maxsplit using .split("<split>", maxsplit=n)

# You can then use the join() function to join a list together. This will create a string from this. an example is an IP address that is broken up. You can join this altogether.


# eg. 7 list comprehension
# You can create a list using expressions.  A simple way to do this is by using a for loop and looping over a set of records for an expression.
# You can also do this using a one line expression. Eg: [ expression for x in sequence if condition ]
# Example: even squared numbers:  squares = [ x**2 for x in range(11 if x % 2 == 0)]

# eg 8. You can delete elements at indexes in a list. You do this by saying del list[index]. All subsequent items will shift down the list.


# eg 9. Taking slices of lists can be done using the following notation: variable[start:end] this will take up to but not including index end.

# eg. 10 -> Copying a list. A list can be reference by one or more variables. If you want to assign a copy of the list, you need to use [:] operator or use x = y.copy().

# eg 11 -> Nested lists is a list that occurs as an element in antoher list. an example would be the use of X and Y cords.


###### TUPLES:
# A tuple is a sequence of values. The values can be any type, and they are indexed by integers, so in that
# respect tuples are a lot like lists. The important difference is that tuples are immutable. That means,
# once you create a tuple, you cannot change the individual elements contained in it.
# Tuples are used to group values together. For example, in Python network programming, to connect to
# a socket you specify the host address and port number as a tuple, e.g. (“localhost”, 6666).
# It is common to enclose the definition of tuples using brackets.

# To create a tuple, you must include a comma after the value in the bracket. A normal value in a bracket is not a tuple!
# You can also create by using tuple() class.


###### SETS:
# a set is an unordered collection of distinct objects (for more details on the types of objects
# that can be stored in a set.  Sets have
# similarities with lists, but an imprtant difference is that the items in a set must be unique. 
# Sets can be used to remove duplicates within a list. 
# You can convert the list into a set, using the code: set(list_variable)

# Selection Set Operations
# len(s) Return the number of elements in set s (cardinality of s).
# x in s Check if x is an element of the set s.
# x not in s Check if x is not an element of the set s.
# s.copy() Return a shallow copy of the set s (i.e. a new set, not a reference to the set s).
# s.add(elem) Add element elem to the set s.
# s.remove(elem) Remove element elem from the set s. Raises KeyError if elem is not
# contained in the set.
# s.discard(elem) Remove element elem from the set s if it is present.
# s.pop() Remove and return an element from the set s. Raises KeyError if the set is empty.
# s.clear() Remove all elements from the set s.


number = 1
list = [2,3,4,5,6,7,8,9]
if number not in list:
    print(list) 

print(list[:6])





