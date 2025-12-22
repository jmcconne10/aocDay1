#!/usr/bin/env python3
from pathlib import Path
import sys
from collections import defaultdict
import utils

BASE_DIR = Path(__file__).parent  # Day1 folder

def createCoordinates(data):

    coordinateList = []
    for line in data:
        x, y = map(int, line.split(","))
        coordinateList.append((x,y))

    return coordinateList

def build_extrema(coords):
    min_y_for_x = {}
    max_y_for_x = {}
    min_x_for_y = {}
    max_x_for_y = {}

    for x, y in coords:
        # For each x → track y bounds
        if x not in min_y_for_x or y < min_y_for_x[x]:
            min_y_for_x[x] = y
        if x not in max_y_for_x or y > max_y_for_x[x]:
            max_y_for_x[x] = y

        # For each y → track x bounds
        if y not in min_x_for_y or x < min_x_for_y[y]:
            min_x_for_y[y] = x
        if y not in max_x_for_y or x > max_x_for_y[y]:
            max_x_for_y[y] = x

    return min_y_for_x, max_y_for_x, min_x_for_y, max_x_for_y

def findSquare(in_coordinates, min_y_for_x, max_y_for_x, min_x_for_y, max_x_for_y):

    largest = 0

    for i in range(len(in_coordinates)):
        for j in range(len(in_coordinates)):
            x1, y1 = in_coordinates[i]
            x2, y2 = in_coordinates[j]
            coordC = x2, y1
            coordD = x1, y2

            cGood = False
            dGood = False

            if x1 > x2 and y1 < y2:  # X1 is top right and X2 bottom left
                #check if coordinate C is in bounds
                #y1 = yNew and xC <= xNew
                #y2 = yC and xC >= xNew
                if min_x_for_y[y1] <= coordC[0]:
                    cGood = True
                elif min_y_for_x[x2] <=coordC[1]:
                    cGood = True

                # check if coordinate C is in bounds
                # max_x_for y2 >= xd
                # max_y_for x1 >= yd
                if max_x_for_y[y2] >= coordD[0]:
                    dGood = True
                elif max_y_for_x[x1] >= coordD[1]:
                    dGood = True

            if x1 < x2 and y1 < y2:  # X1 is top left and X2 bottom right
                # check if coordinate C is in bounds
                # max_x_for_y1 >= xC
                # min_y_for_x2 <= yc
                if max_x_for_y[y1] >= coordC[0]:
                    cGood = True
                elif min_y_for_x[x2] <= coordC[1]:
                    cGood = True

                # check if coordinate D is in bounds
                # min_x_for_y2 <= xd
                # max_y_for_x1 >= yd
                if min_x_for_y[y2] <= coordD[0]:
                    dGood = True
                elif max_y_for_x[x1] > coordD[1]:
                    dGood = True

            if cGood and dGood:
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
    min_y_for_x, max_y_for_x, min_x_for_y, max_x_for_y = build_extrema(coordinates)
    square, size = findSquare(coordinates, min_y_for_x, max_y_for_x, min_x_for_y, max_x_for_y)

    print(size)
    print(square)
