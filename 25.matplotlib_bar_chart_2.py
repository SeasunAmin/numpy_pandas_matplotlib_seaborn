import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np


department = ['CSE','EEE','BBA','LLB','Tex']

class_1 = [30,25,15,20,10] #out of 100
class_2 = [25,30,20,10,15] #out of 100
class_3 = [30,25,15,20,10] #out of 100

style.use("ggplot")
plt.figure(figsize=(12,6))

width = 0.2
department_index = np.arange(len(department))

plt.bar(department_index,class_1,color='b',alpha=0.4,width=0.2,edgecolor='r',linewidth=3,label = "Class 1")
plt.bar(department_index+width,class_2,color='g',alpha=0.4,width=0.2,edgecolor='r',linewidth=3,label = "Class 2")
plt.bar(department_index+width+width,class_3,color='y',alpha=0.4,width=0.2,edgecolor='r',linewidth=3,label = "Class 3")

plt.xticks(department_index + width,department,rotation=20)

plt.title("Departments and students")
plt.xlabel("Department")
plt.ylabel("Students")
plt.legend()
plt.show()