import glob


# txt_list = glob.glob("*.txt")
txt_list = glob.glob("*.txt")

for file in txt_list:
    # 读取txt文件并将内容添加到集合中
    lines_set = set()
    with open(file, 'r') as f:
        for line in f:
            lines_set.add(line.strip())

# 输出不同内容行的数量
unique_lines_count = len(lines_set)
print("不同内容行的数量:", unique_lines_count)
