import sys

lines = sys.stdin.readlines()

score = 0

s = {
    "AX": (0 + 3),
    "AY": (3 + 1),
    "AZ": (6 + 2),
    "BX": (0 + 1),
    "BY": (3 + 2),
    "BZ": (6 + 3),
    "CX": (0 + 2),
    "CY": (3 + 3),
    "CZ": (6 + 1),
}
for line in lines:
    score += s["".join(line.strip().split())]
    

print(score)
