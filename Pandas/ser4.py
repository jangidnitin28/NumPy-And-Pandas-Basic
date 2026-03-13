import numpy as np
import pandas as pd

data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'D', 'C', 'A', 'D', 'B'],
    'Store': ['S1', 'S2', 'S1', 'S2', 'S1', 'S2', 'S1', 'S2', 'S1', 'S2'],
    'Sales': [100, 150, 200, 120, 180, 250, 210, 170, 300, 160],
    'Quantity': [10, 15, 20, 12, 18, 25, 21, 17, 30, 16],
    'Date': pd.date_range(start='2023-01-01', periods=10)
    }

df = pd.DataFrame(data)

# groupedCategory = df.groupby('Category')['Sales'].sum()
# print(groupedCategory)

# groupedStore = df.groupby('Store')['Sales'].sum()
# print(groupedStore)

# groupedMultiple = df.groupby(['Category','Store'])['Sales'].sum()
# print(groupedMultiple)

# print(df['Sales'].mean())
# print(df['Sales'].mode())
# print(df['Sales'].median())
# print(df['Sales'].min())
# print(df['Sales'].max())
# print(df['Sales'].std())
# print(df['Sales'].var())

all = df['Sales'].agg(['mean', 'median', 'min', 'max', 'std', 'var'])
print(all)