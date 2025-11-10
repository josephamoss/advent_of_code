from aoc_2024.utils import read_input

import argparse

# -- ArgumentParser ---------------------------------
parser = argparse.ArgumentParser()
parser.add_argument("--demo", action="store_true", help="Set if running against demo input")
args = parser.parse_args()
is_demo = args.demo

# -- Read Input -------------------------------------
data = read_input(day=2, demo=is_demo)

report_list = [list(map(int, line.split())) for line in data]


# -- Part 1 -----------------------------------------

def is_ordered(input: list):
    sorted_asc = sorted(input, reverse=False)
    sorted_desc = sorted(input, reverse=True)

    if input == sorted_asc or input == sorted_desc:
        return True
    
    return False

def check_trend(input: list):
    diffs = [input[i+1] - input[i] for i in range(len(input) - 1)]

    if all(1 <= d <= 3 for d in diffs):
        # increasing
        return True
    if all(-3 <= d <= -1 for d in diffs):
        # decreasing
        return True

    return False

# check if all are increasing/ decreasing
valid_reports = [report for report in report_list if is_ordered(report)]
# check the jumps are valid
safe_reports = [report for report in report_list if check_trend(report)]

print(f"Part 1 Solution __ Number of safe reports: {len(safe_reports)}")

# -- Part 2 -----------------------------------------

count_safe_reports_part_1 = 0
count_safe_reports_part_2 = 0

for report_line in report_list:

    # run (obtuse) logic from Part 1
    # if already safe, skip to next report
    if is_ordered(report_line) and check_trend(report_line):
        count_safe_reports_part_1 += 1
        count_safe_reports_part_2 += 1
        continue
    
    # if not safe, remove a value and rerun
    for i in range(len(report_line)):
        # e.g. [a, b, c, d] && i=1 -> [a , c, d]
        new_report_line = report_line[:i] + report_line[i+1:]

        if is_ordered(new_report_line) and check_trend(new_report_line):         
            count_safe_reports_part_2 += 1

            # if found a number to remove, stop checking report
            break

print(f"Part 1 Solution [Recalculated] __ Number of safe reports: {count_safe_reports_part_1}")
print(f"Part 2 Solution __ Number of safe reports: {count_safe_reports_part_2}")




        

