# FILE = "day07/test-input.txt"
FILE = "day07/input.txt"


class Directory:
    def __init__(self, name: str, parent):
        self.name = name
        self.subdirs = []
        self.size = 0
        self.parent = parent


with open(FILE) as f:
    lines = f.readlines()
    lines = [item.strip() for item in lines]


root = Directory("/", "")
current_dir = root
for line in lines:
    data = line.split()
    if line == "$ cd /":
        continue
    elif data[0] == "$":
        if data[1] == "ls":
            continue
        elif data[1] == "cd":
            if not data[2] == "..":
                for i in range(len(current_dir.subdirs)):
                    if current_dir.subdirs[i].name == data[2]:
                        current_dir = current_dir.subdirs[i]
                        break
            else:
                current_dir.parent.size += current_dir.size
                current_dir = current_dir.parent
    elif data[0] == "dir":
        current_dir.subdirs.append(Directory(data[1], current_dir))
    else:
        current_dir.size += int(data[0])

while not current_dir.name == "/":
    current_dir.parent.size += current_dir.size
    current_dir = current_dir.parent


def part1(current_dir, result1):
    if current_dir.size <= 100000:
        result1 += current_dir.size
    for directories in current_dir.subdirs:
        result1 = part1(directories, result1)
    return result1


print(part1(root, 0))

total_space = 70000000
required_space = 30000000
available_space = total_space - root.size
needed_space = required_space - available_space


def part2(current_dir, result, required):
    res = result
    if current_dir.size >= required and current_dir.size < result:
        res = current_dir.size
    for directory in current_dir.subdirs:
        res = part2(directory, res, required)
    return res


print(part2(root, total_space, needed_space))
