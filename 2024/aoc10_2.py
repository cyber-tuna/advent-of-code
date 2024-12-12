#!/usr/bin/python3

import sys

lines = [x.strip() for x in sys.stdin]

width = len(lines[0])
height = len(lines)

total = 0

def go(i,j, prev):
    if i < 0 or i >= height:
        return 0

    if j < 0 or j >= width:
        return 0

    cur = lines[i][j]

    if int(cur) != (int(prev) + 1):
        # trail doesn't increase by 1
        return 0

    if int(lines[i][j]) == 9:
        return 1

    return go(i-1, j, cur) + go(i, j+1, cur) + go(i+1, j, cur) + go(i, j-1, cur)

for i, row in enumerate(lines): # row
    for j, column in enumerate(row): # column
        if int(lines[i][j]) == 0:
            total += go(i,j, -1)


print(total)