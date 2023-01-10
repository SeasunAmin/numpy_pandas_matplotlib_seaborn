import numpy as np

arr1 = np.arange(1,17).reshape(4,4)
print(arr1)

arr2 = np.arange(17,33).reshape(4,4)
print(arr2)

arr3 = np.concatenate((arr1,arr2)) # row wise concatenate
print(arr3)

arr4 = np.concatenate((arr1,arr2),axis=1) #column  wise      #vstack and h stack aslo do the same thing.
print(arr4)

print(np.split(arr1,2))