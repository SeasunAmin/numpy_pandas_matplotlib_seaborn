import matplotlib.pyplot as plt

department = ['CSE',"EEE","BBA","LLB","TEX"]
student = [35,20,20,15,10]

slice = [0.1,0,0.1,0,0] #slicing
colors= ['c','y','r','b','g']
textsize = {"fontsize":15}
wedgeprops = {"linewidth":2,"width":1,"edgecolor":"k"}
plt.pie(student, labels=department,explode=slice,colors= colors,
        autopct="%0.2f%%",shadow=True,radius=1.2,startangle=180,textprops=textsize,
        counterclock=True,labeldistance=1.4,wedgeprops= wedgeprops,
        pctdistance=0.5,center=(2,3),
        )
plt.legend(loc=4)
plt.show()