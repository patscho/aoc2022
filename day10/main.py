from cpu import CPU

# FILE = "day10/input-test.txt"
FILE = "day10/input.txt"


with open(FILE) as f:
    instuctions = f.readlines()
    instuctions = [i.strip() for i in instuctions]

cpu = CPU()
for i in instuctions:
    if i == "noop":
        cpu.noop()
    else:
        value = i.split()[1]
        cpu.addx(int(value))

# part 1
print(sum(cpu.signal_strengths))

# part 2
for i in range(len(cpu.crt_rows)):
    print("".join(cpu.crt_rows[i]))
