# FILE = "day14/test-input.txt"
FILE = "day14/input.txt"


class Sand:
    def __init__(self):
        self.x = 500
        self.y = 0
        self.at_rest = False

    def drop(self, cave: dict):
        # Part 1
        # max_x = max([x for (x, _) in cave["rocks"]])
        # min_x = min([x for (x, _) in cave["rocks"]])
        # Part 2
        max_y = max([y for (_, y) in cave["rocks"]])
        occupied = list(cave["rocks"]) + cave["sand"]
        while not self.at_rest:
            if (self.x, self.y + 1) not in occupied and self.y < (max_y + 1):
                self.y += 1
            elif (self.x - 1, self.y + 1) not in occupied and self.y < (max_y + 1):
                self.x -= 1
                self.y += 1
            elif (self.x + 1, self.y + 1) not in occupied and self.y < (max_y + 1):
                self.x += 1
                self.y += 1
            else:
                self.at_rest = True
                cave["sand"].append((self.x, self.y))
            # Part 1
            # if self.x <= min_x or self.x >= max_x:
            #     break
        return cave


with open(FILE) as f:
    rocks = [r.strip() for r in f.readlines()]

cave = {"rocks": set(), "sand": []}

for rock in rocks:
    corners = rock.split(" -> ")
    for i in range(len(corners) - 1):
        start = corners[i]
        end = corners[i + 1]
        (start_x, start_y) = [int(s) for s in start.split(",")]
        (end_x, end_y) = [int(s) for s in end.split(",")]
        if start_x == end_x:
            if start_y < end_y:
                for y in range(start_y, end_y + 1):
                    cave["rocks"].add((start_x, y))
            else:
                for y in range(start_y, end_y - 1, -1):
                    cave["rocks"].add((start_x, y))
        else:
            if start_x < end_x:
                for x in range(start_x, end_x + 1):
                    cave["rocks"].add((x, start_y))
            else:
                for x in range(start_x, end_x - 1, -1):
                    cave["rocks"].add((x, start_y))


while True:
    s = Sand()
    cave = s.drop(cave)
    if s.x == 500 and s.y == 0:
        break
    # print(s.at_rest)
    # print(s.x, s.y)
# print(cave["sand"])
print(len(cave["sand"]))
