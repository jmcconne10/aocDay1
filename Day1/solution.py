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

def turnLeft(steps, currentValue, counter):
    if currentValue == 0:
        steps_to_next_click = 100
    else:
        steps_to_next_click = currentValue

    if steps >= steps_to_next_click:
        counter += 1 + (steps - steps_to_next_click) //100

    newValue = (currentValue - steps) % 100
    return newValue, counter

def turnRight(steps, currentValue, counter):
    if currentValue == 0:
        steps_to_next_click = 100
    else:
        steps_to_next_click = 100-currentValue

    if steps >= steps_to_next_click:
        counter += 1 + (steps - steps_to_next_click) // 100

    newValue = (currentValue + steps) % 100

    return newValue, counter

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
            currentValue, counter = turnLeft(steps,currentValue, counter)
            print(f'Move to location: {currentValue}')
        else:
            currentValue, counter  = turnRight(steps,currentValue, counter)
            print(f'Move to location: {currentValue}')

    print(f'Counter: {counter}')



