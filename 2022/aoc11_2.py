import sys

line = sys.stdin.read().strip()

_monkeys = line.split("Monkey")[1:]
monkeys = []

lcm = 1

class Monkey():
    def __init__(self, items, operation, test, throw_true, throw_false):
        self.items = [int(x) for x in items]
        self.operation = operation
        self.test = int(test)
        self.throw_true = int(throw_true)
        self.throw_false = int(throw_false)
        self.inspected = 0

    def take_turn(self):
        operator, operand = self.operation.split(" ")
        
        while len(self.items) != 0:
            item = int(self.items.pop(0))
            it = item
            self.inspected += 1

            if operand == "old":
                op = item
            else:
                op = int(operand)

            if operator == "+":
                item = item + op
            else:
                item = item * op

            item = item % lcm

            if item % self.test == 0:
                monkeys[self.throw_true].items.append(item)    
            else:
                monkeys[self.throw_false].items.append(item)    

for monkey in _monkeys:
    # parse input file and create monkey objects
    items = monkey.split("Starting items: ")[1].split("\n")[0].split(",")
    operation = monkey.split("Operation: new = old ")[1].split("\n")[0]
    test = monkey.split("Test: divisible by ")[1].split("\n")[0]
    lcm *= int(test)
    throw_true = monkey.split("If true: throw to monkey ")[1].split("\n")[0]
    throw_false = monkey.split("If false: throw to monkey ")[1].split("\n")[0]
    
    monkeys.append(Monkey(items, operation, test, throw_true, throw_false))


print(lcm)

for round in range(10000):
    #print(round)
    for monkey in monkeys:
        monkey.take_turn()

s = [x.inspected for x in monkeys]
s.sort()
print(s.pop() * s.pop())
