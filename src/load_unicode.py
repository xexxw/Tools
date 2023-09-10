import sys
import os
import codecs

def decode_unicode_escape(input_string):
    return codecs.decode(input_string, 'unicode_escape')

# Derive the output file name from the input file name
input_file_path = sys.argv[1]
output_file_path = os.path.splitext(input_file_path)[0] + ".txt"

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        decoded_line = decode_unicode_escape(line)
        output_file.write(decoded_line)
