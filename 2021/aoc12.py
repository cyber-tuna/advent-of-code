edges = {}

path = []
path_count = 0

def visit(node):
    if node == "end":
        global path_count
        path_count += 1
        return
    if node.islower() and node in path:
        return

    path.append(node)

    for neighbor in edges[node]:
        visit(neighbor)

    p = path.pop()

with open("input12.txt", "r") as file:
    lines = file.read().splitlines()
    for line in lines:
        left,right  = line.split('-')

        edges[left] = edges.get(left, set())
        edges[left].add(right)

        edges[right] = edges.get(right, set())
        edges[right].add(left)

visit("start")

print(path_count)
