import numpy as np

name1 = "seasun"
name2 = "Boss"

result = np.char.add(name1,name2)
print(result)

result = np.char.upper(name1)
print(result)

result = np.char.lower(name1)
print(name1)

result=np.char.center(name1,50,fillchar="*")
print(result)

result = np.char.split(name1)
print(result)

result = np.char.find(name1,"s")
print(result+1)