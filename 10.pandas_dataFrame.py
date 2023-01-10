import pandas as pd

#Creating a empty DataFrame

emptyDataFrame = pd.DataFrame()
print("Pandas Empty DataFrame is:\n",emptyDataFrame)

#DataFrame with valus

list = ["Apple","Orange","Mango"]
DataFrame_1 = pd.DataFrame(list)
print(DataFrame_1)

#Multi Column DataFrame

list_of_list = [["apple","orange","mango"], ["rose","lili","sunflower"], ["rice","egg", "curry"] ]

DataFrame_2 = pd.DataFrame(list_of_list)
print(DataFrame_2)

#DataFrame from Dictionary

dictonary = {"ID":[101,102,103,104]}
DataFrame_3 = pd.DataFrame(dictonary)
print(DataFrame_3)

dictonary = {"ID":[101,102,103,104],"Name":["seasun","abul","habul","jobbar"] }
DataFrame_3 = pd.DataFrame(dictonary)
print(DataFrame_3)


#List of Dictonary

list_of_dictonary = [{"Roll": 1, "Phn":120 },{"Roll": 2, "Phn":220 }]
DataFrame_4 = pd.DataFrame(list_of_dictonary)
print(DataFrame_4)

#Creating DataFrame from Dictonary of Series

dictonary_of_series = {"ID":pd.Series([1,2,3]), "Fruts": (['mango','orange','apple']) }
DataFrame_5 = pd.DataFrame(dictonary_of_series)
print(DataFrame_5)