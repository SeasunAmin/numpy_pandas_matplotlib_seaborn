import matplotlib.pyplot as plt
import numpy as np


department = ['CSE','EEE','BBA','LLB','Tex']

class_1 = [30,25,15,20,10] #out of 100

plt.bar(department,class_1,color='b',alpha=0.4,width=0.3,edgecolor='r',linewidth=3,label = "Class 1" )
plt.legend()
plt.show()