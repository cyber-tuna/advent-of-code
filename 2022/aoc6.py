import sys

inp = sys.stdin.read().strip()

for x in range(3, len(inp)):
    s = {inp[x-y] for y in range(4)}

    if len(s) == 4:
        break

print(x+1)
