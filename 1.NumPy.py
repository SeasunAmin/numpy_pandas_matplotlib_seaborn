import  numpy as np

arr_1d = np.array([1,2,3,4,5])
print("NumPy 1D Array : ",arr_1d)
print(type(arr_1d))
print("This array is : ",arr_1d.ndim,"D" )   #Checking the array 1D or 2D or....


arr_2d = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10]
])
print("NumPy 2D array : ",arr_2d)
print("This array is : ",arr_2d.ndim,"D")   #Checking the array 1D or 2D or....

print("Size of ths 1D array is :",arr_1d.size)
print("Size of the 2D array is :",arr_2d.size)

print("Shape of 2D array : ",arr_2d.shape)   # checking the array shape how many row and column.

print("Data type of the array is : ",arr_2d.dtype) # data type checking.