import  pandas as pd

reading_csv_file = pd.read_csv("F:\Dust File\ml_data_set\student_result.csv")
print(reading_csv_file)

#Interpolate function of filling numeric value

interpolate_filling_data = reading_csv_file.interpolate()
print(interpolate_filling_data)

interpolate_filling_data_2 = reading_csv_file.interpolate(limit=1)
print(interpolate_filling_data_2)


interpolate_filling_data_2 = reading_csv_file.interpolate(limit=1,limit_direction='backward')
print(interpolate_filling_data_2)


new_data_frame = reading_csv_file.interpolate(inplace=True) #update tha whole data_frame.
print(new_data_frame)