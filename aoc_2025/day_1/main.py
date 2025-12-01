from aoc_2025.utils import read_input

from enum import Enum

import argparse

# -- ArgumentParser ---------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("--demo", action="store_true", help="Set if running against demo input")
args = parser.parse_args()
is_demo = args.demo

# -- Read Input -------------------------------------
data = read_input(day=1, demo=is_demo)

cleaned_data = []
for i, value in enumerate(data):
    _dir , _val = value[:1], int(value[1:])
    cleaned_data.append([_dir, _val])

START_POSITION = 50
NUM_POSITIONS = 100

# -- Part 1 -----------------------------------------

class Direction(int, Enum):
    L = -1
    R = 1

zero_count = 0
zero_count_2 = 0
cur_position = START_POSITION

def apply_direction(cur_pos: int, rot_dir: str, rot_val: int):
    direction = Direction[rot_dir]
    return cur_pos + direction.value * rot_val

def wrap(position):
    return position % NUM_POSITIONS

for rotation in cleaned_data:
    _rot_dir, _rot_val = rotation[0], rotation[1]
    cur_position_temp = apply_direction(cur_position, _rot_dir, _rot_val)
    cur_position = wrap(cur_position_temp)
    if cur_position == 0:
        zero_count += 1

print(f"Part 1 Solution __ Number of zeroes: {zero_count}")

# -- Part 2 -----------------------------------------

cur_position_2 = START_POSITION

for rotation in cleaned_data:
    _rot_dir, _rot_val = rotation[0], rotation[1]
    start_pos = cur_position_2

    num_full_rotations = _rot_val // NUM_POSITIONS
    zero_count_2 += num_full_rotations

    _final_rot_val = _rot_val % NUM_POSITIONS

    cur_position_2_temp = apply_direction(cur_position_2, _rot_dir, _final_rot_val)

    # if final rotation is outside of range, must have passed through 0
    # > 100 as the case of the final rotation being = 100, equivalent to ending on 0
    if cur_position_2 != 0 and (cur_position_2_temp < 0 or cur_position_2_temp > 100): 
        zero_count_2 += 1

    cur_position_2 = wrap(cur_position_2_temp)
    if cur_position_2 == 0:
        zero_count_2 += 1


print(f"Part 2 Solution __ Number of zeroes: {zero_count_2}")

