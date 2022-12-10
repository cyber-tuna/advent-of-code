import sys

lines = sys.stdin.readlines()

solution = 0

total_size = 0
remaining_size = 0

candidates = []

to_free = 0

class Node:
  
    def __init__(self, name, is_dir=False, parent=None, size=-1):
       self.name = name
       self.is_dir = is_dir
       self.parent = parent
       self.children = []
       self.size = int(size)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def has(self, key):
        for child in self.children:
            if child.name == key:
                return True
        return False

    def get(self, key):
        for child in self.children:
            if child.name == key:
                return child 
        return None

    def add_child(self, name, is_dir, size):
        if not self.has(name):
            self.children.append(Node(name, is_dir, parent=self, size=size))

    def get_size(self):
        total = 0;

        for child in self.children:
            if child.is_dir:
                total += child.get_size()
            else:
                total += child.size
    
        global remaining_size
        if self.is_dir and (70000000 - (total_size - total)) > 30000000: 
            print("found candidate of size", total)
            candidates.append(total) 

        return total


    def print_h(self):
        cur = self
        while True:
            print(cur.name, end="")
            if self.parent is None:
                break
            cur = self.parent
            
cur = Node("root", is_dir=True) 
cur.add_child("/", True, -1)
root = cur

for line in lines:
    line = line.strip()

    if line[0] == '$':
        cmd = line.split(" ")[1]
        if cmd == "cd":
            arg = line.split(" ")[2]

            if arg == "..":
                cur = cur.parent 
            else:
                if cur.has(arg):
                    cur = cur.get(arg)
                else:
                    raise RuntimeError("non existent") 
            
        elif cmd == "ls":
            pass
    else:
        a, b = line.split(" ")

        if a == "dir":
            cur.add_child(b, True, -1)
        else:
            cur.add_child(b, False, a)

total_size = root.get_size()

remaining_size = 70000000 - total_size


candidates.clear()

print(remaining_size)

root.get_size()

print(min(candidates))
