import argparse
from comparison import compare_2_files

parser = argparse.ArgumentParser(description="Comparison of project build protocols")
parser.add_argument('first_file')
parser.add_argument('second_file')
args = parser.parse_args()

try:
    compare_2_files(args.first_file, args.second_file)
except Exception as exc:
    print(exc)
