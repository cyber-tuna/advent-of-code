#!/usr/bin/python3

import sys

l1, l2 = sys.stdin.read().split("\n")
times = [int(x) for x in l1.split(": ")[1].split()]
records = [int(x) for x in l2.split(": ")[1].split()]
wins = []

for i, time in enumerate(times):
    count = 0
    for hold in range(0, time + 1):
        moving_time = time - hold
        distance = moving_time * hold
        if distance > records[i]:
            count += 1

    wins.append(count)

total = 1
for win in wins:
    total *= win

print(total)