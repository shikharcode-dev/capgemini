# Numpy - Numerical Python Library
# A powerful library for numerical computing in Python
# Provides support for large, multi-dimensional arrays and matrices
# Along with a collection of mathematical functions to operate on these arrays

# Example 1: Creating arrays
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])  # Creates a 1D array
# arr2d = np.array([[1, 2, 3], [4, 5, 6]])  # Creates a 2D array
# arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  # Creates a 3D array

# Example 2: Array operations
# arr = np.array([1, 2, 3])
# result = arr * 2  # Multiplies each element by 2: [2, 4, 6]
# result = arr + 5  # Adds 5 to each element: [6, 7, 8]
# result = arr ** 2  # Squares each element: [1, 4, 9]
# result = arr / 2  # Divides each element by 2: [0.5, 1.0, 1.5]

# Example 3: Mathematical functions
# arr = np.array([1, 4, 9, 16])
# sqrt_arr = np.sqrt(arr)  # Square root: [1, 2, 3, 4]
# mean_val = np.mean(arr)  # Calculate mean: 7.5
# sum_val = np.sum(arr)  # Sum of all elements: 30
# max_val = np.max(arr)  # Maximum value: 16
# min_val = np.min(arr)  # Minimum value: 1
# std_val = np.std(arr)  # Standard deviation
# exp_arr = np.exp(arr)  # Exponential of each element
# log_arr = np.log(arr)  # Natural logarithm of each element

# Example 4: Array indexing and slicing
# arr = np.array([10, 20, 30, 40, 50])
# element = arr[0]  # Access first element: 10
# slice_arr = arr[1:4]  # Slice array: [20, 30, 40]
# last_element = arr[-1]  # Access last element: 50
# reverse_arr = arr[::-1]  # Reverse array: [50, 40, 30, 20, 10]
# arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# element_2d = arr2d[1, 2]  # Access element at row 1, column 2: 6
# row = arr2d[0, :]  # Access entire first row: [1, 2, 3]
# column = arr2d[:, 1]  # Access entire second column: [2, 5, 8]

# Example 5: Useful functions
# zeros = np.zeros((3, 3))  # Creates 3x3 array of zeros
# ones = np.ones((2, 4))  # Creates 2x4 array of ones
# range_arr = np.arange(0, 10, 2)  # Creates array: [0, 2, 4, 6, 8]
# random_arr = np.random.rand(3, 3)  # Creates 3x3 array of random numbers between 0 and 1
# identity = np.eye(4)  # Creates 4x4 identity matrix
# linspace_arr = np.linspace(0, 1, 5)  # Creates array of 5 evenly spaced values between 0 and 1: [0, 0.25, 0.5, 0.75, 1]
# full_arr = np.full((2, 3), 7)  # Creates 2x3 array filled with 7

# Example 6: Array data types (dtype)
# int_arr = np.array([1, 2, 3], dtype=np.int32)  # Creates array with 32-bit integers
# float_arr = np.array([1, 2, 3], dtype=np.float64)  # Creates array with 64-bit floats
# bool_arr = np.array([True, False, True], dtype=np.bool_)  # Creates boolean array
# check_dtype = arr.dtype  # Check the data type of an array
# convert_type = arr.astype(np.float32)  # Convert array to different data type

# Example 7: Array shape and dimensions
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# shape = arr.shape  # Returns shape of array: (2, 3) - 2 rows, 3 columns
# ndim = arr.ndim  # Returns number of dimensions: 2
# size = arr.size  # Returns total number of elements: 6
# length = len(arr)  # Returns length of first dimension: 2

# Example 8: Reshaping arrays
# arr = np.arange(12)  # Creates array: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# reshaped = arr.reshape(3, 4)  # Reshapes to 3x4 array
# reshaped = arr.reshape(2, 6)  # Reshapes to 2x6 array
# reshaped = arr.reshape(2, 2, 3)  # Reshapes to 3D array with shape (2, 2, 3)
# reshaped = arr.reshape(-1, 3)  # Automatically calculates first dimension: (4, 3)
# flattened = arr2d.flatten()  # Converts multi-dimensional array to 1D array
# raveled = arr2d.ravel()  # Similar to flatten but returns a view when possible

# Example 9: Array arrangement and sorting
# arr = np.array([3, 1, 4, 1, 5, 9, 2, 6])
# sorted_arr = np.sort(arr)  # Returns sorted array: [1, 1, 2, 3, 4, 5, 6, 9]
# arr.sort()  # Sorts array in-place
# indices = np.argsort(arr)  # Returns indices that would sort the array
# arr2d = np.array([[3, 1], [2, 4]])
# sorted_2d = np.sort(arr2d, axis=0)  # Sort along rows (vertically)
# sorted_2d = np.sort(arr2d, axis=1)  # Sort along columns (horizontally)

# Example 10: Array stacking and concatenation
# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# vstacked = np.vstack((arr1, arr2))  # Vertical stack: [[1, 2, 3], [4, 5, 6]]
# hstacked = np.hstack((arr1, arr2))  # Horizontal stack: [1, 2, 3, 4, 5, 6]
# concatenated = np.concatenate((arr1, arr2))  # Concatenate arrays: [1, 2, 3, 4, 5, 6]
# concatenated_2d = np.concatenate((arr2d1, arr2d2), axis=0)  # Concatenate along rows
# concatenated_2d = np.concatenate((arr2d1, arr2d2), axis=1)  # Concatenate along columns

# Example 11: Array splitting
# arr = np.arange(12)
# split_arr = np.split(arr, 3)  # Splits into 3 equal parts
# split_arr = np.array_split(arr, 5)  # Splits into 5 parts (allows unequal splits)
# arr2d = np.arange(12).reshape(4, 3)
# vsplit = np.vsplit(arr2d, 2)  # Vertical split (splits rows)
# hsplit = np.hsplit(arr2d, 3)  # Horizontal split (splits columns)

# Example 12: Transposing arrays
# arr2d = np.array([[1, 2, 3], [4, 5, 6]])
# transposed = arr2d.T  # Transpose: [[1, 4], [2, 5], [3, 6]]
# transposed = np.transpose(arr2d)  # Alternative way to transpose
# arr3d = np.arange(24).reshape(2, 3, 4)
# transposed_3d = np.transpose(arr3d, (2, 0, 1))  # Transpose with custom axis order
