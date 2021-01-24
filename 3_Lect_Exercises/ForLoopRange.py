# Program to demonstrate the use of ranges in a for loop

# Ranging with a set index -> this will show 0 - N-1
for i in range(10):
    print(i, end=" ")

print("")

i = 0

# Use of range to set a start and end with an incrementing value of 2
for i in range(1,10,2):
    print(i, end=" ")

i = 0
print()
# Example of ranges with characters
message = "This is a test message"
for i in range(len(message)):
    print(i, message[i])

i = 0
