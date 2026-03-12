import numpy as np

#Insert in 1D Array    np.insert(name, index, element)
# array = np.array([1, 2, 3, 4, 5, 6])
# print(np.insert(array, 5, 10))  # Insert 10 at index 3

# Insert in 2D Array
# array = np.array([[1, 2, 3], [4, 5, 6]])
# print(np.insert(array, 1, [10, 11, 12], axis=1))

# Append in 1D Array (insert at  the end)  np.append(name, element)
# array = np.array([1, 2, 3, 4, 5, 6])
# print(np.append(array, 10))  # Append 10 at the end

# Concatenate  (joining two arrays)
# array1 = np.array([1, 2, 3]) 
# array2 = np.array([4, 5, 6])
# print( np.concatenate((array1, array2)) )

# Delete in 1D Array   np.delete(name, index)
# array = np.array([1, 2, 3, 4, 5, 6])
# print(np.delete(array, 2))  # Delete element at index 2

# Delete in 2D Array
# array = np.array([[1, 2, 3], [4, 5, 6]])
# print(np.delete(array, 1, axis=0))  # Delete row at index 1
# print(np.delete(array, 2, axis=1))  # Delete column at index 2