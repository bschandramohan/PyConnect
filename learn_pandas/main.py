import pandas

# data = pandas.read_csv("working_days.csv")
# print(data)
#
# num_working_days = data[data["is_working_day"]].count()
# print(f"Number of working days={num_working_days}")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]  # DataFrame
print(type(gray_squirrels))
print(len(gray_squirrels))

ages = gray_squirrels.Age  # Series
print(type(ages))
print(ages)
