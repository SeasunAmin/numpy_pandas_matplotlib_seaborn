import  pandas as pd

reading_csv_file = pd.read_csv("F:\Dust File\student_info_2.csv")
print(reading_csv_file)

#Droping Null values
droop_null_values = reading_csv_file.dropna()
print(droop_null_values)

#Droping Null values
droop_null_values = reading_csv_file.dropna(axis=1)
print(droop_null_values)


print("..........\n\n")
filling_dataset = reading_csv_file.fillna({'Name': 'No',"Department": '-', 'CGPA': 0})
print(filling_dataset)

#filling data from previous vlaues
s = reading_csv_file.fillna(method='ffill')
print(s)