#!/usr/bin/env python3
from pathlib import Path
import sys

import utils

BASE_DIR = Path(__file__).parent  # Day1 folder

def count_paths_ways_to_dict(grid):
    """
    grid: dict mapping (r, c) -> char
          open cells are anything except '^'
          start cell contains 'S'
    Returns: number of unique paths from S to the bottom row.

    Rules:
    - Normally move DOWN.
    - If DOWN is blocked by '^', move LEFT or RIGHT exactly one cell.
    - After that sideways move, DOWN will always be open (your guarantee).
    """

    # Determine bounds from dict keys
    coords = list(grid.keys())
    min_r = min(r for r, c in coords)
    max_r = max(r for r, c in coords)
    min_c = min(c for r, c in coords)
    max_c = max(c for r, c in coords)

    # Find start coordinate (cell value 'S')
    start = None
    for (r, c), ch in grid.items():
        if ch == "S":
            start = (r, c)
            break
    if start is None:
        raise ValueError("No start 'S' found in grid")

    def open_cell(r, c):
        # Must be within bounds AND not blocked
        if not (min_r <= r <= max_r and min_c <= c <= max_c):
            return False
        # If some coords are missing from dict, treat them as blocked
        ch = grid.get((r, c))
        return ch is not None and ch != "^"

    # ways_to[(r,c)] = number of ways to arrive at (r,c)
    ways_to = {start: 1}

    # Process row by row, left to right
    # (This assumes your movement rules prevent sideways cycles.)
    for r in range(start[0], max_r + 1):
        for c in range(min_c, max_c + 1):
            count = ways_to.get((r, c), 0)
            if count == 0:
                continue
            if not open_cell(r, c):
                continue
            if r == max_r:
                continue  # bottom row, done

            # Forced down if open
            if open_cell(r + 1, c):
                ways_to[(r + 1, c)] = ways_to.get((r + 1, c), 0) + count
            else:
                # Down blocked -> branch left/right one step
                if open_cell(r, c - 1):
                    ways_to[(r, c - 1)] = ways_to.get((r, c - 1), 0) + count
                if open_cell(r, c + 1):
                    ways_to[(r, c + 1)] = ways_to.get((r, c + 1), 0) + count

    # Sum all ways that end anywhere on the bottom row
    total = 0
    for c in range(min_c, max_c + 1):
        if open_cell(max_r, c):
            total += ways_to.get((max_r, c), 0)

    return total


if __name__ == "__main__":
    # Allow overriding file name from command line
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

    data = utils.read_lines(BASE_DIR / filename)
    grid = utils.grid_from_lines(data)

    print(type(grid))
    sum = count_paths_ways_to_dict(grid)

    print(sum)
