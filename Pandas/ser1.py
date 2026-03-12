import numpy as np
import pandas as pd

# labels = ['a', 'b', 'c']
# my_list = [10, 20, 30]
# arr = np.array([10, 20, 30])
# d = {1: 10, 2: 20, 3: 30}

#Pandas Series
# print(pd.Series(arr))
# print(pd.Series(my_list))
# print(pd.Series(my_list, index=labels))
# print(pd.Series(d))
 
#DataFrame
# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 30, 35],
#         'City': ['New York', 'Los Angeles', 'Chicago'],
#         'Salary': [70000, 80000, 90000]
#         }
# print(pd.DataFrame(data))

data_list = [['Alice', 25, 'New York', 70000],
            ['Bob', 30, 'Los Angeles', 80000],
            ['Charlie', 35, 'Chicago', 90000]]
# print(pd.DataFrame(data_list))
header = ['Name', 'Age', 'City', 'Salary']
df2 = pd.DataFrame(data_list, columns=header)
# print(df2)

# print(df2['Name'])  # Accessing a single column
# print(df2[['Name','Salary']])

# df2['Passion'] = ['Traveling', 'Cooking', 'Sports']  # Adding a new column
# print(df2)

# df2.drop('Passion', axis=1, inplace=True)  # Deleting a column
# print(df2)

# print(df2.loc[0]) # Accessing a single row by label
# print(df2.loc[[0,1]]) # Accessing multiple rows by label
# print(df2.iloc[0]) # Accessing a single row by integer position 
# print(df2.loc[[0,1]][['Name','Salary']])

# Conditional selection
# print(df2[df2['Salary'] > 80000])  # Select rows where Salary is greater than 80000
print(df2[(df2['Salary'] > 80000) & (df2['City'] == 'Chicago')])  # Select rows where Salary is greater than 80000 and City is Chicago