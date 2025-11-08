from collections import deque

input = [s for s in open("input.txt").read().split('\n') if s]

# could find the number of stacks
number_of_stacks = 9

stacks = [deque() for i in range(number_of_stacks)]

stack_config = []
move_directions = []

def move_crates_part_1(stacks, num_crates, stack_i, stack_f):
    for i in range(num_crates):
        crates_to_move = stacks[stack_i].pop()
        stacks[stack_f].append(crates_to_move)

    return stacks

def move_crates_part_2(stacks, num_crates, stack_i, stack_f):
    temp_dq = deque()

    for i in range(num_crates):
        crates_to_move = stacks[stack_i].pop()
        temp_dq.append(crates_to_move)
    for i in range(len(temp_dq)):
        stacks[stack_f].append(temp_dq.pop())

    return stacks

for i in range(len(input)):
    if input[i][0:4] != 'move':
        stack_config.append(input[i])
    else:
        move_directions.append(input[i])

for i in range(len(stack_config)-1):
    # find location of [
    positions = [c for c, letter in enumerate(stack_config[i]) if letter == '[']
    print(positions)

    # searching from top to bottom; no floating crates
    # can append from left safely
    for pos in positions:
        stack_index = pos // 4
        crate_id = stack_config[i][pos+1]
        stacks[stack_index].appendleft(crate_id)

for m in range(len(move_directions)):
    move, num_crates, frm, stack_i, to, stack_f = move_directions[m].split(" ")
    stacks = move_crates_part_2(stacks, int(num_crates), int(stack_i)-1, int(stack_f)-1)

top_row = [dq[-1] for dq in stacks]
print(top_row)