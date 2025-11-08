

# opponent
# A: Rock
# B: Paper
# C: Scissors

# me
# X: Rock
# Y: Paper
# Z: Scissors

play_score = {"R": 1, "P": 2, "S": 3}
win_score = {"W": 6, "D": 3, "L": 0}
win_move = {"R": "P", "P": "S", "S": "R"}
move_dict = {"A": "R","B": "P","C": "S","X": "R","Y": "P","Z": "S"}

part_2_outcome = {"X": "L", "Y": "D", "Z": "W"}

input = open("input.txt").read().split('\n')
input.pop()

# print(input)

score = []
score_part_2 = []

for i in range(len(input)):
    opp_move, my_move = move_dict[input[i][0]], move_dict[input[i][2]]
    temp_score = play_score[my_move]
    if(opp_move == my_move): outcome = "D"
    elif(win_move[opp_move] == my_move): outcome = "W"
    else: outcome = "L"

    temp_score += win_score[outcome]
    # print(opp_move, my_move, outcome)
    # print(temp_score)
    score.append(temp_score)

for i in range(len(input)):
    opp_move, outcome = move_dict[input[i][0]], part_2_outcome[input[i][2]]
    temp_score = win_score[outcome]


    if(outcome == "D"): my_move = opp_move
    elif(outcome == "W"): my_move = win_move[opp_move]
    else:  my_move = list(win_move.keys())[list(win_move.values()).index(opp_move)]

    temp_score += play_score[my_move]

    # print(opp_move, outcome, my_move)
    # print(temp_score)

    score_part_2.append(temp_score)

print(sum(score_part_2))