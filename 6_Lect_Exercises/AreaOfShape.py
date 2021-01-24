# Program to demonstrate the use of functions -> calculating the area of a shape
# Cirlce: PieR**2 
# Square: Length * Width

# Imports
from math import pi

# Functions:

def areaofsquare(length, width):
    return (length * width)

def areaofcircle(radius):
    return pi * (radius**2)

print()
print("Area of a Square")
length = int(input("Length: "))
width = int(input("Width: "))
print(areaofsquare(length, width))

print()
print("Area of a Circle")
radius = int(input("Radius: "))
print(areaofcircle(radius))
print()



