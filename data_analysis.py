
import pandas

data = pandas.read_csv("2018_central_park.csv")

gray_color_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_color_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color_count = len(data[data["Primary Fur Color"] == "Black"])

print(gray_color_count)
print(cinnamon_color_count)
print(black_color_count)

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_color_count, cinnamon_color_count, black_color_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("data_count.csv")

