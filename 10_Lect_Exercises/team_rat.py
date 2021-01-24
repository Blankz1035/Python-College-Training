# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 19:15:02 2020

@author: andre
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("uefa_youth.csv", delimiter=",", skiprows=1, encoding="utf8", usecols=(7,9,11))


month, quarter, games_played = data.T

# Frequency
values, frequency = np.unique(month, return_counts=True)

print(values)
print(frequency)

#### Month with Highest Frequency
print(values[np.argmax(frequency)])

fig, ax = plt.subplots()

ax.set_xlabel("Month")
ax.set_ylabel("Frequency")


y_pos = list(range(1, 14))

ax.set_xticks(y_pos)
ax.set_xticklabels(values)

ax.hist(month,bins=12, ec="black")

plt.show()