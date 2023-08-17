import json

# input_file = "/home/pagevalue/lilinjun/slimpajama/new_test/nfcresult/part-00010.jsonl"
output_file = "/home/pagevalue/lilinjun/slimpajama/new_test/json/part-00010.txt"
input_file = "/home/pagevalue/lilinjun/slimpajama/new_test/nfcresult/part-00017.jsonl"

with open(input_file, 'r') as jsonl_file:
    # 创建txt文件
    # with open(output_file, 'w') as txt_file:
    #     # 逐行读取JSONL文件内容
    #     for line in jsonl_file:
    #         # 解析JSON字符串
    #         data = json.loads(line)
    #         # 将数据写入txt文件
    #         # txt_file.write(str(data) + '\n')
    #         print(data)
    for i, line in enumerate(jsonl_file, 1):
            # 解析JSON字符串
        data = json.loads(line)
            # 将数据写入txt文件
            # txt_file.write(str(data) + '\n')
        
        if i== 862186:
            print(data)
            break


# with open(input_file, 'r') as f:
#     for line_number, line in enumerate(f, 1):
