# import pandas
# # with open("weather_data.csv", "r") as data_file:
# #     data = data_file.readlines()
# #     print(data)
# #
# import csv
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
import pandas
data = pandas.read_csv('weather_data.csv')
# print(data["temp"])

# print((data.temp.to_list()))

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
sum = 0
# print(len(temp_list))
for i in temp_list:
    sum += i
avg_temp = sum/len(temp_list)
# print(round(avg_temp,2))
# print(data['temp'].mean())
# print(data.temp.max())
# print(data.condition)
# Get data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
print(monday.condition)



