# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 23:35:53 2020

@author: andre
"""

import matplotlib.pyplot as plt


x_values = []
x = 0.0500
y_values = [0.2047, 0.2167, 0.2328, 0.2493, 0.2621, 0.2674, 0.2621, 0.2437]

for i in range(0, 8):
    
    x_values.append(x)
    x += 0.05
    

fig, ax = plt.subplots()

ax.set_title("Distance moved over time")
ax.set_xlabel("Time")
ax.set_ylabel("Distance")

ax.plot(x_values, y_values)

plt.show()

fig.savefig("Plotting X and Y", bbox="tight")
