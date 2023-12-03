#!/usr/bin/python3

import sys

total = 0
for line in sys.stdin:
    line = line.strip()

    game_num = int(line.split(":")[0].split(" ")[1])
    draws = line.split(":")[1].strip().replace(';', ',').split(",")

    red_max = blue_max = green_max = 0
    for draw in draws:
        quantity, color = draw.strip().split(" ")
        quantity = int(quantity)
        if color == "red":
            red_max = max(quantity, red_max)
        elif color == "green":
            green_max = max(quantity, green_max)
        elif color == "blue":
            blue_max = max(quantity, blue_max)
            
    total += (red_max * blue_max * green_max) 

print(total)

