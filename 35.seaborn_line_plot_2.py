import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tips_data = sns.load_dataset("tips")
#print(tips_data)

sns.lineplot(x="total_bill",y="tip",data=tips_data)
plt.show()