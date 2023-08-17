import codecs

def decode_unicode_escape(input_string):
    return codecs.decode(input_string, 'unicode_escape')

# 输入文件路径和输出文件路径
input_file_path = 'input_file.txt'
output_file_path = 'out_file.txt'

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        decoded_line = decode_unicode_escape(line)
        output_file.write(decoded_line)
