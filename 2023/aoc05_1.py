#!/usr/bin/python3

import sys

maps = sys.stdin.read().split("\n\n")

low = 0

for s in maps[0].split(": ")[1].split():
    seed = int(s)

    for i in range(1,8):
        for line in maps[i].split("\n")[1:]:
            dest, src, size = line.split()
            if seed in range(int(src), int(src) + int(size)):
                seed = int(dest) + seed - int(src)
                break

    if not low:
        low = seed

    low = min(low, seed)

print(low)