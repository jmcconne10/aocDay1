#!/usr/bin/env python3
from idlelib.outwin import file_line_pats
from pathlib import Path
import sys

import utils

BASE_DIR = Path(__file__).parent  # Day1 folder

def createMatrix(data):
    columns = len(data[0].split())
    rows = len(data)
    matrix = []
    flipMatrix = []


    for line in data:
        matrix.append(line.split())

    for j in range(columns):
        list = []
        for k in range(rows):
            list.append(matrix[k][j])
        flipMatrix.append(list)

    return flipMatrix

def doMath(matrix):
    i=0
    results = []
    for line in matrix:
        operator = line[len(line) - 1]
        if operator == "*":
            result = 1
            for number in line:
                if number !="*":
                    result *= int(number)
            results.append(result)
        if operator == "+":
            result = 0
            for number in line:
                if number != "+":
                    result += int(number)
            results.append(result)
    return results

if __name__ == "__main__":
    # Allow overriding file name from command line
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    data = utils.read_lines(BASE_DIR / filename)

    fullArray = createMatrix(data)

    resultsList = doMath(fullArray)

    sum = 0
    for result in  resultsList:
        sum += result
    print(sum)
