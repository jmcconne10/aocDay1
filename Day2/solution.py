#!/usr/bin/env python3
from pathlib import Path
import sys

import utils

BASE_DIR = Path(__file__).parent  # Day1 folder

def findInvalid(strRange):
    start = int(strRange.split("-")[0])
    stop = int(strRange.split("-")[1])

    inValidID = []

    for ID in range(start, stop +1):
        strID = str(ID)
        charCount = len(strID)
        halfChar = int(charCount/2)
        if charCount % 2 == 0:
            firstHalf = strID[:halfChar]
            secondHalf = strID[-halfChar:]
            if firstHalf == secondHalf:
                print(f'Invalid ID: {strID}')
                inValidID.append(ID)

    return inValidID

if __name__ == "__main__":
    # Allow overriding file name from command line
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    data = utils.read_text(BASE_DIR / filename)

    rangeList = data.split(",")

    sum = 0
    for strRange in rangeList:
        invalidIDs = findInvalid(strRange)

        for ID in invalidIDs:
            sum += ID

    print(f'Sum: {sum}')