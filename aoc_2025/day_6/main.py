from aoc_2025.utils import read_input

import argparse

# -- ArgumentParser ---------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("--demo", action="store_true", help="Set if running against demo input")
args = parser.parse_args()
is_demo = args.demo

# -- Read Input -------------------------------------
data = read_input(day=6, demo=is_demo, strip=None)
num_rows = len(data)

operations_row = data[num_rows - 1]
data_rows = data[:(num_rows - 1) ]

# -- Part 1 -----------------------------------------

operations = data[num_rows - 1].split()

data_rows = []
for row in data[:-1]:
    int_row = [int(x) for x in row.split()]
    data_rows.append(int_row)

total = 0
for pos, prob in enumerate(operations):
    if prob == "+":
        _sum = 0
        for row in data_rows:
            _sum += row[pos]
        total += _sum

    if prob == "*":
        _product = 1
        for row in data_rows:
            _product *= row[pos]
        total += _product

print(f"Part 1 Solution __ Total of problem solutions: {total}")

# -- Part 2 -----------------------------------------

def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

def reformat_matrix(M, delim="_"):
    # reformat a list of string, place-value ordered numbers, 
    # using a delimiter, as integers
    # e.g. '34_' -> 34 & '_23' -> 23
    return list(
        map(
            lambda place_val_str: int("".join(filter(lambda x: x != delim, place_val_str))),
            M
        )
    )

# save index of operators, defines start of each 'problem block'
oper_pos = []
for i, val in enumerate(operations_row):
    if val != " ":
        oper_pos.append((val, i))

total = 0

for _iter, oper_data in enumerate(oper_pos):
    # [0, ('*', 0)] 
    # [1, ('+', 4)] 
    problem_matrix = []
    operator = oper_data[0]

    for row in data_rows:
        # extract matrix chunk - based on start positions of problems
        # i.e. if _iter = 0
        # data_row =  _45__64_387_23_ 
        # return slice from [0] to [3] -> _45

        # last case: from index of operator to end of row

        if len(oper_pos)-1 == _iter:
            matrix_row = row[oper_data[1] : len(row)]
        else:
            matrix_row = row[oper_data[1] : oper_pos[_iter + 1][1]-1]

        matrix_row = matrix_row.replace(" ", "_")
        problem_matrix.append(matrix_row)

    problem_matrix_transpose = reformat_matrix(transpose(problem_matrix))

    if operator == "+":
        _sum = 0
        for m_row in problem_matrix_transpose:
            _sum += m_row
        total += _sum

    if operator == "*":
        _product = 1
        for m_row in problem_matrix_transpose:
            _product *= m_row
        total += _product

print(f"Part 2 Solution __ Total of problem solutions using updated Cephlapod math: {total}")
