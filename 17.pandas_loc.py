import pandas as pd

reading_csv = pd.read_csv("F:\Dust File\ml_data_set\student_result.csv")
print(reading_csv)

my_data = reading_csv.loc[0]
print(my_data)

my_data_2 = reading_csv.loc[[0,1]]
print(my_data_2)

my_data_3 = reading_csv.loc[1,"Result"]
print(my_data_3)

my_data_4 = reading_csv.loc[0:2,"Result"]
print(my_data_4)

#showing data using condition
my_data_5 = reading_csv.loc[reading_csv['Result'] < 3.50 ]
print(my_data_5)