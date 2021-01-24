# Program to demonstrate file input / output
# File input starts with the with open()  as keywords.  We use this to access the context manager and create a file variable to process with.

# Test file will be outputed to show some example data.

with open("6_Lect_Exercises/test.txt") as file_in:

    # Testing data reading using a for loop.
    # You will notice there is an extra space in bettwen the lines in the file. This is because these are stored as
    # /n characters. Python print statement also adds a new line too!.
    # We can help this issue by using the strip() function and specify a parameter. This will remove spaces, tab and newlines from start to end.
    # 
    for line in file_in:
        line.strip()
        print(line)


print("Finished")

# If you want to read a file with numbers, these a read into python as strings. You must convert this using the corresponding 
# class. for int() and floats(). 
# These also have the added benefit of removing the \n character from the number too.