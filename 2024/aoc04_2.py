#!/usr/bin/python3

import re
import sys

total = 0

lines = [x.strip() for x in sys.stdin]

w = len(lines[0]) - 1
h = len(lines) - 1

for i in range(1, h): # row
    for j in range(1, w): # column
        a = [lines[i-1][j-1] + lines[i][j] + lines[i+1][j+1] == "MAS",
             lines[i+1][j-1] + lines[i][j] + lines[i-1][j+1] == "MAS",
             lines[i-1][j+1] + lines[i][j] + lines[i+1][j-1] == "MAS",
             lines[i+1][j+1] + lines[i][j] + lines[i-1][j-1] == "MAS"]
 
        total += int(sum(a) >= 2)

print(total)