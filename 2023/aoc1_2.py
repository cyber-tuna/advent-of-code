#!/usr/bin/python3

import re
import sys

sum = 0
for line in sys.stdin:
    line = line.strip()

    new = ""
    for i, a in enumerate(line):
        if a.isnumeric():
            new += a
        elif line[i:i+3] == "one":
            new += '1'
        elif line[i:i+3] == "two":
            new += '2'
        elif line[i:i+5] == "three":
            new += '3'
        elif line[i:i+4] == "four":
            new += '4'
        elif line[i:i+4] == "five":
            new += '5'
        elif line[i:i+3] == "six":
            new += '6'
        elif line[i:i+5] == "seven":
            new += '7'
        elif line[i:i+5] == "eight":
            new += '8'
        elif line[i:i+4] == "nine":
            new += '9'

    sum += int(new[0] + new[-1])

print(sum)
