#!/usr/bin/env python3
from pathlib import Path
import sys

import utils

BASE_DIR = Path(__file__).parent  # Day1 folder

def searchGrid(data):
    availableTP = []
    for pos, ch in gridDict.items():
        counter = 0
        if ch == "@":
            neighbors = utils.neighbors8(pos)
            for npos in utils.neighbors8(pos):
                if npos not in gridDict:
                    continue
                nch = gridDict[npos]
                if nch == "@":
                    counter += 1
            if counter < 4:
                availableTP.append((pos, ch))
                gridDict[pos] = "."


    return availableTP

def part2(data):
    return None

if __name__ == "__main__":
    # Allow overriding file name from command line
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    total = 0
    data = utils.read_lines(BASE_DIR / filename)
    gridDict = utils.grid_from_lines(data)

    innerCounter = True

    while innerCounter == True :
        availableTP = searchGrid(gridDict)
        total += len(availableTP)
        if len(availableTP) == 0:
            innerCounter = False

    print(total)

