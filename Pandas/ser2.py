import numpy as np
import pandas as pd

data = {
    'A' : [1, np.nan, 3, np.nan],
    'B' : [5, np.nan, 7, 8],
    'C' : [9, 10, np.nan, 12]
}

df = pd.DataFrame(data)
# print(df)

# print(df.isna().sum())
# print(df.isna().any())
# print(df.dropna())
# print(df.dropna(thresh=2))  # Drop rows with less than 2 non-NaN values
# print(df.fillna(0, inplace=True))  # Fill NaN values with 0

fillWith = {'A': 0, 'B': 20, 'C': 30}
print(df.fillna(value=fillWith, inplace=True) ) # Fill NaN values with different values for each column
