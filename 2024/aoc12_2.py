#!/usr/bin/python3

import sys

lines = [x.strip() for x in sys.stdin]

width = len(lines[0])
height = len(lines)

total = 0
visited = set()
regions = {}

def border_up(plot, target, visit, side):
    for x in range(1, plot[0]):
        up = (plot[0]-x, plot[1])
        if up not in target:
            break

        if (up[0], up[1] + side) in target:
            break

        visit.add(up)

def border_down(plot, target, visit, side):
    for x in range(1, height-plot[0]+1):
        down = (plot[0]+x, plot[1])
        if down not in target:
            break

        if (down[0], down[1] + side) in target:
            break

        visit.add(down)

def border_left(plot, target, visit, side):
    for x in range(1, plot[1]+1):
        left = (plot[0], plot[1]-x)
        if left not in target:
            break

        if (left[0] + side, left[1]) in target:
            break

        visit.add(left)

def border_right(plot, target, visit, side):
    for x in range(1, width-plot[1]+1):
        right = (plot[0], plot[1]+x)
        if right not in target:
            break

        if (right[0]+side, right[1]) in target:
            break

        visit.add(right)

def go(i, j, index, prev):
    if i < 0 or i >= height:
        return

    if j < 0 or j >= width:
        return

    cur = lines[i][j]

    if prev != cur:
        # not part of the plot
        return

    if (i,j) in visited:
        # already visited, return
        return

    visited.add((i,j))
    regions.setdefault(index, []).append((i,j))

    go(i-1, j, index, cur)
    go(i, j+1, index, cur)
    go(i+1, j, index, cur)
    go(i, j-1, index, cur)

index = 0
for i, row in enumerate(lines): # row
    for j, column in enumerate(row): # column
        if (i,j) not in visited:
            area = 0
            go(i,j, index, lines[i][j])
            index += 1

for val in regions.values():
    target_letter = lines[val[0][0]][val[0][1]]
    target = val

    visit = set()
    sides = 0

    for plot in target:
        if plot in visit:
            # skip visited plots
            continue

        # left borders
        if plot[1]-1 < 0 or \
        lines[plot[0]][plot[1]-1] != target_letter:
            sides += 1
            visit.add(plot)

            border_up(plot,target,visit,-1)
            border_down(plot,target,visit,-1)

    visit.clear()

    # right sides
    for plot in target:
        if plot in visit:
            # skip visited plots
            continue

        if plot[1]+1 >= width or \
        lines[plot[0]][plot[1]+1] != target_letter:
            sides += 1
            visit.add(plot)

            border_up(plot,target,visit,1)
            border_down(plot,target,visit,1)

    visit.clear()

    # top sides
    for plot in target:
        if plot in visit:
            # skip visited plots
            continue

        if plot[0]-1 < 0 or \
        lines[plot[0]-1][plot[1]] != target_letter:
            sides += 1
            visit.add(plot)

            border_right(plot,target,visit,-1)
            border_left(plot,target,visit,-1)

    visit.clear()

    # bottom sides
    for plot in target:
        if plot in visit:
            # skip visited plots
            continue

        if plot[0]+1 >= height or \
        lines[plot[0]+1][plot[1]] != target_letter:
            sides += 1
            visit.add(plot)

            border_right(plot,target,visit,1)
            border_left(plot,target,visit,1)

    total += (sides * len(target))

print(total)
