import sys

inp = sys.stdin.read().strip()

pairs = inp.split("\n\n")

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

solution = 0
for ii, pair in enumerate(pairs):
    _p1, _p2 = pair.split()

    s1 = f"list({_p1})"
    s2 = f"list({_p2})"

    l1 = eval(s1)
    l2 = eval(s2)
    
    print("-------------------------------------------------")
    print(f"pair:\n{pair}")
    if compare_list(l1, l2) > 0:
        print("ADDING", ii)
        solution += (ii + 1)
    print()

print(solution)
