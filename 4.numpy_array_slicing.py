import numpy as np

mx = np.arange(1,101).reshape(10,10)   #first creat an 1D array 1  - 100, then convert it to 2D array using reshape function.
print(mx)

print(mx[0,0])

print(mx[0])   #printing the row

print(mx[:,0]) #printing the column

print(mx[:,0:1]) #Slicing the array and printing it in 2D format.

print(mx[:,0:1].ndim) #checking the dymention of the array.

print(mx[1:4, 1:4])