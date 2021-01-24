# # Program to calculates and displays:
# – the number of grains of wheat on each square,
# – and the total number of grains of wheat.

# 64 squares

num = 1
count = 0
total = 0

while count < 64:
    # add count
    count += 1
    
    # Print out result
    print(f"Square {count} has {num} pieces of wheat.")

    # Sum amount of Wheat 
    total += num

    # Double num each square
    num = num * 2

print(f"\nTotal wheat: {total}")