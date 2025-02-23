# with open("weather_data.csv") as file:
#     data = file.readlines()

# for line in data:
#     newline = line.strip("\n")
#     print(newline)

# import csv

# with open("weather_data.csv") as file:
#     data = list(csv.reader(file))
#     temperatures = []
#     for line in data:
#         if line[1] != "temp":
#             temperatures.append(int(line[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# # print(type(data["temp"]))
# data_dict = data.to_dict()
# # print(data_dict)

# temp_list = data["temp"].max()
# print(temp_list)

# print(data.condition)
# print(data)
# print(data.temp.max())

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp * 1.8 + 32
# print(monday_temp)

# create a dataframe from scratch < ----------
# data_dict = {
#     "students": ["Amy", "Henk"],
#     "grades": [12, 45]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# crreate csv called squirrel count that contains fur color, and count (Get sth, then count)
# logged under Primary Fur Color
# take that data, build a new dataframe from it

data = pandas.read_csv("2018_Central_Park_Squirrel_Data.csv")
counts = data["Primary Fur Color"].value_counts()
print(counts)
counts.to_csv("squirrels.csv")
