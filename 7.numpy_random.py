import numpy as np
import random

ran = np.random.random(1) #printing value betwen 0-1.
print(ran)

ran1 = np.random.randint(1,5)
print(ran1)

ran = np.random.randint(1,5,(3,3)) #creating a array using random function
print(ran)

ran = np.random.rand(3) #creating 1D array
print(ran)

x = [3,4,5,6,7,8]
name = ("seasun","boss","joss")
ran = np.random.choice(name)  #
print(ran)