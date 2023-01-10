def move_right(position: tuple, map) -> tuple:
    x, y = position
    # print(f"inside move_right function. x: {x}, y: {y}")
    if x < len(map[y]) - 1:
        if map[y][x + 1] == ".":
            return (x + 1, y)
        elif map[y][x + 1] == "#":
            return position
    first_dot = map[y].find(".")
    first_wall = map[y].find("#")
    if first_wall == -1 or first_dot < first_wall:
        return (first_dot, y)
    else:
        return position


def move_left(position: tuple, map) -> tuple:
    x, y = position
    # print(f"inside move_left function. x: {x}, y: {y}")
    if x > 0:
        if map[y][x - 1] == ".":
            return (x - 1, y)
        elif map[y][x - 1] == "#":
            return position

    last_wall = -1
    last_dot = 0
    for i in range(len(map[y]) - 1, -1, -1):
        if map[y][i] == ".":
            last_dot = i
            break
    for i in range(len(map[y]) - 1, -1, -1):
        if map[y][i] == "#":
            last_wall = i
            break
    if last_wall == -1 or last_dot > last_wall:
        return (last_dot, y)
    else:
        return position


def move_down(position: tuple, map: list[str]) -> tuple:
    x, y = position
    # print(f"inside move_down function. x: {x}, y: {y}")
    if y < len(map) - 1:
        if map[y + 1][x] == ".":
            return (x, y + 1)
        elif map[y + 1][x] == "#":
            return position
    first_dot = first_dot_from_top(map, x)
    first_wall = first_wall_from_top(map, x)
    if first_wall == -1 or first_dot < first_wall:
        return (x, first_dot)
    else:
        return position


def move_up(position: tuple, map: list[str]) -> tuple:
    x, y = position
    # print(f"inside move_up function. x: {x}, y: {y}")
    if y > 0:
        if map[y - 1][x] == ".":
            return (x, y - 1)
        elif map[y - 1][x] == "#":
            return position
    first_dot = first_dot_from_bottom(map, x)
    first_wall = first_wall_from_bottom(map, x)
    if first_wall == -1 or first_dot > first_wall:
        return (x, first_dot)
    else:
        return position


def first_dot_from_top(map: list[str], x: int) -> int:
    for i in range(len(map)):
        if map[i][x] == ".":
            return i
    return -1


def first_wall_from_top(map: list[str], x: int) -> int:
    for i in range(len(map)):
        if map[i][x] == "#":
            return i
    return -1


def first_dot_from_bottom(map: list[str], x: int) -> int:
    for i in range(len(map) - 1, -1, -1):
        if x < len(map[i]):
            if map[i][x] == ".":
                return i
    return -1


def first_wall_from_bottom(map: list[str], x: int) -> int:
    for i in range(len(map) - 1, -1, -1):
        if x < len(map[i]):
            if map[i][x] == "#":
                return i
    return -1


FILE = "day22/input.txt"
# FILE = "day22/test-input.txt"

with open(FILE) as f:
    data = f.read().splitlines()

directions = data[-1]
map = data[:-2]
max_row_length = max([len(row) for row in map])
for i in range(len(map)):
    while len(map[i]) < max_row_length:
        map[i] += " "
# print(directions, map)


facings = {
    "R": {"clock_wise": "D", "counter_clock_wise": "U", "value": 0},
    "D": {"clock_wise": "L", "counter_clock_wise": "R", "value": 1},
    "L": {"clock_wise": "U", "counter_clock_wise": "D", "value": 2},
    "U": {"clock_wise": "R", "counter_clock_wise": "L", "value": 3},
}

facing = "R"

my_position = (map[0].find("."), 0)

j = 0
number = 0
directions_list = []
for i in range(len(directions)):
    if directions[i].isnumeric():
        continue
    else:
        number = int(directions[j:i])
        j = i + 1
        turn = directions[i]
        directions_list.append(number)
        directions_list.append(turn)
directions_list.append(int(directions[j:]))
print(directions_list)

for item in directions_list:
    # print(item, isinstance(item, int))
    if isinstance(item, int):
        if facing == "R":
            for i in range(item):
                my_position = move_right(my_position, map)
                # print(my_position)
        elif facing == "L":
            for i in range(item):
                my_position = move_left(my_position, map)
                # print(my_position)
        elif facing == "D":
            for i in range(item):
                my_position = move_down(my_position, map)
                # print(my_position)
        elif facing == "U":
            for i in range(item):
                my_position = move_up(my_position, map)
                # print(my_position)
    else:
        if item == "R":
            facing = facings[facing]["clock_wise"]
            # _ = input("Turning right...")
            # print(f"Now facing: {facing}")
        else:
            facing = facings[facing]["counter_clock_wise"]
            # _ = input("Turning left....")
            # print(f"Now facing: {facing}")
print(my_position)
print(f"Add 1 to x and y and then do the math.")
x, y = my_position
x += 1
y += 1

final_password = (y * 1000) + (x * 4) + facings[facing]["value"]
print(final_password)
