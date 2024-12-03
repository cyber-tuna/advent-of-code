#!/usr/bin/python3

import sys

sum = 0
input = sys.stdin.read().strip().split("\n")
a = [int(x.split()[0]) for x in input]
b = [int(x.split()[1]) for x in input]

for x in range(len(a)):
    sum += b.count(a[x]) * a[x]

print(sum)
