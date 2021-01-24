# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 19:03:06 2020

@author: andre
"""

import pandas as pd

df = pd.read_csv("Video_Game_Sales.csv")

print("Length of DataSet: ", len(df))
print("Amount of Values: ", df.size)
print("Total Amount of Columns: ", len(df.columns))
print("Amount of values per column: ", df.count())

print()

print("Setting index to 'Rank'")
df.set_index("Rank")

df.sort_index()

print("\nHead Values()", df.head())

print()

print("Analysis of EU_Sales:") # Against Year

df.sort_values(by="Year")
eu_sales = df["EU_Sales"]
year = df["Year"]
print(eu_sales.describe())

print("Max EU Sales :\n", df.loc[df["EU_Sales"].idxmax()])
print()
print("Min EU Sales -\n", df.loc[df["EU_Sales"].idxmin()])
print()
print("Corr between EU_SALES and Global Sales:\n", eu_sales.corr(df["Global_Sales"]))
print(df.groupby("Genre").describe())

# Visualization using pd.
print()

pub = df.groupby("Publisher").size()

pub = pub[pub> 50]
pub.plot()

print()
print("Scatter plot for games:")

df.plot.scatter("Genre", "EU_Sales")





      
      