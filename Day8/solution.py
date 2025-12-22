#!/usr/bin/env python3
from pathlib import Path
import sys
import itertools
import utils

BASE_DIR = Path(__file__).parent

def dist2(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    dz = a[2] - b[2]
    return dx*dx + dy*dy + dz*dz

def createPairs(coorList, k):
    pairs = []
    for i, j in itertools.combinations(range(len(coorList)), 2):
        d2 = dist2(coorList[i], coorList[j])
        pairs.append((d2, i, j))
    pairs.sort(key=lambda t: t[0])
    return pairs[:k]  # first k "connections" to attempt, in order

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path compression
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

def circuit_sizes(n, pairs):
    dsu = DSU(n)
    for _, i, j in pairs:
        dsu.union(i, j)

    # Count component sizes across ALL nodes (including singletons)
    comp = {}
    for node in range(n):
        root = dsu.find(node)
        comp[root] = comp.get(root, 0) + 1
    return sorted(comp.values(), reverse=True)

if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    k = int(sys.argv[2]) if len(sys.argv) > 2 else 10  # use 10 for the example, 1000 for real input

    data = utils.read_lines(BASE_DIR / filename)

    coorList = []
    for line in data:
        x, y, z = map(int, line.split(","))
        coorList.append((x, y, z))

    pairs = createPairs(coorList, k)
    sizes = circuit_sizes(len(coorList), pairs)

    print("Circuit sizes (desc):", sizes)
    print("Top 3 product:", sizes[0] * sizes[1] * sizes[2])
