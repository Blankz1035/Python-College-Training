# Program which inputs 6 long jump distances displays the average, maximum and minimum
# jump, without using a list or other data structure

# Variables for program
total_jumps = 6
count = 0
average = 0
maximum = 0
minimum = 999999999

while count < total_jumps:
    count += 1
    distance = float(input(f"Enter distance {count}: "))

    # min value
    if distance < minimum:
        minimum = distance
    
    # max
    if distance > maximum:
        maximum = distance
    
    # average
    average += distance
    
print(f"Key Values: Maximum {maximum} | Minimum {minimum} | Average {average/total_jumps:.1f}")


