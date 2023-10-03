import csv
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
grey_count = len(data[fur_color == "Gray"])
red_count = len(data[fur_color == "Cinnamon"])
black_count = len(data[fur_color == "Black"])
data_dict = {
    "Fur": ["grey", "red", "black"],
    "Count": [grey_count, red_count, black_count]
}
fur_data = pandas.DataFrame(data_dict)
fur_data.to_csv("fur_data.csv")
for(index, row) in fur_data.iterrows():
    print(row.count)

#
#
# data = pandas.read_csv('weather_data.csv')
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# sum_temp = sum(temp_list) / len(temp_list)
# data["temp"].mean()
#
# # Get data in columns
# data["temp"].max()
# print(data.condition)
#
# # get data in rows
#
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# # creating dataframe
#
# data_dict = {
#     "students": ["amy", "james", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
