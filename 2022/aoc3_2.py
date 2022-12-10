import string
import sys

lines = sys.stdin.readlines()
total = 0 

for i in range(0, len(lines), 3):
    for j in string.ascii_letters:
        if j in lines[i] and j in lines[i+1] and j in lines[i+2]:
            if j.isupper():
                total += (ord(j) - 38)
            else:
                total += (ord(j) - 96)

print(total)

