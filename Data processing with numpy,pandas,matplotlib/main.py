import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


df = pd.read_csv('employees.csv')

# print(df.head(5))
# print(df[df["First Name"] == "Maria"])
# df["Density"] = df["Bonus %"] / df["Salary"]
# print(df.head())

# print(df.iloc[:3])

# ------------ here ix[] first parameter takes columns and sceound para meter takes rows-----------------

# print(df.ix[:3,:"Start Date"]) # here 3 for index and Start Date for rows

print(df[df["Bonus %"]<5])


movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

