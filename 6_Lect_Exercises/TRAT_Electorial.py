#  Program to exerice the use of Testing and Functions - TRAT - 04/11/2020
# Creaated by: Andy Blankley
# 

# Exercise 1:
# As teams, define, document (using appropriate docstrings) and test (using PyTest) functions to
# calculate and return the following statistics:
# 1. The mean of a list of numbers
# 2. The median (“middle value”) of a list of numbers
# 3. The mode (most frequent number) of a list of numbers
# 4. The range (maximum – minimum) of a list of numbers
# 5. The standard deviation of a list of numbers
# 6. The correlation between two lists of numbers

# Imports:
from math import sqrt

def mean_of_list(l: list):
    """Function to calculate the mean of a given list.

    Args:
        l (list): [Variable of type list for calculation]

    Returns:
        Sum of mean of list as float.
    """
    return float(sum(l) / len(l))

def median_of_list(l: list):
    """Function to calculate the median of a given list.

    Args:
        l (list): [Variable of type list for calculation]

    Returns:
        [median]: [median value represented by number (int/float)]
    """
    mid_index = int(len(l) / 2)

    # Even number
    if len(l) % 2 == 0:
        medianvalue= (l[mid_index -1] + l[mid_index]) / 2
    # Odd
    else:
        medianvalue= l[mid_index]

    return medianvalue

def mode_of_list(l: list):
    """Function to calculate the mode of a given list.

    Args:
        l (list): [Variable of type list for calculation]

    Returns:
        [mode value represented by number (int/float)]
    """
    unique_values = sorted(set(l))

    freq = [ l.count(x) for x in unique_values ]

    return (unique_values[freq.index(max(freq))])

def range_of_list(l: list):
    """Function to calculate the range of a given list.

    Args:
        l (list): [Variable of type list for calculation]

    Returns:
        [range represented by number (int/float)]
    """
    return max(l) - min(l)

def standard_deviation(l: list):
    """[Function to calculate the range of a given list.]

    Args:
        l (list): [Variable of type list for calculation]

    Returns:
        [std_dev]: [represented by number (int/float)]
    """
    l_mean = sum(l) / len(l)

    squared_deviations = [ (x - l_mean) ** 2 for x in l ]

    std_dev =  sqrt(sum(squared_deviations) / (len(l) - 1))
    return std_dev
    
def correlation(x_values: list, y_values: list):
    """Function to calculate the correlation between two given lists.

    Args:
        x_values (list): [Variable of type list for calculation for x co-ordinates]
        y_values (list): [Variable of type list for calculation for y co-ordinates]

    Returns:
        [corr]: [represented by number (int/float)]
    """
    x_means = sum(x_values) / len(x_values)
    y_means = sum(y_values) / len(y_values)

    x_deviations = [ x - x_means for x in x_values ]
    y_deviations = [ y - y_means for y in y_values ]

    xy_deviations = [ x*y for (x,y) in zip(x_deviations,y_deviations)]

    x_sqrd_deviations = [ (x - x_means)**2 for x in x_values]
    y_sqrd_deviations = [ (y - y_means)**2 for y in y_values]

    corr = sum(xy_deviations)/(sqrt(sum(x_sqrd_deviations))* (sqrt(sum(y_sqrd_deviations))))
    return corr

# Exercise 2:
# b) The US Presidential Election uses the Electoral College system, where each of the 50 States and
# the District of Columbia are allocated a number of Electors who elect the President.
# The file us_electoral_college.csv (available from Moodle) contains data on the Electoral
# College system. The first line contains the headings; each subsequent line contains the name of the
# State/District, its population and the number of electors.

# As teams, write and test a program which calculates and displays the following information, using
# the functions from part(a) as appropriate:
# • The Number of States/Districts
# • Population: Total, Mean, Median, Range and Standard Deviation
# • Electors: Total, Mean, Median, Mode, Range and Standard Deviation
# • The Correlation between the Electors and Population of each State/District
# Marks (out of 100)
# Functions: 30 (including appropriate docstrings)
# Unit Tests: 30
# Program: 30
# Output: 10


# Important
# All work to be done in the Doku, except the program output which can be copied and pasted from a
# Python Editor. This is a Team exercise. Students who do not contribute will not receive any marks.
# Only use the Python Features that have been included up to this point.


# Additional Functions:
def print_user_menu():
    """Function to display user menu.
    
    """
    print('''    0 - View menu
    1 - Number of States / Districts
    2 - Population - Total, Mean, Median, Range and Standard Deviation
    3 - Electors - Total, Mean, Median, Mode, Range and Standard Deviation
    4 - Correlation between electors and population of each state/district
    10 - Exit''')
    print()

def list_total(l: list):
    """Function total all given list values.

    Args:
        l (list): [Variable to represent a given list.]

    Returns:
        [int/float]: [Sum of the list values.]
    """
    return sum(l)

def perform_functions(l: list, feature: str):
    """Function to perform all cross over functions for data analysis for user viewing.
    Execution of:
        # Mean, Mode, Median, Range ,  Total , Standard Deviations functions.

    Args:
        l (list): [Variable representing given list]
        feature (str): [Variable representing the feature name from the CSV (Population or Electors)]
    """

    print(f"Total {feature}: {list_total(l)}")
    print(f"Mean of {feature}: {mean_of_list(l):.2f}")
    print(f"Median of {feature}: {median_of_list(l):.2f}")
    print(f"Mode of {feature}: {mode_of_list(l):.2f}")
    print(f"Range of {feature}: {range_of_list(l):.2f}")
    # Standard Deviation:
    print(f"Standard deviation of {feature}: {standard_deviation(l):.2f}")

# Pre-Processing
try:
    print("Program Status: Beginning Pre-Processing / File Import..")
    with open("7_Lect_Exercises/us_electoral_college.csv", encoding="utf-8") as csv_in:
        _ = csv_in.readline()

        # Lists for values: State, Population, Electors
        states = []
        population = []
        electors = []

        index = 0

        for line in csv_in:
            # 3 indexes [0,1,2]
            try:
                s, p, e = line.split(',')
                # Change population and electors to int values.
                p = int(p)
                e = int(e)

            except ValueError:
                print("Error in value during split: ", ValueError)
                print("CSV Index: ", index)
                print(line)
                continue
        
            # Once completed we can add the values to our lists.
            states.append(s); population.append(p); electors.append(e)
            index += 1

except FileNotFoundError:
    print("File has not been found in specified location.")
    exit()
except IsADirectoryError:
    print("File specified is a directory.")
    exit()
except KeyboardInterrupt:
    print("Program has been stopped by user.")
    exit()
finally:
    print("Program Status: Pre-Processing of data has completed..")
    print()

# User Data Output
print("Welcome to data processing of US Electoral College!")
print_user_menu()

pick = 1
try:
    while pick != 10:
        # Take user input : Handle incorrect choice to ensuer program does not terminate
        try:
            pick = int(input("Enter your choice: "))

            if pick == 10:
                continue # contine as loop will break
            
            if pick < 0 or pick > 4:
                raise ValueError
            print()
        except ValueError:
            print("You entered an invalid choice.")
            continue

        # User Selection Handling
        if pick == 0:   # Print User Menu
            print_user_menu()
        elif pick == 1:  # Number of records
            print(f"Total amount of States / Districts: {len(states)}")
        elif pick == 2:  # Population - Total, Mean, Median, Range and Standard Deviation
            perform_functions(population, "Population")
        elif pick == 3:  # Elector - Total, Mean, Median, Mode, Range and Standard Deviation
            perform_functions(electors, "Electors")
        else:
            # pick == 4:  # Correlation - Correlation between electors and population of each state/district
            print(f"Correlation between Population and Electors: {correlation(electors, population)}")

    else:
        print("Thank you for processing the data. Finished.")
except KeyboardInterrupt:
    print("Program has been stopped by user.")
    exit()
