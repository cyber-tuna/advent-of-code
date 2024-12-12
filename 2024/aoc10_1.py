#!/usr/bin/python3

import sys

lines = [x.strip() for x in sys.stdin]

width = len(lines[0])
height = len(lines)

total = 0

s = set()

def go(i,j, prev):
    if i < 0 or i >= height:
        return

    if j < 0 or j >= width:
        return

    cur = lines[i][j]

    if int(cur) != (int(prev) + 1):
        # trail doesn't increase by 1
        return

    if int(lines[i][j]) == 9:
        s.add((i,j))
        return

    # go north
    go(i-1, j, cur)

    # go east
    go(i, j+1, cur)

    # go south
    go(i+1, j, cur)

    # go west
    go(i, j-1, cur)

for i, row in enumerate(lines): # row
    for j, column in enumerate(row): # column
        if int(lines[i][j]) == 0:
            s.clear()
            go(i,j, -1)
            total += len(s)

print(total)