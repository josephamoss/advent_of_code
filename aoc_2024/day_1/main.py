from aoc_2024.utils import read_input

import argparse

# -- ArgumentParser ---------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("--demo", action="store_true", help="Set if running against demo input")
args = parser.parse_args()
is_demo = args.demo

# -- Read Input -------------------------------------
data = read_input(day=1, demo=is_demo)

l_list, r_list = map(list, zip(*(map(int, line.split("   ")) for line in data)))

# -- Part 1 -----------------------------------------
l_list_sorted, r_list_sorted = sorted(l_list), sorted(r_list)

sum_diff = 0

for num in range(len(l_list_sorted)):
    sum_diff += abs(l_list_sorted[num] - r_list_sorted[num])

print(f"Part 1 Solution __ Sum of Differences: {sum_diff}")

# -- Part 2 -----------------------------------------
# converting to set, returns unique values
l_unique = set(l_list)

# create lookup dict
l_dict = dict.fromkeys(l_unique, 0)

for val in r_list:
    if val in l_dict:
        l_dict[val] += 1

sim_score = 0
for num in l_list:
    sim_score += num * l_dict[num]

print(f"Part 2 Solution __ Similarity score: {sim_score}")

# ---------------------------------------------------
