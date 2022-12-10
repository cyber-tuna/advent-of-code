

octopus_map = []
lines = []
total_flashes = 0

def print_map():
    for line in octopus_map:
        print(line)

def increment_steps():
    for i in range(0,len(lines)):
        for j in range(0,len(lines[0])):
            octopus_map[i][j] += 1

def increment(i,j):
    if i < 0 or j < 0 or i > 9 or j > 9:
        return
    if octopus_map[i][j] == 0:
        return
    octopus_map[i][j] += 1

def flash(i,j):
    global total_flashes
    total_flashes += 1
    octopus_map[i][j] = 0
    increment(i-1,j)
    increment(i,j-1)
    increment(i+1,j)
    increment(i,j+1)
    increment(i-1,j-1)
    increment(i-1,j+1)
    increment(i+1,j-1)
    increment(i+1,j+1)

def check_sync():
    for i in range(0,len(lines)):
        for j in range(0,len(lines[0])):
            if octopus_map[i][j] != 0:
                return False

    return True

def do_flashes():
    while True:
        no_flashes = True
        for i in range(0,len(lines)):
            for j in range(0,len(lines[0])):
                if octopus_map[i][j] > 9:
                    flash(i,j)
                    no_flashes = False
        if no_flashes:
            break

with open("input11.txt", "r") as file:
    lines = file.read().splitlines()

for line in lines:
    row = []
    for char in line:
        row.append(int(char))
    octopus_map.append(row)

i = 0
while True:
    i += 1
    increment_steps()
    do_flashes()
    if check_sync():
        break

    print("After step:", i)
    print_map()

print(i)


