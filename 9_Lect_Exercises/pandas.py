# Introduction
# Pandas is an open source library providing high-performance, easy-to-use data structures and data
# analysis tools for the Python programming language. https://pandas.pydata.org/ The name is derived
# from the term "panel data", an econometrics term for data sets that include observations over multiple
# time periods for the same individuals. https://en.wikipedia.org/wiki/Pandas_(software)


# Pandas Data Structures
# A Series is a one-dimensional array-like object which contains a sequence of data values and an
# associated array of labels, called its index.
# A DataFrame is a rectangular block of data (a table). It contains an ordered collection of columns. A
# DataFrame has both a row an column index.

# Installing and Importing
# Importing is usually done as follows:
# import pandas as pd
# pandas is a third-party library, which means it must be installed before you can use it. It's installed
# automatically with Anaconda. If you're not using Anaconda, you'll need to install it, e.g. using pip:
# pip install pandas

# Sample Data
# For the following examples, the data represents information on seismic events (earthquakes) in the last
# 30 days. It has been retrieved from https://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php
# Here's an excerpt of the data:
# The columns include
# Column Description
# time The time of the event
# latitude The location of the event
# longitude
# depth The depth of the event
# mag The magnitude of the event
# nst The number of recording stations use to determine the location
# id A unique identifier for the event
# place The region associated with the event
# type The type of event


# File Input
# To read data from a csv file, use the method read_csv(), for example:
# df = pd.read_csv("all_month.csv")
# This reads the contents of the file into a DataFrame:
# You can limit the columns read from the file using the usecols argument, which is a list of either:
# • integer index values for the columns to include, e.g.
# df = pd.read_csv("all_month.csv", usecols=list(range(7)))
# (which reads in the first 7 columns)
# • column names (corresponding to the header row), e.g.
# df2 = pd.read_csv("all_month.csv", usecols=["time", "depth",
#  "mag", "nst", "id", "place"])
# You can also limit the number of rows to read from the data file, using the nrows argument, e.g.
# df = pd.read_csv("all_month.csv", nrows=100)

# Setting Index Labels
# By default, a DataFrame has a numeric index. You can set a different index label using the values of a
# column, using set_index:
# df3 = df2.set_index("id")
# By default it returns a new DataFrame. You can change the current DataFrame using:
# df2.set_index("id", inplace=True)


# Descriptive and Summary Statistics
# The following attributes and methods cna be used to display summaries of the data:
# columns names of the columns
# size number of values. To get the number of rows, use len(df)
# head(n) first n rows (default is 5)
# count() number of values in each column
# describe() statistics for the numeric columns
# max() maximum value for each column
# min() minimum value for each column
# sum() sum of the values for each column
# mean() average value for each column
# median() median value for each column
# quantile() median value for each column
# std() standard deviation for each numeric column

# By default, head will not display all the columns. To ensure it does, use the following code:
# pd.set_option('display.max_columns', None)
# pd.set_option('display.expand_frame_repr', False)

# To see column names - df.columns. To see number of rows use len(df)
# To see number of values, say df.size()
# To see the number of values in each column:  df.count()
# To get summary statistics on each numerical column: df.describe()

# The statistics 25%, 50% and 75% are called percentiles:
# • The 25% percentile, also called the lower quartile, represents a value for which 25% of the
# values in the column are less than it;
# • The 50% percentile, also called the median, represents a value for which 50% of the values in
# the column are less than it;
# • The 75% percentile, also called the upper quartile, represents a value for which 75% of the
# values in the column are less than it;


# Columns as Series
# A column can be retrieved as a Series using:
# df[“label”]
# or df.label if label is a valid python name
# For example:
# magnitudes = df.mag
# The descriptive and summary methods also work on Series objects

# Index of Maximum and Minimum
# You can get the index associated with a maximum or minimum using idxmax() and idxmin()

# Accessing Rows by Index
# To access the information associated with a particular row, use its index label and loc[]

# To access a row by its integer index, use iloc[]

# Correlation
# To Calculate the Correlation between two Columns, you can use the corr() method:

# Arithmetic with Columns
# You can perform arithmetic on columns: addition, subtraction, multiplication and division, e.g.
# dividing the magnitude by the corresponding number of stations:  df.mag / df.nst
# NaN means “Not a Number” because the
# corresponding value in the nst column
# is missing.

# You could store the resulting series in a variable and then display summary statistics:

# Selecting Values using Boolean Expressions
# You can apply boolean expressions to a Series, e.g.
# df.mag > 0
# which returns a Series of boolean values, corresponding to the values in the mag column that are
# greater than zero:
# This can be used to select the values that satisfy the boolean expression, e.g.
# pos_mag = df.mag[df.mag > 0]
# pos_mag is a Series containing the magnitude values greater than zero.
# You can also apply this to the DataFrame:
# pos_df = df[df.mag > 0]
# pos_df is a subset of the DataFrame for which the mag values are greater than 0

# Unique Values
# You can identify the unique values in a series using:
# series_name.unique()
# eg., the different types of seismic events are given by:
# A Series contains a boolean attribute is_unique which indicates if each value in the Series is
# unqiue: df.id.is_unique

# GroupBy
# You can use the groupby() method to process sections of the data assigned to groups.
# e.g. group the earthquake data by type
# The size() method displays the number of rows associated with each group.
# You can also calculate the means of the numeric columns using:
# The other statistical methods also work with groupby(): median, max, min, sum, std.

# Sorting
# To sort the DataFrame by its index label, use:
# df.sort_index()
# This returns a new, sorted DataFrame.
# You can sort a DataFrame in order of one of the columns:
# df.sort_values(by=”label”)
# where label is the name of a column, e.g.
# df.sort_values(by=”mag”)
# By default, sorting is in ascending order, but you can specify descending order instead, for example:
# df.sort_values(by=”mag”,ascending=False)

# Pandas Visualisation with Matplotlib
# By default, Pandas use Matplotlib for visualisation. You can do a line plot of all the numeric values in
# a DataFrame using:
# df.plot()
# By default, it will use the index labels as the x-axis labels. You can disable this using:
# df2.plot(use_index=False)
# You can specify that the columns be plotted on different Axes:
# df2.plot(use_index=False, subplots=True)


# DataFrame-specific plot arguments
# Argument Description
# subplots Plot each DataFrame column in a separate subplot
# sharex If subplots=True, share the same x-axis
# sharey If subplots=True, share the same y-axis
# figsize Size of figure to create as tuple
# title Plot title as string
# legend Add a subplot legend ( True by default)
# sort_columns Plot columns in alphabetical order; by default uses existing column order

# Plot Types
# plot.area Draw a stacked area plot.
# plot.bar Vertical bar plot.
# plot.barh Make a horizontal bar plot.
# plot.box Make a box plot of the DataFrame columns.
# plot.hist Make a histogram of the DataFrame columns.
# plot.line Plot Series or DataFrame as lines.
# plot.pie Generate a pie plot.
# plot.scatter Create a scatter plot
# plot.hist Make a histogram of the DataFrame’s column.


# Series.plot method arguments
# Argument Description
# label Label for plot legend
# ax matplotlib subplot object to plot on; by default uses active matplotlib subplot
# style Style string to be passed to matplotlib
# alpha The plot fill opacity (from 0 to 1)
# kind Can be 'area' , 'bar' , 'barh' , 'density' , 'hist' , 'kde' , 'line' , 'pie'
# Argument Description
# logy Use logarithmic scaling on the y-axis
# use_index Use the object index for tick labels
# rot Rotation of tick labels (0 through 360)
# xticks Values to use for x-axis ticks
# yticks Values to use for y-axis ticks
# xlim x-axis limits (e.g., [0, 10] )
# ylim y-axis limits
# grid Display axis grid (on by default)

# Examples
# df.mag.hist()
# Histogram of earthquake magnitudes
# df.plot.scatter("mag","nst")
# Scatter plot of number of recording
# stations vs magnitudes

# df.groupby("type").size().plot.bar()
# Bar chart of the number of events of each type
# df.groupby("type").size().plot.pie()
# Pie chart of the number of events of each type



