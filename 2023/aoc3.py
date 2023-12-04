#!/usr/bin/python3

import re
import string
import sys

syms = string.punctuation.replace(".","")

total = 0
lines = [x.strip() for x in sys.stdin]

w = len(lines[0]) - 1
h = len(lines) - 1

for y,  line in enumerate(lines):
    pattern = re.compile("\d+")
    matches = pattern.finditer(line)

    for match in matches:
        for x in range(match.start()-1, match.end() + 1):
            top_y = max(0, y-1)
            bot_y = min(y+1, h)
            xx = min(max(0, x), w)

            if lines[top_y][xx] in syms or \
               lines[y][xx] in syms or \
               lines[bot_y][xx] in syms:
                total += int(line[match.start():match.end()])
                break

print(total)