import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input_file")
parser.add_argument("--output_file")
args = parser.parse_args()
input_file = args.input_file
output_file = args.output_file

with open(input_file, "rb") as file:
    data = pickle.load(file)

with open(output_file, "w", encoding = 'utf-8') as file:
    file.write(str(data))