import string
import sys

stacks = {
    1:["S","C","V","N"],
    2:["Z","M","J","H","N","S"],
    3:["M","C","T","G","J","N","D"],
    4:["T","D","F","J","W","R","M"],
    5:["P","F","H"],
    6:["C","T","Z","H","J"],
    7:["D","P","R","Q","F","S","L","Z"],
    8:["C","S","L","H","D","F","P","W"],
    9:["D","S","M","P","F","N","G","Z"],
}

lines = sys.stdin.readlines()

count = 0

for line in lines:

    line = line.strip().split(" ")
    count, src, dst = int(line[1]), int(line[3]), int(line[5])

    for c in range(count):
        stacks[dst].append(stacks[src].pop())

print("".join(x.pop() for x in stacks.values()))
    
