from aoc_2024.utils import read_input
import re

import argparse

# -- ArgumentParser ---------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("--demo", action="store_true", help="Set if running against demo input")
args = parser.parse_args()
is_demo = args.demo

# -- Read Input -------------------------------------
data = read_input(day=4, demo=is_demo)

print(data)

# -- Part 1 -----------------------------------------
h = len(data) # height
w = len(data[0]) # width
print(h, w)

def is_inside(co_ord: tuple[int,int]):
    """
        co_ord (tuple[int,int]): (row, column) 
        (0,0) (0,1)
        (1,0) (1,1)
    """
    if (0 <= co_ord[0] < h) and (0 <= co_ord[1] < w):
        return True
    return False

target = "XMAS"
answer = 0
for row in range(h):
    for col in range(w):
        if data[row][col] == "X":
            print(f"({row},{col})")
            for del_r in range(-1, 2):
                for del_c in range(-1, 2):
                    if del_r == 0 and del_c == 0:
                        # at the start point
                        continue
                    valid = True

                    for i in range(1,4):
                        r_i = row + del_r * i
                        c_i = col + del_c * i

                        if is_inside((r_i,c_i)) and data[r_i][c_i] == target[i]:
                            continue
                        else:
                            valid = False
                            break
                    if valid:
                        answer += 1
                            
print(f"Part 1 Solution __ Number of valid XMAS: {answer}")

# -- Part 2 -----------------------------------------

# check clockwise around 'A'; order matters
diags = [(-1,-1), (1,-1), (1,1), (-1,1)]
valid_diags = ("MMSS", "MSSM", "SMMS", "SSMM")
answer_2 = 0

for row in range(h):
    for col in range(w):
        if data[row][col] == "A":                
            valid = True

            temp_diag = ""
            for corner in diags:
                r_corner = row + corner[0]
                c_corner = col + corner[1]
                if not is_inside((r_corner, c_corner)):
                    valid = False
                    break
                temp_diag += data[r_corner][c_corner]
            
            if valid and temp_diag in valid_diags:
                answer_2 +=1

print(f"Part 2 Solution __ Number of valid X-MAS: {answer_2}")
