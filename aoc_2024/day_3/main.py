from aoc_2024.utils import read_input
import re

import argparse

# -- ArgumentParser ---------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("--demo", action="store_true", help="Set if running against demo input")
args = parser.parse_args()
is_demo = args.demo

# -- Read Input -------------------------------------
data = read_input(day=3, demo=is_demo)

data_str = data

# -- Part 1 -----------------------------------------
total = 0

for line in data_str:
    # valid data looks like "mul(X,Y)"
    all = re.findall(r"mul\(\d+,\d+\)", line)

    for instruction in all:
        nums = re.findall(r"\d+",instruction)
        int_a, int_b = int(nums[0]), int(nums[1])
        res = int_a*int_b
        total += res

print(f"Part 1 Solution __ Sum of products: {total}")

# -- Part 2 -----------------------------------------
total_1 = 0
total_2 = 0

enabled = True
for line in data_str:
    all = re.findall(r"do\(\)|don\'t\(\)|mul\(\d+,\d+\)", line)
    for instruction in all:

        if instruction == "do()":
            enabled = True
        if instruction == "don't()":
            enabled = False

        nums = re.findall(r"\d+",instruction)
        if nums:
            int_a, int_b = int(nums[0]), int(nums[1])
            res = int_a*int_b
            total_1 += res

            if enabled:
                total_2 += res

print(f"Part 1 Solution [Recalculated] __ Sum of products: {total_1}")
print(f"Part 2 Solution __ Sum of products: {total_2}")