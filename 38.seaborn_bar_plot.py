import matplotlib.pyplot as plt
import seaborn as sns


data_frame = sns.load_dataset("tips")

sns.barplot(x = data_frame.day, y =data_frame.total_bill ,hue=data_frame.sex,errwidth=13)
plt.show()