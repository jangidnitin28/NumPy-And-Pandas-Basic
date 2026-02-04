import numpy as np

#  1D
# array = np.array([1, 2, 3, 4, 5])
# print( array)

# 2D
# array = np.array([[1, 2, 3], [4, 5, 6]])
# print(array)


# array = np.ones(3)
# print(array)

# array = np.ones((2,3))
# print(array)

# array = np.zeros((2,3))
# print(array)

# array = np.full((2,3), 7)
# print(array)

# np.arange(start, stop, step)
# array = np.arange(1, 10, 1)
# print(array)

# Identity Matrix
# indentity_matrix = np.eye(3)
# print(indentity_matrix)

# Indexing
# array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(array)
# print(array[1, 2])  # Output: 6
# print(array[-1, -2])

# Slicing  array[start:stop:step]
# array = np.array([1, 2, 3, 4, 5])
# print(array[0:3:1])
# print(array[::2])    # Output: [1 3 5]
# print(array[1:])     # Output: [2 3 4 5]
# print(array[:3])    # Output: [1 2 3]
# print(array[::-1]) (rverse array)

# Fancy Indexing (list me index pass krdo jo chaiye)
# array = np.array([10, 20, 30, 40, 50])
# print(array[[1, 3, 4]])  # Output: [20 40 50]

# Filtering(Boolean Indexing)
# array = np.array([10, 15, 20, 25, 30])
# print(array[array >= 20])  # Output: [25 30]

# Reshaping 
# array = np.array([[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12]])
# print(array.reshape(4, 3))  # Output: [[ 1  2  3  4]

# Flattening (multiD to 1D) (copy of original array)
# array = np.array([[1, 2, 3], [4, 5, 6]])
# print(array.flatten())  

# ravel (multiD to 1D) (original array)
# array = np.array([[1, 2, 3], [4, 5, 6]])
# print(array.ravel())

 
