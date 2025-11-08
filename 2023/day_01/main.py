import re

if __name__ == "__main__":
    filename = "input.txt"
    part = 2

    running_sum = 0
    f = open(filename, "r")

    repl_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    for line in f.readlines():
        line = line.strip()
        line_old = line

        if part == 2:
            converted_line = line

            for word, digit in repl_dict.items():
                # index of first character for all words found
                # twotwoyear {two} -> [0,3]

                # (?=xyz) enables greedy search
                loc_text_digit = [m.start() for m in re.finditer('(?='+word+')', converted_line)]

                for index, str_loc in enumerate(loc_text_digit):
                    # add the associated digit after the first character; ensuring overlaps are not impacted
                    # eighttwo -> eight2wo -> e8ight2wo
                    # oneight -> o1neight -> o1ne8ight

                    converted_line = converted_line[:(index+int(str_loc+1))] + digit + converted_line[(index+int(str_loc+1)):]
                    
            line = converted_line
            print(line)

        # remove all letters
        numeric_digits_array = [int(d) for d in re.sub('\D', '', line)]
        hidden_num = 10*numeric_digits_array[0] + numeric_digits_array[-1]
        running_sum += hidden_num

        print(line_old, line, hidden_num)

    print(running_sum)

