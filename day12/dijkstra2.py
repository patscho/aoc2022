import sys

# FILE = "day12/test-input.txt"
FILE = "day12/input.txt"


class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        # for node, edges in graph.items():
        #     for adjacent_node, value in edges.items():
        #         if graph[adjacent_node].get(node, False) == False:
        #             graph[adjacent_node][node] = value
        return graph

    def get_nodes(self):
        return self.nodes

    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        return self.graph[node1][node2]


def dijkstra_algorithm(graph: Graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    shortest_path = {}
    previous_nodes = {}
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0

    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(
                current_min_node, neighbor
            )
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node

        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    path.append(start_node)

    print(
        f"We found the following best path vith a value of: {shortest_path[target_node]}"
    )
    print(list(reversed(path)))


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

nodes = []
max_x = len(data[0]) - 1
max_y = len(data) - 1
start = find_point("S")
end = find_point("E")

for y in range(max_y + 1):
    for x in range(max_x + 1):
        nodes.append((x, y))

init_graph = {}
for node in nodes:
    neighbors = get_neighbours(node)
    init_graph[node] = {}
    for n in neighbors:
        init_graph[node][n] = 1

graph = Graph(nodes, init_graph)
previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=start)
print_result(previous_nodes, shortest_path, start_node=start, target_node=end)

a_nodes = [n for n in nodes if get_elevation(n) == 1]
shortest = sys.maxsize
for node in a_nodes:
    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=node)
    if shortest_path[end] < shortest:
        shortest = shortest_path[end]
print(shortest)
