import math
import sys
import time

_lines = sys.stdin.readlines()
lines = [list(x.strip()) for x in _lines]

width = len(lines[0])
height = len(lines)

startx = 0
starty = 0 
endx = 0
endy = 0

for row in range(len(lines)):
    for x in range(len(lines[row])):
        if lines[row][x] == 'S':
            startx = x
            starty = row
            lines[row][x] = 'a' 
        if lines[row][x] == 'E':
            endx = x
            endy = row
            lines[row][x] = 'z'

visited = [[False for x in range(width)] for x in range(height)] 
distance = [[math.inf for x in range(width)] for x in range(height)]
distance[starty][startx] = 0

def go(x, y):
    while True:
        altitude = ord(lines[y][x])
        
        max_alt = altitude + 1
    
        cur_dist = distance[y][x]
        distance_to = cur_dist + 1 
        # right
        if x < (width-1) and ((ord(lines[y][x+1])) <= max_alt) and not visited[y][x+1]:
            distance[y][x+1] = min(distance_to, distance[y][x+1])
    
        # down
        if y < (height-1) and ((ord(lines[y+1][x])) <= max_alt) and not visited[y+1][x]:
            distance[y+1][x] = min(distance_to, distance[y+1][x])
    
        # up
        if y > 0 and ((ord(lines[y-1][x])) <= max_alt) and not visited[y-1][x]:
            distance[y-1][x] = min(distance_to, distance[y-1][x])
    
        # left
        if x > 0 and ((ord(lines[y][x-1])) <= max_alt) and not visited[y][x-1]:
            distance[y][x-1] = min(distance_to, distance[y][x-1])
    
        # mark visited
        visited[y][x] = True 
    
        if visited[endy][endx]:
            break
        
        next_x = math.inf
        next_y = math.inf
        smallest_dist = math.inf
        for x in range(width):
            for y in range(height):
                if not visited[y][x] and distance[y][x] < smallest_dist:          
                    smallest_dist = distance[y][x]
                    next_x = x 
                    next_y = y 
        
        if next_x == math.inf or next_y == math.inf:
            break
    
        x = next_x 
        y = next_y 

go(startx, starty)
print(distance[endy][endx])
