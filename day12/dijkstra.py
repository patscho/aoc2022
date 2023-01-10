from numpy import inf

FILE = "day12/test-input.txt"
# FILE = "day12/input.txt"


def get_neighbours(point: tuple):
    neighbours = {}
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
            neighbours[n] = 1
    return neighbours


def get_elevation(point: tuple):
    x, y = point
    if point == start:
        elevation = 1
    elif point == end:
        elevation = 26
    else:
        elevation = ord(data[y][x]) - 96
    return elevation


def find_point(point: str) -> tuple:
    for row in data:
        if point in row:
            col_index = row.index(point)
            row_index = data.index(row)
            return (col_index, row_index)
    return (-1, -1)


with open(FILE) as f:
    data = f.readlines()
    data = [item.strip() for item in data]

points = []
max_x = len(data[0]) - 1
max_y = len(data) - 1
start = find_point("S")
end = find_point("E")


for y in range(max_y + 1):
    for x in range(max_x + 1):
        points.append((x, y))

costs = {}
graph = {}
for point in points:
    neighbours = get_neighbours(point)
    graph[point] = neighbours
    costs[point] = inf

costs[start] = 0

parents = {}


def search(source, target, graph, costs, parents):
    next_node = source
    while next_node != target:
        for neighbor in graph[next_node]:
            if graph[next_node][neighbor] + costs[next_node] < costs[neighbor]:
                costs[neighbor] = graph[next_node][neighbor] + costs[next_node]
                parents[neighbor] = next_node
            del graph[neighbor][next_node]
        del costs[next_node]
        next_node = min(costs, key=costs.get)
    return parents


result = search(start, end, graph, costs, parents)


def backpedal(source, target, search_result):
    node = target
    back_path = [target]
    path = []
    while node != source:
        back_path.append(search_result[node])
        node = search_result[node]
    for i in range(len(back_path)):
        path.append(back_path[-i - 1])
    return path


print(f"parent directory: {result}")
