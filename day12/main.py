import string

# FILE = "day12/test-input.txt"
FILE = "day12/input.txt"


def find_point(point: str) -> tuple:
    for row in data:
        if point in row:
            col_index = row.index(point)
            row_index = data.index(row)
            return (col_index, row_index)
    return (-1, -1)


def get_neighbours(point: tuple):
    neighbours = []
    current_elevation = get_elevation(point)
    x, y = point
    if x == 0 and y == 0:
        possible_neighbours = [(x + 1, y), (x, y + 1)]
    elif x == 0 and y == max_y:
        possible_neighbours = [(x + 1, y), (x, y - 1)]
    elif x == max_x and y == 0:
        possible_neighbours = [(x - 1, y), (x, y + 1)]
    elif x == max_x and y == max_y:
        possible_neighbours = [(x - 1, y), (x, y - 1)]
    elif x == 0:
        possible_neighbours = [(x + 1, y), (x, y - 1), (x, y + 1)]
    elif x == max_x:
        possible_neighbours = [(x - 1, y), (x, y - 1), (x, y + 1)]
    elif y == 0:
        possible_neighbours = [(x + 1, y), (x - 1, y), (x, y + 1)]
    elif y == max_y:
        possible_neighbours = [(x + 1, y), (x - 1, y), (x, y - 1)]
    else:
        possible_neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    for n in possible_neighbours:
        if get_elevation(n) <= current_elevation + 1:
            neighbours.append(n)
    return neighbours


def paths(point, end):
    routes = []

    def step(point, visited: list):
        neighbours = get_neighbours(point)
        for neighbour in neighbours:
            if neighbour == end:
                visited.append(point)
                visited.append(neighbour)
                routes.append(visited)
            elif neighbour not in visited:
                step(neighbour, visited + [point])

    step(point, [])
    return routes


def get_elevation(point: tuple):
    x, y = point
    if point == start:
        elevation = 1
    elif point == end:
        elevation = 26
    else:
        elevation = ord(data[y][x]) - 96
    return elevation


with open(FILE) as f:
    data = f.readlines()
    data = [item.strip() for item in data]

max_y = len(data) - 1
max_x = len(data[0]) - 1
visited = []
elevation = 1

start = find_point("S")
end = find_point("E")

routes = paths(start, end)
route_lengths = [len(route) for route in routes]
print(min(route_lengths) - 1)
