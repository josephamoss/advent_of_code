from aoc_2025.utils import read_input

import argparse

# -- ArgumentParser ---------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("--demo", action="store_true", help="Set if running against demo input")
args = parser.parse_args()
is_demo = args.demo

# -- Read Input -------------------------------------
data = read_input(day=5, demo=is_demo)

delim_index = data.index("")

fresh_ids_raw, ingredient_ids_raw = data[:delim_index], data[delim_index+1:]

ingredient_ids = list(map(lambda x: int(x), ingredient_ids_raw))

fresh_ids_str = list(map(lambda x: x.split("-"), fresh_ids_raw))
fresh_ids = [[int(j) for j in i] for i in fresh_ids_str]

# -- Part 1 -----------------------------------------

# print(fresh_ids)
# print(ingredient_ids)

# fresh_ids
#   [ [x_1,y_1], [x_2,y_2], ... [x_n,y_n] ]


fresh_ingredient_count = 0

for ing in ingredient_ids:
    for fresh_range in fresh_ids:
        if ing >= fresh_range[0] and ing <= fresh_range[1]:
            fresh_ingredient_count += 1
            break

print(f"Part 1 Solution __ Number of fresh ids: {fresh_ingredient_count}")

# -- Part 2 -----------------------------------------

# !! way too long to execute !! 
# id_map = {}

# for fresh_range in fresh_ids:
#     for i in range(fresh_range[0], fresh_range[1] + 1):
#         try:
#             id_map[i] += 1
#         except KeyError:
#             id_map[i] = 0


sorted_fresh_ids = [x for x in sorted(fresh_ids, key=lambda x: x[0])]

merged_ranges = []


latest_min, latest_max = sorted_fresh_ids[0]

for start, end in sorted_fresh_ids[1:]:
    # print(i, _range, latest_min, latest_max, latest_range)
    if start > latest_max:
        # no overlap - save current range
        merged_ranges.append([latest_min, latest_max])
        latest_min, latest_max = start, end
    else: 
        latest_max = max(latest_max, end)

# append final range 
merged_ranges.append([latest_min, latest_max])

count_fresh_ids = 0
for i in merged_ranges:
    count_fresh_ids += (i[1] - i[0] + 1)

print(f"Part 2 Solution __ Number of ids considered to be fresh: {count_fresh_ids}")
