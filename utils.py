"""
utils.py

A collection of helper functions commonly useful for Advent of Code problems.

IMPORTANT — HOW TO USE WITH DAY FOLDERS:

    Each Day folder contains:
        Day1/
            solution.py
            input.txt
            example.txt

    The recommended AoC pattern is to load files relative to the folder
    containing solution.py instead of relying on the working directory.

    Example in Day1/solution.py:

        from pathlib import Path
        from utils import read_text, read_lines

        BASE_DIR = Path(__file__).parent
        data = read_text(BASE_DIR / "input.txt")

    This works regardless of where PyCharm or your terminal runs the code.
"""

from __future__ import annotations
from collections import deque
from typing import Iterable, Iterator, Callable, TypeVar, Sequence
from pathlib import Path
import re
import math


T = TypeVar("T")
Pos = tuple[int, int]  # (row, col) or (y, x)


# ---------------------------------------------------------------------------
# Basic input helpers (Path-aware)
# ---------------------------------------------------------------------------

def read_text(path: str | Path) -> str:
    """
    Read an entire file as a single string, stripping the trailing newline.

    Args:
        path: Either a string or pathlib.Path.

    Example (inside solution.py):
        BASE_DIR = Path(__file__).parent
        data = read_text(BASE_DIR / "input.txt")
    """
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        return f.read().rstrip("\n")


def read_lines(path: str | Path, keep_empty: bool = False) -> list[str]:
    """
    Read a file and return a list of lines without trailing newlines.

    Args:
        path: str or Path.
        keep_empty: If False, remove blank lines.

    Example:
        lines = read_lines(BASE_DIR / "input.txt")
    """
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]
    if not keep_empty:
        lines = [line for line in lines if line]
    return lines

def read_sections(path: str | Path) -> list[list[str]]:
    """
    Read a file and split into sections separated by blank lines.

    Returns:
        A list of sections, where each section is a list of lines (strings).
        Blank lines are used as separators and are not included.

    Example:
        If the file contains:
            A
            B

            C
            D

        read_sections(...) returns:
            [["A", "B"], ["C", "D"]]
    """
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]

    sections = []
    current = []

    for line in lines:
        if line == "":
            # end of a section
            if current:
                sections.append(current)
                current = []
        else:
            current.append(line)

    # add last section (if file doesn't end with blank line)
    if current:
        sections.append(current)

    return sections

def parse_ints(s: str) -> list[int]:
    """
    Extract all integers (negative and positive) from a string.

    Useful for lines like:
        'x=-3, y=42, z=0'

    Example:
        nums = parse_ints("x=-3, y=42, z=0")  # [-3, 42, 0]
    """
    return [int(x) for x in re.findall(r"-?\d+", s)]


# ---------------------------------------------------------------------------
# Sequence / iterator helpers
# ---------------------------------------------------------------------------

def chunks(iterable: Iterable[T], size: int) -> Iterator[list[T]]:
    """
    Yield lists of length `size` from iterable. Last chunk may be shorter.

    Example:
        for c in chunks([1,2,3,4,5], 2):
            print(c)  # [1,2], [3,4], [5]
    """
    if size <= 0:
        raise ValueError("size must be > 0")

    buf: list[T] = []
    for item in iterable:
        buf.append(item)
        if len(buf) == size:
            yield buf
            buf = []
    if buf:
        yield buf


def pairwise(iterable: Iterable[T]) -> Iterator[tuple[T, T]]:
    """
    Yield overlapping pairs: (item0, item1), (item1, item2), ...

    Reimplements itertools.pairwise so you don't need to import it.

    Example:
        list(pairwise([10,20,30]))  # [(10,20), (20,30)]
    """
    it = iter(iterable)
    try:
        prev = next(it)
    except StopIteration:
        return

    for item in it:
        yield prev, item
        prev = item


def window(iterable: Sequence[T], size: int, step: int = 1) -> Iterator[Sequence[T]]:
    """
    Slide a window of fixed size over a sequence.

    Example:
        list(window([1,2,3,4,5], 3))
        # [[1,2,3], [2,3,4], [3,4,5]]
    """
    if size <= 0:
        raise ValueError("size must be > 0")
    if step <= 0:
        raise ValueError("step must be > 0")

    n = len(iterable)
    for i in range(0, n - size + 1, step):
        yield iterable[i:i + size]


# ---------------------------------------------------------------------------
# Math / utility helpers
# ---------------------------------------------------------------------------

def sign(x: int) -> int:
    """Return -1, 0, or 1 based on the sign of x."""
    return 1 if x > 0 else -1 if x < 0 else 0


def manhattan(a: Pos, b: Pos) -> int:
    """
    Compute Manhattan distance between two points.

    Example:
        manhattan((0,0), (3,4)) == 7
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# ---------------------------------------------------------------------------
# Grid helpers
# ---------------------------------------------------------------------------

def grid_from_lines(lines: list[str]) -> dict[Pos, str]:
    """
    Convert list of strings into a dict grid mapping (r,c) -> char.

    Example:
        lines = ["..#", "#.."]
        grid[(0,2)] == '#'
    """
    grid: dict[Pos, str] = {}
    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            grid[(r, c)] = ch
    return grid


def neighbors4(pos: Pos) -> list[Pos]:
    """Return up/down/left/right neighbors."""
    r, c = pos
    return [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]


def neighbors8(pos: Pos) -> list[Pos]:
    """Return all 8 neighbors including diagonals."""
    r, c = pos
    return [
        (r-1,c-1), (r-1,c), (r-1,c+1),
        (r,  c-1),           (r,  c+1),
        (r+1,c-1), (r+1,c), (r+1,c+1),
    ]


def in_bounds(pos: Pos, height: int, width: int) -> bool:
    """
    Check if pos=(r,c) is within a grid of height x width.
    """
    r, c = pos
    return 0 <= r < height and 0 <= c < width


# ---------------------------------------------------------------------------
# Graph / search helpers
# ---------------------------------------------------------------------------

def bfs(
    start: T,
    neighbors_fn: Callable[[T], Iterable[T]],
    goal_fn: Callable[[T], bool],
) -> tuple[bool, dict[T, T | None]]:
    """
    A generic Breadth-First Search.

    Args:
        start: Starting node.
        neighbors_fn: Function returning neighbors of a node.
        goal_fn: Returns True when node satisfies goal.

    Returns:
        (found, parent)
            found: True if goal reached
            parent: dict mapping node -> its parent; parent[start] = None

    Example (grid BFS):

        lines = read_lines(BASE_DIR / "input.txt")
        height, width = len(lines), len(lines[0])

        def neighbors(pos):
            for n in neighbors4(pos):
                if in_bounds(n, height, width) and lines[n[0]][n[1]] != '#':
                    yield n

        found, parent = bfs(start_pos, neighbors, lambda p: p == goal_pos)
    """
    queue = deque([start])
    parent: dict[T, T | None] = {start: None}

    while queue:
        current = queue.popleft()

        if goal_fn(current):
            return True, parent

        for nxt in neighbors_fn(current):
            if nxt not in parent:  # unvisited
                parent[nxt] = current
                queue.append(nxt)

    return False, parent
