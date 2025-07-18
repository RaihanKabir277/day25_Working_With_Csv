# --------open with traditional method ----------

# with open("weather_data.csv", "r") as file:
#     data = file.readlines()
#     print(data)

# ---------------but its a problem in traditional method 
# -------------there will be \n and also comma and others thing so we need to cleen this ----
# ------ below the way , where do not need to clean the data ----------

# import csv

# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     # next(data)
#     # for row in data:
#     #     # print(row)
#     #     temperatures.append(int(row[1]))
#     # ----------another way --------
#     # for row in data[1:]:
#     #     temperatures.append(int(row[1]))
#     # ---------its work if we convert the data into list like data = list(csv.reader(data_file))

#     # -----------anoyher way to do this --------
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
# print(temperatures)


# ---------------but when the files has more complex rows and columns we need pandas-----------

import pandas
data = pandas.read_csv("weather_data.csv")
# print(data)

# --------for only temperatures -----

temperatures = data["temp"]
# print(temperatures)
# print(type(data))   #total table as called as dataframe
# print(type(temperatures))  # the column of the table is called series in pandas

# ---------convert dataframe to dictionary -----------

data_dictionary = data.to_dict()
# print(data_dictionary)

# ------------convert series to list ------------

series_list = temperatures.to_list()
print(series_list)




