import csv
import json

txt_file = "input.txt"
csv_file = "output.csv"

# 打开txt文件进行读取，并创建一个CSV写入对象
with open(txt_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

# 解析每行的JSON字符串并提取字段
data_list = []
for line in lines:
    line = line.strip()
    data = json.loads(line)
    data_list.append(data)

# 提取字段名
headers = list(data_list[0].keys())

# 将数据写入CSV文件
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(data_list)

print("转换完成！")


