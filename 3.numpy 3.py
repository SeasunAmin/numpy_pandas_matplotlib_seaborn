import numpy as np

#arrange() function

arr_1d = np.arange(1,13)
print(arr_1d)

arr_1d_even_number = np.arange(1,13,2)
print(arr_1d_even_number)


#linspace() function

arr_1d = np.linspace(1,5,4)    #printing four value betwen 1 - 5.
print(arr_1d)

#reshap() function
arr_1d = np.arange(1,13)
arr_2d = arr_1d.reshape(2,6)
print(arr_2d)

#ravel() function is used to convert multi-dymentional array to 1D array.
arr_1d = np.arange(1,13)
arr = arr_1d.reshape(3,4)

single_arr = arr.ravel()
print(single_arr)

#flatten function (works like ravel function())

suck = arr.flatten()
print(suck)


#transpose() function convert the metrix row and collum

trans = arr_2d.transpose()
print(trans)