# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 18:23:45 2020

@author: andre
"""
import numpy as np

datain = np.loadtxt("wine.csv", delimiter=",", skiprows=1)
print(len(datain.T))
print(datain[5, 3])

chlorides,density,pH,sulphates,alcohol,quality = datain.T


print(quality[(int(len(quality) / 2))])


print(np.argmax(quality))

#np.corrcoef(x,y)

print(np.corrcoef(quality, alcohol))
print(np.corrcoef(quality, chlorides))
print()
print(np.corrcoef(quality, density))
print()
print(np.corrcoef(quality, sulphates))