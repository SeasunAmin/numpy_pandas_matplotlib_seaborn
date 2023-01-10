import matplotlib.pyplot as plt
import pandas as pd

reading_dataset = pd.read_csv("F:\python\ML_Practice\\assets\googleplaystore.csv",nrows=1000) #taking only 1000 data from the dataset
print(reading_dataset.shape)

#print(reading_dataset)

x = reading_dataset["Rating"]
y = reading_dataset["Reviews"]

plt.figure(figsize=(12,6))

plt.scatter(x,y,color = "g",alpha=0.7, label="ratings")

plt.scatter(x,reading_dataset["Installs"],color = "r",alpha=0.7,label="install")


plt.title("Google Play Store App Plot")
plt.xlabel("rating")
plt.ylabel("reviews & installs")
plt.legend()
plt.show()