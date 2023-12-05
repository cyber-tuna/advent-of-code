#!/usr/bin/python3

import re
import sys

total = 0
lines = [x.strip() for x in sys.stdin]

w = len(lines[0]) - 1
h = len(lines) - 1

d = {}

for y, line in enumerate(lines):
    pattern = re.compile("\d+")
    matches = pattern.finditer(line)

    for match in matches:
        for x in range(match.start()-1, match.end() + 1):
            top_y = max(0, y-1)
            bot_y = min(y+1, h)
            xx = min(max(0, x), w)

            val = line[match.start():match.end()]
            if lines[top_y][xx] == "*":
                d.setdefault((xx, top_y), []).append(int(val))
            if lines[y][xx] == "*":
                d.setdefault((xx, y), []).append(int(val))
            if lines[bot_y][xx] == "*":
                d.setdefault((xx, bot_y), []).append(int(val))

for key, val in d.items():
    if len(val) >= 2:
        total += val[0] * val[1]

print(total)
