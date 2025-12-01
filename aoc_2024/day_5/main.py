from aoc_2024.utils import read_input

import argparse

# -- ArgumentParser ---------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("--demo", action="store_true", help="Set if running against demo input")
args = parser.parse_args()
is_demo = args.demo

# -- Read Input -------------------------------------
data = read_input(day=5, demo=is_demo)

delim_index = data.index("")

rules, updates = data[:delim_index], data[delim_index+1:]

# -- Part 1 -----------------------------------------

rule_map = {}
# {
    # value: set(ints that can't come before)
    # 75: (47, 61)
# }
for rule in rules:
    key_str, value_str = rule.split("|")
    key, value = int(key_str), int(value_str)
    try:
        rule_map[key].add(value)
    except KeyError:
        rule_map[key] = {value}

# [{a,b,c}, {d,e,f}, {g,h,i}]
update_lists = [list(int(num) for num in update.split(',')) for update in updates]

answer = 0
for update in update_lists:
    for i, value in enumerate(update):
        # get preceeding values
        if i == 0:
            continue

        preceeding = set(update[:i])
        rule_value = rule_map.get(value)
        if (rule_value is not None) and (rule_map[value] & preceeding):
            # print("Overlap")
            break
        # print(rule_value)
        # print(f"{value}: {preceeding}")
        if i == len(update)-1:
            # print(update[len(update)//2])
            answer += update[len(update)//2]

print(f"Part 1 Solution __ Sum of valid middle updates: {answer}")

# -- Part 2 -----------------------------------------

# recursively compare pairs of numbers in list - essentially a bubble sort

def correct_order(update: list, iter):
    # print(f"iteration: {iter} - {update}")
    for i in range(len(update)):
        for j in range(0, i):
            rule = rule_map.get(update[i],[])
            # print(i,j)
            # print(f"pivot = {update[i]}, looking at {update[j]}")
            
            if update[j] in rule:
                # print(f"Found Issue - {update}, swapping {update[i]} & {update[j]}")
                update[j], update[i] = update[i], update[j]
                return(correct_order(update, iter + 1 ))
    
    return update

answer_2 = 0

for update in update_lists:
    sorted_update = correct_order(update, 0)
    answer_2 += sorted_update[len(sorted_update)//2]

final_answer_2 = answer_2 - answer

print(f"Part 2 Solution __ Sum of sorted invalid updates: {final_answer_2}")



# iteration: 0 - [13, 75, 97, 47, 61, 53]
#  1 0
#   pivot = 75, looking at 13
# Found Issue - [13, 75, 97, 47, 61, 53], swapping 75 & 13
# 
# iteration: 1 - [75, 13, 97, 47, 61, 53]
# 1 0
#   pivot = 13, looking at 75
# 2 0
#   pivot = 97, looking at 75
# Found Issue - [75, 13, 97, 47, 61, 53], swapping 97 & 75
# 
# iteration: 2 - [97, 13, 75, 47, 61, 53]
# 1 0
#   pivot = 13, looking at 97
# 2 0
#   pivot = 75, looking at 97
# 2 1
#   pivot = 75, looking at 13
# Found Issue - [97, 13, 75, 47, 61, 53], swapping 75 & 13
# 
# iteration: 3 - [97, 75, 13, 47, 61, 53]
# 1 0
#   pivot = 75, looking at 97
# ...