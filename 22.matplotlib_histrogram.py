import matplotlib.pyplot as plt
import numpy as np
import random

cse_student = np.random.randint(18,35, (100))
eee_student = np.random.randint(15,30, (100))

bins = [15,20,25,30,35,40]

cse_student_result = plt.hist(cse_student,bins,rwidth=0.95,align='mid',orientation='vertical',color='m',label="cse student's")
plt.title("CSE Student Age Histogram",fontsize=14,color='g',fontweight="bold")
plt.xlabel("student's age")
plt.ylabel("number of student's")
plt.legend()
plt.show()
