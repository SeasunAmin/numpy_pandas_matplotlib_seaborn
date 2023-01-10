import pandas as pd


# Checking how many null values
reading_csv_file = pd.read_csv("F:\Dust File\student_info.csv")
print(reading_csv_file)

null_values = reading_csv_file.isnull()
print(null_values)

print("\n....................\n")

reading_csv_file = pd.read_csv("F:\Dust File\student_info_2.csv")
print(reading_csv_file)

null_values = reading_csv_file.isnull()
null_values_file_2 = reading_csv_file.isnull().sum()

print(null_values)
print(null_values_file_2)

#Cheking total null values

total_null_values = reading_csv_file.isnull().sum().sum()
print("Total NUll values : ",total_null_values)
