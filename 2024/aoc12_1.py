#!/usr/bin/python3

import sys

lines = [x.strip() for x in sys.stdin]

width = len(lines[0])
height = len(lines)

total = 0

visited = set()

area = 0
def go(i,j, prev):
    if i < 0 or i >= height:
        return 1

    if j < 0 or j >= width:
        return 1

    cur = lines[i][j]

    if prev != cur:
        # not part of the plot
        return 1

    if (i,j) in visited:
        # already visited, return
        return 0

    global area
    area += 1
    visited.add((i,j))

    return go(i-1, j, cur) + go(i, j+1, cur) + go(i+1, j, cur) + go(i, j-1, cur)


for i, row in enumerate(lines): # row
    for j, column in enumerate(row): # column
        if (i,j) not in visited:
            area = 0
            perimeter = go(i,j, lines[i][j])
            total += (area * perimeter)

print(total)