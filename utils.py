"""
utils.py

A small collection of helper functions that are commonly useful
for Advent of Code-style problems.

How to use:
    from utils import (
        read_text,
        read_lines,
        parse_ints,
        chunks,
        window,
        pairwise,
        sign,
        manhattan,
        grid_from_lines,
        neighbors4,
        neighbors8,
        in_bounds,
        bfs,
    )

You do NOT need to use all of these every day. They're here
so you don't have to keep rewriting the same helpers.
"""

from __future__ import annotations
from collections import deque
from typing import Iterable, Iterator, Callable, TypeVar, Sequence
from pathlib import Path
import re
import math

T = TypeVar("T")
Pos = tuple[int, int]  # (row, col) or (y, x) positions


# ---------------------------------------------------------------------------
# Basic input helpers
# ---------------------------------------------------------------------------

def read_text(path: str | Path) -> str:
    """
    Read the entire file as a single string, stripping trailing newlines.

    IMPORTANT (AoC pattern with Day folders):

        In your DayN/solution.py, do this:

            from pathlib import Path
            from utils import read_text

            BASE_DIR = Path(__file__).parent  # folder where solution.py lives
            data = read_text(BASE_DIR / "input.txt")

        This works even if the working directory is the project ROOT,
        because you're passing an absolute/anchored path.

    Example:
        data = read_text("input.txt")         # uses current working directory
        # or, better in AoC:
        data = read_text(BASE_DIR / "input.txt")
    """
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        return f.read().rstrip("\n")


def read_lines(path: str | Path, keep_empty: bool = False) -> list[str]:
    """
    Read the file as a list of lines, without the trailing newline.

    Args:
        path: Path to the text file (str or pathlib.Path).
        keep_empty: If False (default), empty lines are removed.

    AoC example (inside DayN/solution.py):

        from pathlib import Path
        from utils import read_lines

        BASE_DIR = Path(__file__).parent
        lines = read_lines(BASE_DIR / "input.txt")

    Example:
        lines = read_lines("input.txt")
        first_line = lines[0]
    """
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]
    if not keep_empty:
        lines = [line for line in lines if line != ""]
    return lines
