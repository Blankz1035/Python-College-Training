# Program to demonstrate functions and modular design
# Introduction to Functions
# A function is a named piece of code that performs a certain task. Functions serve two purposes:
# 1. Providing reusable code which avoids duplication
# 2. To simplify the design and implementation of a program.

# Code duplication has the following drawbacks:
# 1.Time wasted writing the same code twice or more.
# 2.This same code must be maintained (changed) in two separate places. This not only takes time, but
# you might change it in only one place, forgetting to repeat the changes elsewhere; with the result that
# your program won't work properly!
# Functions can be used to reuse code and avoid code duplication. This make programs more easily
# understood and easier to maintain.

# You can also reuse a function in a separate program. For example, if the roll_dice() function is
# saved in a file called dice.py you can import the function to use in any other program:
# Notice that, while the name of the file containing the function is dice.py when you import, you drop
# the .py extension.
# (Note: To successfully import from the dice.py file within Spyder, I had to start Spyder from the
# command-line in the directory that contained the dice.py file). 

# def functionNAme ():
    #body

# 1. The keyword def means “definition” - in this case, we are defining a function
# 2. The function name has to follow the same rules for variable names: letters, numbers and
# underscores.
# 3. Following the function name are brackets ()
# 4. Following the brackets is a semi-colon :
# 5. The body of the function is indented: this is the code that is executed when you use the function
# The if statement is used to ensure that the function is only called if the current file is executed as a
# program, not imported from another file. The built-in variable __name__ evaluates to the name of
# the current file. If __name__ evaluates as “__main__” it means that the current file is being
# executed, and so the hello() function call is executed. If __name__ doesn't evaluate as
# “__main__” it means the current file is being imported from elsewhere and therefore the
# hello() function call is not executed.

# Variables with identical names elsewhere in the program are
# distinct from the parameters and variables inside of the function body.

# Optional Parameters: def round(number, ndigits=None):
# You can set default parames in the the functiond definition. This will mean you can pass values or not, but a default will be taken in 
# the latter.

# Important: The order of default versus non-default parameters is important.
# The non-default parameters must come first. You cannot have a non-default parameter after a default
# parameter.
# Example: Function with default minimum and maximum password lengths
# For example, the following function checks if the length of a password is between specified minimum
# and maximum values, which default to 8 and 15 characters, respectively:

# Global and Local Variables
# A global variable is a variable defined in the “main” program and are said to have 'global' scope. A
# local variable is a variable defined within a function and are said to have local 'scope'.
# Local variables can only be accessed from within the function in which they were defined. For
# example, the function to roll two dice and calculate their total uses 3 local variables: roll1, roll2
# and total:

# Variables in the main program, outside a function, are considered global variables. Their values can be
# accessed within a function:

# If you want to change the value of a global variable within a function, then use the global keyword.

# The statement in the function
# global total
# tells Python that the variable total refers to the global variable.

# Global Variables are not recommended
# Functions can access global variables and modify them. Modifying global variables in a function is
# considered poor programming practice. It is better to send a variable in as a parameter or have it be
# returned in the return statement.

# Ideally a function should be considered to be a black-box with inputs and outputs. The function's
# input/output should be completely defined by its function header and return statement. Someone
# reading the program can tell the effect of the function from looking at the function call only. There are
# no side-effects, such as global variables being changed in the function. The only effect of a function is
# the return value (and modifications of list/object parameters).

# Ideally a function should be considered to be a black-box with inputs and outputs. The function's
# input/output should be completely defined by its function header and return statement. Someone
# reading the program can tell the effect of the function from looking at the function call only. There are
# no side-effects, such as global variables being changed in the function. The only effect of a function is
# the return value (and modifications of list/object parameters).


# Multiple Return Values
# Python Functions can return more than 1 value, if required. For example, the built-in function
# divmod() does “modulo” division. It divides one number by a second and returns a tuple containing
# • the number of times the second number divides in to the first (called the quotient)
# • the remainder after the division
# For example, 17 divided by 3 is 5 remainder 2
# quotient remainder
# You can assign the contents of a tuple returned by a function using multiple variables:

#amount,remainder = divmod(4,3)

# In general, you can use a tuple to return multiple values from a function. The difference in the syntax
# of the return statement is that you have multiple values, separated by a comma.

######
# The help information is provide in a documentation string, or docstring. A docstring is a tripe-quoted
# string started on the line immediately after the function definition header:
# define function: 
#   Add string here.
#   body


# Generating Documentation with pydoc
# Python provides a command-line utility, pydoc, for generating documentation from modules (Python
# files). The syntax is:
# pydoc module
# For example:
# pydoc dice2
# will generate documentation from the file dice2.py. Notice how the .py extension is dropped,
# similar to when you import a module.

# It also provides a mechanism to generate the documentation in web format, i.e. using html. The syntax
# is:
# pydoc -w module
# For example:
# This generates the documentation in html format and stores it in the file dice2.html:



# Function Annotations
# Python 3.5 introduced function annotations, also called type hints. They are optional.
#  https://www.python.org/dev/peps/pep-0484/
# Function annotations allow you to indicate the data types associated with function parameters and
# return values.
# For example:
# The function annotations specify that the name parameter should be type str (string) and the
# function will return a string.
#def greeting (name : str) -> str:
#return "hello" + name


def greeting(name: str) -> str:
    """[Greeting]

    Args:
        name (str): String parameter representing name 

    Returns:
        str: [description]
    """

    return "Hello" + name

################################### UNIT TESTING : ############################


# Python provides a number of modules for unit testing, the most straightforward of which is
# pytest. https://docs.pytest.org/en/latest/
# To install pytest using Anaconda, use the command: conda install -c anaconda pytest


# Testing with Pytest
# Pytest expects tests to be located in files whose names begin with test_ or end with _test.py. It
# also expects test cases to be included in functions whose names begin with test_.
# Tests are based on the assert statement. When Python encounters an assert statement it evaluates
# the accompanying expression, which we expect to be True. If the expression is False, Python raises
# an AssertionError exception. Pytest then flags a failed test.
# https://www.tutorialspoint.com/python3/assertions_in_python.htm

# example: def square(number):
#   return number * number
#
# def test_square():
#   assert square(5) == 25
# The assert statement says that we expect the result of square(5) to be equal to 25.
# Both functions are stored in a file test_square_function.py.
# To run the test, use the pytest utility on the command-line, followed by the name of the file:

# You can include multiple test cases, by including multiple assert statements

# In general, the test functions will be stored in a separate file, and the functions to be tested will be
#imported into that file.

# Testing with Floating Point Numbers
# Notice in the previous example how the assert functions store the expected results to 16 decimal
# places? This is because computers have difficulty representing floating point numbers exactly.
# Pytest provides a function approx that checks that two numbers (or two sets of numbers) are equal to
# each other within some tolerance, that is, an allowable error.
# Example: Testing “nearly equal” the using approx()
# For example:
# The default tolerance is 10-6, that is, 0.000001. That means that approx will consider values “equal” is
# they differ by no more than 0.000001.

# You can specify a different tolerance using a second parameter:
# EG: (29, approx(2, 3.456))
# In these examples, the values need only be within 0.01 to be considered “equal”.
# http://randycoulman.com/blog/2018/06/19/comparing-floats-in-tests/


# Running Multiple Tests from Multiple Files
# The previous examples demonstrated using pytest on a specific test file, using the synax:
# pytest test_filename.py
# You can run tests from multiple test files just by running pytest on its own:

# Command-line Options
# The pytest utility has command-line options that may be useful including
# -v verbose – displays details on tests run
# -x run the tests and stop as soon as the first test fails
# --collect-only only show the list of test
# For further information on testing in Python see https://docs.python-guide.org/writing/tests/ 


################################ TOP DOWN DESIGN: #######################
# Top Down Design and Modular Development
# It is easier to solve small problems than it is to solve big ones. Computer programmers use a divide
# and conquer approach to problem solving:
# • a problem is broken into parts
# • those parts are solved individually
# • the smaller solutions are assembled into a big solution
# These techniques are known as top-down design and modular development. Top-down design is the
# process of designing a solution to a problem by systematically breaking a problem into smaller, more
# manageable parts


# Modular Development
# Top-down design leads to modular development. Modular development is the process of developing
# software modules individually,
# then combining the modules to form a solution to an overall problem:
# Modular development of computer software:
# • makes a large project more manageable
# • is faster for large projects
# • leads to a higher quality product
# • makes it easier to find and correct errors
# • increases the reusability of solutions



# Step-By-Step Approach
# 1.Analyse the problem
# Identify the keywords and any required formulae. Perform sample calculations if appropriate.
# Rephrase the problem in your own words.
# 2.Specification
# Create a specification table, identifying the inputs, outputs and the processing steps. The processing
# steps represent a high-level summary of what the program will do.
# 3.Top-Down Design
# a) Identify the Processing Steps that need to be broken into smaller steps.
# b) Keep doing this until manageable “modules” are identified.
# c) Represent the design using a Structure Chart.
# 4.Modular Development
# • Start with the modules at the bottom and work up.
# • Each module should be designed as if it is a program in its own right.
# i. Come up with a suitable name for the module – descriptive, but not too long.
# ii. Write a description of the module, starting with “This module should ...”.
# iii. Analyse, specify the inputs, processing and outputs.
# iv. Write a pseudocode algorithm to describe how the module will be solved.
# 5.The mainline algorithm
# • Write a mainline algorithm which ties the modules together and co-ordinates their activity.
# • This should show the main processing steps and the order in which they are to be performed.
# • It should also show the flow of data and the major control structures. The mainline should be
# easy to read, be of manageable length, and show sound logic structure.
# • You should be able to read a pseudocode mainline and see exactly what is being done in the
# program.
# 32
# Functions and Modular Development
# 6.Implement your design in Python (for design “modules”, think Python “functions”)
# • Implement the modules in the design as functions in Python:
# • The inputs to the module will be parameters in the function.
# • The outputs from the module will be returned by the function.
# • Include a suitable documentation string for the function, including:
# ◦ A brief description of the purpose of the function, from Step 4(ii)
# ◦ A description of the parameters, if any
# ◦ A description of the return values, if any
# • Implement the mainline algorithm as the main part of the program.
# • Include detailed comments to explain your code.
# 7.Test the program.
# Test each function individually, where possible. (Unit Testing).
# Test the program in its entirety. (Application Testing)


###############
# Lambda Expressions
# Lambda expressions provide a special syntax to create anonymous (unnamed or unbound) functions.
# The basic syntax is:
# lambda x : some expression in x
# For example, the following lambda expression creates a function to square a number:
# A lambda expression has the following characteristics:
# 1. It can only contain expressions and can’t include statements in its body (e.g. no if, while
# or for statements).
# 2. It is written as a single line of execution.
# 3. It does not support annotations (type hints).
# 4. It can be immediately called.
# https://realpython.com/python-lambda/
# How would you use this function? It doesn't have a name. One way is to use the special _ syntax
# (single underscore) which stores the value of the last expression in the interactive interpreter:

# Alternatively, you could assign the lambda expression to a function name, and then call the function by
# that name:
# However, the Python Style Guide actually discourages this: “Always use a def statement instead of an
# assignment statement that binds a lambda expression directly to an identifier.”
# https://www.python.org/dev/peps/pep-0008/#programming-recommendations

# By default, the max() function applied to a dictionary identifies the highest “key”, in this case, the
# tuple with the name that's last in alphabetical order:
# To identify the winning competitor, i.e. the tuple associated with the highest value, the code is:
# In this case, the max() function uses the key argument key=results.get to find the highest
# value in the dictionary, and return the associate tuple. results.get is a dictionary method than
# returns the value associated with an item (or None if the item doesn't exist)..
# Similarly, you could use a key parameter to return a dictionary sorted by value:


# Lambda Expressions as Key Functions
# Lambda expressions can also be used as key functions. For example, support you have a list of tuples
# containing the names and bib numbers:
# By default, the list .sort() method will sort the list alphabetically by name (using the first element
# in each tuple):
# You could sort the list in order of Bib number, using the following lambda expression:
# 43
# Functions and Modular Development
# The syntax
# key=lambda competitor : competitor[1]
# instructs Python to sort the competitors list using the item in index 1 of each tuple, in this case, the Bib
# number.
# You can use any name for the variable in the lambda expression, it doesn't have to be the same as the
# list, e.g

def liu(value):
    a = value[0]
    print(a)

ab = list()

liu(ab)





