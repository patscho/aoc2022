from copy import deepcopy

# FILE = "day05/test-input.txt"
FILE = "day05/input.txt"


def move_crate(amount, from_stack, to_stack, stacks):
    """Part 1"""
    for _ in range(amount):
        crate = stacks[from_stack].pop()
        stacks[to_stack].append(crate)
    return stacks


def move_crates(amount, from_stack, to_stack, stacks):
    """Part 2"""
    moving = stacks[from_stack][-amount:]
    stacks[from_stack] = stacks[from_stack][:-amount]
    stacks[to_stack].extend(moving)
    return stacks


def top_crates(stacks):
    word = ""
    for i in range(len(stacks)):
        crate = stacks[f"{i+1}"].pop()
        word += crate
    return word


lines = []
moves = []
with open(FILE) as f:
    for line in f:
        crates_string = line[1::4]
        lines.append(crates_string)
        if line.strip() == "":
            # Read the rest of the file as moves
            for line in f:
                move = line.strip()
                moves.append(move)
stacks = {}
for i in lines[-2]:
    stacks[i] = []
for line in lines[-2::-1]:
    for i in range(0, len(line)):
        if line[i] != " ":
            stacks[f"{i+1}"].append(line[i])

stacks2 = deepcopy(stacks)

# Part 1
for move in moves:
    x, amount, y, from_stack, z, to_stack = move.split()
    stacks = move_crate(int(amount), from_stack, to_stack, stacks)
answer = top_crates(stacks)
print(f"The answer for part 1 is: {answer}")

# Part 2
for move in moves:
    x, amount, y, from_stack, z, to_stack = move.split()
    stacks2 = move_crates(int(amount), from_stack, to_stack, stacks2)
answer = top_crates(stacks2)
print(f"The answer for part 2 is: {answer}")
