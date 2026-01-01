import os
import sys
from pathlib import Path


AOC_DIR = "aoc_2025"

def read_input(day, transformer=str, demo=False, strip="both"):
    """_summary_

    Args:
        day (_type_): _description_
        transformer (_type_): _description_
        demo (bool, optional): _description_. Defaults to False.
    """
    try:
        if demo:
            filename=f"day_{day}_demo.txt"
        else:
            filename=f"day_{day}.txt"

        with open(os.path.join(AOC_DIR,'inputs',filename)) as input_file:
            # return [transformer(line.strip()) for line in input_file]
            lines = []
            for line in input_file:
                if strip == "both":
                    line = line.strip()
                elif strip == "right":
                    line = line.rstrip()
                elif strip is None:
                    line = line.rstrip("\n")

                lines.append(transformer(line))

            return lines

    except Exception as e:
        print(e)