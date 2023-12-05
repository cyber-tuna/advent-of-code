#!/usr/bin/python3

import sys

total = 0
for line in sys.stdin:
    line = line.strip()

    print(line)
    game_num = int(line.split(":")[0].split(" ")[1])

    draws = line.split(":")[1].strip().replace(';', ',').split(",")

    possible = True
    for draw in draws:
        quantity, color = draw.strip().split(" ")
        quantity = int(quantity)
        if color == "red" and quantity > 12:
            possible = False
        elif color == "green" and quantity > 13:
            possible = False
        elif color == "blue" and quantity > 14:
            possible = False
            
    if possible:
        total += game_num

print(total)

