import sys

lines = sys.stdin.readlines()

knots = [[0,0] for x in range(10)]
tails = set()

def update_tail(head, tail):

    x_delta = head[0] - tail[0]
    y_delta = head[1] - tail[1]
    
    if abs(x_delta) < 2 and abs(y_delta) < 2:
        return
    # up 
    if x_delta == 0 and y_delta > 0:
        tail[1] = head[1] - 1 
    # down
    elif x_delta == 0 and y_delta < 0:
        tail[1] = head[1] + 1
    # left
    elif y_delta == 0 and x_delta > 0:
        tail[0] = head[0] - 1 
    # right
    elif y_delta == 0 and x_delta < 0:
         tail[0] = head[0] + 1
    # NE        
    elif x_delta > 0 and y_delta > 0:
        tail[0] += 1
        tail[1] += 1
    # SE
    elif x_delta > 0 and y_delta < 0:
        tail[0] += 1
        tail[1] -= 1
    # SW
    elif x_delta < 0 and y_delta < 0:
        tail[0] -= 1
        tail[1] -= 1
    # NW
    else: 
        tail[0] -= 1
        tail[1] += 1

for line in lines:
    direction, val = line.strip().split(" ")
    val = int(val)

    for x in range(val):
        match direction:
            case "U":
                knots[0][1] += 1
            case "R":
                knots[0][0] += 1 
            case "L":
                knots[0][0] -= 1 
            case _:
                knots[0][1] -= 1 
                
        for y in range(9):
            update_tail(knots[y], knots[y+1])
            tails.add(tuple(knots[9]))

print(len(tails))
