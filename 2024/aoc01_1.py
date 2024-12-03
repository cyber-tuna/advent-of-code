#!/usr/bin/python3

import sys

sum = 0
input = sys.stdin.read().strip().split("\n")
a = [int(x.split()[0]) for x in input]
b = [int(x.split()[1]) for x in input]

a.sort()
b.sort()

for x in range(len(a)):
    sum += abs(a[x] - b[x])

print(sum)