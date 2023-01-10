import pandas as pd

#print(pd.__version__)

list_1 = [3,5,-7,"apple",6.21,"orange"]
print(list_1)

series_1 = pd.Series(list_1)
print(series_1)

series_2 = pd.Series([1,2,3,4])
print(series_2)

#chamging series defolt index

series_3 = pd.Series([3,4,1,2],index=('a','b','c','d'))
print(series_3)

#changing dataType and addind column name
series_4 = pd.Series([1,2,3,4],dtype=float,name="data value")
print(series_4)

max_num = series_4.max()
print(max_num)

#adding two series
add = series_2+series_4
print(add)

#creating series using dectitiomary

dic = pd.Series({"a":1,"b":2,"c":3})
print(dic)