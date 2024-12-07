#!/usr/bin/python3

import sys

lines = [x.strip() for x in sys.stdin]
width = len(lines[0])
height = len(lines)

oob = [-1, height]

next = [(-1, 0), (0,1), (1,0), (0,-1)]

direction = 0

cur_i = 0
cur_j = 0

visited = set()

for i, row in enumerate(lines): # row
    for j, column in enumerate(row): # column
        if column == "^":
            cur_i = i
            cur_j = j
            while(1):
                visited.add((cur_i,cur_j))
                next_i, next_j = next[direction]

                if cur_i + next_i in oob or \
                   cur_j + next_j in oob:
                   break

                if lines[cur_i + next_i][cur_j + next_j] == "#":
                    direction = (direction + 1) % 4
                    next_i, next_j = next[direction]

                cur_i += next_i
                cur_j += next_j

print(len(visited))