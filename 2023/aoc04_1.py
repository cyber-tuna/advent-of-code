#!/usr/bin/python3

import re
import sys

total = 0
lines = [x.strip() for x in sys.stdin]

for line in lines:
    winning = set(re.split('\s+', line.split("|")[0].split(": ")[1].strip()))
    mine = set(re.split('\s+', line.split(" | ")[1]))

    w = len(winning.intersection(mine))

    if w:
        total += 2**(w-1)

print(total)