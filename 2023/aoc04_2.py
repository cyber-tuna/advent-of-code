#!/usr/bin/python3

import re
import sys

total = 0
lines = [x.strip() for x in sys.stdin]

scorecards = {n: 1 for n in range(1, len(lines)+1)}

for i, line in enumerate(lines, start=1):
    winning = set(re.split('\s+', line.split("|")[0].split(": ")[1].strip()))
    mine = set(re.split('\s+', line.split(" | ")[1]))

    for x in range(scorecards[i]):
        matching = len(winning.intersection(mine))
        for x in range(i+1, i+1+matching):
            scorecards[x] += 1

print(sum(scorecards.values()))