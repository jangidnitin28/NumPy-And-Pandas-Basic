"""
Splitting of Arrays

hsplit
vsplit
"""
import numpy as np
array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(np.hsplit(array, 2))  # Split into 2 arrays horizontally
print(np.vsplit(array, 2))  # Split into 2 arrays vertically
