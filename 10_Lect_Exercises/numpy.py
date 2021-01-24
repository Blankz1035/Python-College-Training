# Introduction
# NumPy is an Open Source project for numerical computing with Python. https://numpy.org/about/
# At NumPy’s core is its ndarray data structure, which stands for n-dimensional array. This can be
# used to store a vector (a one-dimensional array, i.e. a single column of numbers), a matrix (a 2-
# dimensional array, used extensively in mathematics) or a multi-dimsional array (n>2). Unlike Python's
# list, type all elements of an ndarray must be of the same type.
# https://en.wikipedia.org/wiki/NumPy
# https://pythoniseasytolearn.blogspot.com/2020/10/array-oriented-programming-with-numpy-1.html


# Advantages of NumPy
# ndarrays take significantly less memory than lists do. NumPy also provides a way to specify the data
# type of the contents of an ndarray, which provides further efficiency.
# https://towardsdatascience.com/a-hitchhiker-guide-to-python-numpy-arrays-9358de570121
# ndarrays are sigificantly faster to process than lists, providing better program runtimes.
# They also provide operations not possible with lists, such as adding/subtracting two ndarrays, and
# multiplication and division of ndarrays
# https://www.educba.com/introduction-to-numpy/
# Installing and Importing
# NumPy is a third-party library, which means it must be installed before you can use it. It's installed
# automatically with Anaconda. If you're not using Anaconda, you'll need to install it, e.g. using pip:
# pip install numpy
# The convention for importing NumPy is:
# import numpy as np


# Creating ndarrays
# https://numpy.org/devdocs/user/absolute_beginners.html
# You can create an ndarray using np.array()
# For example, creating a 1-dimensional array (called a vector):
# a1 = np.array([1,2,3,4,5,6])
# a1

# The len() function displays the length of the ndarray, which is the number of elements in a 1-
# dimensional array.
# You can also use range() to create an ndarray:
# np.array(range(1,7))

# but in fact NumPy provides its own version, arange:
# np.arange(1,7)

# You can create an ndarray from an existing list, for example, a list of 5 random numbers between 1
# and 6:
# numbers = [ randint(1,6) for i in range(5)]

# Numpy provides its own functions for random numbers. For example, to create an ndarray containing 5
# random numbers between 1 and 6:
# np.random.randint(1,6,5)

### np.random.randint takes 3 parameters: low, high and size returns size random integers
# from low (inclusive) to high (exclusive). This means that
# np.random.randint(1,6,5)
# returns 5 random numbers from 1 to 5. To simulate dice rolls, the code would be:
# np.random.randint(1,7,5)

# This behaviour is different from the randint method provided by the random module.
# The size parameter specifies the shape of the ndarray, e.g.
# np.random.randint(1,7,size=(2,5))
# This returns a 2-dimensional array with 2 rows of 5 numbers

# The size parameter is optional, and if it is omitted a single random number is returned:
# np.random.randint(1,7) . result eg = 3.
# To create a 2-dimensional array, you can provide a list containing 2 tuples, which must be of equal size:
# a2 = np.array([(0,1,2,3,4,5), (10,20,30,40,50,60)])

# The dimensions of an ndarray are given by the shape propery, which represents the shape using a
# tuple: a2.shape = (2, 6)
# This is equivalent to a 2x6 matrix (2 rows and 3 columns):
# (
# 0 1 2 3 4 5
# 10 20 30 40 50 60)
# The property ndim provides the number of dimensions of the array:
# returns a number to represent the dimension, etc if it is 1, 2, 3 dimension.

# In NumPy, dimensions are called axes, so a 2-dimensional array has 2 axes, axis 0 and axis 1.
# In this example, the axis 0 has a length of 2 (rows) and axis 1 has a length of 6 (columns).
# The len() function provides the number of rows:
# To get the length of axis 1 (the number of columns) use shape[1]:


# The number of values is given by the size property:
# a2.size
# which is the number of rows x the number of columns (in this example, 2 x 6):
# You can use an existing ndarray to create a new ndarray with a different shape in a number of
# ways; the original ndarray is unchanged:
# The ndarray method ravel() returns a flattened array (i.e. a 1-dimensional array):
# a2.ravel()
# The elements of the original ndarray are re-organised row by row.
# The reshape() method allows you create a new ndarray with a different number of rows and
# columns:
# a2.reshape(3,4) row /column

# You can create a transpose of an ndarray using a.T
# Transposing a 2 x 6 array returns a 6x2 array.
# You can use the arange function with the reshape method to generate a 2-dimensional array using
# the integers in sequence:
# np.arange(12).reshape(3,4)

# You can assign the rows to named variables:
# index, value = a2
# row 0
# row 1
# You can assign the columns to named variables by using the transpose:
# w,x,y,z = a2.T

# Indexing and Slicing ndarrays
# You can index and slice a 1-dimensional array as you would a list:
# a1[2:4]
# a1[0]

# The syntax to slice a 1-dimensional array is a[start:stop] which returns the elements from index
# start up to but not including index stop. The default for start is 0, and the default for stop is
# the length of the array.
# To get a specific element of a 2-dimensional array, provide the row and column index,
# i.e. a[row][column]
# If you provide a single index, it will return the corresponding row:
# a2[0]

# To return a specific column, you could return the corresponding row of the transpose:
# a2.T[0]

# To slice a 2-dimensional array, you provide the start and stop values for the two axes. In this
# example, a45 is a 2-dimensional array with 4 rows and 5 columns:
# a45 = np.arange(20).reshape(4,5)

# To get a 2-dimensional slice of the first 3 rows of the first 4 columns:
# a45[:3,:4]
# To get the middle 2 rows of the middle 3 columns:
# a45[1:3,1:4]
# You can use the slice syntax to return a specific column: a[:,column]

# The syntax [:] returns all elements in a list or 1-dimensional array.

# Basic Arithmetic with ndarrays
# You can add, subtract, multiple and divide ndarrays of the same shape using the standard
# mathematical operators.
# For 1-dimensional arrays a1 and b1:
# a1+b1 = Adds elements of a1 to b1 at index locations.
# minus does the same.
# multiplication and division does the same. 
# "Whole" decimal numbers are represented with a decimal point etc 1.

# Each operation returns an ndarray of the same shape.
# If you divide by an ndarray which contains zeros, you’ll get a runtime warning, and the
# corresponding element will contain the result inf (which stands for infinity):

# You can add, subtract, multiply and divide the elements of an ndarray by the same number:
# a1 + 3  .. will add 3 to all elements.

# For two dimensional arrays, the same will happen to the elements.


### Statistical Functions
# NumPy provides functions to calculate statistics associated with an ndarray.
# For a 1-dimensional array:
# Sum of the values: a1.sum()
# Maximum value: a1.max()
# Minimum value: a1.min()
# Mean of the values: a1.mean()
# Standard deviation: a1.std()
#  of the values
# To calculate the median, you have to use np.median()

# For a 2-dimensional array, the same functions provide results based on all the values in the ndarray:

# However, you also have the option to specify an axis, which means the results will apply to each
# column (axis=0):
# c34.sum(axis=0)
# or row (axis=1)

# You can calculate the correlation between two ndarrays x and y using the function
# np.corrcoef(x,y):
# For two 1-dimensional arrays it returns a 2x2 matrix with the correlations between each array:
#  a1,a1 a1,b1
# b1,a1 b1,b1
# The correlation between x and y is given in the off-diagonal elements, [0,1] and [1,0]

# Examples
# The following programs demonstrate some of the previous features, along with addituional features.
# The first program compares the time to generate sequences of random numbers, and calculate the mode
# and mean of the numbers.
# One million random numbers are generated two ways:
# 1.Using a list comprehension and random.randint
# numbers1 = [randint(1,1000) for i in range(1000000)]
# 2.Using np.random.randint
# numbers2 = np.random.randint(1,1000,1000000)
# NumPy is approximately 100 times faster:

# The mode of the numbers are calculated using
# a) a dictionary
# freq = {}
# for n in number:
#   if number not in freq:
#   freq[n] = 1
# else:
#   freq[n] + 1
# b) NumPy functions unique() and argmax()
# values, freq = np.unique(numbers, return_counts=True)
# return values[np.argmax(freq)]
# By default the function unique() returns the unique values in an ndarray:
# Using the keyword argument return_counts=True also returns the frequencies of each value:

# These two ndarrays can be assigned to separate variables:
# The function argmax() returns the index of the largest number:
# which can be used to identify the mode ( the value with the largest frequency):
# In the program, the mode is calculated 4 ways:
# • using a dictionary to calculate the mode of the list
# • using NumPy to calculate the mode of the list
# • using a dictionary to calculate the mode of the ndarray
# • using NumPy to calculate the mode of the ndarray

# NumPy is approximately 2.5 times faster calculating the mode of an ndarray than the dictionary
# approach is in calculating the mode of a list.

# To use NumPy’s mean() method to calculate the mean of the list of numbers, the function
# np.asarray() is used to convert the list to an array:
# np.asarray(l1).mean()

# The dice rolls are generated using np.random.randint(1, 7, size=(2,1000000))
# which returns a 2-dimensional array, with two rows of one million dice rolls:
# The two rows are added to each other to get the totals:


####### READING DATA FROM FILES
# Reading Data from Files
# Numpy provides functions to read from and write to text files:
# https://numpy.org/doc/stable/reference/routines.io.html
# loadtxt(filename) Load data from a text file.
# genfromtxt(filename) Load data from a text file, with missing values handled as
# specified.
# savetxt(filename) Save an array to a text file.
# By default, loadtxt() assumes whitespace between columns. 

# Example 3: Reading simulated data from a file
# For example, the file sim.dat contains two columns of simulation data separated by a tab.
# loadtxt() returns an ndarray with 427 rows, and 2 columns. Notice how the numbers are
# represented in scientific format: 0.702 is represented as 7.02000e-02, which means 7 x 10-2

# File contents stored in ndarray data
# First column is accessed as data.T[0]
# Second column is accessed as data.T[1]

# You can specify a delimiter, such as a comma:
# loadtxt(filename,delimiter=”,”)
# You can also specify a number of rows to skip, for example, rows containing headers:
# loadtxt(filename,delimiter=”,”,skiprows=1)
# and/or you can specify the number of rows to read:
# loadtxt(filename,delimiter=”,”,skiprows=1,max_rows=100)
# It’s also possible to specify the columns to include, using the keyword argument usecols:
# usecols=n reads the first n columns
# usecols=(n,m,p) reads the columns with index values n, m and p




