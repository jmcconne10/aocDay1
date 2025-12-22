#!/usr/bin/env python3
from pathlib import Path
import sys

import utils

BASE_DIR = Path(__file__).parent  # Day1 folder

def createCoordinates(data):

    coordinateList = []
    for line in data:
        x, y = map(int, line.split(","))
        coordinateList.append((x,y))

    return coordinateList

def findSquare(in_coordinates):

    largest = 0

    for i in range(len(in_coordinates)):
        for j in range(len(in_coordinates)):
            x1, y1 = in_coordinates[i]
            x2, y2 = in_coordinates[j]
            square = (abs(x1 - x2) + 1)* (abs(y1 - y2)+1)
            if square > largest:
                largest = square
                best_coordinates = (in_coordinates[i], in_coordinates[j])
    return best_coordinates, largest

if __name__ == "__main__":
    # Allow overriding file name from command line
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    data = utils.read_lines(BASE_DIR / filename)
    coordinates = createCoordinates(data)
    square, size = findSquare(coordinates)

    print(size)
    print(square)
