import sys



for line in sys.stdin:


    line = line.strip()

    # 按制表符分割行
    columns = line.split('\t')
    # 确保每行至少有三列
    if len(columns) >= 3:
        # # 交换第一列和第三列的内容
        # columns[0], columns[2] = columns[2], columns[0]

        # 输出新的行
        print(columns[1])
