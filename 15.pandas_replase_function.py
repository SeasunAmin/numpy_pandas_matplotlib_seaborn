import pandas as pd


reding_csv_file=pd.read_csv("F:\Dust File\ml_data_set\department_data.csv")
print(reding_csv_file)

#Replasing Data

replase_data = reding_csv_file.replace(to_replace="bba", value="ict")
print(replase_data)


replase_data_2 = replase_data.replace(to_replace=[1,2,3,4,5,6,7,8,9],value="a")
print(replase_data_2)

replase_data_3 = replase_data.replace({"Department": "eee", "ID": 1} ,"none" )
print(replase_data_3)

#replase all the data set's string

replase_all_data = reding_csv_file.replace( to_replace= "[A-Za-z]",value= 0 ,regex=True)
print(replase_all_data)

replase_column =reding_csv_file.replace(to_replace={"Name":"[A-Za-z]"},value=0,regex=True)
print(replase_column)

