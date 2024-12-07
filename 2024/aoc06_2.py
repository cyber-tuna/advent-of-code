#!/usr/bin/python3

import sys

lines = [x.strip() for x in sys.stdin]
width = len(lines[0])
height = len(lines)

oob = [-1, height]

next = [(-1, 0), (0,1), (1,0), (0,-1)]

def is_loop(lines):
    direction = 0
    total = 0
    for i, row in enumerate(lines): # row
        for j, column in enumerate(row): # column
            if column == "^":
                cur_i = i
                cur_j = j
                while(1):
                    next_i, next_j = next[direction]

                    if  cur_i + next_i in oob or \
                        cur_j + next_j in oob:
                        return False

                    if lines[cur_i + next_i][cur_j + next_j] == "#":
                        d = direction
                        direction = (direction + 1) % 4
                        next_i, next_j = next[direction]
                        prev_i, prev_j = next[direction]

                    if lines[cur_i + next_i][cur_j + next_j] == "#":
                        direction = (direction + 1) % 4
                        next_i, next_j = next[direction]

                    if lines[cur_i + next_i][cur_j + next_j] == "#":
                        direction = (direction + 1) % 4
                        next_i, next_j = next[direction]
                        

                    cur_i += next_i
                    cur_j += next_j

                    total += 1
                    if total > (width * height):
                        return True

total = 0
for i, row in enumerate(lines): # row
    for j, column in enumerate(row): # column
        b = [list(x) for x in lines]

        if b[i][j] == "^":
            continue

        b[i][j] = "#"

        if is_loop(b):
            total += 1

print(total)