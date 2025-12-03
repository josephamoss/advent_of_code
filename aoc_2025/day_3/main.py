from aoc_2025.utils import read_input

import argparse

# -- ArgumentParser ---------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("--demo", action="store_true", help="Set if running against demo input")
args = parser.parse_args()
is_demo = args.demo

# -- Read Input -------------------------------------
data = read_input(day=3, demo=is_demo)

print(data)

# -- Part 1 -----------------------------------------

total_joltage = 0

for bank in data:
    bank_lst = [int(x) for x in bank]
    joltage = int

    largest_jolt, largest_jolt_idx = 0, 0
    second_largest_jolt, second_largest_jolt_idx = 0, 0
    
    for i, digit in enumerate(bank_lst):
        if (digit > largest_jolt) and (i != len(bank_lst) - 1):
            largest_jolt, second_largest_jolt = digit, 0
            largest_jolt_idx, second_largest_jolt_idx = i, 0
        elif digit > second_largest_jolt:
            second_largest_jolt = digit
            second_largest_jolt_idx = i

    if largest_jolt_idx < second_largest_jolt_idx:
        joltage = int(''.join(map(str, [largest_jolt, second_largest_jolt])))
    else:
        joltage = int(''.join(map(str, [second_largest_jolt, largest_jolt])))

    total_joltage += joltage

print(f"Part 1 Solution __ Total output joltage: {total_joltage}")

# -- Part 2 -----------------------------------------

total_joltage_2 = 0

for bank in data:
    bank_lst = [int(x) for x in bank]
    joltage = int
    largest_jolt_lst = bank_lst[0:12]

    for i, digit in enumerate(bank_lst[12:]):
        for j in range(len(largest_jolt_lst)):
            if j == 0:
                continue
            if largest_jolt_lst[j] > largest_jolt_lst[j-1]:
                largest_jolt_lst.pop(j-1)
                largest_jolt_lst.append(digit)
                break
            if (j == len(largest_jolt_lst) - 1) and digit > largest_jolt_lst[j]:
                largest_jolt_lst.pop(j)
                largest_jolt_lst.append(digit)

    total_joltage_2 += int(''.join(map(str, largest_jolt_lst)))

print(f"Part 2 Solution __ Total output joltage: {total_joltage_2}")

