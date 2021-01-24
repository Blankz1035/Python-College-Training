# Program to demonstrate the use of pandas.

import matplotlib as plt
import pandas as pd

#  Process the DataFrame as follows:
# • Display the size of the DataFrame (total number of values), the number of columns and
# the number of rows
# • Set the index to the “GEOG_ID” column and then sort the DataFrame by its index
# • Display the first 5 rows of the DataFrame
# • Display summary statistics for the numerical columns in the DataFrame


df = pd.read_csv("population.csv", encoding="latin1", thousands=",");

print(len(df))
print(df.size)
print(len(df.columns))
df.set_index("GEOG_ID", inplace=True)
print(df.head())

print(df.describe())

totpop = df["TOTPOP"]

i = totpop.idxmax()
print(df.loc[i])
print()
print(df.loc[df["POPDENKM"].idxmin()])

print()
print("Female vs Male Pop")
malepop = df["MALE"]
femalepop = df["FEMALE"]

ratio = femalepop -malepop

print(ratio.describe())
print("Correlation: ", femalepop.corr(malepop))

df.plot.scatter("FEMALE", "MALE")






