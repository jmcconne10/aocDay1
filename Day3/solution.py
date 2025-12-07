#!/usr/bin/env python3
from pathlib import Path
import sys

import utils

BASE_DIR = Path(__file__).parent  # Day1 folder

def getResult(line):

    batteryLength = 12
    batteryList = [0] * batteryLength

    nums = []
    for ch in line:
        nums.append(int(ch))
    stringLength = len(nums)

    nextPosition = 0
    digitInBattery = 0

    for digit in batteryList:
        digitInString = nextPosition
        #digits left in string are > stringLength - i
        while batteryLength - (digitInBattery +1) < stringLength - digitInString:
            if batteryList[digitInBattery] < nums[digitInString]:
                    batteryList[digitInBattery] = nums[digitInString]
                    nextPosition = digitInString + 1
            digitInString += 1
        digitInBattery +=1

    return batteryList

if __name__ == "__main__":
    # Allow overriding file name from command line
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    data = utils.read_lines(BASE_DIR / filename)

    total = 0

    for line in data:
        resultList = getResult(line)
        result = int("".join(str(d) for d in resultList))
        total += result
        print(f'Result: {result}')

    print(f'Total: {total}')
