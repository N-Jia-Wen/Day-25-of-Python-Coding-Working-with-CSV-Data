# with open("weather_data.csv") as csv_file:
#     data = csv_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)


# Info of pandas package can be found at pandas.pydata.org
import pandas

data = pandas.read_csv(filepath_or_buffer="weather_data.csv")

# data is of type DataFrame
print(data)

# data["temp"] is of type Series
print(data["temp"])

# Playing around with pandas methods
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

ave_temp = sum(temp_list)/len(temp_list)
print(ave_temp)

print(data["temp"].max())

# Get data in Row
monday = data[data.day == "Monday"]
print(monday)


mon_temp_c = monday.temp[0]
mon_temp_f = (mon_temp_c * 1.8) + 32
print(mon_temp_f)


max_temp_row = data[data.temp == data.temp.max()]
print(max_temp_row)

# Creating DataFrame from scratch
new_data_dict = {
    "students": ["Amy", "James", "Ash"],
    "scores": [76, 56, 65]
}
new_data = pandas.DataFrame(new_data_dict)
print(new_data)

# Convert DataFrame to csv file
new_data.to_csv(path_or_buf="new_data.csv")
