import numpy as np

matrix = np.ones(5)

print(matrix)
print(matrix.dtype)

matrix = np.ones((5), dtype = int)       # changing the data type.
print (matrix)


matrix_2 = np.ones((3,3), dtype= int)   # changing the data type.
print(matrix_2)

matrix_3 = np.zeros((3,3), dtype=int)   # changing the data type.
print(matrix_3)