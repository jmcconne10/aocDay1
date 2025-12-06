#!/usr/bin/env python3
from pathlib import Path
import sys

import utils
from utils import *  # or read_lines, parse_ints, etc.

BASE_DIR = Path(__file__).parent  # Day1 folder

def part1(data):
    return None

def part2(data):
    return None

def turnLeft(steps, currentValue):
    newValue = currentValue - steps
    if newValue < 0:
        newValue = newValue % 100
    return newValue

def turnRight(steps, currentValue):
    newValue = currentValue + steps
    if newValue > 99:
        newValue = newValue % 100
    return newValue

if __name__ == "__main__":
    # Allow overriding file name from command line
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    data = utils.read_lines(BASE_DIR / filename)

    currentValue = 50 # initial location
    counter = 0
    for line in data:
        direction = line[0]  # "L"
        steps = int(line[1:])  # 68
        #print(f'Direction: {direction} Steps: {steps}')
        if direction == "L":
            currentValue = turnLeft(steps,currentValue)
            print(f'Move to location: {currentValue}')
        else:
            currentValue = turnRight(steps,currentValue)
            print(f'Move to location: {currentValue}')
        if currentValue == 0:
            counter+=1
    print(f'Counter: {counter}')



