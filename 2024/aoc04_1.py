#!/usr/bin/python3

import re
import sys

sum = 0

lines = [x.strip() for x in sys.stdin]

w = len(lines[0]) - 1
h = len(lines) - 1

for i in range(len(lines)): # row
    for j in range(len(lines[i])): # column
        # S
        if i < (h - 2):
            sum += int("".join([lines[i+x][j] for x in range(0, 4)]) == "XMAS")

        # N
        if i > 2:
            sum += int("".join([lines[i-x][j] for x in range(0, 4)]) == "XMAS")

        # W
        if j > 2:
            sum += int("".join([lines[i][j-x] for x in range(0, 4)]) == "XMAS")

        # E
        if j < (w - 2): 
            sum += int("".join([lines[i][j+x] for x in range(0, 4)]) == "XMAS")

        # NW
        if j > 2 and i > 2: 
            sum += int("".join([lines[i-x][j-x] for x in range(0, 4)]) == "XMAS")

        # NE
        if j < (w - 2) and i > 2: 
            sum += int("".join([lines[i-x][j+x] for x in range(0, 4)]) == "XMAS")

        # SE
        if i < (h - 2) and j < (w - 2): 
            sum += int("".join([lines[i+x][j+x] for x in range(0, 4)]) == "XMAS")

        # SW
        if i < (h - 2) and j > 2: 
            sum += int("".join([lines[i+x][j-x] for x in range(0, 4)]) == "XMAS")

print(sum)