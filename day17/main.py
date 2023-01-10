class Point:
    def __init__(self, p: tuple) -> None:
        self.x = p[0]
        self.y = p[1]
        self.p = (self.x, self.y)

    def move_left(self):
        self.x -= 1
        self.p = (self.x, self.y)

    def move_right(self):
        self.x += 1
        self.p = (self.x, self.y)

    def move_down(self):
        self.y -= 1
        self.p = (self.x, self.y)

    def below(self):
        return (self.x, self.y - 1)

    def to_left(self):
        return (self.x - 1, self.y)

    def to_right(self):
        return (self.x + 1, self.y)


class Shape:
    def __init__(self, y, shape):
        self.y = y
        self.points = self.init_points(shape)
        self.at_rest = False

    def init_points(self, shape):
        if shape == "-":
            points = [
                Point((3, self.y)),
                Point((4, self.y)),
                Point((5, self.y)),
                Point((6, self.y)),
            ]
        elif shape == "+":
            points = [
                Point((3, self.y + 1)),
                Point((4, self.y + 2)),
                Point((4, self.y + 1)),
                Point((4, self.y)),
                Point((5, self.y + 1)),
            ]
        elif shape == "_|":
            points = [
                Point((3, self.y)),
                Point((4, self.y)),
                Point((5, self.y)),
                Point((5, self.y + 1)),
                Point((5, self.y + 2)),
            ]
        elif shape == "|":
            points = [
                Point((3, self.y)),
                Point((3, self.y + 1)),
                Point((3, self.y + 2)),
                Point((3, self.y + 3)),
            ]
        else:
            # Shape == "="
            points = [
                Point((3, self.y)),
                Point((3, self.y + 1)),
                Point((4, self.y)),
                Point((4, self.y + 1)),
            ]
        return points

    def stop(self):
        self.at_rest = True

    def get_left(self):
        return min([p.x for p in self.points])

    def get_right(self):
        return max([p.x for p in self.points])

    def get_top(self):
        return max([p.y for p in self.points])

    def get_bottom(self):
        return min([p.y for p in self.points])

    def move_left(self):
        for p in self.points:
            p.move_left()

    def move_right(self):
        for p in self.points:
            p.move_right()

    def move_down(self):
        for p in self.points:
            p.move_down()


def push_left(shape: Shape):
    can_move = True
    if shape.get_left() == 1:
        can_move = False
    else:
        for p in shape.points:
            if p.to_left() in occupied:
                can_move = False
        if can_move:
            shape.move_left()


def push_right(shape: Shape):
    can_move = True
    if shape.get_right() == 7:
        can_move = False
    else:
        for p in shape.points:
            if p.to_right() in occupied:
                can_move = False
        if can_move:
            shape.move_right()


def fall_down(shape: Shape):
    global occupied
    can_move = True
    for p in shape.points:
        if p.below() in occupied:
            can_move = False
    if can_move:
        shape.move_down()
    else:
        # print(f"Rock stopped")
        shape.stop()
        occupied += [p.p for p in shape.points]


def print_points(points):
    print("======")
    for p in points:
        print(p.p)


FILE = "day17/input.txt"
# FILE = "day17/test-input.txt"
with open(FILE) as f:
    jet_pattern = f.readline()
# print(jet_pattern)

occupied = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]
shapes = ["-", "+", "_|", "|", "="]
number_of_rocks = 1000000000000
jet_counter = 0
for r in range(number_of_rocks):
    max_y = max([p[1] for p in occupied])
    # print(f"Max y is: {max_y}")
    shape = Shape(y=max_y + 4, shape=shapes[r % 5])
    # print("New shape starts at: ")
    # print_points(shape.points)
    while not shape.at_rest:
        # print("New cycle")
        jet_index = jet_counter % len(jet_pattern)
        if jet_pattern[jet_index] == "<":
            push_left(shape)
            # print("Jet is pushing left")
        else:
            push_right(shape)
            # print("Jet is pushing right")
        jet_counter += 1
        fall_down(shape)
        # print("Rock is falling down")
        # print_points(shape.points)
    # print(occupied)

max_y = max([p[1] for p in occupied])
print(max_y)
