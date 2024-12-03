#!/usr/bin/python3

import sys

sum = 0

def increasing(levels):
    for x in range(len(levels)-1):
        dist = int(levels[x+1]) - int(levels[x])

        if dist > 3 or dist < 1:
            return False

    return True

def decreasing(levels):
    for x in range(len(levels)-1):
        dist = int(levels[x]) - int(levels[x+1])

        if dist > 3 or dist < 1:
            return False

    return True

for report in sys.stdin:
    safe = True
    levels = report.strip().split(" ")

    if increasing(levels) or decreasing(levels):
        sum += 1

print(sum)