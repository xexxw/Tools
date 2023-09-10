# import os
# import glob

# def count_files_by_tag(folder_path, tag):
#    count = 0
#    file_list = []
#    for root, dirs, files in os.walk(folder_path):
#        for file in files:
#            if file.endswith('.txt'):
#                with open(os.path.join(root, file), 'r') as f:
#                    for line in f:
#                        if line.startswith(tag):
#                            count += 1
#                            file_list.append(os.path.join(root, file))
#                            break
#    return count, file_list

# fold_list = glob.glob('*')
# for fold in fold_list:
#     a_count, a_files = count_files_by_tag(fold, 'a')
#     b_count, b_files = count_files_by_tag(fold, 'b')
#     c_count, c_files = count_files_by_tag(fold, 'c')

# with open('a_files.txt', 'w') as f:
#    for file in a_files:
#        f.write(file + '\n')

# with open('b_files.txt', 'w') as f:
#    for file in b_files:
#        f.write(file + '\n')

# with open('c_files.txt', 'w') as f:
#    for file in c_files:
#        f.write(file + '\n')

# print('Files with tag "a":', a_count)
# print('Files with tag "b":', b_count)
# print('Files with tag "c":', c_count)


import os
import sys

def count_and_group_labels(folder_path):
    label_counts = {'Filter_punctuation_number_filter': 0, 'clean': 0, 'ori': 0, 'other': 0}
    label_files = {'Filter_punctuation_number_filter': [], 'clean': [], 'ori': [], 'other': []}

    for filename in os.listdir(folder_path):
        # if filename.endswith('.txt'):
        with open(os.path.join(folder_path, filename), 'r') as file:
            lines = file.readlines()
            if len(lines) > 2:
                line_parts = lines[2].split()
                if len(line_parts) >= 3:
                    label = line_parts[2]
                    if label in label_counts:
                        label_counts[label] += 1
                        label_files[label].append(filename)
                    else:
                        label_counts['other'] += 1
                        label_files['other'].append(filename)

    with open('label_statistics.txt', 'w') as output_file:
        for label, count in label_counts.items():
            output_file.write(f"Label {label}: {count} files\n")
            output_file.write("Files: " + ', '.join(label_files[label]) + "\n\n")

if __name__ == "__main__":
    folder_path = sys.argv[1]
    count_and_group_labels(folder_path)
