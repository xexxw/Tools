import glob

# file_list = glob.glob(f"new_data/pa")
# file_path = "new_data/part-00010"

# line_number = 260006  

file_path = "new_data/part-00017"

line_number = 862186

with open(file_path, "r") as file:
    lines = file.readlines()
    line = lines[line_number]
    print(line)