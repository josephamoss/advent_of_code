# str_list = list(filter(None, str_list))

def get_card_numbers(card_data):
    card_nums = list(filter(None,card_data.split(" ")))
    return card_nums

def parse(lines):
    ticket_data = []

    for line in lines:
        line = line.strip()
        card, data = line.split(":")
        winning_nums, my_nums = data.split("|")
        # print(winning_nums, my_nums)
        ticket_data.append([get_card_numbers(winning_nums),get_card_numbers(my_nums)])

    return ticket_data

def part1(card_data):
    total = 0
    for idx, ticket in enumerate(card_data):
        intersection = list(set(ticket[0]) & set(ticket[1]))
        if len(intersection) > 0:
            score = 2**(len(intersection)-1)
            total+=score
            # print(score, intersection)

    return total

def part2(card_data):
    card_count = [0] * len(card_data)

    for idx, ticket in enumerate(card_data):
        # have original version
        card_count[idx] +=1

        intersection = list(set(ticket[0]) & set(ticket[1]))

        if len(intersection) > 0:
            # number of cards (original + copies)
            total_cards_to_add = card_count[idx]

            # card indexes to add additional cards to
            min_value, max_value = idx + 1, idx + 1 + len(intersection)-1
            for i in range(min_value, max_value + 1):
                card_count[i]+=total_cards_to_add

    return sum(card_count)
     
if __name__ == "__main__":
    filename = "input.txt"

    f = open(filename, "r")
    card_data = parse(f.readlines())

    print(f'Part 1: {part1(card_data)}')
    print(f'Part 2: {part2(card_data)}')
        
