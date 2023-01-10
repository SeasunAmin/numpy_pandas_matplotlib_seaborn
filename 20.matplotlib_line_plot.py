import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7,8,9,10]
tempurature = [35,37,39.9,42.7,45.3,30.2,29.6,27.2,36.6,39.9]

weather_result = plt.plot(days,tempurature)    #plot takes 2 values x,y here x = days and y= tempurature.
#plt.axis([0,10, 0,50]) for changing the axies
plt.title("Dhaka's 10 Days Weather")
plt.xlabel("days")
plt.ylabel("tempurature")
print(plt.show())

