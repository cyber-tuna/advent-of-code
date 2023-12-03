import sys

inp = sys.stdin.read().strip()

inp = inp.replace("\n\n", "\n")

packets = inp.split("\n")

# return 1 if left is less, 0 if equal, -1 if greater 
def compare_list(l1, l2):

    i = max(len(l1), len(l2))
    for x in range(i):
        
        try:
            item1 = l1[x] 
        except IndexError:
            print("Left side ran out of items, so inputs are in the right order")
            return 1

        try:
            item2 = l2[x] 
        except IndexError:
            print("Right side ran out of items, so inputs are not in the right order")
            return -1 

        print(f"compare {item1} vs {item2}")

        if isinstance(item1, int) and isinstance(item2, int):
            if item1 < item2:
                print("left side is smaller - correct order")
                return 1 
            elif item1 > item2:
                print("right side is smaller - INCORRECT order")
                return -1
        elif isinstance(item1, list) and isinstance(item2, list):
            ret = compare_list(item1, item2)
            if ret == 1 or ret == -1:
                return ret
        else:
            if isinstance(item1, int) and isinstance(item2, list):
                ret = compare_list([item1], item2)
                if ret == 1 or ret == -1:
                    return ret
            elif isinstance(item1, list) and isinstance(item2, int):
                ret = compare_list(item1, [item2])
                if ret == 1 or ret == -1:
                    return ret
            else:
                raise RuntimeError("invalid combotron")

    return 0 

# bubble sort

packets.append("[[2]]")
packets.append("[[6]]")

while True:
    swaps = False
    for x in range(0, len(packets)-1):
        _p1 = packets[x]
        _p2 = packets[x+1]
    
        s1 = f"list({_p1})"
        s2 = f"list({_p2})"
    
        l1 = eval(s1)
        l2 = eval(s2)
        
        print("-------------------------------------------------")
        if compare_list(l1, l2) > 0:
            pass
        else:
            swaps = True
            tmp1 = _p1
            tmp2 = _p2
            packets[x] = _p2
            packets[x+1] = _p1


    if not swaps:
        break 

divider1 = 0
divider2 = 0
for x in range(len(packets)):
    print(packets[x])
    if packets[x] == "[[2]]":
       divider1 = (x+1)
    if packets[x] == "[[6]]":
        divider2 = (x+1)

print(divider1 * divider2)
