from aoc_2025.utils import read_input

import argparse

# -- ArgumentParser ---------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("--demo", action="store_true", help="Set if running against demo input")
args = parser.parse_args()
is_demo = args.demo

# -- Read Input -------------------------------------
data = read_input(day=4, demo=is_demo)

# paper_map = data
paper_map = list(map(lambda x: list(x), data))

# -- Part 1 -----------------------------------------
# fewer than 4 rolls of paper in the 8 adjacent positions

# TODO: visualise this - whilst iterating, mark which one is being considered
# change to x if it is valid or not

# ..@@.@@@@.
# @@@.@.@.@@

# ..xx.xx@x.
# x@@.@.@.@@


height = len(data) 
width = len(data[0])
print(height, width)

count_accessible_rolls = 0

def is_inside(co_ord: tuple[int,int]):
    """
        co_ord (tuple[int,int]): (row, column) 
        (0,0) (0,1) ..
        (1,0) (1,1) ..
        ..    ..
    """
    if (0 <= co_ord[0] < height) and (0 <= co_ord[1] < width):
        return True
    return False

for row in range(height):
    for col in range(width):
        if paper_map[row][col] == "@":
            # print(f"({row},{col})")

            count_adjacent_rolls = 0
            for del_r in range(-1, 2):
                for del_c in range(-1, 2):
                    if del_r == 0 and del_c == 0:
                        # at the start point
                        continue

                    r_i = row + del_r
                    c_i = col + del_c

                    if not is_inside((r_i,c_i)):
                        continue
                    
                    if paper_map[r_i][c_i] == "@":
                        count_adjacent_rolls += 1
            
            if count_adjacent_rolls < 4:
                count_accessible_rolls += 1

print(f"Part 1 Solution __ Number of accessible rolls: {count_accessible_rolls}")

# -- Part 2 -----------------------------------------
# remove accessible paper until no more is accessible

# mutable paper map
paper_map_mut = paper_map

removed_rolls_track = []

can_remove_rolls = True

while can_remove_rolls:
    removable_rolls = []
    for row in range(height):
        for col in range(width):
            if paper_map_mut[row][col] == "@":
                # print(f"({row},{col})")

                count_adjacent_rolls = 0
                for del_r in range(-1, 2):
                    for del_c in range(-1, 2):
                        if del_r == 0 and del_c == 0:
                            # at the start point
                            continue

                        r_i = row + del_r
                        c_i = col + del_c

                        if not is_inside((r_i,c_i)):
                            continue
                        
                        if paper_map_mut[r_i][c_i] == "@":
                            count_adjacent_rolls += 1
                
                if count_adjacent_rolls < 4:
                    removable_rolls.append((row,col))
    
    num_removed = len(removable_rolls)

    if num_removed == 0:
        can_remove_rolls = False
    
    removed_rolls_track.append(num_removed)

    for roll in removable_rolls:
        paper_map_mut[roll[0]][roll[1]] = "."

print(f"Rolls removed track: {removed_rolls_track}")

print(f"Part 2 Solution __ Number of rolls that can be removed: {sum(removed_rolls_track)}")

