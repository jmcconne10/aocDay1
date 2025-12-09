#!/usr/bin/env python3
from pathlib import Path
import sys

import utils

BASE_DIR = Path(__file__).parent  # Day1 folder

def createRanges(data):
    rangeList = []
    for freshRange in data:
        parts = freshRange.split("-")
        num0 = int(parts[0])
        num1 = int(parts[1])
        rangeList.append((num0,num1))
    return rangeList

def mergeRanges(data):
    data.sort(key=lambda r: r[0])  # Sort by start

    cleanedRanges = []
    i = 0
    for subRange in data:
        if not cleanedRanges:
            cleanedRanges.append((subRange[0], subRange[1]))
            continue
        else:
            curr_start, curr_end = cleanedRanges[i]
            if subRange[0] <= curr_end +1:
                curr_end = max(subRange[1], curr_end)
                cleanedRanges[i] = (curr_start, curr_end)
            else:
                i += 1
                cleanedRanges.append((subRange[0], subRange[1]))
    return cleanedRanges

def sum_IDs(data):
    counter = 0
    for mergedRange in data:
        counter += mergedRange[1] - mergedRange[0] + 1

    return counter


if __name__ == "__main__":
    # Allow overriding file name from command line
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    data = utils.read_sections(BASE_DIR / filename)

    freshRanges = data[0]
    rangeList = createRanges(freshRanges)
    mergedRanges = mergeRanges(rangeList)
    final = sum_IDs(mergedRanges)

    print(rangeList)
    print(mergedRanges)
    print(final)
