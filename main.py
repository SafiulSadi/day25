# # import pandas
# # # with open("weather_data.csv", "r") as data_file:
# # #     data = data_file.readlines()
# # #     print(data)
# # #
# # import csv
# # with open('weather_data.csv') as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #
# #     print(temperatures)
# import pandas
# # data = pandas.read_csv('weather_data.csv')
# # print(data["temp"])
#
# # print((data.temp.to_list()))
# #
# # data_dict = data.to_dict()
# # # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # sum = 0
# # # print(len(temp_list))
# # for i in temp_list:
# #     sum += i
# # avg_temp = sum/len(temp_list)
# # # print(round(avg_temp,2))
# # print(data['temp'].mean())
# # print(data.temp.max())
# # print(data.condition)
# # Get data in Row
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
# # monday = data[data.day == "Monday"]
# # print(monday.temp)
# # monday_temp = monday.temp[0] * 9/5 + 32
# # print(monday_temp)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")
import pandas
# data = pandas.read_csv("centralpark.csv")
# # print(data["Primary Fur Color"])
# fur_color = data["Primary Fur Color"]
# grey_count = len(fur_color[fur_color == "Gray"])
# print(grey_count)
# red_count = len(fur_color[fur_color == "Cinnamon"])
# print(red_count)
# black_count = len(fur_color[fur_color == "Black"])
# print(black_count)
# squirrel_count = {"grey": grey_count, "red": red_count, "black": black_count}
# print(squirrel_count)
# data = pandas.DataFrame(squirrel_count)
# data.to_csv("squirrel_count.csv")
# # print(squirrel_count_csv)
data = pandas.read_csv("centralpark.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_squirrels_count)
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_squirrels_count)
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_squirrels_count)
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count,black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count")
















