import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tempurature = [35, 37, 39.9, 42.7, 45.3, 35.5, 29.6, 27.2, 36.6, 39.9]
tempurature_2 = [28.5, 29.4, 30.9, 32.7, 35.3, 41.5, 36.6, 32.2, 29.6, 30.9]

weather_result = plt.plot(days, tempurature, color = 'r',marker = 'o',linestyle = '--', linewidth = 3,markersize = 10, label = "Dhaka" )
weather_result = plt.plot(days, tempurature_2, color = 'm',marker = 'o',linestyle = '--', linewidth = 3,markersize = 10, label = "Sylhet" )
plt.title("Dhaka & Sylhet 10 Days Weather", fontsize = 10)
plt.xlabel("days")
plt.ylabel("tempurature")

#plt.legend(["Tem-line"],loc = 1)
plt.legend(loc=1)

#plt.grid(color = 'k' , linewidth = 2)
print(plt.show())