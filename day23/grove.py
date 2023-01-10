class Grove:
    def __init__(self, grove_data) -> None:
        self.elves = self.parse_grove_data(grove_data)

    def parse_grove_data(self, grove_data) -> list:
        elves = []
        for y in range(len(grove_data)):
            for x in range(len(grove_data[y])):
                if grove_data[y][x] == "#":
                    elves.append((x, y))
        return elves

    def is_north_empty(self, position) -> bool:
        x, y = position
        if (
            (x - 1, y + 1) in self.elves
            or (x, y + 1) in self.elves
            or (x + 1, y + 1) in self.elves
        ):
            return False
        else:
            return True

    def is_south_empty(self, position) -> bool:
        x, y = position
        if (
            (x - 1, y - 1) in self.elves
            or (x, y - 1) in self.elves
            or (x + 1, y - 1) in self.elves
        ):
            return False
        else:
            return True

    def is_west_empty(self, position) -> bool:
        x, y = position
        if (
            (x - 1, y + 1) in self.elves
            or (x - 1, y) in self.elves
            or (x - 1, y - 1) in self.elves
        ):
            return False
        else:
            return True

    def is_east_empty(self, position) -> bool:
        x, y = position
        if (
            (x + 1, y + 1) in self.elves
            or (x + 1, y) in self.elves
            or (x + 1, y - 1) in self.elves
        ):
            return False
        else:
            return True
