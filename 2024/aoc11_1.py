#!/usr/bin/python3

import sys

stones = sys.stdin.read().strip().split()

total = 0

for stone in stones:
    pre_blink = [stone]
    for x in range(25): # blinks
        post_blink = []
        for s in pre_blink:
            if int(s) == 0:
                post_blink.append('1')
            elif len(s) % 2 == 0: # even number of digits
                half = len(s) // 2
                post_blink.append(str(int(s[:half])))
                post_blink.append(str(int(s[half:])))
            else: # multiply by 2024
                post_blink.append(str(int(s) * 2024))

        pre_blink = post_blink

    total += len(pre_blink)

print(total)

