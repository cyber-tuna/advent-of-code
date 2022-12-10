import string
import sys

lines = sys.stdin.readlines()

count = 0

for line in lines:
    one, two = line.strip().split(",")
    one = one.split("-")
    two = two.split("-")
    
    if all([int(x) in range(int(one[0]), int(one[1])+1) for x in two]):
        print(one,two)
        count += 1
    elif all([int(x) in range(int(two[0]), int(two[1])+1) for x in one]):
        print(one,two)
        count += 1

print(count)
