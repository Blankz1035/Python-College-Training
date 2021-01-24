# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 21:19:26 2020

@author: andre
"""

# Airlines csv
import matplotlib as plt
import pandas as pd


df = pd.read_csv("airline.csv")

print(len(df))
print(df.count())
print(df.size)

df2 = pd.read_csv("airline.csv", usecols=["UniqueCarrier", "FlightNum", 
                                         "ActualElapsedTime","CRSElapsedTime"])

print(df2.size)

df3 = pd.read_csv("airline.csv", usecols=list(range(10)))
print(df3.describe())

dep = df[df["DepDelay"] >= 0]
print(len(dep))

print(df.loc[df["DepDelay"].idxmax()])

print(df["CRSElapsedTime"].corr(df["ActualElapsedTime"]))

print(df.groupby("UniqueCarrier").size())