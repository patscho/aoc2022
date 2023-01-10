FILE = "day18/test-input.txt"
# FILE = "day18/input.txt"

with open(FILE) as f:
    cubes = [tuple(map(int, item.strip().split(","))) for item in f.readlines()]


def adjecent(xyz: tuple):
    return [
        (xyz[0] + 1, xyz[1], xyz[2]),
        (xyz[0] - 1, xyz[1], xyz[2]),
        (xyz[0], xyz[1] + 1, xyz[2]),
        (xyz[0], xyz[1] - 1, xyz[2]),
        (xyz[0], xyz[1], xyz[2] + 1),
        (xyz[0], xyz[1], xyz[2] - 1),
    ]


visible_list = []
for c in cubes:
    visible = 6
    for a in adjecent(c):
        if a in cubes:
            visible -= 1
    visible_list.append(visible)

print(sum(visible_list))
