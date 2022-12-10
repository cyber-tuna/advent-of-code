import sys

lines = sys.stdin.readlines()

forest = []
max_score = 0

d = len(lines)

for line in lines:
    forest.append(list(line.strip()))

for x in range(d):
    for y in range(d):

        # left
        left = 0
        for i in range(y-1, -1, -1):
            left += 1
            if forest[x][i] >= forest[x][y]:
                break

        # right
        right = 0
        for i in range(y+1, d):
            right += 1
            if forest[x][i] >= forest[x][y]:
                break

        # up 
        up = 0
        for i in range(x-1, -1, -1):
            up += 1
            if forest[i][y] >= forest[x][y]:
                break
        # down 
        down = 0
        for i in range(x+1, d):
            down += 1
            if forest[i][y] >= forest[x][y]:
                break

        max_score = max(max_score, up*down*left*right) 

print(max_score)
