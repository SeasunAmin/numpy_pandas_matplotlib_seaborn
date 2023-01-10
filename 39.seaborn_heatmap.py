import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

arr_1 = np.linspace(1,5,9).reshape(3,3)
#print(arr_1)

#sns.heatmap(arr_1)
#plt.show()

global_warming_data = pd.read_csv("F:\\python\\ML_Practice\\assets\global_warming.csv")

globaldata = global_warming_data.drop(columns=["Country Code","Indicator Name","Indicator Code"],axis=1).set_index("Country Name")
#globaldata.head(6)
sns.heatmap(globaldata,cmap="coolwarm",annot=True)

plt.show()



arr_2 =np.array( [ ['A1','A2','A3'],['B1','B2','B3'],['C1','C2','C3']])

print(arr_2)
sns.heatmap(arr_1, annot=arr_2, fmt="s")
plt.show()