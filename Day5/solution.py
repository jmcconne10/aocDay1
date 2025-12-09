#!/usr/bin/env python3
from pathlib import Path
import sys

import utils

BASE_DIR = Path(__file__).parent  # Day1 folder

def createRanges(data):

    newList = []
    for freshRange in data:
        parts = freshRange.split("-")
        newList.append((int(parts[0]),int(parts[1])))

    return newList

def checkIngredients(freshRange, ingredients):

    counter = 0
    freshIngredients = []
    for ID in ingredients:
        for subRange in freshRange:
            if int(ID) >= subRange[0] and int(ID) <=subRange[1]:
                counter += 1
                freshIngredients.append(ID)
                break

    return freshIngredients, counter

if __name__ == "__main__":
    # Allow overriding file name from command line
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    data = utils.read_sections(BASE_DIR / filename)

    freshRanges = data[0]
    ingredientIDs = data[1]

    cleanRanges = createRanges(freshRanges)

    freshIngredients, counter = checkIngredients(cleanRanges, ingredientIDs)

    print(counter)
