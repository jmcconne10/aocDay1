#!/usr/bin/env python3
from pathlib import Path
import sys

import utils

BASE_DIR = Path(__file__).parent  # Day1 folder

def part1(data):
    return None

def part2(data):
    return None

if __name__ == "__main__":
    # Allow overriding file name from command line
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    data = utils.read_text(BASE_DIR / filename)

    print(data)
