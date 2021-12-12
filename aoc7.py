import time 
start = time.time()

def triangular_number(num):
    return int((pow(num,2) + num)/2)

def find_minimum():
    crabs = []
    with open("input7.txt") as file:
        crabs = [int(x) for x in file.read().split(",")]

    largest = max(crabs)

    quanity_by_position = [0]*(largest+1)
    for crab in crabs:
        quanity_by_position[crab] += 1

    fuel_cost_lookup = {}

    minimum = 99999999999999
    cost_by_position = [0]*(largest+1)
    for i in range(0,largest+1):
        for j in range(0,largest+1):
            distance = abs(i-j)
            fuel_cost = 0
            if distance in fuel_cost_lookup:
                fuel_cost = fuel_cost_lookup[distance]
            else:
                fuel_cost = triangular_number(abs(i-j))
                fuel_cost_lookup[distance] = fuel_cost

            cost_by_position[i] += (fuel_cost*quanity_by_position[j])
            if cost_by_position[i] > minimum:
                break
        if cost_by_position[i] < minimum:
            minimum = cost_by_position[i]

    print(minimum)

find_minimum()

end = time.time()
print("Algorithm took: ", end - start)