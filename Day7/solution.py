#!/usr/bin/env python3
from pathlib import Path
import sys

import utils

BASE_DIR = Path(__file__).parent  # Day1 folder

def findStart(line):
    idx = line.find("S")
    return idx

def moveBeam(startCoord, lines):
    countNum = 0
    for line in lines:
        if line.find("S") > -1:
            beamPositions = []
            beamPositions.append(startCoord)
            continue
        if "^" in line:
            newPositions = []
            for coord in beamPositions:
                update = False
                if line[coord] == "^":
                    if (coord-1) not in newPositions:
                        newPositions.append(coord - 1)
                        update = True
                    if (coord+1) not in newPositions:
                        newPositions.append(coord + 1)
                        update = True
                    if update == True:
                        countNum +=1
                else:
                    newPositions.append(coord)
            beamPositions = newPositions

    return countNum

if __name__ == "__main__":
    # Allow overriding file name from command line
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    data = utils.read_lines(BASE_DIR / filename)

    startCoord = findStart(data[0])

    numberBeams = moveBeam(startCoord, data)

    print(numberBeams)
