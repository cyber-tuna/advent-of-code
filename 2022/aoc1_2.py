import sys

inp = sys.stdin.read().strip()

totals = []
for elf in inp.split("\n\n"):
    totals.append(sum([int(x) for x in elf.split("\n")]))

total = totals.pop(totals.index(max(totals))) + \
        totals.pop(totals.index(max(totals))) + \
        totals.pop(totals.index(max(totals))) 

print(total)
