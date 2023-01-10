FILE = "day05/test-input.txt"

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
    for i in range(len(line) - 1, -1, -1):
        if line[i] != " ":
            stacks[f"{i+1}"].append(line[i])
