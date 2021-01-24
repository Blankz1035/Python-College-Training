# Program to demonstrate the use of FileOuput

# File Output
# To store information in a file, you need to
# 1.Open the file in write or append mode
# 2.Write data to the file

# Opening a File in Write or Append Mode
# To open a file so that you can store data in the file, you need to specify a file mode:
# with open(filename, mode) as file_variable:
# where
# mode is “r” if you are reading from the file (this is the default)
# “w” if you are writing to the file (over-writing existing contents)
# “a” if you are adding to the file (appending).

# In the same way that all data is read from a file as strings, the .write() method writes data to the file
# as strings. So, if you need to store a number in a file, you have to convert it to a string using the str()
# function, for example:
# lotto_file.write(str(number))
# If you have multiple values to write to a file, join them together using the + operator:
# usersfile.write(“Username:” + username)

# Unlike print(), which automatically creates a newline whenever you print something, the write
# function doesn't include a newline when it stores information in a file.
