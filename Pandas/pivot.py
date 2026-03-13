import numpy as np
import pandas as pd

data = {
    'Date': pd.date_range('2023-01-01', periods=20),

    'Product': ['A', 'B', 'C', 'D'] * 5,

    'Region': [
        'East', 'West', 'North', 'South',
        'East', 'West', 'North', 'South',
        'East', 'West', 'North', 'South',
        'East', 'West', 'North', 'South',
        'East', 'West', 'North', 'South'
    ],

    'Sales': np.random.randint(100, 1000, 20),

    'Units': np.random.randint(10, 100, 20),

    'Rep': [
        'John', 'Mary', 'Bob', 'Alice',
        'John', 'Mary', 'Bob', 'Alice',
        'John', 'Mary', 'Bob', 'Alice',
        'John', 'Mary', 'Bob', 'Alice',
        'John', 'Mary', 'Bob', 'Alice'
    ]
}

df = pd.DataFrame(data)
# print(df)

# table = pd.pivot_table(df, values='Sales', index='Region', columns='Product', aggfunc='sum', fill_value=0)
# print(table)

# table = pd.pivot_table(df, values=['Sales','Units'], index='Region', columns='Product', aggfunc='sum', fill_value=0)
# print(table)

# table = pd.crosstab(df['Region'], df['Product'], values=df[['Sales','Units']], aggfunc='sum', fill_value=0)
# print(table)

# General Operations
# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.describe())
# print(df['Units'] + 10)

# Applying functions
def square(x):
    return x**2

# print(df['Units'].apply(square))

# for apply changes in origional
df['Units'] = df['Units'].apply(square)
print(df)