#!/usr/bin/python3

import sys

l1, l2 = sys.stdin.read().split("\n")
time = int(''.join(l1.split(": ")[1].split()))
record = int(''.join(l2.split(": ")[1].split()))

total = 0
for hold in range(0, time + 1):
    moving_time = time - hold
    distance = moving_time * hold
    if distance > record:
        total += 1

print(total)