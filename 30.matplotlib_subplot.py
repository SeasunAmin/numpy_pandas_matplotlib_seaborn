import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import random
from matplotlib import style

plt.figure(figsize=(12,7))

#first graph
plt.subplot(2,2,1)

days = [1,2,3,4,5,6,7,8,9,10]
tempurature = [35,37,39.9,42.7,45.3,30.2,29.6,27.2,36.6,39.9]

weather_result = plt.plot(days,tempurature)    #plot takes 2 values x,y here x = days and y= tempurature.
#plt.axis([0,10, 0,50]) for changing the axies
plt.title("Dhaka's 10 Days Weather")
plt.xlabel("days")
plt.ylabel("tempurature")


#sceond graph
plt.subplot(2,2,2)
cse_student = np.random.randint(18,35, (100))
eee_student = np.random.randint(15,30, (100))

bins = [15,20,25,30,35,40]

cse_student_result = plt.hist(cse_student,bins,rwidth=0.95,align='mid',orientation='vertical',color='m',label="cse student's")
plt.title("CSE Student Age Histogram",fontsize=14,color='g',fontweight="bold")
plt.xlabel("student's age")
plt.ylabel("number of student's")
plt.legend()


#third graph
plt.subplot(2,2,3)

department = ['CSE','EEE','BBA','LLB','Tex']

class_1 = [30,25,15,20,10] #out of 100
class_2 = [25,30,20,10,15] #out of 100
class_3 = [30,25,15,20,10] #out of 100


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


#fourth graph
plt.subplot(2,2,4)
department = ['CSE',"EEE","BBA","LLB","TEX"]
student = [35,20,20,15,10]

slice = [0.1,0,0,0,0] #slicing
colors= ['c','y','r','b','g']
textsize = {"fontsize":10}
plt.pie(student, labels=department,colors= colors, explode=slice,
        autopct="%0.2f%%",shadow=True,radius=1.2,startangle=180,textprops=textsize)

plt.show()