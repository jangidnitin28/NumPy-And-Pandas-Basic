import numpy as np

arr = np.array([1, 2, np.inf, 4, -np.inf, 5])
print(np.isinf(arr))  # Check for infinite values

print(np.nan_to_num(arr, posinf=100, neginf=-100))  # Replace inf with specified values