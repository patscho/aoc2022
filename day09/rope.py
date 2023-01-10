class Knot:
    def __init__(self, x: int, y: int):
        self.pos = (x, y)

    def up(self):
        x, y = self.pos
        self.pos = (x, y + 1)

    def down(self):
        x, y = self.pos
        self.pos = (x, y - 1)

    def left(self):
        x, y = self.pos
        self.pos = (x - 1, y)

    def right(self):
        x, y = self.pos
        self.pos = (x + 1, y)


class Rope:
    def __init__(self, number_of_knots: int):
        self.knots = [Knot(0, 0) for _ in range(number_of_knots)]
        self.visited_by_tail = [(0, 0)]
        self.visited_by_head = [(0, 0)]

    def move_head(self, direction: str):
        direction = direction.lower()
        head = self.knots[0]
        if direction == "u":
            head.up()
        elif direction == "d":
            head.down()
        elif direction == "l":
            head.left()
        elif direction == "r":
            head.right()

    def move_tail(self, head: Knot, tail: Knot):
        head_x, head_y = head.pos
        tail_x, tail_y = tail.pos
        if head_x - tail_x == 2 and head_y - tail_y == 2:
            tail_x += 1
            tail_y += 1
        elif head_x - tail_x == 2 and head_y - tail_y == -2:
            tail_x += 1
            tail_y -= 1
        elif head_x - tail_x == -2 and head_y - tail_y == -2:
            tail_x -= 1
            tail_y -= 1
        elif head_x - tail_x == -2 and head_y - tail_y == 2:
            tail_x -= 1
            tail_y += 1
        elif head_x - tail_x == 2:
            tail_x += 1
            tail_y = head_y
        elif head_x - tail_x == -2:
            tail_x -= 1
            tail_y = head_y
        elif head_y - tail_y == 2:
            tail_y += 1
            tail_x = head_x
        elif head_y - tail_y == -2:
            tail_y -= 1
            tail_x = head_x
        tail.pos = (tail_x, tail_y)

    def move(self, direction):
        self.move_head(direction)
        for i in range(1, len(self.knots)):
            self.move_tail(self.knots[i - 1], self.knots[i])
        self.visited_by_head.append(self.get_head_pos())
        self.visited_by_tail.append(self.get_tail_pos())

    def get_tail_pos(self) -> tuple:
        return self.knots[-1].pos

    def get_head_pos(self) -> tuple:
        return self.knots[0].pos
