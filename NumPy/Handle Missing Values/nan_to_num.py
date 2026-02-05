import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 5])
print(np.nan_to_num(arr, nan=50))