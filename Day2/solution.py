#!/usr/bin/env python3
from pathlib import Path
import sys

import utils

BASE_DIR = Path(__file__).parent  # Day1 folder

def findInvalid(strRange, invalidID_list):
    start = int(strRange.split("-")[0])
    stop = int(strRange.split("-")[1])

    for ID in range(start, stop +1):
        strID = str(ID)
        charCount = len(strID)
        halfChar = int(charCount/2)

        for i in range(1, halfChar + 1):
            invalid = True
            if charCount % i == 0:
                c = list(utils.chunks(strID, i))

                first = c[0]

                for j in range(1, len(c)):
                    if first != c[j]:
                        invalid = False
                        break
            else:
                invalid = False
            if invalid == True and ID not in invalidID_list:
                invalidID_list.append(ID)
                print(f'Invalid ID: {ID}')

    return invalidID_list


if __name__ == "__main__":
    # Allow overriding file name from command line
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    data = utils.read_text(BASE_DIR / filename)

    rangeList = data.split(",")

    sum = 0
    invalidID_list = []
    for strRange in rangeList:
        invalidID_list = findInvalid(strRange, invalidID_list)

    print(invalidID_list)
    for ID in invalidID_list:
        sum += ID

    print(f'Sum: {sum}')