#!/usr/bin/python3

import re
import sys

input = sys.stdin.read().strip()

sum = 0
for mul in re.findall('mul\(\d{1,3},\d{1,3}\)', input):
    x, y = (mul.strip("mul(").strip(")")).split(",")
    sum += int(x) * int(y)

print(sum)