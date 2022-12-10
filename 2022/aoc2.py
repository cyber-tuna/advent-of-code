import sys

lines = sys.stdin.readlines()

score = 0

for line in lines:
    game = "".join(line.strip().split())
    
    s = ord(game[1]) - 87

    if game == "AY" or game == "BZ" or game == "CX":
        score += (6 + s)
    elif game == "AX" or game == "BY" or game == "CZ":
        score += (3 + s)
    else:
        score += s

print(score)
