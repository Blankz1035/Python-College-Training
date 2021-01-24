# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 22:52:51 2020

@author: andre
"""

import matplotlib.pyplot as plt

webhits = [743, 832, 655, 800, 937, 1016, 871, 995, 1252, 1879, 1456, 1695, 1659, 1820, 1746, 1425, 1573,
1131, 1072, 958, 870, 1012, 1063, 834]

time = list(range(1, 25))

fig, ax = plt.subplots()

ax.set_title("Web Hits Per Hour")
ax.set_xlabel("Time")
ax.set_ylabel("Web Hits")
ax.plot(time, webhits)
plt.show()

fig.savefig("Sample fig for webhits over time", bbox="tight")
