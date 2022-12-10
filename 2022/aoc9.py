import sys

lines = sys.stdin.readlines()

head = [0,0]
tail = [0,0]

tails = set()

def diff():
    if abs(head[0] - tail[0]) > 1 or \
       abs(head[1] - tail[1]) > 1:
       return True
    
    return False
    

for line in lines:
    direction, val = line.strip().split(" ")
    val = int(val)

    for x in range(val):
        if direction == "U":
            head[1] += 1
            if diff():
                tail[0] = head[0]
                tail[1] = head[1]-1
        if direction == "R":
            head[0] += 1 
            if diff():
                tail[1] = head[1]
                tail[0] = head[0]-1
        if direction == "L":
            head[0] -= 1 
            if diff():
                tail[1] = head[1]
                tail[0] = head[0]+1
        if direction == "D":
            head[1] -= 1 
            if diff():
                tail[0] = head[0]
                tail[1] = head[1]+1
        tails.add(tuple(tail))
    
print(len(tails))
