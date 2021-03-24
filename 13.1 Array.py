from numpy import *
arr = array([[1, 2], [3, 4], [5, 6]])  # 2D array

print(arr)
print(arr.dtype) # to check type of array
print(arr.ndim) # Check dimensions of array
print(arr.shape) # return number of rows and columns
print(arr.size) # return size of array
arr2 = arr.flatten() # it convert 2D array to 1D array
print(arr2)
arr3 = arr2.reshape(2, 3, 1)  # it will convert 1D array to 2D or 3D array
print(arr3)  # 2 arrays with 3 row and 1 columns

