import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib import style
style.use("ggplot")

cse_student = np.random.randint(18,35, (100))
eee_student = np.random.randint(15,30, (100))

bins = [15,20,25,30,35,40]

plt.figure(figsize=(10,5))  #changing histogram size

#adding two histogeram at once.
cse_student_result = plt.hist([cse_student,eee_student],bins,rwidth=0.95,align='mid',orientation='vertical',
                              color=['m','y'],label=["cse student's", "eee student's" ])

plt.title("CSE Student Age Histogram",fontsize=14,color='g',fontweight="bold")
plt.xlabel("student's age")
plt.ylabel("number of student's")
plt.legend()
#plt.grid(color = 'b')
plt.show()
