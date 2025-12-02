from aoc_2025.utils import read_input

import argparse

# -- ArgumentParser ---------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("--demo", action="store_true", help="Set if running against demo input")
args = parser.parse_args()
is_demo = args.demo

# -- Read Input -------------------------------------
data = read_input(day=2, demo=is_demo)
data_cleaned = data[0].split(",")

invalid_ids_1 = []
invalid_ids_2 = []

# -- Part 1 -----------------------------------------

for id_range in data_cleaned:
    id_limits = id_range.split("-")
    _first_id, _last_id = int(id_limits[0]), int(id_limits[1])
    _ids = list(range(_first_id, _last_id + 1))
    _candidate_ids = [x for x in _ids if len(str(x)) % 2 == 0 ]

    for id in _candidate_ids:
        str_id = str(id)
        id_len_mid = int(len(str_id)/2)
        if int(str_id[:id_len_mid]) == int(str_id[id_len_mid:]):
            invalid_ids_1.append(id)

print(f"Part 1 Solution __ Sum of Invalid Ids: {sum(invalid_ids_1)}")

# -- Part 2 -----------------------------------------

import math

for id_range in data_cleaned:
    
    id_limits = id_range.split("-")
    _first_id, _last_id = int(id_limits[0]), int(id_limits[1])
    _ids = list(range(_first_id, _last_id + 1))


    for id in _ids:
        str_id = str(id)
        id_len = len(str_id)
        max_seq_len = math.floor(id_len/2)

        for seq_len in range(1, max_seq_len + 1):
            if (id_len % seq_len != 0):
                continue
                
            id_split_lst = [str_id[x:x+seq_len] for x in range(0, id_len, seq_len)]
            if len(set(id_split_lst)) == 1:
                invalid_ids_2.append(id)
                break


print(f"Part 2 Solution __ Sum of Invalid Ids: {sum(invalid_ids_2)}")
