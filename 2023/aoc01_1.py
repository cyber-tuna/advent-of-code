#!/usr/bin/python3

import re
import sys

sum = 0
for line in sys.stdin:
    line = re.sub('[abcdefghijklmnopqrstuvwxyz]', '', line.rstrip())
    sum += int(line[0] + line[-1])

print(sum)
