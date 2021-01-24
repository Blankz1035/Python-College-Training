# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 23:50:36 2020

@author: andre
"""

import matplotlib.pyplot as plt

data = {"Apache":30, "Google":9, "Microsoft": 5, "nginx": 20}

fig, ax = plt.subplots()

ax.set_title("Web Server Market Share")

y_pos = [i for i in range(len(data))]

ax.set_yticks(y_pos)
ax.set_yticklabels(data.keys())

ax.set_xlabel("Share")
ax.set_ylabel("Developer")

ax.barh(y_pos, data.values())

plt.show()

fig.savefig("Web Server Market Share", bbox="tight")