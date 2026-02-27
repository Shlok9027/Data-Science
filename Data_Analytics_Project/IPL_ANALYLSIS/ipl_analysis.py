import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('IPL_Squad_2023.csv')

print(df.head())
print(df.tail())

print(df.shape)


df.drop(['Unnamed: 0'], axis=1, inplace=True)

print(df.head())