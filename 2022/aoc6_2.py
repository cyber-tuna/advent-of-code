import sys

inp = sys.stdin.read().strip()

for x in range(13, len(inp)):
    s = {inp[x-y] for y in range(14)}

    if len(s) == 14:
        break

print(x+1)
