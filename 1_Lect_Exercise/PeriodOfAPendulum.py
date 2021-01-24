# Program to calculate period of pendulum swing by Andy Blankley

# A pendulum is a weight suspended from a pivot so
# that it can swing freely (e.g. in grandfather clock).
# The period T is the time (in seconds) required to complete
# one full cycle, over and back:
# --- where l is the length of the pendulum
# --- and g is the acceleration due to gravity (9.81m/s).

# Write a program to calculate the period of a pendulum and
# display the output formatted to 2 decimal places.

# Formula: T = 2*PI(SQRT(l/g))
import math

pendulum_length = int(input("Enter the length of the pendulum: "))

time = 2 * math.pi * (math.sqrt(pendulum_length / 9.81))

print("This program will show the length of time a cycle of swing per length of pendulum takes!")
print("Pendulum Length: ", pendulum_length)
print(f"Period of time per cycle is {time:.2f}")