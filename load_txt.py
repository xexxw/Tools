json_path="/home/pagevalue/lilinjun/slimpajama/nfcresult/test/"
# txt_path="/home/pagevalue/lilinjun/slimpajama/new_test/nfcresult/dup_18gram/"
txt_path="/home/pagevalue/lilinjun/slimpajama/nfcresult/dup"



import os
from glob import glob
import re
import json

# file_list = glob(f"{txt_path}/duplicate_pairs_filter_range13*.txt")
file_list = glob(f"{txt_path}/duplicate_pairs*.txt")
results = []
seen = set()
count = 0

for file_path in file_list:
# 逐行读取文件内容
    with open(file_path, 'r') as file:
        for i, line in enumerate(file,1):
            if line not in seen:
            # 使用正则表达式提取文件名和数字
                # matches = re.findall(r'(\w+\-\d+\.jsonl)@(\d+)', line)
                matches = re.findall(r'(\w+\-\w+\-\d+\.jsonl)@(\d+)', line)
                if matches:
                    for filename, number in matches:
                        
                        results.append((filename, int(number)))
                        seen.add(line)
                        count += 1
                        if count == 100:
                            break


            if i==15:
                break
            

for filename, number in results:
    with open(os.path.join(json_path, filename), 'r') as jsonl_file:
        lines = jsonl_file.readlines()
        
        text = json.loads(lines[number])
        print(f"File: {filename}, Line: {number}, Text: {text}")
        print("\n")

 # 提取的结果是一个元组，将文件名和数字添加到结果列表
                
