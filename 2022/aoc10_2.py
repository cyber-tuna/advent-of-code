import sys

lines = sys.stdin.readlines()

cycle = 1
instruction = lines.pop(0)
register = 1

state = instruction.split(" ")[0].strip()
  
solution = 0
while len(lines) != 0:
    pixel = ((cycle-1)%40)

    if pixel >= (register-1) and pixel <= (register+1):
        print("#", end="")
    else:
        print(".", end="")

    if (pixel+1) % 40 == 0:
        print()

    ins = instruction.split(" ")

    if len(ins) > 1:
        opcode, operand = ins[0], int(ins[1])

    # State machine
    match state:
        case "noop":
            instruction = lines.pop(0)
            state = instruction.split(" ")[0].strip()
        case "addx":
            state = "addx_2" 
        case "addx_2":
            register += operand
            instruction = lines.pop(0)
            state = instruction.split(" ")[0].strip()

    cycle += 1

print()
