# 12 red cubes
# 13 green cubes
# 14 blue cubes

def parse(lines):
    game_data = []

    for line in lines:
        line = line.strip()
        game, data = line.split(":")
        rounds = data.split(";")
        # print(rounds)
        round_data = []
        for round in rounds:
            cubes = round.split(",")
            cube_data = {}
            for cube in cubes:
                num, colour = cube.split(" ")[1], cube.split(" ")[2]
                cube_data[colour] = int(num)
            round_data.append(cube_data)
        game_data.append(round_data)
    return game_data

def part1(game_data): 
    total_in_bag = {'red': 12, 'green': 13, 'blue':14}
    total = 0

    for idx, game in enumerate(game_data):
        valid = True
        for game_round in game:
            for colour in game_round:
                if(game_round[colour] > total_in_bag[colour]):
                    valid = False
        if valid:
            total += idx + 1
        # else:
            # print("Invalid")
    
    return total

def part2(game_data):
    # get max of each 
    total = 0
    for game in game_data:
        print(game)
        power = 1
        for colour in ['red','blue','green']:
            power *= max(list(map(lambda r: r[colour] if colour in r else 0, game)))
        total += power

    return total

if __name__ == "__main__":
    filename = "input.txt"

    f = open(filename, "r")
    game_data = parse(f.readlines())

    # print(f'Part 1: {part1(game_data)}')
    print(f'Part 2: {part2(game_data)}')
    
        
    

