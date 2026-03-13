import numpy as np
import pandas as pd

employee = pd.DataFrame({
    'employee_id' : [0, 1, 2],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})

salary = pd.DataFrame({
    'employee_id' : [0, 1, 2],
    'Salary': [70000, 80000, 90000],
    'Bonus': [5000, 6000, 7000]
})

# print(pd.merge(employee, salary,on='employee_id',how='inner'))  # Merge DataFrames based on index and employee_id
# print(pd.merge(employee, salary,on='employee_id',how='outer'))
# print(pd.merge(employee, salary,on='employee_id',how='left'))
# print(pd.merge(employee, salary,on='employee_id',how='right'))

# print(pd.concat([employee, salary], axis=1))


employee = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}, index=[0,1,4])

salary = pd.DataFrame({
    'Salary': [70000, 80000, 90000],
    'Bonus': [5000, 6000, 7000]
}, index=[0,1,2])

# print(employee.join(salary))
print(employee.join(salary,how='inner'))

