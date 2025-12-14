#!/usr/bin/env python3
from idlelib.outwin import file_line_pats
from pathlib import Path
import sys

import utils

BASE_DIR = Path(__file__).parent  # Day1 folder

def createMatrix(data):
    rows = len(data)
    matrix = []
    flipMatrix = []

    for line in data:
        newList = []
        for ch in line:
            newList.append(ch)
        matrix.append(newList)

    columns = 0
    for line in matrix:
        if columns < len(line):
            columns = len(line)

    for i in range(columns):
        columnList = []
        for j in range(rows):
            if i < len(matrix[j]):
                currentChar = matrix[j][i]
                if currentChar != "+" and currentChar != "*":
                    columnList.append(currentChar)
        flipMatrix.append(columnList)

    cleanedFlip = []
    for line in flipMatrix:
        s = "".join(line)
        if s and s.isspace():
            cleanedFlip.append("end")
        else:
            intS = int(s)
            cleanedFlip.append(intS)
    cleanedFlip.append("end")
    finalFlip = []
    tempFlip = []
    k = 0

    for line in cleanedFlip:
        if line == "end":
            finalFlip.append(tempFlip)
            tempFlip = []
        else:
            tempFlip.append(line)
    return finalFlip

def findOperators(matrix):
    lastLine = matrix[len(matrix) -1]
    operators = lastLine.split()
    return operators


def doMath(matrix, operators):
    i=0
    results = []

    for line in matrix:
        operator = operators[i]
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
        i += 1
    return results

if __name__ == "__main__":
    # Allow overriding file name from command line
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    data = utils.read_lines(BASE_DIR / filename)

    fullArray = createMatrix(data)
    operators = findOperators(data)

    resultsList = doMath(fullArray, operators)




    sum = 0
    for result in  resultsList:
        sum += result
    print(sum)
