#!/usr/bin/env python3
from pathlib import Path
import sys

import utils

BASE_DIR = Path(__file__).parent  # Day1 folder

def getResult(line):
    nums = []
    for ch in line:
        nums.append(int(ch))

    highFirst = nums[0]
    firstPosition = 0
    for i in range(1, len(nums) - 1):
        if highFirst < nums[i]:
            highFirst = nums[i]
            firstPosition = i

    highSecond = nums[firstPosition +1]
    secondPostion = firstPosition +1

    for i in range(secondPostion, len(nums)):
        if highSecond < nums[i]:
            highSecond = nums[i]
            secondPostion = i

    highValue = int(str(highFirst) + str(highSecond))

    return highValue

if __name__ == "__main__":
    # Allow overriding file name from command line
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    data = utils.read_lines(BASE_DIR / filename)

    total = 0

    for line in data:
        result = getResult(line)
        total += result
        print(f'Result: {result}')

    print(f'Total: {total}')
