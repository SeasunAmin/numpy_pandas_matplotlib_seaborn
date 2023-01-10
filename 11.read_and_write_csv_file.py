import pandas as pd
import os
reading_csv_file = pd.read_csv("F:\Dust File\student_info.csv")
print(reading_csv_file)

print(os.getcwd())

#Printing Specific row and column

reading_csv_file = pd.read_csv("F:\Dust File\student_info.csv",nrows=3)  #reading rows
print("ROW  is :\n\n",reading_csv_file)

reading_csv_file_column = pd.read_csv("F:\Dust File\student_info.csv",usecols=[0,2])
print("Column is :\n\n",reading_csv_file_column)

#Printing data from first and last 
print(reading_csv_file.head(1))
print(reading_csv_file.tail(1))