#!/usr/bin/python3

import re
import sys

input = "".join(line.strip() for line in sys.stdin)
sum = 0

# Remove all disabled code
m = re.sub('don\'t\(\).*?do\(\)', '', input)

# Edge case where there may be a final don't() not followed by a do()
m = re.sub('don\'t\(\)(.*)', '', m)

for mul in re.findall('mul\(\d{1,3},\d{1,3}\)', m):
   x, y = (mul.strip("mul(").strip(")")).split(",")
   sum += int(x) * int(y)

print(sum)