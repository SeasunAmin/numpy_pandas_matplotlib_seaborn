import pandas as pd

read_csv_file = pd.read_csv("F:\Dust File\student_info_2.csv",na_values=["not found"])
print(read_csv_file)


read_csv_file = pd.read_csv("F:\Dust File\student_info_2.csv",na_values={"Name": "not found","Department": "unavabile"})
print(read_csv_file)

read_csv_file = pd.read_csv("F:\Dust File\student_info_2.csv",keep_default_na= False)
print(read_csv_file)