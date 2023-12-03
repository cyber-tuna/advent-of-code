import sys

lines = sys.stdin.readlines()

width = 0
height = 0

for line in lines:
    _points = line.split("->")
    points = [x.strip().split(",") for x in _points]

    for point in points:
        width = max(int(point[0]), width)
        height = max(int(point[1]), height)

height += 1
width += 500

cave = [['.' for x in range(width)] for y in range(height)]
cave.append(["." for x in range(width)])
cave.append(["#" for x in range(width)])

for line in lines:
    _points = line.split("->")
    points = [x.strip().split(",") for x in _points]

    for x in range(len(points) - 1):
        p1 = points[x]
        p2 = points[x+1]

        p1x = int(p1[0])
        p1y = int(p1[1])

        p2x = int(p2[0])
        p2y = int(p2[1])

        # Vertical line (p1x == p2x)
        if p1x == p2x:
            length = abs(int(points[x+1][1]) - int(points[x][1])) + 1
           
            if p1y < p2y: 
                for j in range(length):
                    cave[p1y+j][p1x] = "#"
            else:
                for j in range(length):
                    cave[p1y-j][p1x] = "#"

        # Horizontal line (p1y == p2y)
        elif p1y == p2y:
            length = abs(int(points[x+1][0]) - int(points[x][0])) + 1

            if p1x < p2x: 
                for j in range(length):
                    cave[p1y][p1x+j] = "#"
            else:
                for j in range(length):
                    cave[p1y][p1x-j] = "#"
        else:
            raise RuntimeError("unknown condition")


# Now pour the sand
sand_count = 0
while True:
    sandx = 500
    sandy = 0

    while True:
        # move down
        if cave[sandy+1][sandx] == ".":
            sandy += 1
            continue
    
        # move left 
        if cave[sandy+1][sandx-1] == ".":
            sandy += 1
            sandx -= 1
            continue
            
        # move right 
        if cave[sandy+1][sandx+1] == ".":
            sandy += 1
            sandx += 1
            continue
            
        # then it comes to rest
        cave[sandy][sandx] = "o"
        sand_count += 1
        break
    
    if sandy == 0 and sandx == 500:
        break

print(sand_count)

