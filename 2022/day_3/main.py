
# remove empty strings
input = [s for s in open("input.txt").read().split('\n') if s]

test = ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT","CrZsJsPPZsGzwwsLwLmpwMDw"]

def split_string(str):
    str_len = len(str)
    split_len = int(str_len/2)
    # print(split_len)
    return [str[:split_len], str[split_len:]]

def part_1(list_, total_score=0):

    for i in range(len(list_)):

        x,y = split_string(list_[i])
        common_item = "".join(set(x).intersection(y))

        temp_score = ord(common_item.lower())-96
        if common_item.isupper():
            temp_score += 26

        total_score += temp_score
    return total_score

def part_2(list_, total_score=0):

    for i in range(0, len(list_), 3):
        x,y,z = list_[i], list_[i+1], list_[i+2]
        common_item = "".join(set(x).intersection(y, z))

        temp_score = ord(common_item.lower())-96
        if common_item.isupper():
            temp_score += 26

        total_score += temp_score
    return total_score

print(part_2(input))