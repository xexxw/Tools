import pickle
import sys

# Read the pickle data from standard input
data = pickle.load(sys.stdin.buffer)

# Derive the output file name from the input file name
input_file = sys.argv[1]

# Assume the input file ends with ".pickle"
output_file = input_file[:-7] + ".txt"  

# Write the data to the output file
with open(output_file, "w", encoding='utf-8') as file:
    file.write(str(data))
