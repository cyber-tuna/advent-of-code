import string
import sys

lines = sys.stdin.readlines()

total = 0 
for line in lines:
    l = len(line.strip())
    left = line[0:l//2]
    right = line[l//2:l]
    
    for i in string.ascii_letters:
        if i in left and i in right:
            if i.isupper():
                total += (ord(i) - 38)
            else:
                total += (ord(i) - 96)

print(total)
         
