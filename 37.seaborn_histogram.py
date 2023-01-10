import seaborn as sbs
import matplotlib.pyplot as plt

data_frame = sbs.load_dataset("tips")
sbs.displot(data_frame['tip'],bins=10,kde=True)
plt.show()