# Program to demonstrate exception handling and the due process.

# Introduction to Exception Handling
# Program errors detected during execution are called Runtime Errors. Whenever a runtime error occurs,
# it creates an exception. The program stops running at this point and Python prints out the traceback (or
# stack trace), which ends with a message describing the exception that occurred.
# https://buildmedia.readthedocs.org/media/pdf/howtothink/latest/howtothink.pdf (page 213)

# Example - diving a number by 0.

# Some common exceptions:
# NameError  - incorrect naming of functions / variables calling.
# ValueError - value issue. example like using split function or trying to convert an int of a decimal.
# IndexError - array out of bounds.
# TypeError - assignment of a value where not possible -> tuples.
# KeyError - indexing an array where key is not a valid variable.
# FileNotFoundError -> file not found in  current directory.
# ImportError -> issue importing a module feature.
# ModuleNotFoundError -> software package not available for importing.
# KeyboardInterrupt  -> program stopping by keyboard entering -> eg. ctrl + c
# IsADirectoryError -> File being opened is a directory.
# PermissionError -> File is read-only etc.


# When a runtime error occurs in a program, Python is said to raise an exception. If you do not
# specifically handle the exception, the exception will reach the user as an error message and the program
# will terminate.


# Approaches:
# There are two main approaches to runtime errors/exceptions in programming:
# 1. Try to predict and avoid them. This approach is called “Look Before You Leap”. This means
# that you should ensure that something is allowed first and do it only if it’s allowed.
# 2. Try and see: Try to run the code and then use exception handling to deal with the consequences.
# This is often referred to as “Easier to Ask Forgiveness than Permission”.
# For example, suppose you want to open a file in your program. There are a num,ber of things that
# could go wrong:
# • The file does not exist in the specified location
# • The file is not a file (it exists, but it's a directory)
# • You (and your program) does not have the required permissions to access the file.
# In the “Look Before You Leap” approach, you could write code to
# could check that the file exists
# and check that the file is actually a file
# and check that you have permission to open it

# if...else flow control. 

# However you can use try .. except control blocks to handle exceptions
# Exception Handling Syntax
# Python uses try-except to handle exceptions. The basic syntax is:
# try:
# run some code that could raise an exception
# except:
# run other code to deal with the exception raised

# The except block catches any and all exceptions that arise in the try block. It's far better to
# explicitly specify the individual exceptions that can arise. 

# It is best practice to always specify the individual; exception, rather than use the bare except clause.
# https://realpython.com/the-most-diabolical-python-antipattern/

# Additional Exception Handling Syntax
# You can add an else block to a try-except structure, in order to instruct the program to execute a
# certain block of code only in the absence of exceptions. The syntax is:
# try:
# # run some code that could raise an exception
# except SomeException:
# # run other code to deal with SomeException
# except SomeOtherException:
# # run other code to deal with SomeOtherException
# else:
# # run more code if no exception arose in the try block

# It's similar to how you can add an else to a while or a for. The code in the else block is only
# executed if no exceptions were encountered in the try block.

# Python also provides a finally clause in order to instruct the program to execute a certain block of
# code whether or not an exception arose. It can be used as a “clean up” operation after the tryexcept-else structure. The syntax is:
# try:
# # run some code that could raise an exception
# except SomeException:
# # run other code to deal with SomeException
# except SomeOtherException:
# # run other code to deal with SomeOtherException
# else:
# # run more code if no exception arose in the try block
# finally:
# # run more code whether or not an exception arose

# Traditionally, the finally clause was used to close a file after opening it, but this is not necessary
# when using the with statement to open a file.

# You can also give a user the option to try again by using a while loop. Loop over as usual. 
# You can have nested try except blocks.

